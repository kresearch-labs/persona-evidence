# Probe UE 5.8.3 Python API: full BlueprintEditorLibrary surface + node creation + runtime python
import unreal, os

REPORT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "api_probe2.txt")
lines = []
def note(m):
    lines.append(m)
    unreal.log("[PROBE2] %s" % m)

# 1. Full BlueprintEditorLibrary attrs
bpl = unreal.BlueprintEditorLibrary
attrs = sorted(dir(bpl))
note("BPL_FULL_BEGIN")
for a in attrs:
    try:
        fn = getattr(bpl, a)
        if callable(fn):
            try:
                note("  %s%s" % (a, str(inspect_sig := getattr(fn, "__doc__", ""))[:0] or ""))
            except Exception:
                pass
    except Exception:
        pass
# simpler: just list names
note("BPL_ATTRS: " + ", ".join(attrs))
note("BPL_FULL_END")

# 2. doc signatures for the interesting ones
for name in ["add_function_graph", "add_member_variable", "compile_blueprint",
             "create_blueprint_asset_with_parent", "call_method", "add_event_dispatcher",
             "find_execute_pin", "find_input_pin", "find_output_pin", "find_then_pin",
             "find_self_pin", "find_result_pin", "find_condition_pin", "find_data_input_pin",
             "find_else_pin", "find_event_graph", "find_input_pin_by_index", "find_output_pin_by_index"]:
    fn = getattr(bpl, name, None)
    if fn:
        note("SIG %s :: %s" % (name, (fn.__doc__ or "no doc").replace("\n", " | ")[:400]))

# 3. node creation hunt across likely libraries
for libname in ["BlueprintEditorLibrary", "EditorUtilityLibrary", "EditorAssetLibrary",
                "PythonBPLib", "KismetSystemLibrary", "KismetLibrary", "AssetToolsHelpers"]:
    try:
        lib = getattr(unreal, libname, None)
        if lib is None:
            continue
        hits = [a for a in dir(lib) if any(k in a.lower() for k in ("node", "spawn", "wire", "link", "connect", "pin", "graph", "schema"))]
        if hits:
            note("NODEHUNT %s: %s" % (libname, ", ".join(sorted(hits))))
    except Exception as e:
        note("NODEHUNT %s err %s" % (libname, e))

# 4. any class with 'node' in name
node_classes = [c for c in dir(unreal) if "node" in c.lower() and ("graph" in c.lower() or "blueprint" in c.lower() or "ed" in c.lower())]
note("NODE_CLASSES: " + ", ".join(node_classes[:40]))

# 5. runtime python check
try:
    note("runtime_py_available=%s" % unreal.PythonBPLib is not None)
except Exception:
    pass
for sub in ["PythonScriptGameSubsystem", "PythonScriptLibrary"]:
    note("has %s = %s" % (sub, hasattr(unreal, sub)))

# 6. EnhancedInput details
ei = [c for c in dir(unreal) if "InputMapping" in c or "InputAction" in c]
note("ENHANCED_INPUT_CLASSES: " + ", ".join(sorted(ei)[:30]))

# 7. save game
note("SaveGame class: %s" % hasattr(unreal, "SaveGameObject"))

# 8. widget / UMG creation from python
umg = [c for c in dir(unreal) if c.startswith("Widget")][:25]
note("UMG_CLASSES: " + ", ".join(umg))

with open(REPORT, "w") as f:
    f.write("\n".join(lines))
note("report written: %s" % REPORT)
