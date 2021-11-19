
import sqlite3
from employee import Employee

#DAL : CRUD  => Insert,Select,Update,Delete
FOLDER = '/Users/aniron/Documents/BofA_Python_Training_15Nov21/day3/database/'

def connectdb():
    global conn
    conn=sqlite3.connect(FOLDER+'emp.db') ### create this db if not present
    global cursor
    cursor=conn.cursor() ## like a pen!!!
    print("connected to Emp database")

def create_table():
    try:
        cursor.execute(""" CREATE TABLE employees (
                first text,
                last text,
                pay integer
        )""")
        print("employee table created")
        ### download sqllite db browser to see emp.db database!!! sqllitebrowser.org
        ### check the emp.db table in "DB Browser for SQLite"
    except Exception as ex:
        print(ex)

def insert_emp(emp):
    try:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                            {'first': emp.first, 'last': emp.last, 'pay': emp.pay}
        )
        cursor.execute('commit') ### write it actually now !
        print(f'{emp} inserted')

    except Exception as ex:
        print(ex)

def get_emps_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return cursor.fetchall()

def remove_emp(emp):
    cursor.execute("DELETE FROM employees WHERE first=:first AND last=:last", 
                {'first': emp.first, 'last': emp.last}
    )
    cursor.execute("commit")
    print(f'removed {emp}')

if __name__ == '__main__':
    connectdb()
    # create_table()
    emp1 = Employee('Imran', 'Sk', 10000000)
    emp2 = Employee('A', 'B', 232323)
    insert_emp(emp1)
    insert_emp(emp2)

    emps = get_emps_by_name('Sk')
    print(emps)

    remove_emp(emp1)
    print('after deleting')
    emps = get_emps_by_name('Sk')
    print(emps)
    
    conn.close()
