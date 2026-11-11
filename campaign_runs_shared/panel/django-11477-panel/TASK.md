# TASK
The project (django, checked out at an old commit) has this issue:

translate_url() creates an incorrect URL when optional named groups are missing in the URL pattern
Description
	
There is a problem when translating urls with absent 'optional' arguments
(it's seen in test case of the patch)


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
