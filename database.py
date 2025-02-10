import mysql.connector

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root123",
                database="libra_tech",
                port=3307
            )
        return cls._instance

    def execute(self, query, params=None):
        cursor = self.connection.cursor()  # Create a new cursor each time
        try:
            cursor.execute(query, params or ())
            result = cursor.fetchall()  # Fetch all results
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return []
        finally:
            cursor.close()  # Close the cursor after each operation
