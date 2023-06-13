#!/usr/bin/python3
import psycopg2
import login
import base

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
    
    print('<tbody>')
    for i in range(len(result)):
        if i >= MAX:
                break
        print('<tr>')
        for value in result[i]:
            print('<td>{}</td>'.format(value)) 
        print('<td><a href="update.cgi?table={}&request={}&SKU={}"><span style="color: red;">&#10060;</span></a></td>'.format("customer","delete",result[i][0]))
        print('</tr>'),
    print('</tbody>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="#"><span style="color: #fff;">&Lang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&lang;</span></a>')
    print('<p>Page 0/0</p>')
    print('<a href="#"><span style="color: #fff;">&rang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&Rang;</span></a>')
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<a href="update.cgi?table={}&request={}"><span style="color: #7289da;">{}</span></a>'.format("customer","add","Add a Client"))
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