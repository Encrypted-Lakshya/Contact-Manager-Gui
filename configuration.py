import mysql.connector                                  #Importing MySQL
from mysql.connector import Error                       #Importing Error from MySQL to gather the errors in the sql script if any
import os                                               #Importing os to create operaating system and run the SQL in its suitable environment
from dotenv import load_dotenv                          

#Loading environment variables from .env files
load_dotenv()

class DatabaseManager:
    def __init__(self):
        "Initialize the database connection using environment variable"
        try:
            self.connection = mysql.connector.connect(
            host = os.getenv("DB_Host","localhost"),
            user = os.getenv("DB_User","root"),
            password = os.getenv("DB_Password","J@rvis"),
            database = os.getenv("DB_name","project")
            )

            if self.connection.is_connected():         #Checking connection if established
                self.cursor = self.connection.cursor(dictionary=True)
                print("Connected to MySQL DataBase.")
                self._create_table()
        except Error as e:
            print(f"Error connecting to MySQL DataBase: {e}")
            raise

    def _create_table(self):                        #Fucntion to create the tables to take the dataa inputs
        try:
            self.cursor.execute("""
                create table if not exists contacts(
                    id int auto_increment primary key,
                    name varchar(100) not null,
                    gender varchar(20),
                    phone int,
                    email varchar(100),
                    address varchar(200),
                    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.connection.commit()                #Calling function to create tables
            print("Tables are created successfully.")

        except Error as e:                          #Calling error to provide error if any found
            print(f"Error creating tables: {e}")
            raise
    
    def close(self):                            #Closing DataBase connection
        if hasattr(self,'connection') and self.connection.is_connected():
            self.cursor.close()                 #Closing cursor to stop database creation and importing entries
            self.connection.close()             #Closing connection to be disconnected from database
            print("MySQL connection is closed.")

    def create_contact(self, name, gender=None, phone=None, email=None, address=None):
        try:
            #Creaating query to take input for the data fields
            query = """
                    INSERT INTO contacts(name, gender, phone, email, address)
                    VALUES(%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query,(name,gender,phone,email,address))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            self.connection.rollback()
            return None
        
    def get_contact_through_id(self, contact_id):
        "Get a contact by id"
        query = "SELECT * from contacts where id = %s"
        self.cursor.execute(query, (contact_id,))
        return self.cursor.fetchone()
    
    def get_all_contacts(self):
        "Getting aall the contacts"
        query = "SELECT * from contacts order by name"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def searching_contact(self, search_term):
        """Searching contacts by name, phone, or email"""
        query = """
            SELECT * from contacts
            where name like %s or phone like %s or email like %s
            order by name
        """
        parameter = f"%{search_term}%"
        self.cursor.execute(query,(parameter,parameter,parameter))
        return self.cursor.fetchall()

    def update_contact(self, contact_id, name=None, gender=None, phone=None, email=None, address=None):        #Function for updating contacts
        try:
            current = self.get_contact_through_id(contact_id)
            if not current:
                return False
            
            name = name if name is not None else current['name']
            gender = gender if gender is not None else current['gender']
            phone = phone if phone is not None else current['phone']
            email = email if email is not None else current['email']
            address = address if address is not None else current['address']

            query ="""
                UPDATE contacts
                set name = %s, gender = %s, phone = %s, email = %s, address = %s
                where id = %s
            """

            self.cursor.execute(query,(name, gender, email, phone, address, contact_id))
            self.connection.commit()
            return self.cursor.rowcount>0
        except Error as e:
            print(f"Error updating contact: {e}")
            self.connection.rollback()
            return False
    
    def delete_contact(self, contact_id):              #Function to delete the require entries or values
        """Delete a contact"""
        try:
            query = "DELETE from contacts where id = %s"
            self.cursor.execute(query,(contact_id,))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting contact:{e}")
            self.connection.rollback()
            return False
    