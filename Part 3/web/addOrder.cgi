#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()

base.Setup()

if not form.getvalue('order_no'):
    print('<h3>Adding a new order</h3>')

    # The form will send the info needed for the SQL query
    print('<form action="addOrder.cgi" method="post">')
    print('<p>Order Number: <input type="text" name="order_no"/></p>')
    print('<p>Customer Number: <input type="text" name="cust_no"/></p>')
    print('<p>Date: <input type="text" name="date"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')

else:
    # Gets the values for each param
    order_no = form.getvalue('order_no')
    cust_no = form.getvalue('cust_no')
    date = form.getvalue('date')
    SKU = form.getvalue('SKU')
    qty = form.getvalue('quantity')

    connection = None

    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Start the transaction
        connection.autocommit = False


        # Insert Order
        sql_order = "INSERT INTO \"order\" (order_no, cust_no, date) VALUES %(param)s;"
        data_order = {'param': (order_no, cust_no, date)}
        cursor.execute(sql_order, data_order)

        # Insert Contains
        sql_contains = "INSERT INTO contains (order_no, SKU, qty) VALUES %(param)s;"
        data_contains = {'param': (order_no, SKU, qty)}
        cursor.execute(sql_contains, data_contains)

        # Commit the transaction
        connection.commit()
        
        # Reset autocommit mode
        connection.autocommit = True

    except Exception as e:
        # Rollback the transaction on error
        connection.rollback()
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=orders.cgi" />')

base.finish()


# TRANSACTION