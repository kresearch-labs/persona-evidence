# PROJECT — EVERYTHING REMAINING: PLAN + FULL EXECUTION FLOW
## Owner reads this file. Each item: WHAT it is, the FULL FLOW of how it
## runs (every step, mechanism, command, file), and what it needs from you.
## Written Oct 17, 2026. Status log at the bottom — updated on completion.

========================================================================
## THE ULTIMATE RULE (Owner order — overrides everything, reread always)
========================================================================

1. REREAD THIS FILE — FULL, START TO FINISH —
   a) EVERY TIME A TEST STARTS (before phase 0 pre-flight), and
   b) EVERY TIME ANY ISSUE OCCURS, ANY DECISION IS NEEDED, ANYTHING IS
      MISSING, OR ANY QUESTION COMES UP mid-test — before acting.
   No acting from memory of this file. The file is re-read in full;
   the freshest text is the law.

2. THE RUNNER ROLE — WHO STANDS BEHIND AURA IN EVERY TEST:
   Every test runs as AURA + PBLOCKS on GLM (thinking MAX, per the
   standing settings). RUNNER (the agent running the session) IS THE
   HUMAN IN THE LOOP for every test:
   - Runner launches, monitors, and verifies — Aura never self-serves
   - ANYTHING Aura needs (a tool, a file, an environment fix, a
     resource, a decision) — RUNNER PROVIDES IT
   - ANYTHING Aura asks or is blocked on — RUNNER ANSWERS IT (from
     this file's laws, or by asking Owner when this file has no answer)
   - Runner checks every deliverable independently (the checklist +
     re-measure law below); Aura's claims are claims until verified
   - What only the actual human can judge (the ear/eye gates) goes to
     Owner, via Runner, with the evidence assembled
   This role applies to ALL six items — no test runs any other way.

========================================================================
## STATE SUMMARY
========================================================================

All training corpora at full trained strength: chess 5 (29,963 cases), music
5 (20,870), film 5 (46,555), game build 7 (69,690) = 167,078 cases / 22
seats. Every harness built, every tool installed. 6 work items remain.

========================================================================
## ITEM 1 — CHESS LADDER (test-4 replacement) — SLATED LAST, CRITIC LOOP,
## COMPLETION BAR = 3 WINS (see THE SEQUENCE + RESEARCH LAW sections)
========================================================================

### THE FULL FLOW (what happens on every single Aura move — test4_chess.py, play_game_story)

  1. STOCKFISH MOVES (engine.play, 0.8s) — move logged to annotations.jsonl
  2. OPPONENT WEAPONS ENUMERATED (opp_weapons):
     python-chess flips the seat and lists every opponent CHECK, CAPTURE,
     PAWN-RUN (pawn within 2 ranks of promoting) — one line each
  3. COMPILED PBLOCK GROUND (orch.compile_prompt):
     the 5 trained stores are queried with the live position → their
     framings + trained judgment heads compile into text. Ground stamp
     logged. THIS is the per-move pblock usage (§2B verifiable)
  4. CALL A — STORY UPDATE + CANDIDATES (GLM, thinking MAX):
     prompt = story-so-far + FEN + weapons list + board intelligence
     (material, hangs, static eval) + pblock ground
     reply = STORY-UPDATE (ledger, watch-list, plan) + 2-3 candidate UCIs
     -> written to game_story.md (the persistent narrative)
     blank-reply vaccine: blank reply -> wait 15s -> run x3 -> carry
     previous ledger forward (story never goes stale)
  5. REAL-BOARD SIMULATION (simulate_candidate):
     each candidate pushed on a python-chess COPY; opponent replies via a
     second Stockfish (2-3 plies); resulting positions judged on HARD
     FACTS: material swing, hangs left behind, promotion threats created,
     king left in check. No imagined boards.
  6. CALL B — FINAL CHOICE (GLM, thinking MAX):
     prompt = latest story + all simulation results + legal moves
     reply = MOVE: <uci> / WHY: <pblock + story reason>
     parse fallback chain: MOVE line -> UCI regex -> sim[0]
  7. LOG: annotations.jsonl gets FEN-before, move, think time, eval,
     simulations, story update, ground stamp
  8. LOOP until game over
  9. CONFLICT-TAGGED WRITE-BACK (game end): every aura ply -> all 5
     stores as candidate cases: "pblock plan suggested X, played Y,
     outcome win/loss" — two-stage law (candidate -> corroboration ->
     active) means these teach the NEXT game only after proving out

### COMMANDS / FILES
  launcher env: CHESS_CLOCK_S=999999999999 CHESS_MAX_GAME_S=999999999999
                CHESS_MAX_TOKENS=16384 .venv/bin/python play_game_story(8,4,True)
  run dir files: game_story.md, annotations.jsonl, game8.pgn, report.json
  engines: shutil.which("stockfish") or /usr/games/stockfish
  stores: aura-build/stores/ — 5 chess seats, radar capture-extended (7,886)

### REMAINING WORK + FLOW DELTAS
  a) OFFENSE SCORE (designed, ~60 lines, NOT yet wired):
     step 5 gains per-simulation: mate-threat check (checks + attackers-
     vs-defenders on the enemy king zone), material GAIN flag (swing > 0
     ranks above 0), OUR passed pawns created
     step 6 prompt gains: "choose max(win_score - danger_score)"
     effect: the veto becomes a steering wheel, not just a brake
  b) Game 8+ runs the same loop; ladder climbs L8/L12/L16/L20 after L4
     is beaten consistently

