# TASK
The project (django, checked out at an old commit) has this issue:

Fixture dirs duplicates undetected if dir is Path instance
Description
	
When FIXTURE_DIRS contains Path instances, the duplicate check in loaddata does not detect duplicates.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
