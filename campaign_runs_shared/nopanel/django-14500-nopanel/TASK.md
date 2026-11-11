# TASK
The project (django, checked out at an old commit) has this issue:

Squashed migration is not marked as unapplied
Description
	 
		(last modified by Markus Holtermann)
	 
When unapplying a squashed migration and the replaced migration files are still around, the MigrationExecutor mark the squash migration as unapplied, too, not only the replaced migrations.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
