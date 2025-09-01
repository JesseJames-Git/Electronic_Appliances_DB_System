# ELECTRICAL APPLIANCES DATABASE SYSTEM
## Description
- This is a database system for a company consisting of Suppliers, Products, Customers and their details.

It consist of:
1. A database file containing the data from CRUD Operations(Create, Read, Update, Delete).
2. A Models file(models.py) that deals with defining the database.
3. A CRUD file(crud.py) that deals with defining the operations on the operations.
4. A CLI file(cli.py) that defining the running app.

- Several test were carried out on the app to ensure good functionality.

## How to use
### Requirements:
- A Computer
- Basic knowledge of navigating in the command line
- Python  installed in your computer

### Steps:
1. Open the terminal in your system and navigate your desired directory.

    ``` cd <name_of_desired_directory> ```

* If you want the app in a new directory just create a new directory using mkdir command
Example:
    ``` mkdir <name_of_desired_directory> ```

2. In your directory run the command below to clone the app into your local system.
    ``` git clone git@github.com:JesseJames-Git/Electronic_Appliances_DB_System.git ```

3. Navigate to the newly created folder(Electronic_Appliances_DB_System) using this command.
    ``` cd Electronic_Appliances_DB_System ```

4. Run the command below to put your project in a virtual environment.
    ``` pipenv shell ```

5. The following dependancies wiil be used to  make your app interact with the database: SQLAlchemy, Alembic and Click. Add them to your folder using the command below:
    ``` pip install sqlalchemy alembic click ```

6. Run this command to run the CLI app:
    ``` python lib/cli.py ```


- After cloning and setting up the app, ensure you follow the navigational details. 

- Feel free to interact with the application using the options given. 

* NOTE :
- Make deletions and updates carefully to avoid data loss.

## Contact Details
If you have any questions, contact me through:

- Email: jessejamesjj007@gmail.com

## Author
The entire project was done by Jesse James Kang'ethe Macibi.

## License
MIT License

Copyright (c) 2025 JesseJames-Git

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.