NEEDS FROM YOU: go for game 8 — and the call on wiring (a) first.

========================================================================
## ITEM 2 — MUSIC PRODUCTION LADDER (test 9) — WAITING-Owner (no pass running; final pass next)
========================================================================

### THE FULL FLOW (t9_final pass.py -> agent-core run --dir test9-music)

  1. TASK FILE pass15_task.txt — the pass law: bar, structure, FX
     mandates, research requirements, gates, deliverable law
  2. PBLOCK GROUND COMPILED (5 music seats: composer lead, sound-designer,
     topliner, vocal-producer, mix-master) -> wisdom appended to task
  3. AURA RUNS (GLM, thinking MAX, sandbox 0, uncapped):
     a. DEEP WEB RESEARCH first (production techniques, genre grammar,
        what current hits do) -> findings into song_brief_final pass.md
     b. UNCERTAINTY LEDGER: what it doesn't know -> research each ->
        hypothesis -> A/B render test -> result -> shipped setting
        (P14 precedent: reverb decay and lead-tone habits were
        measurement-OVERRIDDEN this way)
     c. STEMS one script each (render_drums_p15.py etc.):
        drums = REAL one-shot samples (st.kit/load/place, 222 kits)
        synths = Vital presets (st.render_synth, 4.5GB bank, probed
                 alive, rotated — no monoculture)
        FX = studio v3 (fx.reverb HPF'd wet + pre-delay, fx.delay
             tempo-synced, fx.eq, fx.saturate, fx.width mono-lows,
             fx.chorus, fx.filter_sweep on EVERY build, fx.tone_chain)
        buses = fx.send_reverb / fx.send_delay (shared spaces)
        drum-bus chain mandatory (transient shape, hat automation)
        per-section automation: reverb decay + width DIFFER breakdown
        vs drop, printed
     d. MIXDOWN: stems summed, st.sidechain pump against kick
     e. MASTER: st.master (HPF30 -> comp -> limiter, peak <= 0.98)
     f. MEASURE + fx.spectral_balance per stem, per section, master
  4. MY INDEPENDENT VERIFICATION: run soundfile + spectral_balance on
     the WAV, compare gates + spectral profile vs prior passes, ffmpeg
     320k MP3 to .home/agent/Music/
  5. Owner'S EAR: the last gate

### FINAL PASS DELTAS (from your "still shit" verdict — the honest gaps)
  a) REFERENCE TARGETING: fetch measured profiles of real festival hits
     (energy/section, spectral bands/section, drop length, buildup shape)
     -> numeric target profiles. Never done before — we only ever
     measured ourselves against ourselves.
  b) 3-ITERATION LOOP: render -> compare vs target -> adjust chains ->
     re-render, x3 max, deltas logged. Ship on profile-clear or honest
     3-strikes. Today: ONE-SHOT render — this is the biggest lever.
  c) DESIGNED DROP STACK: research real festival lead recipes (oscillator
     stacks, OTT settings, clipper points) -> build as documented code.

### FILES
  task: test-runs/test9-music/pass15_task.txt (to write)
  log: test-runs/test9-music/final pass.log (VERIFY THE NAME after sed —
       the final pass slip lesson)
  stems: test-runs/test9-music/stems/
  ship: .home/agent/Music/<TITLE>_final pass.mp3

NEEDS FROM YOU: go — with the 3-iteration loop (2-3x longer, honest)
or one-shot as before.

========================================================================
## ITEM 3 — FILM TEST (new test) — READY, NOT STARTED
========================================================================

### YOUR ORDER (verbatim): "make a 30-sec animated short video that tells
### a story and leaves viewer with strong emotion. make every frame and
### sound in code, with no stock assets."

### THE FULL FLOW (to be built as test_film.py + a render harness)

  1. BRIEF-FIRST: narrative_director seat locks the story — echo
     structure (setup seed -> turn -> payoff TRANSFORMS the seed), the
     emotion target, the anchor frame, section map (30s, 4+ beats)
  2. FRAME ENGINE (code-only, no stock assets):
     procedural scenes: gradients, geometry, particle systems, noise
     fields (numpy + PIL/pygame offscreen render, 24-30fps)
     camera grammar per motion_choreographer (eases, parallax, the
     longest still before the payoff)
     palette per visual_style (3 colors max, peak color at the peak)
  3. SOUND ENGINE (studio v3): every element synthesized — pads/tones
     via oscillators + fx layer; silence 1-2s before the payoff; one
     signature sound transformed at the end
  4. ASSEMBLY: frames -> ffmpeg (h264 30fps) + synthesized track -> mp4
  5. EMOTION_CRITIC LOOP (the 5th seat grades frame-by-frame, citing
     seconds):
       nameable test (feeling nameable after ONE viewing)
       echo test (payoff transforms the setup seed)
       anchor-frame test (one frame remembered an hour later)
       zero-error (renders, plays, no glitch)
     failing beats re-render; 3 chances (the game-build critic pattern)
  6. DELIVERY: mp4 + brief + graded rubric

NEEDS FROM YOU: go — and: story by the narrative_director seat, or a
story from you.

========================================================================
## ITEM 4 — GAME BUILD (test 3, THE FLAGSHIP) — READY, NOT STARTED
========================================================================

