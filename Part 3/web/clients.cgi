#!/usr/bin/python3
import psycopg2, cgi, math
import login
import base

form = cgi.FieldStorage()
current = form.getvalue('current')
if not current:
    current = 0
else:
    current = int(current)

if current < 0:
    current = 0

MAX = 20

base.Setup()

connection = None
try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    base.addTabs(1)

    # Making query
    sql = 'SELECT * FROM customer;'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Display Header
    print('<div class="header">')
    print('<div style="text-align:center; margin-top: 60px;">')
    print('<p><b>Customers</b></p>') 
    print('</div>')

    # Displaying results
    print('<div class="table-container">')
    print('<table border="0">')
    print('<thead><tr><th>ID</th><th>Name</th><th>E-mail</th><th>Phone</th><th>Address</th></tr></thead>')
    
    count = len(result)
    if current > count:
        current = math.floor(count/MAX)*MAX

    print('<tbody>')
    for i in range(current, len(result)):
        if i >= MAX + current:
                break
        print('<tr>')
        for value in result[i]:
            print('<td>{}</td>'.format(value)) 
        print('<td><a href="delete.cgi?table={}&id={}" style="text-decoration: none;"><span style="color: red;">&#10060;</span></a></td>'.format("customer",result[i][0]))
        print('</tr>'),
    print('</tbody>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="clients.cgi?current={}"><span style="color: #fff;">&Lang;</span></a>'.format(0))
    print('<a href="clients.cgi?current={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX))
    print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
    print('<a href="clients.cgi?current={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX))
    print('<a href="clients.cgi?current={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX))
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center; margin-top: 0px; margin-bottom: 20px;">')
    print('<a href="addCustomer.cgi"><button class="button" style="background-color: #7289da; width: 200px;">{}</button></a>'.format("Add a Client"))
    print('</div>')

    # Closing connection
    cursor.close()
    base.finish()

except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()