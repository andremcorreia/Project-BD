#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
orderID = form.getvalue('orderID')
custID = form.getvalue('custID')

base.Setup()

if not form.getvalue('confirmation'):
    print('<p style="font-size:30px;">Are you sure you wish to pay order {} from customer {}?</p>'.format(orderID, custID))

    # The form will send the info needed for the SQL query
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<button href="orders.cgi" class="button" style="background-color: grey;">Cancel</button>')
    print('<form action="pay.cgi?orderID={}&custID={}&confirmation={}" method="post" style="margin-left: 40px; margin-right: 40px;">'.format(orderID, custID, "yes"))
    print('<button type="submit" class="button" style="background-color: #25b80b;">Confirm</button>')
    print('</form>')
    print('</div>')

else:

    connection = None
    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Query
        sql = "INSERT INTO pay (order_no, cust_no) VALUES %(param)s;"
        data = {'param': (orderID, custID)}

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
    
base.finish()