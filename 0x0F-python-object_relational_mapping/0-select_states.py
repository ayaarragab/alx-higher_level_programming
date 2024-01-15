#!/usr/bin/python3
"""
a script that lists all states from
the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    connection = MySQLdb.connect(
                user="root",
                database="hbtn_0e_0_usa",
                host="localhost",
                port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cursor.fetchall()
    if query_rows:
        for row in query_rows:
            if row:
                print(row)
    cursor.close()
    connection.close()
