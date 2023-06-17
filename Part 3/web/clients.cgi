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
    base.addTabs(1)

    # Making query
    sql = f'SELECT * FROM customer WHERE name ILIKE %s;'
    cursor.execute(sql, ('%' + search_query + '%',))
    result = cursor.fetchall()
    num = len(result)

    print('<div class="header">')

    print('<div style="text-align:center; margin-top: 60px; font-size: 18px;">')
    print('<p><b>Customers</b></p>')
    print('<form action="clients.cgi" method="get">')
    print('<input type="search" name="query" placeholder="🔍 Search by name" value="{}" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc;">'.format(search_query))
    print('</form>')

    print('</div>')

    print('<div class="table-container">')
    print('<table border="0">')

    count = len(result)

    if count > 0:
        print('<thead><tr><th>ID</th><th>Name</th><th>E-mail</th><th>Phone</th><th>Address</th></tr></thead>')

    # Paging Overflow check
    
    if current >= count:
        current = math.floor((count - 1)/MAX)*MAX

    print('<tbody>')
    for i in range(current, len(result)):
        if i >= MAX + current:
            break
        print('<tr>')
        for value in result[i]:
            print('<td>{}</td>'.format(value))
        print('<td><a href="delete.cgi?table={}&id={}&name={}" style="text-decoration: none; font-size:12px;"><span style="color: red;">❌</span></a></td>'.format("customer",result[i][0],result[i][1]))
        print('</tr>'),
    print('</tbody>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="clients.cgi?current={}&query={}"><span style="color: #fff;">⟪</span></a>'.format(0, search_query))
    print('<a href="clients.cgi?current={}&query={}"><span style="color: #fff;">⟨</span></a>'.format(current - MAX, search_query))
    print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
    print('<a href="clients.cgi?current={}&query={}"><span style="color: #fff;">⟩</span></a>'.format(current + MAX, search_query))
    print('<a href="clients.cgi?current={}&query={}"><span style="color: #fff;">⟫</span></a>'.format(math.floor(count/MAX)*MAX, search_query))
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center; margin-top: 0px; margin-bottom: 20px;">')
    print('<a href="addCustomer.cgi"><button class="pushable" style="background: #3a5ac9;"><span class="front" style="background: #7289da;">{}</span></button></a>'.format("Add a Customer"))
    print('</div>')

    cursor.close()
except Exception as e:
    print('<h1>No customers with searched name</h1>')

finally:
    if connection is not None:
        connection.close()

base.finish()