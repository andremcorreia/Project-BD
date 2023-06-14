#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()

base.Setup()

if not form.getvalue('order_no'):
    print('<h3 style="font-size: 24px;">Adding a new order</h3>')

    # The form will send the info needed for the SQL query
    print('<form action="addOrder.cgi" method="post">')
    print('<div style="margin-left: -20px;">')
    print('<p>Order Number:</p> <input type="text" name="order_no" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Customer Number:</p> <input type="text" name="cust_no" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Date:</p> <input type="text" name="date" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Product SKU:</p> <input type="text" name="SKU" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Quantity:</p> <input type="text" name="quantity" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')

    # Add a cancel button to the left of the submit button
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="orders.cgi" class="button" style="background-color: grey; margin-left: -20px;">Cancel</a>')
    print('<form action="addOrder.cgi" method="post" style="margin-left: 20px; margin-right: 20px;">')
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
    print('</form>')
    print('</div>')
    
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
        sql_order = 'INSERT INTO "order" (order_no, cust_no, date) VALUES %(param)s;'
        data_order = {'param': (order_no, cust_no, date)}

        print('<p>{}</p>'.format(sql_order % data_order))

        cursor.execute(sql_order, data_order)

        # Insert Contains
        sql_contains = "INSERT INTO contains (order_no, SKU, qty) VALUES %(param)s;"
        data_contains = {'param': (order_no, SKU, qty)}

        print('<p>{}</p>'.format(sql_contains % data_contains))

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

    print('<meta http-equiv="refresh" content="10; url=orders.cgi" />')

base.finish()
