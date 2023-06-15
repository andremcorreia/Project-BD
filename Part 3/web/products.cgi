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
    base.addTabs(0)

    # Making query
    #sql = 'SELECT product.SKU, product.name, product.description, product.price, supplier.TIN, supplier.name, supplier.date FROM product JOIN supplier USING (SKU);'
    sql = 'SELECT product.SKU, product.name, product.description, product.price, product.ean FROM product;'
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
    #print('<tr><th>SKU</th><th>Name</th><th>Description</th><th>Price</th><th>Supplier TIN</th><th>Supplier Name</th><th>Contract Date</td></tr>')
    print('<tr><th>SKU</th><th>Name</th><th>Description</th><th>Price</th><th>ean</th><th>Suppliers</td></tr>')
 
    count = len(result)
    if current > count:
        current = math.floor(count/MAX)*MAX

    for i in range(current, len(result)):
        row = result[i]
        if i >= MAX + current:
                break
        print('<tr>')
        print('<td>{}</td>'.format(row[0]))
        print('<td>{}</td>'.format(row[1]))
        print('<td><a href="edit.cgi?sku={}&name={}&type={}"style="text-decoration: none;"><span style="color: #7289da;">{}</span></a></td>'.format(row[0],row[1],"Description",row[2]))
        print('<td><a href="edit.cgi?sku={}&name={}&type={}"style="text-decoration: none;"><span style="color: #7289da;">{}</span></a></td>'.format(row[0],row[1],"Price",row[3]))
        print('<td>{}</td>'.format(row[4]))
        
        print('<td><a href="products.cgi?orderID={}&custID={}"style="text-decoration: none;"><span style="color: #1fb622;">{}</span></a></td>'.format(row[0],row[1],"pay"))

        #print('<td>{}</td>'.format(row[5]))
        #print('<td>{}</td>'.format(row[6]))
        print('<td><a href="delete.cgi?current={}&id={}&name={}"style="text-decoration: none;"><span style="color: red;">&#10060;</span></a></td>'.format("product",row[0],row[1]))
        print('</tr>')

    print('</tbody>')

    print('</table>')
    print('</div>')
    print('<div class="navigation">')
    print('<a href="products.cgi?current={}"><span style="color: #fff;">&Lang;</span></a>'.format(0))
    print('<a href="products.cgi?current={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX))
    print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
    print('<a href="products.cgi?current={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX))
    print('<a href="products.cgi?current={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX))
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')
    print('<a href="addProduct_Supplier.cgi"><button class="button" style="background-color: #7289da; width: 200px;">{}</button></a>'.format("Add a Product"))
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
