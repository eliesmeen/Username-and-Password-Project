CollectUSR+PASS Project
This is a Python project that allows users to register and log in using a MySQL database. The project securely stores user credentials using hashed passwords before saving them in the database.

Features
User Registration: Users can register by entering a username and password. Passwords are securely hashed using bcrypt before being stored in the database.
User Login: Users can log in with their username and password. The entered password is compared against the hashed password in the database for validation.
Requirements
Python Packages
The project requires the following Python packages:

mysql-connector-python
bcrypt
python-dotenv
Other Requirements
Python 3.8+
MySQL installed and running on your system.
A properly configured .env file with your MySQL database credentials.
Installation Instructions
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone <repository_url>
cd CollectUSR+PASS
2. Install Python and Dependencies
Make sure Python is installed on your machine. You can verify this by running:

bash
Copy code
python --version
Next, install the required Python packages listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
3. Set Up the .env File
Create a .env file in the project directory to store your MySQL database credentials. You can copy the example provided:

bash
Copy code
cp .env.example .env
Edit the .env file with your MySQL credentials:

env
Copy code
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password_here
MYSQL_DATABASE=login_system
4. Set Up the MySQL Database
Ensure that your MySQL server is running and create the required database and table.

Create the Database:

Log in to MySQL and run the following command:

sql
Copy code
CREATE DATABASE login_system;
Create the Users Table:

After creating the database, create a table for users with this SQL query:

sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
5. Run the Project
Now that everything is set up, you can run the Python script:

bash
Copy code
python python.py
6. Usage
Once the script is running, you'll be prompted to either register a new user or log in. Simply follow the on-screen instructions to interact with the system.

requirements.txt
Make sure your project has a requirements.txt file that includes the following dependencies:

Copy code
mysql-connector-python
bcrypt
python-dotenv
You can create or update the requirements.txt by running:

bash
Copy code 
pip freeze > requirements.txt
Additional Notes:
The .env file contains sensitive credentials and should never be committed to version control (e.g., GitHub). Make sure your .gitignore includes .env to avoid pushing it to the repository.

If you're sharing this project, include instructions for how to create the .env file based on the provided .env.example file.