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

if not form.getvalue('new'):
    print('<p>Editing the {} from {}</p>'.format(type, name))

    # The form will send the info needed for the SQL query
    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post">'.format(sku, name,type))
    print('<div style="margin-left: -20px;">')
    print('<p>{}:</p> <input type="text" name="new" style="background-color: lightgrey; width: 110%;"{}/>'.format(type, settings))
    print('</div>')

    # Add a cancel button to the left of the submit button
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="products.cgi" class="button" style="background-color: grey; margin-left: -20px;">Cancel</a>')
    print('<form action="edit.cgi?sku={}&name={}&type={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(sku, name,type))
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
    print('</form>')
    print('</div>')

    print('</form>')

else:

    connection = None
    try:

        new = form.getvalue('new')

        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        # Query
        if type == "Description":
            sql = "UPDATE product SET description = %s WHERE SKU = %s;"
        elif type == "Price":
            sql = "UPDATE product SET price = %s WHERE SKU = %s;"
        data = (new, sku)

        print('<p>{}</p>'.format(sql % data))

        # Feed the data to the SQL query as follows to avoid SQL injection
        cursor.execute(sql, data)

        # Commit the update (without this step the database will not change)
        connection.commit()
        # Closing connection
        cursor.close()

    except Exception as e:
        print('<h1>{}</h1>'.format(str(e)))
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=products.cgi" />')
    
base.finish()
