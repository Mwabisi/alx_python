#!/usr/bin/python3
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()