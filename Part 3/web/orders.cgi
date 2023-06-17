#!/usr/bin/python3
import psycopg2, cgi, math
import login
import base

MAX = 20

form = cgi.FieldStorage()
current = form.getvalue('current')
search_query = form.getvalue('query', '')

if not current:
    current = 0
else:
    current = int(current)
if current < 0:
    current = 0

base.Setup()

connection = None

try:
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()
    base.addTabs(2)

    # Making query
    if search_query:
        sql = 'SELECT * FROM "order" WHERE cust_no = %s;'
        cursor.execute(sql, (search_query,))
    else:
        sql = 'SELECT * FROM "order";'
        cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    print('<div class="header">')
    print('<div style="text-align:center; margin-top: 60px;">')
    print('<p><b>Orders</b></p>') 
    print('<form action="orders.cgi" method="get">')
    print('<input type="search" name="query" placeholder="🔍 Search by Customer ID" value="{}" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 45%">'.format(search_query))
    print('</form>')
    print('</div>')

    print('<div class="table-container">')
    print('<table border="0">')

    count = len(result)

    if count > 0:
        print('<tr><th>ID</th><th>Customer ID</th><th>Date</th></tr>')

    # Paging Overflow check
    if current >= count:
        current = math.floor((count - 1)/MAX)*MAX

    for i in range(current, len(result)):
        row = result[i]
        if i >= MAX + current:
                break
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        sql = 'SELECT * FROM pay WHERE order_no={};'.format(row[0])
        cursor.execute(sql)
        pay_result = cursor.fetchone()
        
        # Pay functionality
        if pay_result:
            print('<td>Already Paid</td>')
        else:
            print('<td><a href="pay.cgi?orderID={}&custID={}"style="text-decoration: none;"><span style="color: #1fb622;">{}</span></a></td>'.format(row[0],row[1],"pay"))
        print('</tr>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&Lang;</span></a>'.format(0, search_query))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX, search_query))
    print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX, search_query))
    print('<a href="orders.cgi?current={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX, search_query))
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<a href="addOrder.cgi"><button class="pushable" style="background: #3a5ac9;"><span class="front" style="background: #7289da;">{}</span></button></a>'.format("Add an Order"))
    print('</div>')

    cursor.close()

except Exception as e:
    print('<h1>No order Found</h1>')

finally:
    if connection is not None:
        connection.close()

base.finish()
