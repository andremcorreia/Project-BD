#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()
customer_number = form.getvalue('customer_number')
customer_name = form.getvalue('customer_name', '')
customer_email = form.getvalue('customer_email')
customer_phone = form.getvalue('customer_phone', '')
customer_address = form.getvalue('customer_address', '')
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Adding Customer</title>')
print('</head>')
print('<body>')
# The string has the {}, the variables inside format() will replace the {}
print('<h3>Adding the Customer with number number {} and email {}</h3>'.format(customer_number, customer_email))
# The form will send the info needed for the SQL query
#print('<form action="clients.cgi" method="post">')
#print('<p><input type="hidden" name="account_number" value="{}"/></p>'.format(account_number))
#print('<p>New balance: <input type="text" name="balance"/></p>')
#print('<p><input type="submit" value="Submit"/></p>')
#print('</form>')

connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    
    # Making query
    cursor.execute("INSERT INTO customer (cust_no, name, email, phone, address) VALUES ('%(cust_no)s', %(name)s', %(email)s', %(phone)s', %(address)s')", {'cust_no':customer_number, 'name': customer_name, 'email': customer_email, 'phone': customer_phone, 'address': customer_address});
    # Commit the update (without this step the database will not change)
    connection.commit()

    # Closing connection
    cursor.close()
except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')