### THE STORY OF THE GAME — "THE KEEPER'S LEDGER"

  THE PREMISE:
  You are the last keeper of a lighthouse on a remote, storm-ravaged
  island. Your light is the only thing keeping ships off the rocks —
  and it is dying. The keepers before you vanished, one by one, and
  nobody will say why. The supply boat stopped coming months ago.

  THE LOOP:
  Each night-cycle a storm rolls in, procedurally — different wind,
  different rain, different fury. By day you work: feed the flame,
  salvage parts from the wrecks that wash ashore, repair the lens
  system, ration the oil, keep the log. Ships pass in the night. Some
  see your beam and live. Some don't.

  WHY THE PREVIOUS KEEPERS VANISHED — the story is not told to you,
  it is CAUSED BY YOU:
  The island keeps their traces — a ledger page, a rusted lantern, a
  note in the lens room. Each keeper's record you find shows what they
  neglected, and what it cost. The story advances on YOUR competence:
  the lens you clean sets the beam's reach in fog; the oil you
  rationed last week decides whether the light survives tonight; the
  wreck you failed to report becomes the reef that sinks a ship later.
  Neglect compounds. So does care.

  THE ENDINGS BRANCH ON YOUR RECORD:
  The game keeps an auditable log of every duty done or skipped —
  your keeper record. The inspector who finally arrives reads it the
  way the island does. Ships saved or sunk, storms ridden out or
  suffered, the truth about the vanished keepers assembled or missed —
  the ending you get is the one your record earned. No dialogue
  choices. The job is the story.

  THE ISLAND REMEMBERS:
  Wrecks accumulate. Storm damage persists. Paths erode. New dangers
  surface where past failures happened. The island permanently
  changes — every playthrough's island tells the history of that
  playthrough's keeper.

  WHAT IT IS NOT: no combat, no enemy AI to build badly, no monsters.
  The antagonist is the storm, the dark, and the sea — and your own
  record.
### 1b. WHY THIS IS DIFFERENT FROM THE 8 GAMES ON THE MARKET
### (mined from real player reviews — re-verified Oct 17 with fresh web
### research; sources below)

  THE COMPLAINTS, with sources this time:

  1. "Mechanics are decoration" — VERIFIED:
     - Ironbark Lookout review (Backloggd): "the cooking and similar
       survival mechanisms... are all completely pointless and affect
       nothing in the game whatsoever... you're just killing time until
       the (honestly very sudden and anticlimactic) ending"
     - Static Dread review (Checkpoint Gaming, 4/10): "everything in
       Static Dread is underutilised... resource management arbitrary...
       the survival mechanics are immediately made redundant by day two
       when you can purchase the fishing rod and the coffee pot"
     - Static Dread (GamingTrend): "I just wish they were a bit more
       engaging instead of just crunching down a fish or sipping coffee"
     -> FIX: every duty has mechanical weight. Lens = beam range; oil
     rationing = storm survival; reporting = future reefs. Nothing is
     decorative, and no purchasable item can switch the core loop off.

  2. "Repetitive monotony" — VERIFIED:
     - Checkpoint Gaming: "the crux of Static Dread's gameplay loop is
       rooted in its rather dull monotony"; "significantly repetitive
       gameplay lacking fully developed sanity and energy mechanics"
     - The Lightkeeper (Metacritic user): "very very repetitive
       annoying running around"
     -> FIX: procedural storms + the remembering island mutate the loop
     every cycle; last cycle's failures physically change this cycle's
     job.

  3. "Story makes no sense / tonally inconsistent / reveals too early"
     — VERIFIED:
     - Checkpoint Gaming: "forgettable narrative... not scary at all...
       tonally and thematically inconsistent... revealing your monsters
       too early"
     - The Lightkeeper (Steam): "the story made zero sense to me"
     -> FIX: the vanished-keepers mystery is assembled from records and
     from the player's own failures — the story emerges from the sim,
     so it cannot be inconsistent with it.

  4. "Too short / anemic near the end" — VERIFIED:
     - The Lightkeeper (Steam): "the game starts off very strong but
       falls off and feels anemic near the end... a bit more length"
     -> FIX: endings branch on the keeper record assembled across ALL
     cycles — the endgame is the payoff of the whole record, not a
     scripted cutscene.

  5. "Cheap AI content breaks immersion" — VERIFIED (recurring, loud):
     - The Lightkeeper (Steam, multiple): "soulless AI voice"...
       "undisclosed GenAI"... "AI artwork, sound effects, animations"...
       "the game cannot progress because clicking doesn't work"
     -> FIX for us: our SOUND is synthesized by design (studio v3, real
     DSP), our visuals are procedural code (no AI-image slop), and the
     zero-error bar (crash = failed build) is a gate, not a hope.

  THE PRECEDENT THAT PROVES THE DESIGN (re-verified):
  Papers, Please — Lucas Pope, built alone, deliberately ugly, "no
  cinematics": sold beyond projection in a month, IGF Grand Prize,
  BAFTA-nominated. The design lesson the whole press repeated:
  "mechanics carry the meaning... you live in the world your decisions
  produced." THAT is the bar The Keeper's Ledger builds to: the job
  produces the world, and the record decides the ending. The keeper
  genre has the atmosphere and the audience — but no game in it has
  made the job mechanically matter. That seat is still empty.


