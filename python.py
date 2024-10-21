import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv
from pathlib import Path

# Load the .env file explicitly
env_path = Path('.env')  # or specify the correct path if .env is in another directory
load_dotenv(dotenv_path=env_path)

mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_database = os.getenv('MYSQL_DATABASE')

# Print the values to verify they are fetched correctly
print(f"Host: {mysql_host}, User: {mysql_user}, Password: {mysql_password}, Database: {mysql_database}")

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

cursor = conn.cursor()

# Step 2: Function to register a new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ").encode('utf-8')

    # Hash the password
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    # Insert the username and hashed password into the database
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
    conn.commit()
    print(f"User {username} registered successfully!\n")

# Step 3: Function to log in an existing user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ").encode('utf-8')

    # Fetch the hashed password from the database
    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        stored_hashed_password = result[0].encode('utf-8')
        # Verify the password entered matches the stored hashed password
        if bcrypt.checkpw(password, stored_hashed_password):
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Step 4: Main program loop
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection to the database
cursor.close()
conn.close()

