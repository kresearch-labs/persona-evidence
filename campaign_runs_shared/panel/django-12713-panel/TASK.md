# TASK
The project (django, checked out at an old commit) has this issue:

Allow overridding widget in formfield_for_manytomany().
Description
	 
		(last modified by Mariusz Felisiak)
	 
It does not work when I set widget param to function formfield_for_manytomany().
This is different from the formfield_for_foreignkey() function.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