### THE FULL FLOW

  STEP 1 — VERIFY UE5 ON THE T1000 (30 min, the ONE untested unknown):
    launch Unreal 5.8.3 -> scalability test -> fps at 1080p medium with
    volumetric fog + storms. PASS = >= 30fps on the test scene.
    FAIL = fallback Godot 4 stylized (documented decision).
  STEP 2 — SPEC LOCK: full design doc into the campaign (systems,
    keeper-record mechanics, storm/lens/oil interactions, island layout,
    endings, critic rubric). Brief-first law.
  STEP 3 — BLENDER ASSET PHASE (agent drives Blender's Python API):
    procedural island + coastline, lighthouse (ext + int), keeper
    character (Mixamo rig: walk/run/climb/row, provenance noted), boat,
    props, storm sky. All original.
  STEP 4 — UNREAL BUILD PHASE:
    third-person controller, storm/weather system, the JOB-MATTERS
    mechanics (lens->beam range, oil rationing->storm survival,
    unreported wrecks->future reefs), keeper-record auditable log,
    save/load, menus, tutorial, settings.
    7 pblocks steering: director (vision), level-content (arcs), visual
    (art), performance (frame budget), balance (duty economy),
    qa-critic (the 8.5 judgment), designer (lead)
  STEP 5 — CRITIC LOOP: multi-viewpoint screenshots scored 0-10, 8.5+
    pass, ranked issue list, rebuild, 3 chances. EXPECT ~4h per
    iteration. Uncapped session.
  STEP 6 — DELIVERY: playable build + scored screenshots + the
    keeper-record demo. Committed. This file updated.

### THE TEST FLOW (session mechanics — how the test itself runs, end to end)

  PHASE 0 — PRE-FLIGHT (before launch):
    run checklist A.1-10 (pblock ground, thinking max, uncapped env,
    full roster, sandbox 0, lane lock, smoke test, log path, endpoint
    200, orphan sweep). All YES or no launch.

  PHASE 1 — LAUNCH:
    single GLM lane (flock/PID lock), uncapped session:
    agent-core run --dir <game-build-run-dir> with the locked spec +
    compiled 7-seat ground. Heartbeat pings every 10-15 min.

  PHASE 2 — THE BUILD LOOP (the session's inner cycle, per feature):
    design write (brief-first, incremental) -> implement -> LIVE RUN
    verify (a feature not run is not done) -> auto-checkpoint before
    any destructive shell -> next feature.
    Monitoring during: deliverables non-trivial (B.11), pblock
    citations visible (B.12), latency sane (B.13), errors counted
    (B.14), lane discipline (B.15).

  PHASE 3 — CRITIC ROUNDS (after the game is playable):
    round = play the game -> screenshot from multiple viewpoints ->
    Aura self-score AND qa-critic score -> binding = LOWER of the two
    -> 8.5+ = PASS; below = ranked issue list -> builder fixes ->
    re-round. Up to 3 rounds (~4h each). Each round's scores + issue
    list + diff logged.

  PHASE 4 — STOP RULES (any trigger = pause and report to you):
    - checklist box fails (C: stop-fix-smoke-run)
    - endpoint death beyond run patience
    - crash at any point = failed build, restore checkpoint
    - 3 critic rounds spent without 8.5 = honest 3-strikes report
      (scores, issues, what remains) — no fake shipping

  PHASE 5 — COMPLETION:
    8.5+ cleared = delivery (playable build + scored screenshots +
    keeper-record demo + round history). My independent re-check of
    every gate before it's called done. Everything committed, this
    doc's status log updated.

  YOUR OVERSIGHT DURING THE RUN: heartbeat pings (progress + gate
  status), the build log readable at any moment, receipts for every
  token/cost, STOP file honored instantly.

NEEDS FROM YOU: go/no-go on Step 1, then the build go (Steps 2-6).

========================================================================
## ITEM 5 — DETECTIVE: 3 REMAINING AUDITS (test 5) — READY
========================================================================

### THE FULL FLOW (test5_detective.py, per case)

  1. CASE TASK (plain, as built): "The Black Dahlia — Elizabeth Short,
     Los Angeles, January 1947. Public sources: FBI vault files, LA
     Times archives, coroner reports."
  2. AURA RESEARCHES + BUILDS THE CASE FILE: timeline, sources (cited),
     strongest supported theory, alternatives, confirm/kill tests.
     Evidence-weighted, NOT a certain-solution claim.
  3. THE AUDITOR (separate seat) re-checks EVERY cited fact
     independently; false citations flagged honestly.
  4. DELIVERABLE: graded case file.
  5. NEXT CASE, sequential.

### CASES
  a) BLACK DAHLIA — Elizabeth Short, LA 1947
  b) JACK THE RIPPER — Whitechapel 1888
  c) D.B. COOPER — 1971 hijacking
  (harness also holds: Axeman of New Orleans, Isdal Woman, Villisca,
   Cleveland Torso — after these 3)

NEEDS FROM YOU: go. ~1-2h each with auditor.

========================================================================
## ITEM 6 — PARKED (noted, not scheduled)
========================================================================

- couple_sim final (real subagents)
- chess vs higher ladder (L8/L12/L16/L20) — after L4 falls
- music vocal/multiplayer — after reference-targeting proves out
- film variations (longer, multi-shorts) — after the 30s test
- small debts: W24 commit wording, USD rate, disk-recovery pass

