#!/usr/bin/python3
import psycopg2, cgi
import login, base

form = cgi.FieldStorage()

base.Setup()

order_no = form.getvalue('order_no')
cust_no = form.getvalue('cust_no')
date = form.getvalue('date')
SKUs = form.getlist('SKU[]')
qtys = form.getlist('quantity[]')

# Form
if not order_no or not cust_no or not date or not SKUs or not qtys:
    print('<h3 style="font-size: 24px;">Adding a new order</h3>')

    print('<form action="addOrder.cgi" method="post">')
    print('<div style="margin-left: -20px;">')
    print('<p>Order Number:</p> <input type="text" name="order_no" style="background-color: lightgrey; width: 110%;"/>')
    if (order_no or cust_no or date or SKUs or qtys) and not order_no:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('<p>Customer Number:</p> <input type="text" name="cust_no" style="background-color: lightgrey; width: 110%;"/>')
    if (order_no or cust_no or date or SKUs or qtys) and not cust_no:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('<p>Date:</p> <input type="text" name="date" style="background-color: lightgrey; width: 110%;"/>')
    if (order_no or cust_no or date or SKUs or qtys) and not date:
        print('<div style="color: #f5473b; font-size: 12px;">Required field</div>') 
    print('</div>')
    
    # Dynamic form for adding multiple products
    print('<div id="product-forms">')
    print('<div style="margin-left: -20px;">')
    print('<h4>Product 1:</h4>')
    print('<p>Product SKU:</p> <input type="text" name="SKU[]" style="background-color: lightgrey; width: 110%;"/>')
    print('<p>Quantity:</p> <input type="text" name="quantity[]" style="background-color: lightgrey; width: 110%;"/>')
    print('</div>')
    print('</div>')

    if (order_no or cust_no or date) and (not SKUs or not qtys):
        print('<div style="color: #f5473b; margin-left: -20px; font-size: 12px;">At least 1 product required</div>') 
    
    # Buttons
    print('<button type="button" onclick="addProductForm()" class="button" style="background-color: #7289da; margin-left: 0px;  margin-top: 20px; height: 50px; width: 200px;">Add another product</button>')
    print('<div class="confirm-buttons" style="display: flex; justify-content: center; margin-top: 10px;">')
    print('<a href="orders.cgi" class="button" style="background-color: grey; margin-left: -20px; line-height: 50px; line-height: 50px;">Cancel</a>')
    print('<form action="addOrder.cgi" method="post" style="margin-left: 20px; margin-right: 20px;">')
    print('<button type="submit" class="button" style="background-color: #25b80b; margin-right: -20px;">Submit</button>')
    print('</form>')
    print('</div>')
    
    print('</form>')
    
    # JavaScript code for adding more products
    print('''
        <script>
            var productCount = 1;
            function addProductForm() {
                productCount++;
                var productForms = document.getElementById("product-forms");
                var newForm = document.createElement("div");
                newForm.style.marginLeft = "-20px";
                newForm.innerHTML = '<h4>Product ' + productCount + ':</h4>' +
                                    '<p>Product SKU:</p> <input type="text" name="SKU[]" style="background-color: lightgrey; width: 110%;"/>' +
                                    '<p>Quantity:</p> <input type="text" name="quantity[]" style="background-color: lightgrey; width: 110%;"/>';
                productForms.appendChild(newForm);
            }
        </script>
    ''')

# Execution of the queries
else:
    connection = None

    try:
        connection = psycopg2.connect(login.credentials)
        cursor = connection.cursor()

        connection.autocommit = False

        sql_order = 'INSERT INTO "order" (order_no, cust_no, date) VALUES %(param)s;'
        data_order = {'param': (order_no, cust_no, date)}

        cursor.execute(sql_order, data_order)

        for SKU, qty in zip(SKUs, qtys):
            sql_contains = "INSERT INTO contains (order_no, SKU, qty) VALUES %(param)s;"
            data_contains = {'param': (order_no, SKU, qty)}
            cursor.execute(sql_contains, data_contains)

        connection.commit()
        connection.autocommit = True
        cursor.close()

    except Exception as e:
        connection.rollback()
        print('<h1>An error occurred.</h1>')

    finally:
        if connection is not None:
            connection.close()

    print('<meta http-equiv="refresh" content="0; url=orders.cgi" />')

base.finish()
