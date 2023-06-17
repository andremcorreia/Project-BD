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

    base.addTabs(0)

    # Making query
    sku = form.getvalue('id')
    Pname = form.getvalue('Pname')
    if not sku:
        sql = 'SELECT p.SKU, p.name, p.description, p.price FROM product p WHERE name ILIKE %s;'
        cursor.execute(sql, ('%' + search_query + '%',))
    else:
        sql = "SELECT supplier.TIN, supplier.name, supplier.address, supplier.SKU, supplier.date FROM supplier WHERE SKU = %s AND name ILIKE %s;"
        cursor.execute(sql, (sku, ('%' + search_query + '%',)))

    result = cursor.fetchall()
    
    print('<div class="header">')
    print('<div style="text-align:center; margin-top: 60px;">')
    if not sku:
        print('<p><b>Products and Suppliers</b></p>') 
        print('<form action="products.cgi" method="get">')
    else:
        print('<p><b>Suppliers of {}</b></p>'.format(Pname)) 
        print('<form action="products.cgi" method="get">')
        print('<input type="hidden" name="current" value="{}">'.format(current))
        print('<input type="hidden" name="id" value="{}">'.format(sku))
        print('<input type="hidden" name="Pname" value="{}">'.format(Pname))
    print('<input type="Search" name="query" placeholder="🔍 Search by name" value="{}" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc;">'.format(search_query))
    print('</form>') 
    print('</div>')

    print('<div class="table-container">')
    print('<table border="0">')

    # Paging Overflow check
    count = len(result)
    if current >= count:
        current = math.floor((count - 1)/MAX)*MAX

    if not sku:
        if count > 0:
            print('<tr><th>SKU</th><th>Name</th><th>Description</th><th>Price</th><th>Suppliers</td></tr>')

        for i in range(current, len(result)):
            row = result[i]
            if i >= MAX + current:
                    break
            print('<tr>')
            print('<td>{}</td>'.format(row[0]))
            print('<td>{}</td>'.format(row[1]))
            print('<td><a href="edit.cgi?sku={}&name={}&type={}"style="text-decoration: none;"><span style="color: #7289da;">{}</span></a></td>'.format(row[0],row[1],"Description",row[2]))
            print('<td><a href="edit.cgi?sku={}&name={}&type={}"style="text-decoration: none;"><span style="color: #7289da;">{}</span></a></td>'.format(row[0],row[1],"Price",row[3]))
            print('<td><a href="products.cgi?current={}&id={}&Pname={}"style="text-decoration: none;"><span style="color: #1fb622;">{}</span></a></td>'.format(0, row[0], row[1], "See Suppliers"))
            print('<td><a href="delete.cgi?table={}&id={}&name={}"style="text-decoration: none;"><span style="color: red;">&#10060;</span></a></td>'.format("product",row[0],row[1]))
            print('</tr>')

    else:
        if count > 0:
            print('<tr><th>TIN</th><th>Name</th><th>Address</th><th>SKU</th><th>Date</td></tr>')

        for i in range(current, len(result)):
            row = result[i]
            if i >= MAX + current:
                    break
            print('<tr>')
            print('<td>{}</td>'.format(row[0]))
            print('<td>{}</td>'.format(row[1]))
            print('<td>{}</td>'.format(row[2]))
            print('<td>{}</td>'.format(row[3]))
            print('<td>{}</td>'.format(row[4]))
            print('<td><a href="delete.cgi?table={}&id={}&name={}&supp_count={}&sku={}"style="text-decoration: none;"><span style="color: red;">&#10060;</span></a></td>'.format("supplier",row[0],row[1], count, sku))
            print('</tr>')

    print('</tbody>')
    print('</table>')
    print('</div>')
    print('<div class="navigation">')

    if not sku:
        print('<a href="products.cgi?current={}&query={}"><span style="color: #fff;">&Lang;</span></a>'.format(0, search_query))
        print('<a href="products.cgi?current={}&query={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX, search_query))
        print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
        print('<a href="products.cgi?current={}&query={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX, search_query))
        print('<a href="products.cgi?current={}&query={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX, search_query))
    
    else:
        print('<a href="products.cgi?current={}&id={}&Pname={}&query={}"><span style="color: #fff;">&Lang;</span></a>'.format(0, sku, Pname, search_query))
        print('<a href="products.cgi?current={}&id={}&Pname={}&query={}"><span style="color: #fff;">&lang;</span></a>'.format(current - MAX, sku, Pname, search_query))
        print('<p>Page {}/{}</p>'.format(math.floor(current/MAX) + 1, math.ceil(count/MAX)))
        print('<a href="products.cgi?current={}&id={}&Pname={}&query={}"><span style="color: #fff;">&rang;</span></a>'.format(current + MAX, sku, Pname, search_query))
        print('<a href="products.cgi?current={}&id={}&Pname={}&query={}"><span style="color: #fff;">&Rang;</span></a>'.format(math.floor(count/MAX)*MAX, sku, Pname, search_query))        
    
    print('</div>')
    print('<div class="footer">')
    print('<div style="text-align: center;">')

    if not sku:
        print('<a href="addProduct_Supplier.cgi"><button class="pushable" style="background: #3a5ac9;"><span class="front" style="background: #7289da;">{}</span></button></a>'.format("Add a Product"))

    else:
        print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku, Pname))
        print('<div style="margin-bottom: 30px;"> </div>') 
        #print('<a href="products.cgi"><button class="button" style="background-color: grey; margin-left: -20px; line-height: 50px;">Cancel</button></a>')
        #print('<a href="addSupplier.cgi"><button class="pushable" style="background: #3a5ac9;"><span class="front" style="background: #7289da;">{}</span></button></a>'.format("Add a Customer"))
        print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
        print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku, Pname))
        print('<a href="products.cgi" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Back</span></a>')
        print('<a style="margin-right: 40px;"> </a>')
        print('<button type="submit" class="pushable" style="background: #3a5ac9;"><span class="front" style="background: #7289da;">Add a Supplier</button>')    
        print('</form>')

    print('</div>')
    print('</form>')

    print('</div>')

    cursor.close()

except Exception as e:
    print('<h1>Nothing found with searched name</h1>')

finally:
    if connection is not None:
        connection.close()

base.finish()
