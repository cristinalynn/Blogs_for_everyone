# Blogs for Everyone

Blog for Everyone is a user-friendly command-line interface (CLI) application that allows Blog readers to efficiently manage authors, blogs and readers.

# Installation

###
To install and run Blogs for Everyone, ensure that you have Python 3 and pip installed on your system.
###

1. Clone this repository to your local machine and navigate to its directory.
###
2. Run pipenv install to install all the necessary package dependencies.
###
3. Run pipenv shell to enter the virtual environment.
###
4. Navigate to the lib/db directory and run python seed.py to populate        the database with mock data.
###
5. Return to the lib directory by running cd ...
###
6. Run python cli.py to start using Blogs for Everyone.
###

# Using CLI

Welcome To Blogs for Everyone (Main Menu)

1.Manage Authors
#
2. Manage Blogs
#
3. Manage Readers
#
4. Exit

Author Management (Main Menu Option 1)

1. Create Author
#
2. Delete Author
#
3. List Authors
#
4. Go Back

Blog Management (Main Menu Option 2)

1. Create Blog
#
2. Delete Blog
#
3. List Blogs
#
4. Go Back

Reader Management (Main Menu Option 3)

1. Create Reader
#
2. Delete Reader
#
3. List Readers
#
4. Go Back

# Visual

Visual of CLI and Database

# Resources

SQLite
SQLALchemy
Alembic
Faker