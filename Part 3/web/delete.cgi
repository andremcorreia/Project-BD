#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
table = form.getvalue('table')
id = form.getvalue('id')

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # --- WAITING RESPONSE FROM PROFESSOR ---

    #connection.autocommit = False

    #if table == 'customer':
    #    sql_del = "DELETE FROM customer WHERE cust_no = {};".format(id)
    #    cursor.execute(sql_del)
        
    # --- WAITING RESPONSE FROM PROFESSOR ---

    # Commit the update (without this step the database will not change)
    connection.commit()
    # Closing connection
    cursor.close()

except Exception as e:
    connection.rollback()
    print('<h1>An error occurred.</h1>')

finally:
    if connection is not None:
        connection.close()