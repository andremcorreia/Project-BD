#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()
table = form.getvalue('table')
id = form.getvalue('id')
name = form.getvalue('name')
supp_counter = form.getvalue('supp_count')
sku = form.getvalue('sku')

base.Setup()

refreshed = False

back = "clients"
if table == "product" or table == "supplier":
    back = "products"

# Corfirmation form
if not form.getvalue('confirmation'):
    print('<h3 style="font-size:30px;">Are you sure you wish to delete {}, {}? 🗑️</h3>'.format(table, name))

    if table == 'supplier':
        if int(supp_counter) == 1:
            print('<p style="font-size:30px;">&#9888;&#65039; Warning: This will delete its associated product, as there\'s no more suppliers &#9888;&#65039;</p>')


    print('<form action="delete.cgi?table={}&id={}&name={}&confirmation={}&supp_count={}&sku={}" method="post">'.format(table, id, name, "yes", supp_counter, sku))
    print('<div style="margin-bottom: 30px;"> </div>') 

    # Buttons
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<form action="delete.cgi?table={}&id={}&name={}&confirmation={}&supp_count={}&sku={}" method="post" style="margin-left: 20px; margin-right: 20px;">'.format(table, id, name, "yes", supp_counter, sku))
    print('<a href="{}.cgi" class="pushable" style="background-color: #80857f; text-decoration: none;"><span class="front" style="background: #d6dbd5; color: black;">Cancel</span></a>'.format(back))
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
        connection.autocommit = True

        # Delete customer Logic
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

        # Delete product Logic
        elif table == 'product':
            # Get all TIN (supplier) associated with product
            sql_get_supp = "SELECT TIN FROM supplier WHERE SKU = '{}';".format(id)
            cursor.execute(sql_get_supp)
            suppliers = cursor.fetchall()

            # Get all distinct order_no associated with product
            sql_get_orders = "SELECT DISTINCT order_no FROM contains WHERE SKU = '{}';".format(id)
            cursor.execute(sql_get_orders)
            dist_orders = cursor.fetchall()
            
            sql_get_contains = "SELECT DISTINCT SKU FROM contains WHERE order_no = {};"
            orders_to_del = []

            for order in dist_orders:
                cursor.execute(sql_get_contains.format(order[0]))
                result = cursor.fetchall()
                if len(result) == 1:
                    orders_to_del += [order[0]]

            connection.autocommit = False

            sql_del = "DELETE FROM contains WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
            for order in orders_to_del:
                sql_del = 'DELETE FROM pay WHERE order_no = {};'.format(order)
                cursor.execute(sql_del)
                sql_del = 'DELETE FROM process WHERE order_no = {};'.format(order)
                cursor.execute(sql_del)
                sql_del = 'DELETE FROM "order" WHERE order_no = {};'.format(order)
                cursor.execute(sql_del)

            sql_del = "DELETE FROM delivery WHERE TIN = '{}';"
            for supp in suppliers:
                cursor.execute(sql_del.format(supp[0]))

            sql_del = "DELETE FROM supplier WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
            
            sql_del = "DELETE FROM product WHERE SKU = '{}';".format(id)
            cursor.execute(sql_del)
        
        # Delete supplier Logic
        elif table == 'supplier':
            supp_counter = int(supp_counter)
            if supp_counter > 1:
                sql_del = "DELETE FROM supplier WHERE TIN = '{}';".format(id)
                cursor.execute(sql_del)
            else:
                refreshed = True
                print('<meta http-equiv="refresh" content="0; url=delete.cgi?table={}&id={}&confirmation={}" />'.format('product', sku, "yes"))

        connection.commit()
        connection.autocommit = True
        cursor.close()

    except Exception as e:
        connection.rollback()
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    if not refreshed:
        print('<meta http-equiv="refresh" content="0; url={}.cgi" />'.format(back))

base.finish()