#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Project - Add Customer</title>')
print('</head>')
print('<body>')

    

if not form.getvalue('cust_no'):
    print('<h3>Adding a new customer</h3>')

    # The form will send the info needed for the SQL query
    print('<form action="addCustomer.cgi" method="post">')
    print('<p>Number: <input type="text" name="cust_no"/></p>')
    print('<p>Name: <input type="text" name="name"/></p>')
    print('<p>Email: <input type="text" name="email"/></p>')
    print('<p>Phone (optional): <input type="text" name="phone"/></p>')
    print('<p>Address (optional): <input type="text" name="address"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')

else:

    cust_no = form.getvalue('cust_no')
    name = form.getvalue('name')
    email = form.getvalue('email')
    phone = form.getvalue('phone')
    address = form.getvalue('address')

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
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=clients.cgi" />')

print('</body>')
print('</html>')
