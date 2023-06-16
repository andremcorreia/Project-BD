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
    print('<h3 style="font-size: 24px;">Adding a new Supplier for {}</h3>'.format(prod_name))

    print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post">'.format(sku,prod_name))
    print('<div style="margin-left: -20px;">')
    print('<p>TIN:</p> <input type="text" name="TIN" style="background-color: lightgrey; width: 110%;"/>')
    if (name_supplier or date) and not TIN:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Supplier Name:</p> <input type="text" name="Sname" style="background-color: lightgrey; width: 110%;"/>')
    if (TIN or date) and not name_supplier:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('<p>Address:</p> <input type="text" name="address" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Contract date:</p> <input type="text" name="date" style="background-color: lightgrey; width: 110%;"/>')
    if (TIN or name_supplier) and not date:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>')
    print('</div>')

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="products.cgi?id={}&Pname={}" class="button" style="background-color: grey; margin-left: -20px; line-height: 50px;">Cancel</a>'.format(sku,prod_name))
    print('<form action="addSupplier.cgi?SKU={}&Pname={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku,prod_name))
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
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
