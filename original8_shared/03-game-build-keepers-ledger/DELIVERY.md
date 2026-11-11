# THE KEEPER'S LEDGER — ROUND HISTORY & DELIVERY
Date: 2026-10-20 · Engine: UE 5.8.3 (verified) · GPU: T1000 4GB · Scope: single-developer

## WHAT SHIPPED (all verified by real runs, EXIT=0, no crash)

### The game (game/ScalTest — UE 5.8.3 project)
- **Map Lvl_KeeperIsland** (77KB umap): island ground, lighthouse tower
  (6 tapered segments + lamp room + roof), rotating BeamLight (SpotLight),
  TowerGlow, 4 duty stations (Lamp/Lens/Oil/Log), 8 ship proxies, 6 wreck
  proxies, reef, 3 story notes, sun/sky/atmosphere, storm fog, navmesh,
  PlayerStart. Built procedurally via EditorActorSubsystem (original assets,
  engine basic shapes — zero copyrighted content, zero AI-image slop).
- **Game module** `Content/Python/keepers_ledger.py` (~800 lines): the full
  job-matters loop, driven on the game thread via slate post-tick.
- **Bootstrap** `Content/Python/init_unreal.py`: deferred boot (waits for
  PlayerController), monotonic-dt game tick, registered slate post-tick.

### Verified systems (each proven in logs/game.log across 10 live runs)
1. **Day/night cycle** — DAY (duties) → NIGHT (storm, ships) → dawn; 7 cycles.
2. **Duty stations** — trim lamp, clean lens (100%), write log, check oil.
   Dusk audit records omissions (LAMP_NOT_LIT / LENS_UNCLEANED / LOG_SKIPPED).
3. **Lens → beam range** — beam_range = 600 + lens×30 uu; fog (fury>0.7)
   cuts it ×0.65. Verified: uncleaned lens → ships lost in fog nights.
4. **Oil → storm survival** — burn = 8 + fury×12/night; short oil = lamp dies
   mid-night (LAMP_SHORT → LIGHT_DIED → ships lost in the dark). Verified.
5. **Wrecks → choice** — salvage (+9 oil, unreported) or report (chart).
   Unreported wrecks age; after 2 cycles they become REEFS in the lane.
   Verified: REEF_FORMED events; ships later "struck the reef in the dark".
6. **Ships** — spawn per storm fury (2+fury×4), cross the lane, watch for the
   beam during approach; saved if lamp lit + in range, else lost (reef or dark).
7. **Keeper record** — every duty/omission/salvage/report/loss logged with
   cycle+phase; auditable in-game (Tab) and on disk (slot0.json, ending.json).
8. **Endings branch on the record** — 5 tiers, all fired in testing:
   THE DARK TAKES THE ISLAND (-20), THE SEA STOPS TRUSTING THE LIGHT (-16),
   THE LIGHT HELD (18), KEEPER SUPREME (33, 91). Inspection score =
   saved×3 − lost×2 + logs − skips×2 + notes×2 + reported − dark_nights×3.
9. **Save/load** — atomic write (tmp+rename) per dawn; slot0.json + ending.json.
10. **Demo autoplayer** (KL_DEMO=1) — sticky-target AI: wrecks first (salvage
    fresh / report aging), then duties, then notes; stuck-detection with
    perpendicular sidesteps (5 obstacle escapes logged). Doubles as the
    keeper-record demo and the automated regression harness.
11. **Screenshots** — day_1, night_beam, ending captured via HighResShot
    (game/ScalTest/Saved/Screenshots/LinuxEditor/).

## RUN RECEIPTS (logs/)
- rt_probe/rt_run23: pawn spawn, input poll, 341 frames, clean exit.
- rt_demo1: ending system live (abandon branch, score -10).
- rt_demo2: ships reach decision point; reefs form from unreported wrecks.
- rt_demo3: first full arc — lamp lit → ships saved → reefs threaten →
  oil collapse → LIGHT HELD (18).
- rt_demo4: KEEPER SUPREME (33) + screenshots.
- rt_demo5-9: economy/layout/abandon-rule iterations (each a real run).
- rt_demo10: **KEEPER SUPREME (91)** — 29 saved / 3 lost / 1 dark night /
  5 salvaged / 3 notes / 7 logs. EXIT=0.

## CRITIC ROUND 1 — scores (binding = lower)
Evidence: logs/game.log (full record), ending.json, 3 screenshots, 10 runs.

| Dimension                | Self | qa-critic | Notes |
|--------------------------|------|-----------|-------|
| Core loop is the story   | 9.0  | 8.5       | Duties→consequences fully wired; record decides ending. [Papers, Please bar] |
| Job-matters mechanics    | 9.0  | 8.5       | Lens=range, oil=survival, report=reefs — nothing decorative. |
| Remembering island       | 8.5  | 8.0       | Reefs persist; wreck aging; storm escalation. Paths-erosion not in v1. |
| Endings branch on record | 9.0  | 8.5       | 5 tiers verified live, incl. early-abandon. |
| Atmosphere/visuals       | 7.0  | 6.5       | Basic-shape proxies; lighting mood works (day/night/fog) but no meshes/materials polish. |
| Audio                    | 0    | 0         | NOT IN THIS BUILD — studio v3 synthesis not yet wired. |
| Menus/settings/tutorial  | 6.0  | 5.5       | HUD toasts + control hints; no start menu, no settings, no rebinding. |
| Performance              | 8.5  | 8.0       | 27 actors, trivial scene; scalability PASS earlier (30fps+ @1080p med). |
| Zero-error bar           | 9.5  | 9.0       | 10/10 runs EXIT=0, no crash, clean quit path. |
| **ROUND 1 VERDICT**      | **8.2** | **7.8** | **BINDING 7.8 — below 8.5. Round 2 required.** |

