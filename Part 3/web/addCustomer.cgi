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

# Form
if not cust_no or not name or not email:
    print('<h3 style="font-size: 24px;"> Adding a new customer 👨‍💻</h3>')

    print('<form action="addCustomer.cgi" method="post">')
    print('<div style="margin-left: -20px;">')
    print('<p>Number:</p> <input type="text" name="cust_no" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (name or email) and not cust_no:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Name:</p> <input type="text" name="name" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (cust_no or email) and not name:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Email:</p> <input type="text" name="email" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (cust_no or name) and not email:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Phone (optional):</p> <input type="text" name="phone" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    print('</div>')
    print('<div style="margin-left: -20px;">')
    print('<p>Address (optional):</p> <input type="text" name="address" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    print('</div>')

    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 50px;">')
    print('<form action="addCustomer.cgi" method="post" style="margin-left: 20px; margin-right: 20px;">')
    print('<a href="clients.cgi" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Cancel</span></a>')
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

        sql = "INSERT INTO customer (cust_no, name, email, phone, address) VALUES %(param)s;"
        data = {'param': (cust_no, name, email, phone, address)}

        cursor.execute(sql, data)

        connection.commit()
        cursor.close()

    except Exception as e:
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=clients.cgi" />')

base.finish()