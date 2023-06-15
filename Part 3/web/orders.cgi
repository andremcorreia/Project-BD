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
    base.addTabs(2)

    # Making query
    sql = 'SELECT * FROM "order";'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Display Header
    print('<div class="header">')
    print('<div style="text-align:center; margin-top: 60px;">')
    print('<p><b>Orders</b></p>') 
    print('</div>')

    # Displaying results
    print('<div class="table-container">')
    print('<table border="0">')
    print('<tr><th>ID</th><th>Customer ID</th><th>Date</th></tr>')
    
    count = len(result)
    if current > count:
        current = math.floor(count/MAX)*MAX

    for i in range(current, len(result)):
        row = result[i]
        if i >= MAX + current:
                break
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        # Check if order_no is in pay table
        sql = 'SELECT * FROM pay WHERE order_no={};'.format(row[0])
        cursor.execute(sql)
        pay_result = cursor.fetchone()
        
        if pay_result:
            print('<td>Already Paid</td>')
        else:
            print('<td><a href="pay.cgi?orderID={}&custID={}"style="text-decoration: none;"><span style="color: #1fb622;">{}</span></a></td>'.format(row[0],row[1],"pay"))
        print('</tr>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&Lang;</span></a>'.format(0))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX))
    print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX))
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<a href="addOrder.cgi"><button class="button" style="background-color: #7289da; width: 200px;">{}</button></a>'.format("Place an Order"))
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
