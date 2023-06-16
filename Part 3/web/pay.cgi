#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
orderID = form.getvalue('orderID')
custID = form.getvalue('custID')

base.Setup()

# Confirmation form
if not form.getvalue('confirmation'):
    print('<h3 style="font-size:30px;">Are you sure you wish to pay order {} from customer {}? 💸</h3>'.format(orderID, custID))

    print('<form action="pay.cgi?orderID={}&custID={}&confirmation={}" method="post">'.format(orderID, custID, "yes"))
    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<form action="pay.cgi?orderID={}&custID={}&confirmation={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(orderID, custID, "yes"))
    print('<a href="orders.cgi" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Cancel</span></a>')
    print('<a style="margin-right: 40px;"> </a>')
    print('<button type="submit" class="pushable" style="background-color: #147303;"><span class="front" style="background: #2cc211;">Submit</button>')    
    print('</form>')

    print('</div>')
    print('</form>')

# Execution of the queries
else:
    connection = None

    try:
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        sql = "INSERT INTO pay (order_no, cust_no) VALUES %(param)s;"
        data = {'param': (orderID, custID)}

        cursor.execute(sql, data)

        connection.commit()
        cursor.close()

    except Exception as e:
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=orders.cgi" />')
    
base.finish()