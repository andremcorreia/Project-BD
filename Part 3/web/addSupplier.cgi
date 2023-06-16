#!/usr/bin/python3
import psycopg2
import cgi
import login, base

form = cgi.FieldStorage()

base.Setup()
sku = form.getvalue('SKU')
prod_name = form.getvalue('Pname')
TIN = form.getvalue('TIN')
name_supplier = form.getvalue('Sname')
address = form.getvalue('address')
date = form.getvalue('date')

# Form
if not TIN or not name_supplier or not date:
    print('<h3 style="font-size: 24px;">Adding a new Supplier for {} 🚚</h3>'.format(prod_name))

    print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post">'.format(sku,prod_name))
    print('<div style="margin-left: -20px;">')
    print('<p>TIN:</p> <input type="text" name="TIN" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (name_supplier or date) and not TIN:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Supplier Name:</p> <input type="text" name="Sname" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (TIN or date) and not name_supplier:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Address:</p> <input type="text" name="address" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    print('<p>Contract date:</p> <input type="text" name="date" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"/>')
    if (TIN or name_supplier) and not date:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('</div>')

    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku,prod_name))
    print('<a href="products.cgi?id={}&Pname={}" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Cancel</span></a>'.format(sku,prod_name))
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

        sql_supplier = "INSERT INTO supplier (TIN, name, address, SKU, date) VALUES %(param)s;"
        data_supplier = {'param': (TIN, name_supplier, address, sku, date)}
        cursor.execute(sql_supplier, data_supplier)

        connection.commit()
        cursor.close()

    except Exception as e:
        connection.rollback()
        print('<h1>An error occurred.</h1>')
        
    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=products.cgi?id={}&Pname={}" />'.format(sku, prod_name))

base.finish()
