#!/usr/bin/python3
import psycopg2
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Project</title>')
print('<style>')

# General
print('body {')
print('  display: flex;')
print('  flex-direction: column;')
print('  justify-content: center;')
print('  align-items: center;')
print('  background-color: #1e2124;')
print('  color: #fff;')
print('  height: 100vh;')
print('  font-size: 18px;')
print('}')

# Header
print('header {')
print('  display: flex;')
print('  flex-direction: column;')
print('  background-color: #fff;')
print('  color: #fff;')
print('  position: fixed;')
print('  top: 25;')
print('  left: 50;')
print('}')

# Footer
print('footer {')
print('  background-color: #fff;')
print('  color: #fff;')
print('  position: fixed;')
print('  top: 75;')
print('  left: 50;')
print('}')

# Table Outside
print('.table-container {')
print('  background-color: #1e2124;')
print('  color: #fff;')
print('}')

# Table Inside
print('.table-container td {')
#print('  border-style: groove;')
print('  color: #fff;')
print('}')

# Tabs 
print('.tabs {')
print('  display: flex;')
print('  justify-content: space-between;')
print('  width: 100%;')
print('  position: fixed;')
print('  top: 0;')
print('  left: 0;')
print('}')

print('.tab {')
print('  display: flex;')
print('  justify-content: center;')
print('  align-items: center;')
print('  flex-grow: 1;')
print('  height: 50px;')
print('  background-color: #36393e;')
print('  border: 1px solid #1e2124;')
print('  text-decoration: none;')
print('  color: #fff;')
print('  font-size: 24px;')
print('}')

print('.tab-active {')
print('  display: flex;')
print('  justify-content: center;')
print('  align-items: center;')
print('  flex-grow: 1;')
print('  height: 50px;')
print('  background-color: #1e2124;')
print('  color: #fff;')
print('  text-decoration: none;')
print('  font-size: 24px;')
print('}')

print('.tab:hover {')
print('  background-color: #424549;')
print('}')

# Navigation
print('.navigation {')
print('  display: flex;')
print('  justify-content: space-between;')
print('  margin-bottom: 10px;')
print('}')

print('.navigation a {')
print('  text-decoration: none;')
print('  color: #fff;')
print('}')

print('</style>')
print('</head>')
print('<body>')

connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Setting up the tabs
    print('<div class="tabs">')
    print('<a href="products.cgi" class="tab">Products</a>')
    print('<div class="tab-active">Customers</div>')
    print('<a href="orders.cgi" class="tab">Orders</a>')
    print('</div>')

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
    print('<table border="5">')
    print('<tr><td>ID</td><td>Name</td><td>E-mail</td><td>Phone</td><td>Address</td></tr>')
    
    for row in result:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: red;">{}</span></a></td>'.format("customer","delete",row[0],"X"))
        print('</tr>'),
    
    print('</table>')
    print('<div class="navigation">')
    print('<a href="#"><span style="color: #fff;">&Lang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&lang;</span></a>')
    print('<p>Page 0/0</p>')
    print('<a href="#"><span style="color: #fff;">&rang;</span></a>')
    print('<a href="#"><span style="color: #fff;">&Rang;</span></a>')
    print('</div>')
    print('</div>')

    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<a href="update.cgi?table={}?request={}"><span style="color: #7289da;">{}</span></a>'.format("customer","add","Add a Client"))
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