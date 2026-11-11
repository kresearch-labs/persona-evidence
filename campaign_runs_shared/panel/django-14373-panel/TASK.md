# TASK
The project (django, checked out at an old commit) has this issue:

DateFormat.Y() is not zero-padded.
Description
	
The Y specifier for django.utils.dateformat.DateFormat is supposed to always return a four-digit year padded with zeros. This doesn't seem to be the case for year < 1000.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
