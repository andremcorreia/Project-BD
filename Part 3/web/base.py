#!/usr/bin/python3
import psycopg2
import login

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
    print('  padding: 5pt 10pt;')
    print('  word-wrap: break-word;') # Prevent text overflow
    print('}')
    print('.table-container tr:nth-child(even) td {')
    print('  background-color: #36393e;')
    print('}')

    # Additional styles for table header
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
    print('}')

    print('.tab {')
    print('  display: flex;')
    print('  justify-content: center;')
    print('  align-items: center;')
    print('  flex-grow: 1;')
    print('  height: 50px;')
    print('  background-color: #36393e;')
    print('  border: 1px solid #1e2124;')
    print('  text-decoration: none;')
    print('  color: #fff;')
    print('  font-size: 24px;')
    print('}')

    print('.tab-active {')
    print('  display: flex;')
    print('  justify-content: center;')
    print('  align-items: center;')
    print('  flex-grow: 1;')
    print('  height: 50px;')
    print('  background-color: #1e2124;')
    print('  color: #fff;')
    print('  text-decoration: none;')
    print('  font-size: 24px;')
    print('}')

    print('.tab:hover {')
    print('  background-color: #424549;')
    print('}')

    # Navigation
    print('.navigation {')
    print('  display: flex;')
    print('  justify-content: space-between;')
    print('  margin-bottom: 10px;')
    print('}')

    print('.navigation a {')
    print('  text-decoration: none;')
    print('  color: #fff;')
    print('}')

    print('</style>')
    print('</head>')
    print('<body>')

def addTabs(tabID):
    tabs = ["tab-active" if i == tabID else "tab" for i in range(3)]
    tabNames = ["Products", "Customers", "Orders"]
    tabLinks = ["products.cgi", "clients.cgi", "orders.cgi"]
    print('<div class="tabs">')
    for i in range(3):
        tag = 'div' if i == tabID else 'a href="{}"'.format(tabLinks[i])
        print('<{} class="{}">{}</{}>'.format(tag, tabs[i], tabNames[i], tag.split()[0]))
    print('</div>')



def finish():
    print('</body>')
    print('</html>')
