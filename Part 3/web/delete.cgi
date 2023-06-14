#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
table = form.getvalue('table')
id = form.getvalue('id')

base.Setup()

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    connection.autocommit = True

    if table == 'customer':
        sql_get_orders = 'SELECT order_no FROM "order" WHERE cust_no = {};'.format(id)
        cursor.execute(sql_get_orders)
        orders = cursor.fetchall()

        connection.autocommit = False
        sql_del = "DELETE FROM  WHERE order_no = {};"
        to_check = ('pay', 'contains', 'process', '\"order\"')
        for tab in to_check:
            for value in orders:
                cursor.execute(sql_del[:12] + tab + sql_del[12:].format(value[0]))

        sql_del = "DELETE FROM customer WHERE cust_no = {};".format(id)
        cursor.execute(sql_del)

    elif table == 'product':
        sql_get_supp = "SELECT TIN FROM supplier WHERE SKU = {}".format(id)
        cursor.execute(sql_get_supp)
        suppliers = cursor.fetchall()

        connection.autocommit = False
        to_check = ('product', 'contains', 'supplier')
        sql_del = "DELETE FROM  WHERE SKU = {}".format(id)

    # Commit the update (without this step the database will not change)
    connection.commit()
    connection.autocommit = True

    # Closing connections
    cursor.close()

except Exception as e:
    connection.rollback()
    print('<h1>{}</h1>'.format(str(e)))
    print('<h1>An error occurred.</h1>')

finally:
    if connection is not None:
        connection.close()

base.finish()