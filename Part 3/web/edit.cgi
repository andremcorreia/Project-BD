#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
sku = form.getvalue('sku')
name = form.getvalue('name')
type = form.getvalue('type')

if type == "Description":
    settings = 'size="20"'
else:
    settings = ""

base.Setup()

# Form
if not form.getvalue('new'):
    print('<h3 style="font-size:30px;" > Editing the {} for {} 📝</h3>'.format(type, name))

    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post">'.format(sku, name,type))
    print('<div style="margin-left: -20px;">')
    print('<p>{}:</p> <input type="text" name="new" style="padding:5px; font-size:12px; border-radius:5px; border:0px solid #ccc; width: 110%;"{}/>'.format(type, settings))
    print('</div>')

    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku, name,type))
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
        new = form.getvalue('new')

        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        if type == "Description":
            sql = "UPDATE product SET description = %s WHERE SKU = %s;"
        elif type == "Price":
            sql = "UPDATE product SET price = %s WHERE SKU = %s;"
        data = (new, sku)

        cursor.execute(sql, data)
        connection.commit()
        cursor.close()

    except Exception as e:
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=products.cgi" />')
    
base.finish()
