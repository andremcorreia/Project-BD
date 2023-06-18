#!/usr/bin/python3
import psycopg2
import cgi
import login, base

form = cgi.FieldStorage()

base.Setup()

SKU = form.getvalue('SKU')
name_product = form.getvalue('name_prod')
description = form.getvalue('description')
price = form.getvalue('price')
ean = form.getvalue('ean')
TIN = form.getvalue('TIN')
name_supplier = form.getvalue('name_supp')
address = form.getvalue('address')
date = form.getvalue('date')

# Form
if not SKU or not name_product or not price or not TIN or not name_supplier or not date or (address and not base.addressCheck(address)):
    print('<h3 style="font-size: 24px;">Adding a new Product and Supplier 🗿</h3>')

    print('<form action="addProduct_Supplier.cgi" method="post">')
    print('<div style="margin-left: -20px;">')
    print('<p>SKU:</p> <input type="text" name="SKU" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (name_product or price or TIN or name_supplier or date) and not SKU:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('<p>Product Name:</p> <input type="text" name="name_prod" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (SKU or price or TIN or name_supplier or date) and not name_product:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Description:</p> <input type="text" name="description" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    print('<p>Price:</p> <input type="text" name="price" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (SKU or name_product or TIN or name_supplier or date) and not price:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Ean (optional):</p> <input type="text" name="ean" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    print('<p>Supplier TIN:</p> <input type="text" name="TIN" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (SKU or name_product or price or name_supplier or date) and not TIN:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Supplier Name:</p> <input type="text" name="name_supp" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (SKU or name_product or price or TIN or date) and not name_supplier:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Supplier Address:</p> <input type="text" name="address" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if address and not base.addressCheck(address):
        print('<div style="color: #f5473b; font-size: 12px;">Must be of format | street, XXXX-XXX city |</div>')
    print('<p>Contract Date:</p> <input type="text" name="date" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (SKU or name_product or price or TIN or name_supplier) and not date:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('</div>')

    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<form action="addProduct_Supplier.cgi" method="post" style="margin-left: 20px; margin-right: 20px;">')
    print('<a href="products.cgi" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Cancel</span></a>')
    print('<a style="margin-right: 40px;"> </a>')
    print('<button type="submit" class="pushable" style="background-color: #147303;"><span class="front" style="background: #2cc211;">Submit</button>')    
    print('</form>')
    print('</div>')
    print('</form>')

# Execution of the queries
else:
    connection = None

    try:
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        connection.autocommit = False

        sql_product = "INSERT INTO product (SKU, name, description, price, ean) VALUES %(param)s;"
        data_product = {'param': (SKU, name_product, description, price, ean)}
        cursor.execute(sql_product, data_product)

        sql_supplier = "INSERT INTO supplier (TIN, name, address, SKU, date) VALUES %(param)s;"
        data_supplier = {'param': (TIN, name_supplier, address, SKU, date)}
        cursor.execute(sql_supplier, data_supplier)

        connection.commit()
        connection.autocommit = True
        cursor.close()


    except Exception as e:
        connection.rollback()
        print('<h1>An error occurred.</h1>')
    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=products.cgi" />')

base.finish()
