# THE KEEPER'S LEDGER — DESIGN DOC (SPEC LOCK v1.0)
Date: 2026-10-20. Engine: Unreal 5.8.3 (Step 1 verdict: PASS, 52fps steady @1080p medium, T1000).
Owner: gamedesigner (LEAD). One owner per decision; decisions log and stick [game_director:5666e7d38315].
Status: LOCKED for build. Changes require a dated entry in section 17 (Changelog).

---

## 1. VISION (game_director seat)

**One line: The job is the story.**

You are the last keeper of a storm-ravaged island lighthouse. The keepers before you
vanished, one by one. The supply boat stopped coming. Every night a storm tests the
light; every day the island shows you what last night cost — and what the keepers
before you left behind.

Pillars (in priority order — when in doubt, cut toward the top):
1. **Every duty has mechanical weight.** Nothing is decorative. If a duty doesn't
   change a number that matters, it doesn't ship.
2. **The island remembers.** Wrecks, damage, erosion, reefs — the island is the
   history of your playthrough, physically.
3. **The record is the story.** No dialogue choices. An auditable log of duties done
   and skipped decides what the inspector reads and which ending you earn.
4. **The storm is the antagonist.** Procedural, readable, fair. It has tells. It
   never cheats.

Tone: quiet dread + competence fantasy. The Papers, Please precedent: mechanics carry
the meaning; you live in the world your decisions produced.

Name-promise check [game_director:76c0c46d67f3]: "The Keeper's Ledger" promises a
keeper's job AND a ledger that matters. The build delivers exactly these two things.
Feature creep is the enemy; anything not in this doc is out of scope.

## 2. CORE LOOP (gamedesigner seat)

**Cycle = one Day + one Night. Target 12–18 real minutes. A full run = 12 cycles + ending (~3h).**

### DAY (work phase)
1. **Read the night's report** at the log desk: what the beam did, which ships passed
   or were lost, what failed, what washed ashore.
2. **Duties** (each maps to mechanics — see section 3):
   - Load oil / set the ration
   - Clean the lens (clarity), repair the mechanism (rotation + wick feed)
   - Salvage wrecks on Wreck Shore (parts, oil)
   - Report wrecks at the chart house (marks them on the chart, prevents reefs)
   - Maintain paths (drainage) where storms eroded them
   - Keep the log (write the day's entry — feeds the record's completeness)
3. **Explore** for the five traces of the previous keepers (optional, story-critical).
4. **Light the lamp at dusk.** The night then runs on what you actually loaded, set,
   cleaned, and repaired. No take-backs.

### NIGHT (storm phase)
- A procedural storm rolls in (section 4). The beam runs autonomously from your day's work.
- You may move through the tower at night: trim the wick, nudge the ration, restart a
  stalled mechanism — physical interventions under time pressure, not menus.
- Ships spawn on lanes and resolve against your beam's real reach, the real fog, and
  the real hazard map (including reefs your unreported wrecks became).
- Outcomes post to the ledger at dawn: PASSED / TURNED AWAY / WRECKED.

### DAWN
Results post. Damage persists. New wrecks may have washed ashore. Autosave (diegetic:
"the log is written"). The island shows its memory.

## 3. THE JOB-MATTERS SYSTEMS (anti-decoration law — the heart of the game)

