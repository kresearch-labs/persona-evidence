# RUNTIME PROBE — does Python work in -game mode?
# Bootstrapped via -ExecCmds="pyexec <this file>". Writes receipts to logs/.
# Tests: (1) execution, (2) world access, (3) timer-driven python callback,
#        (4) file IO + json save, (5) SystemLibrary timer fns, (6) widget creation.
import unreal, os, json, traceback

BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LOG = os.path.join(BASE, "logs", "rt_probe.txt")
def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

w("=== RT PROBE START ===")
w("unreal version: %s" % unreal.SystemLibrary.get_engine_version())

# --- 2. world access attempts ---
world = None
try:
    sub = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
    world = sub.get_game_world()
    w("world via UnrealEditorSubsystem: %s" % world)
except Exception as e:
    w("UnrealEditorSubsystem failed: %s" % e)
if world is None:
    try:
        world = unreal.EditorLevelLibrary.get_game_world()
        w("world via EditorLevelLibrary: %s" % world)
    except Exception as e:
        w("EditorLevelLibrary failed: %s" % e)
if world is None:
    try:
        eng = unreal.get_engine()
        w("engine attrs sample: %s" % [a for a in dir(eng) if "world" in a.lower()][:10])
    except Exception as e:
        w("engine introspect failed: %s" % e)

# --- 5. SystemLibrary timer functions ---
sl = [a for a in dir(unreal.SystemLibrary) if "timer" in a.lower()]
w("SystemLibrary timer fns: %s" % sl)
gs = [a for a in dir(unreal.GameplayStatics) if "save" in a.lower() or "player" in a.lower()]
w("GameplayStatics save/player fns: %s" % gs)

# --- 3. timer-driven python callback ---
TICKS = {"n": 0}
def on_timer():
    TICKS["n"] += 1
    if TICKS["n"] <= 3:
        w("TIMER TICK %d at %s" % (TICKS["n"], unreal.SystemLibrary.get_real_time()))
    if TICKS["n"] == 3:
        w("TIMER_TEST_PASS: 3 ticks received")
        # --- 4. file IO + json (save path check) ---
        try:
            save_dir = os.path.join(BASE, "game", "ScalTest", "Saved", "KeeperSaves")
            os.makedirs(save_dir, exist_ok=True)
            data = {"cycle": 1, "oil": 87.5, "record": [{"t": "LAMP", "d": "lit"}]}
            tmp = os.path.join(save_dir, "slot0.json.tmp")
            with open(tmp, "w") as f:
                json.dump(data, f)
            os.replace(tmp, os.path.join(save_dir, "slot0.json"))
            w("FILEIO_TEST_PASS: atomic json save written")
        except Exception:
            w("FILEIO_TEST_FAIL: %s" % traceback.format_exc())
        # --- 6. player controller + HUD print ---
        try:
            pc = unreal.GameplayStatics.get_player_controller(world, 0)
            w("player controller: %s" % pc)
            unreal.SystemLibrary.print_string(pc, "KEEPERS LEDGER RT PROBE OK", True, True,
                                              unreal.Color(r=1, g=0.8, b=0.2, a=1), 10.0)
            w("PRINT_TEST_PASS")
        except Exception:
            w("PRINT_TEST_FAIL: %s" % traceback.format_exc())
        # --- widget creation probe ---
        try:
            wbp_classes = [c for c in dir(unreal) if c == "UserWidget"]
            w("UserWidget class present: %s" % wbp_classes)
            # can we create a plain widget tree object?
            wt = unreal.WidgetTree()
            w("WidgetTree constructible: %s" % (wt is not None))
        except Exception:
            w("WIDGET probe fail: %s" % traceback.format_exc())
        # --- quit cleanly ---
        try:
            unreal.SystemLibrary.execute_console_command(world, "quit")
            w("QUIT issued")
        except Exception:
            w("QUIT failed: %s" % traceback.format_exc())

try:
    td = unreal.TimerDynamicDelegate()
    td.bind_callable(on_timer)
    fn = None
    for name in ("k2_set_timer_delegate", "k2_set_timer_for_time_and_next", "k2_set_timer"):
        fn = getattr(unreal.SystemLibrary, name, None)
        if fn:
            w("using timer fn: %s" % name)
            break
    if fn is None:
        w("NO TIMER FN on SystemLibrary")
    else:
        try:
            fn(td, 0.5, True, 0.0)
        except TypeError:
            fn(td, 0.5, True)
        w("TIMER_ARMED")
except Exception:
    w("TIMER_ARM_FAIL: %s" % traceback.format_exc())

w("=== RT PROBE SETUP DONE (async tests pending) ===")