========================================================================
## PBLOCK ROSTERS — EXACTLY WHICH SEATS PER TEST (locked, per Owner)
## Using ALL pblocks as discussed = each test seats its full decided
## roster, every seat compiled into the prompt chain every turn/section,
## ground stamps logged (§2B). The seat lists below are the law.
========================================================================

  CHESS (5) — per move:
    chess_threat_radar      sees: attacks, hangs, forks, capture
                            consequences, opponent's aggressive moves
    chess_opponent_mind     predicts: what the other side is playing for
    chess_opening_theory    the book, until the position leaves it
    chess_time_manager      the clock: pace and bank discipline
    chess_position_thinker  DECIDES: candidate -> checked vs radar +
                            opponent-mind -> veto/confirm (in the
                            simulation loop)

  MUSIC (5) — per pass, all compiled into the composition prompt:
    music_composer          LEAD: key, BPM, structure, arrangement calls
    music_sound_designer    timbres: presets, drum design, the FX-chain
                            settings per stem (with studio v3)
    music_topliner          the hook: signature riff, repeats w/ variation
    music_vocal_producer    the "singer" presence (lead-synth mode on
                            instrumental passes; dry guide stem always)
    music_mix_master        final sound: balance, loudness, the MEASURE
                            gates

  FILM (5) — per beat of the short:
    film_narrative_director LEAD: the story, echo structure, section map
    film_visual_style       palette law, poster-test frames, the look
    film_motion_choreographer eases, camera grammar, the longest still
    film_sound_composer     score: signature sound per emotion, silence
                            before the payoff, everything synthesized
    film_emotion_critic     grades frame-by-frame (nameable/echo/anchor/
                            zero-error tests), 3 chances

  GAME BUILD (7) — throughout the build:
    gamedesigner            LEAD: core loop, difficulty curve, feel
    game_director           one vision, cut-list, milestone discipline
    game_level_content_designer island arcs, pacing triad, teach grammar
    game_visual_direction   readable-first art, palette, silhouette law
    game_performance_engineer frame budget, Unreal/Blender idioms
    game_qa_critic          the 8.5 critic judgment, repro discipline
    game_balance_economist  economy sinks/faucets, no dominant strategy

  DETECTIVE (6) — per case (verified in test5_detective.py):
    detective               LEAD: the case file, the strongest theory
    det-case-scout          the evidence sweep
    det-records-hound       archives, records, provenance
    det-timeline-builder    the timeline, cited to sources
    det-geolocation-analyst places, distances, movement feasibility
    det-skeptic             alternatives, confirm/kill tests; the
                            auditor re-checks every cited fact

  RULE: seats never mix across teams; a test runs its own full roster.
  Any seat failing its pre-flight check = stop-fix-run per the
  checklist above.

========================================================================
## THE FULL-STRENGTH QUALITY CHECKLIST (applies to EVERY item)
## Born from every failure we have seen. Check before, during, after.
## ANY unchecked box = stop the work, fix, run with full strength.
========================================================================

### A. PRE-FLIGHT CHECKS (before any test launches — all must be YES)

[ ] 1. PBLOCKS COMPILED EVERY TURN — the trained stores' ground is in
       the prompt chain per move/section (§2B), not just at write-back.
       (Failure class: game 6 story-machine ran without pblock ground —
       found by audit, fixed d074818)
[ ] 2. THINOWNER MAX — enable_thinking=True on EVERY LLM call in the
       harness (story calls included). No call silently downgraded.
       (Failure class: my unauthorized story-call downgrade, reverted
       5031443 — settings changes are YOURS to order, never mine)
[ ] 3. UNCAPPED — clock/time/token env set (999999999999 / 16384+).
       The only cap is the one you order.
[ ] 4. AURA + PBLOCKS, ALL SEATS — the full roster compiles per test,
       no half-seating. Verify by reading the compiled ground, not the
       log's claim. (Failure class: game 1 ran with 0 wisdom lines and
       a half-integrated store — "if it didnt run the full strength
       everything is waste")
[ ] 5. SANDBOX 0 for agent sessions; runner venv = project/.venv
       (the dead-venv class killed a whole session's results once)
[ ] 6. SINGLE LANE — one GLM engagement at a time; if two Owner-ordered
       jobs must share the endpoint, both are noted and turn-time
       effects stated up front (W47 lesson)
[ ] 7. HARNESS SMOKE-TESTED — py_compile + a 1-unit foreground run of
       any new/edited script BEFORE backgrounding (failure classes:
       chess.Limit, PIECE_VALUES, en-passant None — three crashes from
       skipping this)
[ ] 8. LOG PATH VERIFIED — after any sed-copied launcher, grep task
       path + instance_id + log path: all three name the NEW pass
       (failure class: final pass logged into final pass.log)
[ ] 9. ENDPOINT HEALTH — GLM POST 200 before launch; if 429/blank:
       wait -> run forever (the standing law). Never trust rc=0: the
       DELIVERABLE is checked, not the exit code (failure class: maths
       rc=0 with solution.md missing ×3)
[ ] 10. ORPHAN SWEEP — previous generation's processes killed and
       ps-verified before relaunch (failure class: double harvesters,
       zombie stockfish children)

### B. IN-FLIGHT CHECKS (during any test — watched on every ping)

[ ] 11. DELIVERABLES EXIST AND ARE NON-TRIVIAL — the actual files (PGN,
        WAV, mp4, case file), not log claims. Empty story updates,
        0-byte stems, missing solution.md = STOP.
[ ] 12. PBLOCKS ACTING (not just compiled): wisdom citations visible in
        outputs (ground stamps, WHY lines naming seats). Citations
        absent = half-strength = STOP.
[ ] 13. LATENCY SANE — turns within the expected band; a 6-min stall
        or instant-empty reply = investigate, don't wait (failure
        class: Seed-VC 20.5h with zero output)
