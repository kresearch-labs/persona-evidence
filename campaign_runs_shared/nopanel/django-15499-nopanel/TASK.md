# TASK
The project (django, checked out at an old commit) has this issue:

Optimize CreateModel + AlterModelManagers to CreateModel
Description
	
During migration optimization, CreateModel + AlterModelOptions is reduced to just CreateModel, with the model options. Similarly, CreateModel + AlterModelManagers can become just CreateModel.


Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
