#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Project - Add Order</title>')
print('</head>')
print('<body>')

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

    connection = None

    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Query
        sql = "INSERT INTO \"order\" (order_no, cust_no, date) VALUES %(param)s;"
        data = {'param': (order_no, cust_no, date)}

        # The string has the {}, the variables inside format() will replace the {}
        # Feed the data to the SQL query as follows to avoid SQL injection
        cursor.execute(sql, data)

        # Commit the update (without this step the database will not change)
        connection.commit()
        # Closing connection
        cursor.close()
    except Exception as e:
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=orders.cgi" />')

print('</body>')
print('</html>')