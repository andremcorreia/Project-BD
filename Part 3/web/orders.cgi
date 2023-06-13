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
    base.addTabs(2)

    # Making query
    sql = 'SELECT o.order_no, o.cust_no, o.date, p.order_no AS pay_check FROM "order" o LEFT JOIN pay p ON o.order_no = p.order_no;'
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
    print('<tr><td>ID</td><td>Customer ID</td><td>Date</td></tr>')
    
    for row in result:
        print('<tr>')
        for value in row[:3]:
            print('<td>{}</td>'.format(value))
        if row[3] is not None:
            print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: #1fb622;">{}</span></a></td>'.format("order","pay",row[0],"pay"))
        else:
            print('<td>Already Payed</td>')
        print('</tr>')

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
    print('<td><a href="update.cgi?table={}?request={}"><span style="color: #0c86cc;">{}</span></a></td>'.format("order","add","Place an Order"))
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
