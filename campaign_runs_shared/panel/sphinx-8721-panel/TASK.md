# TASK
The project (doc, checked out at an old commit) has this issue:

viewcode creates pages for epub even if `viewcode_enable_epub=False` on `make html epub`
**Describe the bug**
viewcode creates pages for epub even if `viewcode_enable_epub=False` on `make html epub`

**To Reproduce**
```
$ make html epub
```

**Expected behavior**
module pages should not be created for epub by default.

**Your project**
No

**Screenshots**
No

**Environment info**
- OS: Mac
- Python version: 3.9.1
- Sphinx version: HEAD of 3.x
- Sphinx extensions:  sphinx.ext.viewcode
- Extra tools: No

**Additional context**
No



Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
Do NOT run the project's test suite; the grading harness tests it officially.
