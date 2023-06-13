#!/usr/bin/python3
import psycopg2
import cgi
import login

form = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Project - Add Product/Supplier</title>')
print('</head>')
print('<body>')

if not form.getvalue('SKU'):
    print('<h3>Adding a new Product and Supplier</h3>')
    # The form will send the info needed for the Product and Supplier SQL query
    print('<form action="addProduct_Supplier.cgi" method="post">')
    print('<p>SKU: <input type="text" name="SKU"/></p>')
    print('<p>Product Name: <input type="text" name="name_prod"/></p>')
    print('<p>Description: <input type="text" name="description"/></p>')
    print('<p>Price: <input type="text" name="price"/></p>')
    print('<p>Ean (optional): <input type="text" name="ean"/></p>')
    print('<p>Supplier TIN: <input type="text" name="TIN"/></p>')
    print('<p>Supplier Name: <input type="text" name="name_supp"/></p>')
    print('<p>Supplier Address: <input type="text" name="address"/></p>')
    print('<p>Contract Date: <input type="text" name="date"/></p>')
    print('<p><input type="submit" value="Submit"/></p>')
    print('</form>')
else:
    SKU = form.getvalue('SKU')
    name_product = form.getvalue('name_prod')
    description = form.getvalue('description')
    price = form.getvalue('price')
    ean = form.getvalue('ean')

    TIN = form.getvalue('TIN')
    name_supplier = form.getvalue('name_supp')
    address = form.getvalue('address')
    date = form.getvalue('date')

    connection = None

    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Start the transaction
        connection.autocommit = False

        # Insert Product
        sql_product = "INSERT INTO product (SKU, name, description, price, ean) VALUES %(param)s;"
        data_product = {'param': (SKU, name_product, description, price, ean)}
        cursor.execute(sql_product, data_product)

        # Insert Supplier
        sql_supplier = "INSERT INTO supplier (TIN, name, address, SKU, date) VALUES %(param)s;"
        data_supplier = {'param': (TIN, name_supplier, address, SKU, date)}
        cursor.execute(sql_supplier, data_supplier)

        # Commit the transaction
        connection.commit()

        # Reset autocommit mode
        connection.autocommit = True

    except Exception as e:
        # Rollback the transaction on error
        connection.rollback()
        print('<h1>An error occurred.</h1>')
    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=products.cgi" />')

print('</body>')
print('</html>')
