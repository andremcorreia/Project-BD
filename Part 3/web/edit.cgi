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
    print('<p>Editing the {} from {}</p>'.format(type, name))

    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post">'.format(sku, name,type))
    print('<div style="margin-left: -20px;">')
    print('<p>{}:</p> <input type="text" name="new" style="background-color: lightgrey; width: 110%;"{}/>'.format(type, settings))
    print('</div>')

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="products.cgi" class="button" style="background-color: grey; margin-left: -20px; line-height: 50px;">Cancel</a>')
    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku, name,type))
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
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
