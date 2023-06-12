#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Project</title>')
print('<style>')
print('body {')
print('  display: flex;')
print('  justify-content: center;')
print('  align-items: center;')
print('  background-color: #444;')  # Change background color to dark mode
print('  color: #fff;')  # Change text color to white
print('}')

print('.table-container {')
print('  margin: 10px;')
print('  background-color: #444;')  # Change table container background color to dark mode
print('  color: #fff;')  # Change table text color to white
print('}')

print('.table-container td {')
print('  color: #fff;')  # Change table data text color to white
print('}')

print('</style>')
print('</head>')
print('<body>')

connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT * FROM "order";'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying results
    print('<div class="table-container">')
    print('<p>Orders</p>')
    print('<table border="5">')
    print('<tr><td>ID</td><td>Customer ID</td><td>Date</td></tr>')
    
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: #1fb622;">{}</span></a></td>'.format("order","pay",row[0],"pay"))
        print('</tr>')

    print('</table>')
    print('<td><a href="update.cgi?table={}?request={}"><span style="color: #0c86cc;">{}</span></a></td>'.format("order","add","Place an Order"))
    print('</div>')


    # Closing connection
    cursor.close()

except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if connection is not None:
        connection.close()

print('</body>')
print('</html>')
