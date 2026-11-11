# Incident Log — Aura SWE-bench Verified Campaign

Compiled from driver.log, logs/watchdog_supervisor.log, logs/serial_finisher.log,
per-run stderr scans and the w10 third-attempt log. Sorted by timestamp.

| timestamp | instance | arm | type | description |
|---|---|---|---|---|
| 2026-10-30 19:34:08 | django__django-11532 | nopanel | STALL | wave 2: log idle 1000000000s -> kill+retry |
| 2026-10-30 19:34:08 | django__django-11532 | panel | STALL | wave 2: log idle 1000000000s -> kill+retry |
| 2026-10-30 19:34:08 | django__django-14631 | panel | STALL | wave 3: log idle 1000000000s -> kill+retry |
| 2026-10-31 11:49:10 | matplotlib__matplotlib-13989 | nopanel | CLOSED-UNVERIFIED | wave 3: finished diff=482B, receipt not 'completed' (rc: Not finished — not written: bug.) |
| 2026-10-31 12:00:15 | matplotlib__matplotlib-20859 | nopanel | CLOSED-UNVERIFIED | wave 3: finished diff=761B, receipt not 'completed' (rc: Not finished — not written: bug., legend) |
| 2026-10-31 12:40:32 | matplotlib__matplotlib-13989 | panel | CLOSED-UNVERIFIED | wave 3: finished diff=482B, receipt not 'completed' (rc: Not finished — not written: bug.) |
| 2026-10-31 12:52:33 | matplotlib__matplotlib-20859 | panel | CLOSED-UNVERIFIED | wave 3: finished diff=761B, receipt not 'completed' (rc: Not finished — not written: bug., legend) |
| 2026-10-31 14:58:34 | matplotlib__matplotlib-25311 | nopanel | CLOSED-UNVERIFIED | wave 4: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-10-31 15:59:33 | mwaskom__seaborn-3069 | panel | CLOSED-UNVERIFIED | wave 4: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-10-31 16:22:37 | pydata__xarray-3095 | panel | CLOSED-UNVERIFIED | wave 4: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-10-31 17:36:14 | scikit-learn__scikit-learn-12973 | nopanel | CLOSED-UNVERIFIED | wave 4: finished diff=1403B, receipt not 'completed' (rc: Not finished — not written: it.) |
| 2026-10-31 17:42:14 | scikit-learn__scikit-learn-11578 | nopanel | CLOSED-UNVERIFIED | wave 4: finished diff=674B, receipt not 'completed' (rc: Not finished — stopped: write_file keeps) |
| 2026-10-31 18:23:50 | scikit-learn__scikit-learn-12973 | panel | CLOSED-UNVERIFIED | wave 4: finished diff=1381B, receipt not 'completed' (rc: Not finished — not written: it.) |
| 2026-10-31 18:40:55 | sphinx-doc__sphinx-10614 | nopanel | CLOSED-UNVERIFIED | wave 5: finished diff=1310B, receipt not 'completed' (rc: Not finished — not written: issue.) |
| 2026-10-31 18:43:55 | sphinx-doc__sphinx-11510 | nopanel | CLOSED-UNVERIFIED | wave 5: finished diff=2999B, receipt not 'completed' (rc: Not finished — not written: conf.py) |
| 2026-10-31 20:00:12 | sphinx-doc__sphinx-10614 | panel | CLOSED-UNVERIFIED | wave 5: finished diff=1310B, receipt not 'completed' (rc: Not finished — not written: issue.) |
| 2026-10-31 20:01:43 | sphinx-doc__sphinx-11510 | panel | CLOSED-UNVERIFIED | wave 5: finished diff=2999B, receipt not 'completed' (rc: Not finished — not written: conf.py) |
| 2026-10-31 20:55:50 | sphinx-doc__sphinx-9602 | panel | CLOSED-UNVERIFIED | wave 5: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-10-31 22:09:54 | django__django-12209 | nopanel | CLOSED-UNVERIFIED | wave 6: finished diff=0B, receipt not 'completed' (rc: Not finished — the loop guard stopped th) |
| 2026-10-31 22:23:29 | django__django-12406 | nopanel | CLOSED-UNVERIFIED | wave 6: finished diff=560B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-10-31 23:29:46 | django__django-13837 | nopanel | CLOSED-UNVERIFIED | wave 6: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-10-31 23:55:03 | django__django-14349 | nopanel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 00:23:54 | django__django-15128 | nopanel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 00:27:27 | django__django-15252 | nopanel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 01:29:07 | django__django-16263 | nopanel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 01:58:52 | django__django-13513 | panel | CLOSED-UNVERIFIED | wave 6: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-11-01 02:24:40 | django__django-13837 | panel | CLOSED-UNVERIFIED | wave 6: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 02:40:50 | django__django-14017 | panel | CLOSED-UNVERIFIED | wave 7: finished diff=566B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 02:51:25 | django__django-14349 | panel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-01 03:38:17 | django__django-15104 | panel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-11-01 03:46:21 | django__django-15252 | panel | CLOSED-UNVERIFIED | wave 7: finished diff=874B, receipt not 'completed' (rc: Not finished — not written: table.) |
| 2026-11-01 05:15:51 | django__django-16263 | panel | CLOSED-UNVERIFIED | wave 7: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-02 10:11:40 | django__django-11433 | panel | PREP-FAIL | workdir/clone prep failed |
| 2026-11-02 17:22:10 | matplotlib__matplotlib-20676 | nopanel | CLOSED-UNVERIFIED | wave 8: finished diff=887B, receipt not 'completed' (rc: Not finished — not written: bug.) |
| 2026-11-02 17:31:33 | matplotlib__matplotlib-20826 | panel | CLOSED-UNVERIFIED | wave 8: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-11-02 17:36:36 | matplotlib__matplotlib-20676 | panel | CLOSED-UNVERIFIED | wave 8: finished diff=887B, receipt not 'completed' (rc: Not finished — not written: bug.) |
| 2026-11-02 20:36:06 | pylint-dev__pylint-6386 | panel | CLOSED-UNVERIFIED | wave 8: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-11-02 21:33:13 | pytest-dev__pytest-7490 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: Not finished — the loop guard stopped th) |
| 2026-11-02 22:44:22 | scikit-learn__scikit-learn-14710 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=1077B, receipt not 'completed' (rc: ▄ step 101 · 100 tools · 56:32 · ↑3888.6) |
| 2026-11-03 00:13:29 | sphinx-doc__sphinx-10323 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=255B, receipt not 'completed' (rc: [2K⋯ for the issue) |
| 2026-11-03 00:14:29 | sphinx-doc__sphinx-10449 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=1832B, receipt not 'completed' (rc: Not finished — not written: folder.) |
| 2026-11-03 01:14:48 | sphinx-doc__sphinx-7440 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=4150B, receipt not 'completed' (rc: ▄ step 145 · 146 tools · 58:49 · ↑5347.4) |
| 2026-11-03 01:17:40 | sphinx-doc__sphinx-10323 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=721B, receipt not 'completed' (rc: ▄ step 49 · 60 tools · 56:48 · ↑1435.9k) |
| 2026-11-03 01:19:11 | sphinx-doc__sphinx-10449 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=1832B, receipt not 'completed' (rc: ▄ step 45 · 50 tools · 59:06 · ↑1207.7k) |
| 2026-11-03 13:21:00 | sphinx-doc__sphinx-11445 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=1044B, receipt not 'completed' (rc: ▄ step 31 · 37 tools · 5:13 · ↑601.9k ↓2) |
| 2026-11-03 13:21:00 | sphinx-doc__sphinx-7440 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: [2K⋯ . Hmm, but there) |
| 2026-11-03 13:21:00 | sphinx-doc__sphinx-7462 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: ▄ step 47 · 46 tools · 7:48 · ↑963.3k ↓3) |
| 2026-11-03 13:21:00 | sphinx-doc__sphinx-7590 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=7127B, receipt not 'completed' (rc: ▄ step 78 · 86 tools · 6:13 · ↑2399.4k ↓) |
| 2026-11-03 13:26:10 | sphinx-doc__sphinx-7462 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   ✔  ◈ run_command  {"ok": true, "exit_c) |
| 2026-11-03 13:26:10 | sphinx-doc__sphinx-7748 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=2916B, receipt not 'completed' (rc: ▄ step 44 · 42 tools · 2:49 · ↑785.7k ↓2) |
| 2026-11-03 13:26:10 | sphinx-doc__sphinx-7757 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: [2K⋯ nodes?) |
| 2026-11-03 13:59:57 | sphinx-doc__sphinx-7590 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 14:01:28 | sphinx-doc__sphinx-7748 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 14:24:03 | sphinx-doc__sphinx-7910 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:24:03 | sympy__sympy-13551 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=651B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:25:04 | sympy__sympy-13647 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:26:04 | sympy__sympy-13757 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:27:05 | sphinx-doc__sphinx-8035 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:33:36 | sympy__sympy-13877 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: Done.) |
| 2026-11-03 14:46:38 | sympy__sympy-13852 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 14:52:39 | sphinx-doc__sphinx-8120 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=1133B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:53:40 | sphinx-doc__sphinx-8265 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 14:58:40 | sympy__sympy-13877 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=2133B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:09:12 | sympy__sympy-16792 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:09:43 | sympy__sympy-13878 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:09:43 | sympy__sympy-18211 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:10:45 | sphinx-doc__sphinx-8475 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=1072B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:10:45 | sympy__sympy-14531 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:12:46 | sphinx-doc__sphinx-8593 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:13:47 | sphinx-doc__sphinx-8595 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 15:13:47 | sympy__sympy-18763 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:06:40 | sphinx-doc__sphinx-8638 | panel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc:   ✔  ◈ run_command  {"ok": true, "exit_c) |
| 2026-11-03 16:06:40 | sympy__sympy-15599 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=714B, receipt not 'completed' (rc: ▄ step 28 · 34 tools · 20:53 · ↑748.5k ↓) |
| 2026-11-03 16:06:40 | sympy__sympy-21596 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   ✔  ◈ run_command  {"ok": true, "exit_c) |
| 2026-11-03 16:06:40 | sympy__sympy-21847 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: [2K⋯ the filter: `if max(p) |
| 2026-11-03 16:07:12 | sympy__sympy-22080 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:07:12 | sympy__sympy-22456 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:09:14 | sympy__sympy-22714 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:10:14 | sympy__sympy-23824 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=589B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:10:45 | sphinx-doc__sphinx-8721 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:11:45 | sphinx-doc__sphinx-9258 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:12:46 | sphinx-doc__sphinx-9281 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:12:46 | sympy__sympy-15809 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=565B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:14:17 | sympy__sympy-15976 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:30:49 | sympy__sympy-24443 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 16:42:53 | sphinx-doc__sphinx-9320 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=770B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 16:51:52 | sympy__sympy-18698 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:01:25 | sphinx-doc__sphinx-9461 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: ▄ step 66 · 65 tools · 14:23 · ↑1644.0k) |
| 2026-11-03 17:08:58 | sympy__sympy-19495 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:11:39 | sympy__sympy-19783 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:16:41 | sympy__sympy-20801 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:24:14 | sympy__sympy-20428 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:24:45 | sympy__sympy-21847 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:24:45 | sympy__sympy-22080 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:41:20 | sympy__sympy-22456 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=1174B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:50:52 | sympy__sympy-23413 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc:   (full traceback: set AURA_DEBUG=1)) |
| 2026-11-03 17:55:23 | sympy__sympy-24443 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 20:02:42 | sphinx-doc__sphinx-8621 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=0B, receipt not 'completed' (rc: Not finished — the model kept thinking i) |
| 2026-11-03 21:20:57 | sphinx-doc__sphinx-8638 | nopanel | CLOSED-UNVERIFIED | wave 9: finished diff=687B, receipt not 'completed' (rc: ▄ step 100 · 105 tools · 57:37 · ↑3735.4) |
| 2026-11-03 21:20:57 | sphinx-doc__sphinx-8638 | nopanel | RETRY-REQUEUE | failed close -> requeued, attempt 1/2 |
| 2026-11-03 21:55:44 | sphinx-doc__sphinx-9673 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=551B, receipt not 'completed' (rc: ▄ step 85 · 86 tools · 57:15 · ↑2810.9k) |
| 2026-11-03 21:55:44 | sphinx-doc__sphinx-9673 | panel | RETRY-REQUEUE | failed close -> requeued, attempt 1/2 |
| 2026-11-03 22:21:17 | sphinx-doc__sphinx-9698 | panel | CLOSED-UNVERIFIED | wave 0: finished diff=624B, receipt not 'completed' (rc: ▄ step 23 · 23 tools · 57:16 · ↑356.9k ↓) |
| 2026-11-03 22:21:17 | sphinx-doc__sphinx-9698 | panel | RETRY-REQUEUE | failed close -> requeued, attempt 1/2 |
| 2026-11-04 00:48:53 | sphinx-doc__sphinx-9673 | nopanel | CLOSED-UNVERIFIED | wave 0: finished diff=551B, receipt not 'completed' (rc: ▄ step 63 · 69 tools · 59:51 · ↑2048.5k) |
| 2026-11-04 00:48:53 | sphinx-doc__sphinx-9673 | nopanel | RETRY-REQUEUE | failed close -> requeued, attempt 1/2 |
| 2026-11-04 01:03:57 | (system) | - | WATCHDOG | WEDGE-SIGNATURE: counts frozen (99, 0, 0, 97, 0, 0) with free slots -> restarting driver |
| 2026-11-04 01:04:00 | (system) | - | WATCHDOG | WATCHDOG-RELAUNCHED driver |
| 2026-11-04 01:09:00 | (system) | - | WATCHDOG | DRIVER DOWN -> relaunching |
| 2026-11-04 01:09:00 | (system) | - | WATCHDOG | WATCHDOG-RELAUNCHED driver |
| 2026-11-04 12:24:01 | (system) | - | WATCHDOG | DRIVER DOWN -> relaunching |
| 2026-11-04 12:24:01 | (system) | - | WATCHDOG | WATCHDOG-RELAUNCHED driver |
| 2026-11-04 13:31:49 | sphinx-doc__sphinx-7757 | nopanel | RESCUE-OK | serial re-run rc=0 diff=1082B receipt=completed |
| 2026-11-04 14:36:20 | sphinx-doc__sphinx-7910 | panel | RESCUE-OK | serial re-run rc=0 diff=1673B receipt=completed |
| 2026-11-04 14:58:37 | sphinx-doc__sphinx-8265 | panel | RESCUE-OK | serial re-run rc=0 diff=1588B receipt=completed |
| 2026-11-04 15:11:13 | sphinx-doc__sphinx-8593 | panel | RESCUE-OK | serial re-run rc=0 diff=778B receipt=completed |
| 2026-11-04 15:15:31 | sphinx-doc__sphinx-8595 | panel | RESCUE-OK | serial re-run rc=0 diff=637B receipt=completed |
| 2026-11-04 15:29:01 | sphinx-doc__sphinx-8638 | panel | RESCUE-OK | serial re-run rc=0 diff=686B receipt=completed |
| 2026-11-04 15:32:24 | sphinx-doc__sphinx-8621 | nopanel | RESCUE-UNVERIFIED | serial re-run rc=1 diff=0B receipt=uncertain |
| 2026-11-04 15:35:59 | sympy__sympy-16792 | nopanel | RESCUE-OK | serial re-run rc=0 diff=1828B receipt=completed |
| 2026-11-04 15:37:43 | sympy__sympy-22714 | nopanel | RESCUE-OK | serial re-run rc=0 diff=704B receipt=completed |
| 2026-11-04 15:41:08 | sphinx-doc__sphinx-8721 | panel | RESCUE-OK | serial re-run rc=0 diff=545B receipt=completed |
| 2026-11-04 15:52:51 | sphinx-doc__sphinx-9258 | panel | RESCUE-OK | serial re-run rc=0 diff=2199B receipt=completed |
| 2026-11-04 15:56:32 | sphinx-doc__sphinx-9281 | panel | RESCUE-OK | serial re-run rc=0 diff=551B receipt=completed |
| 2026-11-04 16:04:21 | sympy__sympy-15976 | panel | RESCUE-OK | serial re-run rc=0 diff=2043B receipt=completed |
| 2026-11-04 16:06:25 | sympy__sympy-24443 | nopanel | RESCUE-UNVERIFIED | serial re-run rc=1 diff=0B receipt=uncertain |
| 2026-11-04 16:19:51 | sympy__sympy-18698 | panel | RESCUE-OK | serial re-run rc=0 diff=1116B receipt=completed |
| 2026-11-04 16:40:08 | sphinx-doc__sphinx-9461 | panel | RESCUE-OK | serial re-run rc=0 diff=4906B receipt=completed |
| 2026-11-04 16:50:42 | sympy__sympy-19495 | panel | RESCUE-OK | serial re-run rc=0 diff=803B receipt=completed |
| 2026-11-04 17:01:08 | sympy__sympy-19783 | panel | RESCUE-UNVERIFIED | serial re-run rc=0 diff=0B receipt=completed |
| 2026-11-04 17:11:59 | sympy__sympy-20801 | panel | RESCUE-OK | serial re-run rc=0 diff=766B receipt=completed |
| 2026-11-04 17:25:08 | sympy__sympy-20428 | panel | RESCUE-OK | serial re-run rc=0 diff=453B receipt=completed |
| 2026-11-04 17:30:34 | sympy__sympy-21847 | panel | RESCUE-OK | serial re-run rc=0 diff=1050B receipt=completed |
| 2026-11-04 17:44:32 | sympy__sympy-22080 | panel | RESCUE-OK | serial re-run rc=0 diff=1638B receipt=completed |
| 2026-11-04 18:00:10 | sympy__sympy-23413 | panel | RESCUE-OK | serial re-run rc=0 diff=1331B receipt=completed |
| 2026-11-04 18:04:19 | sympy__sympy-24443 | panel | RESCUE-UNVERIFIED | serial re-run rc=1 diff=0B receipt=uncertain |
| 2026-11-04 18:19:16 | sympy__sympy-13798 | panel | RESCUE-OK | 3rd-attempt rc=0 diff=1108B receipt=completed |
| 2026-11-04 18:31:19 | sympy__sympy-18698 | panel | RESCUE-OK | 3rd-attempt rc=0 diff=727B receipt=completed |
| 2026-11-04 18:34:32 | sympy__sympy-18763 | panel | RESCUE-OK | 3rd-attempt rc=0 diff=745B receipt=completed |
| 2026-11-04 18:42:03 | sympy__sympy-19783 | panel | RESCUE-OK | 3rd-attempt rc=0 diff=1279B receipt=completed |
| 2026-11-04 18:44:42 | sympy__sympy-24443 | panel | RESCUE-UNVERIFIED | 3rd-attempt rc=1 diff=0B receipt=uncertain |
| 2026-11-04 19:29:59 | (system) | - | WATCHDOG | AUTO-ANSWERER DOWN -> relaunching |
| 2026-11-04 19:32:53 | (system) | - | WATCHDOG | AUTO-ANSWERER DOWN -> relaunching |
| 2026-11-04 19:37:09 | (system) | - | WATCHDOG | AUTO-ANSWERER DOWN -> relaunching |
| 2026-11-04 19:40:18 | (system) | - | WATCHDOG | AUTO-ANSWERER DOWN -> relaunching |

## Campaign-level incidents (compiled; per-event rows above are run-level)

| period | type | description |
|---|---|---|
| 2026-11-02 (bursts 14:24 / 16:07 / 17:11 / 17:25) | ENDPOINT-DROP | model-server endpoint drop bursts produced 0B patches across busiest arm; instances re-run at wave end |
| 2026-11-03 18:28 → 11-04 01:38 | KERNEL-OOM-CRASH | 41 kernel OOM kills (1,315 GB released; procs 18–47 GB) from 8-concurrent endgame pools stacking sphinx memory balloons on a 32 GB box; box died ~9 h; reboot 10:57 Nov 4; zero data loss (diffs+receipts survived in workdirs) |
| 2026-11-03 (evening) | DOUBLE-DRIVER | two driver processes racing on one state file; fixed; driver_state self-healed (counts matched log) |
| 2026-11-04 01:03:57 | WATCHDOG-WEDGE | counts frozen with free slots → driver killed+relaunched by watchdog |
| 2026-11-04 12:24 | DRIVER-DOWN | supervisor relaunch after reboot rebuild |
| per-run signal evidence | see verify12 scan | SIGTERM/exit-15: 8 runs · SIGKILL: 10 runs · oom text: 62 runs — all panel arm, sphinx-weighted; nopanel: 0 |
