## 📇 Contact Management App

A desktop application for managing personal and business contacts, built using **Python**, **Tkinter**, and **MySQL**. It offers a graphical user interface to create, update, delete, and search contact information.

---

### ✨ Features

✅ Create new contacts with details like:

* Name
* Gender
* Phone
* Email
* Address

✅ View all saved contacts in a table view

✅ Search contacts by:

* Name
* Phone
* Email

✅ Edit/update existing contacts

✅ Delete contacts

✅ User-friendly GUI with a modern theme

✅ MySQL database backend with automatic table creation

---

### 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – for the graphical user interface
* **MySQL** – for persistent data storage
* **mysql-connector-python** – Python driver for MySQL
* **python-dotenv** – for environment variable management

---

### 📁 Project Structure

```
project-root/
├── configuration.py         # Handles database connection and queries
├── interface.py             # Defines the Tkinter GUI interface
├── execution.py             # Entry point to launch the app
├── requirements.txt         # Python dependencies
└── .env                     # Database credentials (not committed to version control)
```

---

### ⚙️ Installation

1. **Clone the repository:**

```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

* Windows:

  ```
  venv\Scripts\activate
  ```
* macOS/Linux:

  ```
  source venv/bin/activate
  ```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

### 🗄️ Database Setup

The app automatically creates the required `contacts` table if it does not exist.

#### 1. Create a MySQL database

Login to MySQL and run:

```sql
CREATE DATABASE project;
```

> *Or use any preferred database name. Update your `.env` file accordingly.*

#### 2. Create a `.env` file

In the project root, create a file named `.env`:

```
DB_Host=localhost
DB_User=root
DB_Password=your_password
DB_name=project
```

Replace values as per your MySQL setup.

---

### 🚀 Running the Application

Run:

```bash
python execution.py
```

This launches the GUI window for managing contacts.

---

### 💡 Example Usage

* Click **“Add Contact”** to enter details.
* Use **Search** to filter contacts by name, phone, or email.
* Select a contact in the list and click **Edit** to modify details.
* Click **Delete** to remove a contact.

---

### 📦 Requirements

See [`requirements.txt`](requirements.txt):

```
mysql-connector-python==8.0.33
python-dotenv==1.0.0
```

---

### 🐞 Troubleshooting

* **Database Connection Error:**

  * Ensure MySQL server is running.
  * Check credentials in `.env`.
* **GUI not launching:**

  * Check Python version (must be Python 3).
  * Confirm all dependencies are installed.

---

### 📜 License

This project is licensed under the [MIT License](LICENSE).

---
Made with ❤️ by  Lakshya Rohra
