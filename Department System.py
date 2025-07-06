import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="department_db"
)

cursor = db.cursor()

# Create Tables (only run once)
def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department_id INT,
        role VARCHAR(100),
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        employee_id INT,
        task TEXT,
        status VARCHAR(50),
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )""")

# CRUD: Departments
def add_department(name):
    cursor.execute("INSERT INTO departments (name) VALUES (%s)", (name,))
    db.commit()
    print("Department added.")

# CRUD: Employees
def add_employee(name, department_id, role):
    cursor.execute("INSERT INTO employees (name, department_id, role) VALUES (%s, %s, %s)", (name, department_id, role))
    db.commit()
    print("Employee added.")

# CRUD: Tasks
def assign_task(employee_id, task, status="Assigned"):
    cursor.execute("INSERT INTO tasks (employee_id, task, status) VALUES (%s, %s, %s)", (employee_id, task, status))
    db.commit()
    print("Task assigned.")

# View Tasks
def view_tasks():
    cursor.execute("""
    SELECT e.name, t.task, t.status FROM tasks t
    JOIN employees e ON t.employee_id = e.id
    """)
    for row in cursor.fetchall():
        print(row)

# Sample usage
if __name__ == "__main__":
    create_tables()
    # add_department("HR")
    # add_employee("Anziya", 1, "Manager")
    # assign_task(1, "Submit performance report")
    view_tasks()