### 3.1 OIL ECONOMY (game_balance_economist seat)
- Oil is the single survival resource. Sources: salvage from wrecks (barrels), a finite
  island reserve in the shed, no resupply (the boat is gone — that's the story).
- **Burn rate = f(flame height).** You set flame height: higher = longer reach, more burn.
- **Ration:** you set the night's ration at the tank. Tank capacity is finite; the
  ration decides how long the light holds.
- **Dark interval:** if oil hits zero mid-storm, the beam dies for as long as the oil
  stays at zero. Every ship in fog during a dark interval is at maximum risk. The
  record logs the interval to the minute.
- Tradeoff: burn bright (save ships, drain reserve) vs ration (risk dark intervals).
  Storm fury is random enough that neither pure strategy dominates [game_balance_economist:0b5d7f574911].

### 3.2 LENS → BEAM REACH
- **Clarity 0–100%:** salt crust and soot accumulate daily; cleaning restores it.
  Clarity multiplies effective reach, and fog is the storm's main weapon — so lens
  work is literally ships-saved.
- **Alignment:** mechanism wear degrades alignment; repair restores it.
- **Cracks:** neglect clarity below 20% for two nights and the lens cracks — a
  permanent reach penalty until repaired with lens parts salvaged from wrecks.

### 3.3 MECHANISM (rotation + wick feed)
- The lens assembly rotates; the flash characteristic is how ships identify the light.
  Wear → rotation stalls → steady beam → ships misread it in rain.
- Wick feed jams → flame dips → dark intervals even with oil in the tank.
- Both repaired with clockwork/gears salvaged from wrecks. Wear is visible (wobble,
  tick irregularity — audio tells before failure).

### 3.4 WRECKS → REEFS (the remembering island)
- Storms wash wrecks ashore (hull sections, cargo, oil barrels, sometimes a crew's
  belongings — story material).
- Each wreck must be **salvaged** (parts + oil) AND **reported** at the chart house.
- **Unreported wreck = unmarked hazard.** Later storms push it off the shore into the
  approach lanes; it becomes a reef that wrecks future ships. The island literally
  accumulates your neglect as new dangers on the map.
- Reported wrecks get a buoy (built from salvage) — marked, safe, visible.
- Island holds max 6 wreck sites. Each unreported one raises ship-loss odds in every
  later storm. This is the game's memory made physical.

### 3.5 THE KEEPER RECORD (auditable log — the story spine)
- Every duty done or skipped posts a timestamped, categorized entry:
  LAMP / LENS / MECHANISM / WRECKS / LOG / ISLAND.
- Entries are **facts, not judgments**: "Night 4: dark interval 47 min. 2 ships unaccounted."
- The record is a real serialized data structure (in the save file), viewable in-game
  as the ledger book.
- **The inspector reads it** at the end (section 6). The ending is arithmetic on the
  record — no hidden flags, no dialogue.
- **The five traces** (previous keepers) each show THEIR record fragment: what they
  neglected, what it cost. The mystery assembles from records — yours and theirs.
  The truth: each keeper broke under the same job; the sea took them when their
  records failed. No monsters. The horror is the ledger.
- **Story-emerges-from-sim guarantee:** trace texts reference duty categories and
  consequences, never player-specific state they can't know — so the story cannot
  contradict the sim, because it is made of the sim's own data.

### 3.6 SHIPS (the score)
- Ships spawn on 2–3 approach lanes per night; count scales with fury and cycle.
- Resolution per ship: sees the beam (reach × clarity × alignment vs fog) → holds a
  safe course; else risk roll against hazards (rocks, unreported reefs, drifting wrecks).
- Outcomes: PASSED / TURNED AWAY (safe, no credit) / WRECKED (distress flare at night;
  the wreck washes ashore next day — and waits for your report).
- You never talk to ships. Flares, bells, and the beam are the only voices.

## 4. STORM SYSTEM (procedural)
- Parameters: fury 1–5, wind direction/speed, rain density, fog density, duration,
  gust events, lightning strikes.
- **Seeded:** storm seed = run_seed + cycle → deterministic per run (reproducible for
  QA and for the critic rubric).
- Fury curve across 12 cycles (escalation with breather valleys [game_level_content_designer:bb3570f4e15b]):
  `1, 2, 2, 3, 2, 4, 3, 4, 5, 3, 5, 5` — tuned by balance seat; breathers before spikes.
- Gusts above threshold damage the mechanism, crack the lens path, erode paths.
- Lightning = flash light + synthesized thunder. **No VolumetricCloud actors** (Step 1
  budget law: 15ms GPU). Storm sky = volumetric fog + SkyAtmosphere + rain particles.

## 5. ISLAND LAYOUT (game_level_content_designer seat)
One island, five regions, walkable end-to-end in ~4–6 minutes. No fast travel (the
walk is short and the island IS the game).

1. **Lighthouse Point** (center-south, high ground): the tower — lamp room (lens,
   mechanism, tank), keeper's room below (log desk, record book, bed).
2. **Cottage Row** (east): cottage, supply shed (finite starting stock), signal post.
3. **Wreck Shore** (west): where the sea returns what it takes; salvage bench.
4. **Old Landing** (north): the pier, the supply boat's last mooring (story), the
   chart house (wreck chart + report desk).
5. **The Back Hills** (south): the five trace sites of the vanished keepers, hidden in
   weather and terrain; a spring; the old path.

**Paths erode:** storm gusts damage the main path (mud, rockfall). Eroded path = slow
travel until you maintain it (drainage duty). The island's geography carries your
history [game_level_content_designer:bb3570f4e15b].

**Secret density:** traces reward exploration, never gate the core loop
[game_level_content_designer:88b0470741a8]. You can finish all 12 cycles without
finding a single trace — and get a worse ending for it, honestly earned.

**Late-game anti-grind:** cycles 9–12 mutate the job with what the island has become
(new reefs you made or marked, eroded or maintained paths, wreck sites open or
cleared) — the late game is your history demanding attention, not the same loop
harder [game_level_content_designer:c811113b62ec — avoid repetitive grind samey].

## 6. ENDINGS (branch on the record — no dialogue choices)
Cycle 13, dawn: the inspector's boat finally arrives. They walk the island and read
the ledger. The ending is **derived arithmetic on the record**:

Inputs: ships_saved, ships_lost, dark_interval_minutes, wrecks_reported/unreported,
traces_found (0–5), mechanism_failures, log_completeness (0–100%).

| Ending | Condition (shape) | Beat |
|---|---|---|
| **A. The Light Holds** | high saved, few dark intervals, all wrecks reported, log complete | The inspector re-staffs the light. You train the next keeper. |
| **B. The Ledger and the Sea** | solid record, some gaps | The inspector takes the ledger for the archive; you stay on. Bittersweet. |
| **C. The Quiet Resignation** | poor record, but honest log | Relieved of duty, alive. The light dims behind you. |
| **D. Another Name in the Ledger** | poor record, gaps, unreported wrecks, long dark intervals | The inspector reads your record the way we read the vanished keepers'. The island keeps its next trace. |
| **E. The Truth Assembled** (secret) | all 5 traces + a record that answers them | The full story of the keepers, assembled from their records and yours. |

Each ending: the inspector's walk (scripted), ledger entries read as on-screen text
(no VO), one final shot of the light — burning or dark. No dialogue choices anywhere.

## 7. TUTORIAL (cycle 1 = diegetic onboarding)
- Cycle 1 storm is fury 1 (gentle). The previous keeper's final note guides you:
  a short note at each work station teaches exactly one duty, in the world.
- No wall-of-text. No UI tutorial overlay beyond control hints.
- Accessibility day one: rebindable keys, camera distance option, subtitles for all
  diegetic text [gamedesigner:299af5f81d60 — the options themselves are the law; that
  case's failure was the crash loop, which our zero-error gate covers].

## 8. SAVE / LOAD (performance seat law)
- **Save anywhere** outside the storm-critical window; checkpoints justify themselves
  (dawn autosave is diegetic: the log is written) [gamedesigner:25ec01749aa9].
- **Serialized off-thread, atomic write (tmp + rename), size capped <5MB**
  [game_performance_engineer:32de12d63ae9, cb56bfc3e8bb, 35e6436f27c1, a3a5a32d5781, 46f8a3d79c59].
- Save contains: full world state, keeper record, island memory (wrecks/reefs/erosion),
  storm seed state, cycle counter. Loading restores exactly.
- Autosave at every dawn + manual save at the log desk. Single slot + backup.

<!-- PART 2 below -->

## 9. ART DIRECTION (game_visual_direction seat)
**Look: painterly-realist, storm-muted, one warm light.**
- Palette: cold slate blues/greens (sea, rain, rock), warm amber (the lamp, the hearth,
  oil). The lamp is the only saturated warm source in the world — the player's eye
  learns to find it, and to fear its absence.
- **Readability first** [game_visual_direction:6cc7f93959c6]: at gameplay distance,
  interactables read via shape + subtle emissive rim; hazards (rocks, reefs) read via
  white water even in rain. The beam must always be legible as a volume.
- **The one-screenshot rule** [game_visual_direction:95ad438b650f, 6f6cdeb763ba]: the
  key art frame is the lamp room at night, storm behind the glass, beam cutting fog
  over black water. Every vista in the game must sell the game in one frame.
- Screenshake only from authored impacts (lightning strike, hull crack, gust hitting
  the gallery) — never global ambient wobble [game_visual_direction:9711bf681caa].
- Lighting: Lumen GI (verified in Step 1), dim cool key (overcast), lamp as hero light.
  Interior = single warm practicals. No volumetric clouds (budget law).
- Materials: procedural Blender textures baked to simple maps; no AI-generated images
  anywhere. Grain/vignette subtle in post.

## 10. AUDIO (studio v3 — synthesized, real DSP, no AI slop)
- Storm bed: filtered noise wind (gust-modulated), rain layers by density, thunder
  synthesized (noise burst → convolution), sea loop by fury.
- Diegetic: lamp hiss, mechanism tick (irregular when worn — the audio tell), bell
  buoy, flare crack, hull groans, pen on paper at the log desk.
- Music: none during play. One motif for the inspector's walk and endings.
- All SFX via studio v3 API (api_v3_fx.py) → WAV → UE import. Provenance: synthesized.

## 11. PERFORMANCE BUDGET (game_performance_engineer seat — the 30fps reality)
Target: **1080p, medium, ≥30fps steady on T1000 4GB** (Step 1 measured 52fps headroom).

| Line | Budget |
|---|---|
| Base scene (island, tower, props) | ~19ms GPU (measured) |
| Volumetric fog (storm) | included above (measured) |
| Rain particles (GPU sprites, capped 2k) | ≤1.5ms |
| Lightning flash (dynamic light, rare) | ≤0.5ms amortized |
| Beam light + volumetric shaft | ≤2.0ms |
| Ships (max 3 concurrent, simple) | ≤1.0ms |
| Character + anims | ≤0.5ms |
| UI (ledger book, HUD) | ≤0.5ms |
| **Total worst-case** | **~26ms → 38fps floor; target 33ms → 30fps guaranteed** |

Laws: no VolumetricCloud actors (15ms measured). No Lumen HW ray tracing. VSM on.
Texture pool capped. Save serialized off-thread, atomic, <5MB
[game_performance_engineer:32de12d63ae9]. Every build runs the smoke suite
[game_qa_critic:3ba945b1661e]: boot → new game → one duty → save → load → exit clean.

## 12. BALANCE SHEET (game_balance_economist seat — the duty economy)
Numbers v1 (tune in playtests; every change logged in section 17):

- **Oil:** tank 100 units. Burn = flame_height(0.5–1.5) × 6 units/hour-of-night.
  Night = 8 game-hours. Full flame full night = 48 units. Ration caps the night's burn.
- **Oil sources:** wreck barrels 15–25 each (1–2 per storm); shed reserve 120 total
  (finite — the clock of the run); no other source. Total economy ≈ 120 + ~10 barrels
  ≈ enough for ~26 night-equivalents at full flame — scarcity is real by cycle 8+.
- **Lens clarity:** decays 8–15%/day (storm-dependent). Cleaning = 1 day-duty, full restore.
  Reach multiplier = 0.4 + 0.6×clarity. Crack penalty −25% until repaired (2 lens parts).
- **Mechanism:** wear +5–12%/night (gust-dependent). Stall risk = wear% above 60.
  Repair = 1 day-duty + 1 clockwork part.
- **Wrecks:** 0–2 wash ashore per storm. Salvage = 1 duty each. Report = 1 duty each.
  Unreported wreck: +8% ship-loss odds per storm per wreck (compounding, max 6 wrecks).
- **Ships:** 2–5 per night by fury. Base loss odds 12% in fury-3 fog with healthy beam;
  scales with (fog × (1−reach) × hazards).
- **Paths:** erosion events per storm; eroded path = 2× travel time until maintained.
- **Traces:** 5 total; each requires reaching its site (weather-gated, not skill-gated).
- **No dominant strategy check** [game_balance_economist:0b5d7f574911]: full-flame
  heroics drains the reserve by cycle ~9 (dark intervals later); pure rationing
  accumulates loss odds via unreported wrecks and lens cracks. The counter to both
  is the wreck economy — salvage is the only renewable, and it requires reporting.
- **Weakest-option tracking** [game_balance_economist:2770c06f838f]: if playtesting
  shows a duty nobody takes (e.g. path maintenance), it gets buffed or cut publicly
  in the changelog — no zombie duties.
- **Readable tells** [game_balance_economist:694d025cc82f]: every failure state has a
  pre-failure signal (mechanism tick irregularity, lens salt shimmer, tank gauge,
  weather glass at the chart house).

## 13. CRITIC RUBRIC (game_qa_critic seat — the 8.5 gate)
Each round, both scores (self + critic) grade these 10 lines, 0–10 each, weighted:

| # | Line | Weight |
|---|---|---|
| 1 | Zero errors: boots, plays start→finish, exits clean; crash = fail | gate |
| 2 | Job-matters: every duty demonstrably changes outcomes (demo-able) | ×2 |
| 3 | The record: auditable, complete, endings derive from it | ×2 |
| 4 | Island remembers: wrecks/reefs/erosion persist and matter | ×1.5 |
| 5 | Storm: procedural, readable tells, fair, no cheating | ×1 |
| 6 | Performance: ≥30fps steady @1080p medium on T1000 (measured) | ×1 |
| 7 | Feel: third-person control, interact clarity, diegetic UI | ×1 |
| 8 | Audio: synthesized, diegetic, tells present | ×0.5 |
| 9 | Art: one-screenshot rule, readability, warm/cold language | ×1 |
| 10 | Tutorial + accessibility: cycle-1 onboarding, options day one | ×0.5 |

Binding score = LOWER of (self, critic). PASS = ≥8.5. Below → ranked issue list →
fixes → re-round. Max 3 rounds; then honest 3-strikes report. Bug workflow per
[game_qa_critic:e61a7c5dee5a]: filed → confirmed → assigned → fixed → verified →
closed, with repro steps. Verify on target hardware, not only dev machine
[game_qa_critic:16291a2159ac] — the T1000 IS the target; all perf claims from it.

## 14. ASSET LIST (derived from this design — with provenance)
All original or properly licensed; provenance logged per file in assets_blender/PROVENANCE.md.

### Environment (Blender procedural — original)
- Island terrain 240m, ocean plane, cliff rocks ×25, pier (deck+posts), cottage,
  shed, chart house, signal post, wreck hulls ×3, driftwood, fences — all built in
  Blender 5.2.2 via Python API (tools/build_*.py). Provenance: original, this machine.
- Lighthouse: tower (tapered), gallery, lamp room (glazing bars), lamp core, roof,
  interior: spiral stair, 3 landings, log desk, tank, lens assembly (procedural).

### Character (the keeper — ONE character, no others on screen)
- Body + oilskin outfit + hat: built in Blender (procedural base mesh, hand-tuned).
- Rig: Mixamo auto-rigger (provenance: Adobe Mixamo, account "Test", downloaded via
  CDP session; logged per-file). Animations needed (FINAL LIST — replaces the plan's
  provisional note):
  1. Idle 2. Walk 3. Run 4. Climb ladder/stair 5. Carry (oil can) 6. Clean lens
  7. Repair mechanism 8. Pump/transfer oil 9. Write log 10. Row (ending only)
  If Mixamo blocks: fallback = in-Blender procedural walk/run/idle (documented decision).

### Props
- Oil can, barrel, lantern, ledger book, pen, chart, buoy, flare, wrench, cloth,
  gears, lens parts, wick, storm glass, bed, stove, chair, shelf, rope coil.

### FX (in-engine, procedural)
- Rain (GPU sprites), fog volumes, beam (spotlight + volumetric shaft material),
  lightning flash lights, sea foam (material), flare (particle + light), smoke wisp.

### Audio (studio v3 synthesized — see section 10)
- wind_loop, rain_light/heavy, thunder_near/far, sea_loop, lamp_hiss, mechanism_tick,
  mechanism_stall, bell, flare, hull_groan, pen_scratch, page_turn, footsteps
  (wood/rock/mud), ui_tick, inspector_motif.

## 15. BUILD PLAN (sequence — designer LEAD)
1. **M1 Playable vertical slice** (cycles 1–3): island + tower + keeper controller +
   oil/lens/mechanism + one storm + ships + record v1 + save/load + smoke suite.
2. **M2 Full loop** (12 cycles): wreck/reef memory, paths, traces ×5, endings A–D,
   tutorial pass, balance v1 numbers live.
3. **M3 Polish**: ending E, audio pass, art pass (one-screenshot vistas), options,
   critic round 1.
4. **Critic rounds** (≤3): play → screenshots (multi-viewpoint) → scores → issues →
   fixes → re-round. Round history in rounds/.
5. **Delivery**: playable build + spec + screenshots + record demo + round history.

## 16. RISKS
- Mixamo SPA automation may fail → fallback: procedural anims in Blender (decided,
  not a blocker). 15-minute rule applies [Runner rule].
- T1000 VRAM 4GB → texture budget enforced; measured 2480MiB in Step 1.
- Scope: 12 cycles × 5 regions is the MAX. Cut candidates (in order): rowing ending
  beat, ending E secret, path erosion detail. Core job-matters loop is never cut.
- Single-developer reality: every system ships in its simplest honest form first.

## 17. CHANGELOG
- 2026-10-20 v1.0: Spec locked. Engine verdict Unreal 5.8.3 (Step 1, 52fps steady).
  Clouds banned by budget law. Mixamo anim list finalized (10 anims). Balance v1 numbers set.
