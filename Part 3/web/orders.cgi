#!/usr/bin/python3
import psycopg2, math
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
    print('<tr><td>ID</td><td>Customer ID</td><td>Date</td></tr>')

    count = len(result)
    
    for row in result:
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
            print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: #1fb622;">{}</span></a></td>'.format("order","pay",row[0],"pay"))
        print('</tr>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="#"><span style="color: #fff;">&Lang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&lang;</span></a>')
    print('<p>Page 0/{}</p>'.format(math.ceil(count/20)))
    print('<a href="#"><span style="color: #fff;">&rang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&Rang;</span></a>')
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<td><a href="addOrder.cgi?"><span style="color: #0c86cc;">{}</span></a></td>'.format("Place an Order"))
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
