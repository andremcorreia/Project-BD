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
    base.addTabs(0)

    # Making query
    sql = 'SELECT product.SKU, product.name, product.description, product.price, supplier.TIN, supplier.name, supplier.date FROM product JOIN supplier USING (SKU);'
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Display Header
    print('<div class="header">')
    print('<div style="text-align:center; margin-top: 60px;">')
    print('<p><b>Products and Suppliers</b></p>') 
    print('</div>')

    # Displaying results
    print('<div class="table-container">')
    print('<table border="0">')
    print('<tr><td>SKU</td><td>Name</td><td>Description</td><td>Price</td><td>Supplier TIN</td><td>Supplier Name</td><td>Contract Date</td></tr>')
    
    for row in result:
        print('<tr>')
        print('<td>{}</td>'.format(row[0]))
        print('<td>{}</td>'.format(row[1]))
        print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: #0c86cc;">{}</span></a></td>'.format("product","description",row[0],row[2]))
        print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: #0c86cc;">{}</span></a></td>'.format("product","price",row[0],row[3]))
        print('<td>{}</td>'.format(row[4]))
        print('<td>{}</td>'.format(row[5]))
        print('<td>{}</td>'.format(row[6]))
        print('<td><a href="update.cgi?table={}?request={}?SKU={}"><span style="color: red;">{}</span></a></td>'.format("product","delete",row[0],"X"))
        print('</tr>')

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
    print('<a href="addProduct_Supplier.cgi"><span style="color: #7289da;">{}</span></a>'.format("Add a Product"))
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
