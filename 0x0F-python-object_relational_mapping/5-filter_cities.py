#!/usr/bin/python3
"""
a script that lists all states from
the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == '__main__':
    connection = MySQLdb.connect(
                user=sys.argv[1],
                password=sys.argv[2],
                database=sys.argv[3],
                host="localhost",
                port=3306)
    cursor = connection.cursor()
    # if sys.argv[4]:
    cursor.execute("SELECT cities.id, cities.name, states.name FROM"
                   " cities JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s"
                   "ORDER BY cities.id ASC",
                   (sys.argv[4],))
    #     if query_rows:
    #         for i, element in enumerate(query_rows):
    #             if i != len(query_rows) - 1:
    #                 print(element[1], end=", ")
    #             else:
    #                 print(element[1])
    print(", ".join(map(lambda x: x[1], cursor.fetchall())))
    cursor.close()
    connection.close()
