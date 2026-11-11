
## W102 - empty-content-with-reasoning run (823ebc5)
ROOT CAUSE of the report-only run death: GLM burned the entire completion
budget on reasoning (the chronology WAS composed - we watched it stream with
[S#] citations) and returned BLANK content 3 consecutive times. The gate and
the W85 landing both fired correctly; the model just had no budget left to
emit content. FIX: the loop run the turn ONCE with thinking disabled
(land in content), then restores standing MAX. Verified build_agent + schemas.

## W104b - NIGHT SUPERVISOR (the mechanism behind "the sequence runs itself")
Owner's challenge accepted: the promise was intent, not mechanism. BUILT NOW:
night_supervisor.sh - a 5-min-cycle supervisor that (1) relaunches any dead
lane run-wrapped with banked assets carried, (2) starts film when the
detective report completes, (3) starts game build when film ships, (4) exits
only when all three are done. Launched persistently (survives session end).
Now the sequence literally does run itself: dead lane -> auto-relaunch with
everything banked; completed lane -> next lane starts.
