import mysql.connector

def connection():
    connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "studentrecordms_db"
)
    if connection.is_connected():
        print("connected to Mysql XAMPP server")
        return connection
    else:
        print("Failed to Connect")
        connection.close()



 