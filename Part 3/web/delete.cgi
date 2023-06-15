#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
table = form.getvalue('table')
id = form.getvalue('id')
name = form.getvalue('name')
# Get the number of suppliers of the product (sku) associated with current supplier
supp_counter = int(form.getvalue('supp_count'))
sku = form.getvalue('sku')

base.Setup()

back = "clients"
if table == "product":
    back = "products"
elif table == "supplier":
    back = "products"

if not form.getvalue('confirmation'):
    print('<p style="font-size:30px;">Are you sure you wish to delete {}, {}?</p>'.format(table, name))

    # The form will send the info needed for the SQL query
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="{}.cgi" class="button" style="background-color: grey; margin-left: -20px; line-height: 50px;">Cancel</a>'.format(back))
    print('<form action="delete.cgi?table={}&id={}&name={}&confirmation={}&supp_count={}&sku={}" method="post" style="margin-left: 40px; margin-right: 40px;">'.format(table, id, name, "yes", supp_counter, sku))
    print('<button type="submit" class="button" style="background-color: #25b80b;">Confirm</button>')
    print('</form>')
    print('</div>')

else:

    connection = None
    try:
        # Creating connection
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()
        connection.autocommit = True

        if table == 'customer':
            # Get all order_no associated with customer
            sql_get_orders = 'SELECT order_no FROM "order" WHERE cust_no = {};'.format(id)
            cursor.execute(sql_get_orders)
            orders = cursor.fetchall()

            connection.autocommit = False

            sql_del = "DELETE FROM  WHERE order_no = {};"
            to_check = ('pay', 'contains', 'process', '\"order\"')
            for tab in to_check:
                for value in orders:
                    cursor.execute(sql_del[:12] + tab + sql_del[12:].format(value[0]))

            sql_del = "DELETE FROM customer WHERE cust_no = {};".format(id)
            cursor.execute(sql_del)

        elif table == 'product':
            # Get all TIN (supplier) associated with product
            sql_get_supp = "SELECT TIN FROM supplier WHERE SKU = '{}';".format(id)
            cursor.execute(sql_get_supp)
            suppliers = cursor.fetchall()

            # Get all distinct order_no associated with product
            sql_get_orders = "SELECT DISTINCT order_no FROM contains WHERE SKU = '{}';".format(id)
            cursor.execute(sql_get_orders)
            dist_orders = cursor.fetchall()
            
            # Get all order_no associated with product
            sql_get_orders = "SELECT order_no FROM contains WHERE SKU = '{}';".format(id)
            cursor.execute(sql_get_orders)
            orders = cursor.fetchall()

            connection.autocommit = False

            sql_del = "DELETE FROM delivery WHERE TIN = '{}';"
            for supp in suppliers:
                cursor.execute(sql_del.format(supp[0]))

            sql_del = "DELETE FROM contains WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
            for order in dist_orders:
                # Count of contains entries with certain order_no
                if orders.count(order) == 1:
                    sql_del = 'DELETE FROM pay WHERE order_no = {};'.format(order[0])
                    cursor.execute(sql_del)
                    sql_del = 'DELETE FROM process WHERE order_no = {};'.format(order[0])
                    cursor.execute(sql_del)
                    sql_del = 'DELETE FROM "order" WHERE order_no = {};'.format(order[0])
                    cursor.execute(sql_del)

            sql_del = "DELETE FROM supplier WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
            
            sql_del = "DELETE FROM product WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
        
        elif table == 'supplier':
            if supp_counter > 1:
                sql_del = "DELETE FROM supplier WHERE TIN = '{}';".format(id)
                cursor.execute(sql_del)
            else:
                print('<form action="" method="post">')
                print('<input type="hidden" name="table" value="\'product\'">')
                print('<input type="hidden" name="id" value="\'{}\'">'.format(sku))
                print('</form">')

        # Commit the update (without this step the database will not change)
        connection.commit()
        connection.autocommit = True

        # Closing connections
        cursor.close()

    except Exception as e:
        connection.rollback()
        print('<h1>{}</h1>'.format(str(e)))
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="10; url={}.cgi" />'.format(back))

base.finish()