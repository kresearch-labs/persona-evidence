# TASK
The project (django, checked out at an old commit) has this issue:

Statement created by _create_unique_sql makes references_column always false
Description
	
This is due to an instance of Table is passed as an argument to Columns when a string is expected.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
