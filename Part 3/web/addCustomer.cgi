#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()

base.Setup()

cust_no = form.getvalue('cust_no')
name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')
address = form.getvalue('address')

if not cust_no or not name or not email:
    print('<h3 style="font-size: 24px;">Adding a new customer</h3>')

    # The form will send the info needed for the SQL query
    print('<form action="addCustomer.cgi" method="post">')
    print('<div style="margin-left: -20px;">')
    if name or email:
        print('<div style="color: red; font-size: 12px;">Required field</div>') 
    print('<p>Number:</p> <input type="text" name="cust_no" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')
    print('<div style="margin-left: -20px;">')
    if cust_no or email:
        print('<div style="color: red; font-size: 12px;">Required field</div>') 
    print('<p>Name:</p> <input type="text" name="name" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')
    print('<div style="margin-left: -20px;">')
    if cust_no or name:
        print('<div style="color: red; font-size: 12px;">Required field</div>')
    print('<p>Email:</p> <input type="text" name="email" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Phone (optional):</p> <input type="text" name="phone" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Address (optional):</p> <input type="text" name="address" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')

    # Add a cancel button to the left of the submit button
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="clients.cgi" class="button" style="background-color: grey; margin-left: -20px; line-height: 50px;">Cancel</a>')
    print('<form action="addCustomer.cgi" method="post" style="margin-left: 20px; margin-right: 20px;">')
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
    print('</form>')
    print('</div>')

    print('</form>')

else:

    connection = None

    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Query
        sql = "INSERT INTO customer (cust_no, name, email, phone, address) VALUES %(param)s;"
        data = {'param': (cust_no, name, email, phone, address)}

        # Feed the data to the SQL query as follows to avoid SQL injection
        cursor.execute(sql, data)

        # Commit the update (without this step the database will not change)
        connection.commit()
        # Closing connection
        cursor.close()
    except Exception as e:
        print('<h1>{}</h1>'.format(str(e)))
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=clients.cgi" />')

base.finish()