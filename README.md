# todoList

Django based to-do-list like web app

This application has been created to store and manage remaining tasks in proper categories.
First time I used Django Admin to manage data.

The application contains:
1. Models:
    - Category
    - Task with one to many relation to Category model as there can be more than one tasks in one category
2. Classes:
    - to create, modify, delete categories and tasks
    - to display all categories and tasks
    
3. Separated html templates for almost every action.
4. Cooperation with SQLite database.
5. Separated file for local settings.