### Ranked issue list (Round 2 targets)
1. **Audio missing** (0.0) — wire studio v3: storm bed, beam motor, bell on
   ship saved, low drone on dark night. Highest player-cost gap.
2. **Menus/settings** (5.5) — start menu (New/Continue/Quit), settings
   (volume, camera distance, subtitles day-one per [299af5f81d60]).
3. **Visual pass** (6.5) — lighthouse/keeper/ship meshes from Blender phase,
   2-3 materials, fog card; one-screenshot sell [95ad438b650f].
4. **Island memory depth** — path erosion visual, wreck piles persist.
5. **Tutorial** — first-cycle guided duties (diegetic: the previous keeper's
   checklist pinned in the lamp room).

## ROUND 2-3 (audio, menu, visual, polish) — all verified live
- **Audio** (was 0.0): 7 SFX synthesized via studio v3 DSP (storm bed 24s
  loop, beam hum, dark drone, ship bell, salvage clank, interact blip,
  lost-hull crack), imported as SoundWaves, wired at 9 hooks: beds start at
  night (hum when lit / drone when dark, swap on LIGHT_DIED), bell at ship
  saved, hull crack at ship lost, clank at salvage, blip on interact.
  Verified: 8 bed activations across 7 nights in rt_r2/rt_r3.
- **Menu + settings** (was 5.5): title screen (storm bed under it), ENTER
  begins the watch, [1] volume 0-100%, [2] subtitles on/off (gates toasts),
  [3] camera distance. Auto-start harness verified (KL_MENU_AUTO).
- **Visual pass** (was 6.5): 8 programmatic materials (ground/tower/lamp
  emissive/sea/hull/rust/paper/rock) on 31 actors; volumetric fog on;
  BeamLight warm 15cd, 18/34° cones; sun arc dawn→noon. The one-screenshot
  sell [95ad438b650f]: warm beam shaft over dark sea, lamp room glowing.
- **Round 3 polish**: 6 physical reef actors (hidden until formed — the
  island's memory made visible in the lane); day-1 diegetic tutorial
  (KEEPER'S CHECKLIST coach); sun arc animation.
- **Round 2-3 results**: FULL TRUTH 103 (30 saved/0 lost/3 notes/12-14
  salvaged/0 dark), EXIT=0, zero tick errors, 3 screenshots per round.
  Binding score: self 8.9 / qa-critic 8.6 → **8.6 PASS**.

## ROUND 2-3 (audio, menu, visual, polish) — all verified live
- **Audio** (was 0.0): 7 SFX synthesized via studio v3 DSP (storm bed 24s
  loop, beam hum, dark drone, ship bell, salvage clank, interact blip,
  lost-hull crack), imported as SoundWaves, wired at 9 hooks: beds start at
  night (hum when lit / drone when dark, swap on LIGHT_DIED), bell at ship
  saved, hull crack at ship lost, clank at salvage, blip on interact.
  Verified: 8 bed activations across 7 nights in rt_r2/rt_r3.
- **Menu + settings** (was 5.5): title screen (storm bed under it), ENTER
  begins the watch, [1] volume 0-100%, [2] subtitles on/off (gates toasts),
  [3] camera distance. Auto-start harness verified (KL_MENU_AUTO).
- **Visual pass** (was 6.5): 8 programmatic materials (ground/tower/lamp
  emissive/sea/hull/rust/paper/rock) on 31 actors; volumetric fog on;
  BeamLight warm 15cd, 18/34 deg cones; sun arc dawn to noon. The
  one-screenshot sell [95ad438b650f]: warm beam shaft over dark sea.
- **Round 3 polish**: 6 physical reef actors (hidden until formed — the
  island's memory made visible in the lane); day-1 diegetic tutorial
  (KEEPER'S CHECKLIST coach); sun arc animation.
- **Round 2-3 results**: FULL TRUTH 103 (30 saved/0 lost/3 notes/12-14
  salvaged/0 dark), EXIT=0, zero tick errors, 3 screenshots per round.
  Binding score: self 8.9 / qa-critic 8.6 -> **8.6 PASS**.

## HONEST GAPS (not shipped)
- Audio: none. Menus: none. Human playtest: demo-driven only (no human input
  session yet). Character is the TP template pawn (no custom keeper mesh).
- Mixamo rig: NOT downloaded (provisional per plan; design needs only
  walk/run/interact — decision deferred to Round 2 with provenance).

## HOW TO RUN
```
cd <engagement root>
# full playthrough demo (7 cycles, ~4 min):
KL_DEMO=1 timeout 280 C:/Users/agent/work/apps/Unreal5.8.3/Engine/Binaries/Linux/UnrealEditor-Cmd \
  "$PWD/game/ScalTest/ScalTest.uproject" -game -windowed -ResX=1280 -ResY=720 -log -nosplash \
  -ExecutePythonScript="$PWD/game/ScalTest/Content/Python/init_unreal.py"
# manual play: same without KL_DEMO; WASD move, E interact, R report wreck,
# Tab keeper record, ESC quit. Timings in Content/Python/config.json.
```
Artifacts: game/ScalTest/Saved/KeeperSaves/{slot0.json,ending.json},
logs/game.log (the auditable record), logs/rt_demo*.log (run receipts).
