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
        # Get all order_no associated with customer
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
        # Get all TIN (supplier) associated with product
        sql_get_supp = "SELECT TIN FROM supplier WHERE SKU = {};".format(id)
        cursor.execute(sql_get_supp)
        suppliers = cursor.fetchall()

        # Get all distinct order_no associated with product
        sql_get_orders = 'SELECT DISTINCT order_no FROM contains WHERE SKU = {};'.format(id)
        cursor.execute(sql_get_orders)
        dist_orders = cursor.fetchall()
        
        # Get all order_no associated with product
        sql_get_orders = 'SELECT order_no FROM contains WHERE SKU = {};'.format(id)
        cursor.execute(sql_get_orders)
        orders = cursor.fetchall()

        connection.autocommit = False

        sql_del = 'DELETE FROM delivery WHERE TIN = {};'
        for supp in suppliers:
            cursor.execute(sql_del.format(supp))

        sql_del = "DELETE FROM contains WHERE SKU = {};".format(id)
        cursor.execute(sql_del)
        for order in dist_orders:
            # Count of contains entries with certain order_no
            if orders.count(order) == 1:
                sql_del = 'DELETE FROM "order" WHERE order_no = {};'.format(order)
                cursor.execute(sql_del)

        sql_del = "DELETE FROM supplier WHERE SKU = {};".format(id)
        cursor.execute(sql_del)
           
        sql_del = 'DELETE FROM product WHERE SKU = {};'.format(id)
        cursor.execute(sql_del)

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