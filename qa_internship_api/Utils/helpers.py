import mysql.connector


def connect_db(sql):
    # Establish a connection to the database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="apitestingdb"
    )

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute a query
    cursor.execute(sql)

    # Fetch the results
    results = cursor.fetchall()
    try:
        return results
    finally:
        # Close the cursor and connection when you're done
        cursor.close()
        cnx.close()