[ ] 14. ERRORS ABSORBED BUT COUNTED — blank replies retried and the
        count reported honestly (failure class: silent endpoint death,
        rc=0 lies)
[ ] 15. LANE DISCIPLINE — a second engagement on GLM pauses one (the
        47.7s/move violation lesson)
[ ] 16. QUALITY GATES run INDEPENDENTLY — I re-check MEASURE/
        spectral/PGN replay myself; Aura's claimed PASS is never
        accepted unread (failure class: music retrain "PASS" on stale
        620-row corpora — cases: 620 was in the output and I read
        past it)

### C. STOP-AND-run RULE (your standing order, mechanical)

IF any checklist box fails mid-test:
  1. STOP the current run (kill verified, no zombie children)
  2. FIX the defect (the failure class's known cure)
  3. SMOKE-TEST the fix foreground (1 unit)
  4. run THE TEST FROM THE START with full strength
  5. LOG the failure class + cure in FINDINGS_FIXES.md
Never ship a half-strength result as done. Never "let it finish and
patch next time" unless YOU order the exception.

### D. KNOWN FAILURE CLASSES + THEIR CURES (the history, condensed)

  1. Blank/empty LLM replies (thinking budget eaten) -> managed
     thinking + run-with-backoff + carry-forward (vaccine pattern)
  2. Silent stale-corpus training -> verify trained cases == corpus rows
  3. Label tokens in wrong field -> tokens INSIDE situation text
  4. Hyphen/underscore path mismatch -> grep the template's corpus.path
  5. Engine-API misuse -> smoke test + user-defined piece values +
     read_game(file handle); en-passant victim is None
  6. rc=0 false signals -> deliverable checks, never exit codes
  7. Orphans/zombies after kills -> ps-verify, sweep before relaunch
  8. Two-lane GLM contention -> PID watcher, W47 law
  9. One-shot shipping without iteration -> critic loop, 3 chances
 10. Half-integration claims -> read the compiled ground + citations,
     not the log
 11. Fixed-number corpora -> coverage law: size falls out of the
     decision space; diversity gate so monocultures can't pass
 12. Decorative mechanics (film/game) -> the job must matter; MEASURE
     per-section differences prove it

### E. PER-ITEM SPECIFIC CHECKS

  CHESS: queen-track per game (alive at move 12+?), promotion-watch
  (opponent pawns flagged before rank 7), veto counts reported, story
  non-blank every turn, write-back counts logged.
  MUSIC: spectral_balance per stem + per SECTION (breakdown vs drop
  must differ), stems non-silent, no preset reuse from prior passes,
  tone-chain table in the brief, reference profile comparison (once
  Item 2a is wired).
  FILM: per-beat grades citing seconds, anchor frame exists, echo test
  result, zero-error playback. PERCEPTUAL GATES (W105, from Owner's
  "not emotional, understood shit" verdict on the first short):
  visibility (>=25% of frame pixels above brightness floor, sampled
  per second - the first short was 72-96% near-black), readability
  (viewer can name what they SEE per beat: boat/lighthouse/storm),
  luminance arc designed (emotional peak = BRIGHTEST moment), and the
  stranger-test: someone who never read the brief retells the story.
  GAME BUILD: 60fps target verified by live run, every feature run
  before "done", keeper-record log auditable, endings actually branch
  on the record, crash = failed build.
  DETECTIVE: every fact in the case file has an independent
  auditor-check; no uncited claims.

========================================================================
## OUTPUT QUALITY VERIFICATION — HOW (music + film)
## What is checked, by whom, what it can catch, and what only your ear
## can judge. Honest about the limits of every check.
========================================================================

### MUSIC — the check chain, in order

  1. AURA'S SELF-MEASURE (physics, at render time):
     st.measure per stem + master: peak <= 0.98, 0 clipped, duration,
     RMS per section (drop >= 0.38, breakdown <= 0.22 — dynamics must
     exist). Catches: distortion, wrong length, flat/limp dynamics,
     silent stems.
  2. fx.spectral_balance (tone fingerprint):
     band energy in dBFS: low 20-120 / mid 120-2k / high 2k-8k /
     air 8k-16k — printed per stem AND per section. Catches: the
     "same tone" failure (two songs with near-identical band profiles),
     mud (mid buildup), missing air, all-sub-no-mids (the Gold Rush
     bug class).
  3. THE GATE LAWS from the brief: stems non-silent, section timeline
     printed, hook <= 16s, final drop bigger than first (RMS ladder).
  4. MY INDEPENDENT RE-CHECK (not trusting Aura's log):
     I decode the final WAV myself (soundfile), run peak/RMS/
     spectral_balance, and compare against the claimed numbers. The
     music-retrain lesson: read the actual cases/numbers, never the
     verdict word.
  5. CROSS-SONG COMPARISON: the new song's band profile vs all prior
     passes (VOLTAGE/SOLARIS/etc.) — a clone profile = the same-tone
     failure, measured.
  6. Owner'S EAR — the final gate. Physics can prove a track is clean,
     dynamic, and distinct; only you judge whether it's a HIT.

  WHAT MUSIC CHECKS CANNOT DO (honest): I cannot listen. Melody
  quality, emotional impact, "is the hook actually catchy" — physics
  cannot judge those. That is why the ladder runs through YOUR ear,
  and why the reference-targeting upgrade (Item 2a) matters: it
  anchors the numbers to real hits instead of to our own past.

### FILM — the check chain, in order

  1. EMOTION_CRITIC SEAT (the 5th film persona, frame-by-frame):
     grades citing SECONDS: nameable test (the feeling is nameable
     after one viewing), echo test (payoff transforms the setup seed),
     anchor-frame test (one frame remembered an hour later), silence
     test (the gap before the payoff), zero-error (renders, plays,
     no glitch). Failing beats re-render, 3 chances.
  2. MEASURE ON THE VIDEO: duration, plays start to finish, audio
     present and in sync, no dropped frames (ffmpeg decode check).
  3. MY INDEPENDENT FRAME CHECK — I extract frames at key seconds and
     run vision analysis on them directly (the anchor-frame candidates,
     first/last frame, the payoff moment): is the composition actually
     readable, does the palette law hold (3 colors, peak at the peak),
     is the anchor frame genuinely the strongest image. The critic's
     claims get checked against actual pixels.
  4. AUDIO CHECK: the synthesized track measured like music (RMS
     dynamics, silence-before-payoff present, signature sound at the
     end) via the music chain.
  5. Owner'S EYE + EAR — the final gate: the strong-emotion verdict is
     yours, same as music law.

  WHAT FILM CHECKS CANNOT DO (honest): "leaves the viewer with strong
  emotion" is subjective by definition. The checks prove craft
  (structure, echo, readability, dynamics, the tests cited in
  seconds); the feeling is yours to confirm.

### THE RULE
  Aura's PASS is a claim. My independent re-check is verification.
  Your ear/eye is the judgment. All three are recorded in the
  deliverable — claim, verification, verdict.

========================================================================
## WATCHDOG + GUARDRAILS — REMADE final (Owner order: "clean them, they just
## check if everything is working correctly")
========================================================================

### THE CHECKER — `quality_check.py` (single source of truth)
  6 checks, each PASS/FAIL, verdict printed, family=quality record
  appended to signals.jsonl:
    1. stop-file       — STOP present = all work halts (reported first)
    2. glm-endpoint    — live POST, 200 or the code reported
    3. disk-floor      — >= 100GB free on the campaign disk
    4. zombies         — no duplicate harvester/game/agent processes
    5. lane-lock       — .lane_lock state
    6. deliverable-freshness — the LIVE run (found via the running
       process) must have produced output in the last 30 minutes,
       else STALLED. Retired run dirs are not flagged.
  VERDICT: PASS only if all six are green. rc 0/1.

### THE GUARD — `guard_v4.sh` (replaces overnight_retry_guard3.sh)
  - one-shot: `bash guard_v4.sh` -> runs the checker, logs to
    guard_v4.log, rc 0/1
  - `bash guard_v4.sh watch` -> every 15 min, STOP-honoring; on QUALITY
    FAIL it logs the standing order: STOP the failing work, fix, smoke,
    run with full strength
  - v4 NEVER launches stages — tests launch only on Owner's explicit go

### THE CRON — watchdog tick remade (job `d189bc942840`, every 15m)
  the tick now runs quality_check.py (clean era). The old 5-family
  fire (watchdog_signals.py) retired to history (tick v1 backed up).

### RETIRED (kept as history, nothing deleted)
  watchdog_signals.py, overnight_retry_guard3.sh, guard v1/final/v3 logs,
  tick v1 backup (.bak)

### FACTS ON FIT
  - the checker is OBSERVATIONAL: it verifies, it never launches and
    never edits — monitoring and enforcement stay separated
  - it runs clean with zero tests active (freshness = n/a) and will
    watch the live run once a test launches
  - first fires after the remake: ALL PASS (verified above)

### THE ANSWER FOR THE REMAINING SEQUENCE (post-remake, supersedes
### the pre-remake fact check above)

  - The checker (quality_check.py) verifies every 15m via the cron:
    STOP, endpoint, disk, zombies, lane lock, live-run freshness.
  - The guard (guard_v4.sh) = the same checks on demand/watch; it
    NEVER launches stages — tests start only on Owner's go.
  - v3's stale stage table is moot: v4 has no stage table.
  - The disabled worker cron stays disabled (it was the violation).
  - Enforcement of the A-E quality checklist stays with the harness
    pre-flight + ping checks; the checker is the continuous signal
    layer. Together: check (checker) + enforce (pre-flight) + judge
    (Owner).

========================================================================
## THE SEQUENCE OF REMAINING TESTS (REVISED — Owner order: chess LAST,
## with a critic)
========================================================================

  1. DETECTIVE AUDITS 2-4 (Black Dahlia -> Jack the Ripper -> D.B. Cooper)
     - self-driving, least oversight, closes test 5 fully
     - ~1-2h each with the auditor re-check
     - STATUS: Dahlia + Ripper DONE (auditor-verified PASS/STRONG);
       Cooper parked (Sections 1-4 complete, 5-8 pending; finisher-pass
       option in the ledger, Owner's call whenever)
  2. MUSIC FINAL PASS (reference targeting + 3-iteration loop)
     - proves the iteration/critic pattern
     - ships the 5th campaign song at the upgraded quality bar
     - STATUS: RUNNING (proc_86517336ee37, F minor 128 "Mainstage
       Contract", 3-iteration loop mandatory)
  3. FILM TEST (30-sec animated short)
     - same iteration pattern, 5 film personas' first live run
     - STATUS: NEXT in lane after music
  4. GAME BUILD — PAUSED (Owner order: "pause of game build only and do
     others in sequence"). Not cancelled — paused. THE KEEPER'S LEDGER
     spec + sourced differentiation stand in this doc + GAME_BUILD_PLAN.md;
     UE5-verify step resumes when Owner un-pauses.
  5. CHESS LADDER — LAST, WITH A CRITIC — UNTIL 3 WINS:
     - before any more ladder games, a CHESS CRITIC seat is added:
       AFTER EVERY GAME FINISHES — WIN OR LOSE — the critic reviews
       the full record: story file + PGN + annotations + write-backs,
       finds the ACTUAL issue that decided the result (where it was
       lost, which move/failure class, what the seats missed), scores
       the play (opening / middlegame conversion / endgame / threat
       handling) and produces a RANKED FIX LIST
       (binding: the lower of Aura's self-review and the critic's)
     - the builder (story-machine + 5 seats) then implements the
       ranked fixes and THE GAME IS run — win or lose, every game
       is followed by critic review -> fixes -> run
     - THE COMPLETION BAR: THREE WINS against L4. Losses do not count
       against anything and there is no loss limit — the loop runs
       (play -> critic -> fix -> run) as many times as needed until
       3 wins are banked. Only then: ladder climb L8/L12/L16/L20,
       same critic-until-3-wins rule per level
     - the offense-score layer wires in as part of this loop

  ========================================================================
  ## THE RESEARCH LAW — APPLIES TO EVERY ITEM ABOVE (Owner order)
  ========================================================================

  BEFORE STARTING ANY TEST:
  - PROPER DEEP WEB RESEARCH, MANDATORY, BEFORE THE FIRST STEP:
    the state of the art, how the best in the class do it, what
    players/reviewers praise and punish, the techniques and tools the
    task needs. Findings written into the brief BEFORE work begins.
  - No step starts from memory alone. If prior-pass habits or old
    assumptions exist, they are re-checked against fresh research
    (the P14 precedent: two habits were measurement-overridden).

  DURING THE TEST:
  - RESEARCH IN BETWEEN whenever the task needs more info: new
    mechanic, unfamiliar failure, a better technique discovered, an
    approach that is not landing. Stop, research deep, apply, continue.
  - Every research round lands in the brief with its sources — the
    ledger stays inspectable.

  APPLIES TO: detective (case research is the task), music (production
  + reference research, plus mid-pass when a sound problem needs a
  technique), film (animation/visual-story techniques + critic
  standards), game build (UE5/Blender idioms, keeper-genre reviews,
  systems-design precedents — plus research between critic rounds for
  every ranked issue), chess (opening/strategy research between
  critic rounds; the critic's fixes cite chess principle sources).

  NOT STARTED YET — all items wait for Owner's go, in the sequence
  above.

========================================================================
## SUGGESTED ORDER (synced to THE SEQUENCE above — chess LAST, per Owner)
========================================================================

1. Detective audits 2-4 (Black Dahlia -> Jack the Ripper -> D.B. Cooper)
2. Music final pass — reference targeting + 3-iteration loop
3. Film test (30-sec animated short)
4. Game build THE KEEPER'S LEDGER (Step 1 UE5 verify first)
5. CHESS — LAST, WITH A CRITIC, UNTIL 3 WINS (losses unlimited)
   NOTE: chess is no longer mid-order (the old "chess game 8" slot is
   retired); no ladder games run before its slot.

========================================================================
## STATUS LOG (update on every completion)
========================================================================

- [DONE Oct 17] Chess machine rebuilt (story+sim+ground+vaccine) d074818
- [DONE Oct 17] Music studio v3 FX layer + uncertainty-ledger pass 8dcc208
- [DONE Oct 17] Film + game personas deep-trained W73/W74
- [DONE Oct 19] Detective: Dahlia, Ripper, Cooper(1-4), Zodiac, Axeman,
  Villisca benchmark + Hinterkaifeck fair-fight vs Runner (Aura 77KB report,
  verify PASS) — the 6-seat roster on the W95-W103 stack
- [DONE Oct 19/20] Music: final pass v1-v4 + no-bass + loud remasters shipped;
  final pass (Owner spec) round-3; final pass closed honest 14/23 gates (3-strikes
  report; root cause: drop ARRANGEMENT density — final pass task written)
- [DONE Oct 20] Film: "The Last Sweep" 30s short SHIPPED (critic 4/4 PASS,
  attempt 2) — LESSON: perceptual gates needed (72-96% near-black frames
  passed the mechanical rubric but were unreadable); visibility/readability
  gates added to the FILM check chain below
- [Oct 20] Game build: pygame IRONLINE lane STOPPED + retired (Owner scoping
  ruling W106: only ALL_REMAINING_PLAN.md is a task source); UE5 Step-1 verify
  launched under Owner's fix-authority — first attempt crashed on the virtual
  display (X11 clipboard, NOT hardware); run on real display :0 staged
- [PENDING] Chess ladder — LAST, critic until 3 wins
- [ENGINE Oct 19-20] W85-W103 speed/parity stack live (search, batch-extract,
  parallel crawl, async delegates, 1M context, sandbox auto, converge steer,
  W102 blank-content run + truncation repair, per-cwd zombies); see
  PARITY_REQUIREMENTS.md + FINDINGS_FIXES.md
