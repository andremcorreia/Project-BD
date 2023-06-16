#!/usr/bin/python3
def Setup():
    print('Content-type:text/html\n\n')
    print('<html>')
    print('<head>')
    print('<title>Project</title>')
    print('<meta name="viewport" content="width=device-width, initial-scale=1">')
    print('<style>')

    # General
    print('body {')
    print('  display: flex;')
    print('  flex-direction: column;')
    print('  justify-content: center;')
    print('  align-items: center;')
    print('  background-color: #1e2124;')
    print('  color: #fff;')
    print('  min-height: 100vh;')
    print('  font-size: 18px;')
    print('  margin: 0;')
    print('  padding: 0;')
    print('  font-family: Arial, Helvetica, sans-serif;')
    print('  background-image: linear-gradient(to bottom, #1e2124, #25292d, #1e2124);')
    print('  background-repeat: no-repeat;')
    print('  background-position: center;')
    print('}')

    # Buttons
    print('.button {')
    print('  text-decoration: none;')
    print('  height: 50px;')
    print('  width: 120px;')
    print('  text-align: center;')
    print('  font-size: 20px;')
    print('  color: white;')
    print('  border-radius: 10px;')
    print('}')
    print('.button:hover {')
    print('  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);')
    print('}')

    # Header
    print('header {')
    print('  background-color: #fff;')
    print('  color: #fff;')
    print('  position: fixed;')
    print('  top: 25;')
    print('  left: 50;')
    print('}')

    # Footer
    print('footer {')
    print('  position: fixed;')
    print('  top: 75;')
    print('  left: 50;')
    print('}')

    # Table Outside
    print('.table-container {')
    print('  background-color: #1e2124;')
    print('  color: #fff;')
    print('  width: 100%;')
    print('}')

    # Table Inside
    print('.table-container table {')
    print('  table-layout: fixed;')
    print('}')
    print('.table-container td, .table-container th {')
    print('  border-collapse: collapse;')
    print('  border: none;')
    print('  padding: 3.5pt 10pt;')
    print('  word-wrap: break-word;')
    print('}')
    print('.table-container tr:nth-child(even) td {')
    print('  background-color: #36393e;')
    print('}')

    print('.table-container tr {')
    print('  padding: 10px;')
    print('}')
    print('.table-container tr:hover td {')
    print('  background-color: #6b6e70;')
    print('}')

    print('.table-container th {')
    print('  border: none;')
    print('  padding: 5pt 10pt;')
    print('}')

    # Tabs
    print('.tabs {')
    print('  display: flex;')
    print('  justify-content: space-between;')
    print('  width: 100%;')
    print('  position: fixed;')
    print('  top: 0;')
    print('  left: 0;')
    print('  background-color: #1e2124;')
    print('}')

    print('.tab {')
    print('  display: flex;')
    print('  justify-content: center;')
    print('  width: 33.33%;')
    print('  align-items: center;')
    print('  flex-grow: 1;')
    print('  height: 50px;')
    print('  background-color: #36393e;')
    print('  border: 1px solid #1e2124;')
    print('  text-decoration: none;')
    print('  text-align: center;')
    print('  color: #fff;')
    print('  font-size: 24px;')
    print('  border-radius: 10px;')
    print('  background-image: linear-gradient(to bottom, #36393e, #25292d);')
    print('}')

    print('.tab-active {')
    print('  display: flex;')
    print('  width: 33.33%;')
    print('  justify-content: center;')
    print('  align-items: center;')
    print('  flex-grow: 1;')
    print('  height: 50px;')
    print('  background-color: #1e2124;')
    print('  color: #fff;')
    print('  text-align: center;')
    print('  text-decoration: none;')
    print('  font-size: 24px;')
    print('  border-radius: 10px;')
    print('}')

    print('.tab:hover {')
    print('  background-image: linear-gradient(to bottom, #424549, #25292d);')
    print('}')

    # Navigation
    print('.navigation {')
    print('  display: flex;')
    print('  justify-content: space-between;')
    print('  margin-bottom: 0px;')
    print('}')

    print('.navigation a {')
    print('  text-decoration: none;')
    print('  color: #fff;')
    print('}')

    print('.navigation a:hover {')
    print('  color: #7289da;')
    print('}')

    print('</style>')
    print('</head>')
    print('<body>')

def addTabs(tabID):
    tabs = ["tab-active" if i == tabID else "tab" for i in range(3)]
    tabNames = ["Products & Suppliers", "Customers", "Orders"]
    tabLinks = ["products.cgi", "clients.cgi", "orders.cgi"]
    print('<div class="tabs">')
    for i in range(3):
        tag = 'div' if i == tabID else 'a href="{}"'.format(tabLinks[i])
        print('<{} class="{}">{}</{}>'.format(tag, tabs[i], tabNames[i], tag.split()[0]))
    print('</div>')

def finish():
    print('</body>')
    print('</html>')

