# CollectUSR+PASS

A simple command-line Python app that allows users to register and log in using a MySQL database. Passwords are securely hashed using `bcrypt`, and credentials are managed using environment variables via `python-dotenv`.

---

## 🔐 Features

- **User Registration**  
  Hashes and stores new user passwords securely in the database.

- **User Login**  
  Verifies input credentials against the stored hashed passwords.

- **Secure Configuration**  
  Credentials are stored in a `.env` file and loaded at runtime (not hard-coded).

---

## 🛠️ Requirements

### Python Packages

- `mysql-connector-python`
- `bcrypt`
- `python-dotenv`

### System Requirements

- Python 3.8+
- MySQL Server installed and running

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <(https://github.com/eliesmeen/Username-and-Password-Project)>
cd CollectUSR+PASS
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up the `.env` File

Create a `.env` file in the root of the project with the following content:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password_here
MYSQL_DATABASE=login_system
```

> ✅ Tip: You can also copy from a `.env.example` file if provided.

---

## 🧱 MySQL Setup

### 1. Create the Database

Log into MySQL and run:

```sql
CREATE DATABASE login_system;
```

### 2. Create the Users Table

```sql
USE login_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

---

## ▶️ Running the App

Run the script with:

```bash
python python.py
```

You'll be prompted to:
- Register a new user
- Log in
- Exit the program

Follow the on-screen instructions in the terminal.
