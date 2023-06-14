import random

num_entries = 1000000  # Specify the number of entries you want to generate

# List of street names
street_names = [
    "Rua da Alegria",
    "Avenida dos Aliados",
    "Travessa das Flores",
    "Largo do Carmo",
    "Praça da Liberdade",
    "Avenida da Boavista",
    "Rua de Santa Catarina",
    "Estrada da Circunvalação",
    "Rua Mouzinho da Silveira",
    "Travessa dos Congregados",
    "Avenida Infante Dom Henrique",
    "Praça de Carlos Alberto",
    "Rua do Almada",
    "Avenida Dom Afonso Henriques",
    "Travessa de Cedofeita",
    "Largo dos Lóios",
    "Rua do Rosário",
    "Avenida da República",
    "Rua de Santa Teresa",
    "Travessa dos Clérigos",
    "Praça dos Leões",
    "Rua das Flores",
    "Avenida Central",
    "Travessa da Ribeira",
    "Largo de São Domingos",
    "Rua das Taipas",
    "Avenida Fernão de Magalhães",
    "Rua de Ceuta",
    "Travessa do Carregal",
    "Praça de D. João I",
    "Avenida de Montevideu",
    "Rua da Bainharia",
    "Avenida da França",
    "Travessa dos Mercadores",
    "Largo de São João Novo",
    "Rua de Santo Ildefonso",
    "Avenida do Brasil",
    "Rua do Bonjardim",
    "Travessa da Queimada",
    "Praça de Parada Leitão",
    "Avenida Camilo",
    "Rua de José Falcão",
    "Travessa das Virtudes",
    "Largo do Priorado",
    "Rua de Santa Catarina de Alexandria",
    "Avenida dos Combatentes",
    "Rua de Cedofeita",
    "Travessa do Rosário",
    "Praça de Guilherme Gomes Fernandes",
    "Avenida Marechal Gomes da Costa",
    "Rua de Passos Manuel",
    "Travessa das Oliveiras",
    "Largo da Sé",
    "Rua da Boa Nova",
    "Avenida do Parque",
    "Rua de Santo António",
    "Travessa dos Mártires",
    "Praça de Poveiros",
    "Avenida do Dr. Antunes Guimarães",
    "Rua de São Bento da Vitória",
    "Travessa do Carvalho",
    "Largo da Maternidade",
    "Rua de Serpa Pinto",
    "Avenida de Fernão de Magalhães",
    "Rua de Alexandre Braga",
    "Travessa das Pedras",
    "Praça de Almeida Garrett",
    "Avenida do Parque da Cidade",
    "Rua de Santo Ildefonso",
    "Travessa do Almada",
    "Largo do Amor de Perdição",
    "Rua de Camões",
    "Avenida do Brasil",
    "Rua de Sá da Bandeira",
    "Travessa dos Artistas",
    "Praça da Ribeira",
    "Avenida Engenheiro Duarte Pacheco",
    "Rua de Santa Teresa",
    "Travessa da Lada",
    "Largo da Estação",
    "Rua de Oliveira Monteiro",
    "Avenida dos Aliados",
    "Rua da Bélgica",
    "Travessa dos Cedros",
    "Praça de Carlos Alberto",
    "Avenida Dom Afonso Henriques",
    "Rua de Alves Redol",
    "Travessa de Cedofeita",
    "Largo dos Clérigos",
    "Rua das Virtudes",
    "Avenida da Liberdade",
    "Rua de Álvares Cabral",
    "Travessa da Ribeira",
    "Largo dos Lóios",
    "Rua de Gonçalo Cristóvão",
    "Avenida do Marechal Gomes da Costa",
    "Rua de Cândido dos Reis",
    "Travessa dos Ferreiros",
    "Praça da Batalha",
    "Avenida do Parque da Cidade",
    "Rua do Dr. Ricardo Jorge",
    "Travessa da Prelada",
    "Largo da Sé"
    "Main Street",
    "First Avenue",
    "Park Road",
    "Oak Street",
    "Maple Avenue",
    "Elm Street",
    "Cedar Lane",
    "Pine Street",
    "Washington Street",
    "Broadway",
    "High Street",
    "Church Road",
    "Market Street",
    "Hillside Avenue",
    "School Street",
    "Central Avenue",
    "North Street",
    "River Road",
    "Spring Street",
    "Chestnut Street",
    "Meadow Lane",
    "Sunset Boulevard",
    "Lakeview Drive",
    "Victoria Road",
    "Bridge Street",
    "Grove Avenue",
    "Country Lane",
    "Park Avenue",
    "Rose Street",
    "Birch Lane",
    "Forest Drive",
    "Cottage Lane",
    "Holly Court",
    "Meadow Lane",
    "Pleasant Street",
    "Riverside Drive",
    "Acacia Avenue",
    "Willow Street",
    "Laurel Lane",
    "Hickory Lane",
    "Magnolia Drive",
    "Orchard Street",
    "Hillcrest Avenue",
    "Brookside Drive",
    "Cherry Street",
    "Mansion Road",
    "Garden Lane",
    "Green Street",
    "Sycamore Street",
    "Summer Street",
    "Windsor Road",
    "Maple Lane",
    "Pinecrest Drive",
    "Crescent Street",
    "Prospect Avenue",
    "Mountain View Drive",
    "Walnut Street",
    "Cottonwood Lane",
    "Sherwood Drive",
    "Juniper Lane",
    "Locust Street",
    "Willow Lane",
    "Heather Court",
    "Spruce Street",
    "Cypress Lane",
    "Cedar Street",
    "Hilltop Road",
    "Sunset Avenue",
    "Oakwood Drive",
    "Pleasant Avenue",
    "Lake Street",
    "Riverside Drive",
    "Elmwood Avenue",
    "Beech Street",
    "Peachtree Street",
    "Magnolia Court",
    "Park Lane",
    "Rosewood Drive",
    "Valley Road",
    "Holly Street",
    "Poplar Lane",
    "Vine Street",
    "Mountain View Road",
    "Acorn Lane",
    "Birch Street",
    "Forest Lane",
    "Sunny Lane",
    "Main Street",
    "Cedar Avenue",
    "Pine Lane",
    "Maple Court",
    "River Street"
]
# List of city names
city_names = [
    "Lisbon",
    "Porto",
    "Vila Nova de Gaia",
    "Amadora",
    "Braga",
    "Funchal",
    "Coimbra",
    "Setúbal",
    "Almada",
    "Leiria",
    "Viseu",
    "Guimarães",
    "Evora",
    "Faro",
    "Santarém",
    "Viana do Castelo",
    "Barreiro",
    "Maia",
    "Odivelas",
    "Vila Franca de Xira",
    "Rio Tinto",
    "Aveiro",
    "Matosinhos",
    "Gondomar",
    "Guilhabreu",
    "Ponte de Lima",
    "Oeiras",
    "Ermesinde",
    "Fafe",
    "Caldas da Rainha",
    "Entroncamento",
    "Amora",
    "Póvoa de Varzim",
    "Beja",
    "Torres Vedras",
    "Vila do Conde",
    "Câmara de Lobos",
    "Montijo",
    "Albufeira",
    "Castelo Branco",
    "Mangualde",
    "Angra do Heroísmo",
    "Peso da Régua",
    "Lagoa",
    "Almancil",
    "Vila Real",
    "Chaves",
    "Amarante",
    "Mirandela",
    "Olhão",
    "Portimão",
    "Sesimbra",
    "Loures",
    "Santa Maria da Feira",
    "Covilhã",
    "Vila Nova de Famalicão",
    "Esposende",
    "Águeda",
    "Santa Cruz",
    "Marco de Canaveses",
    "Oliveira de Azeméis",
    "Peniche",
    "São João da Madeira",
    "Sintra",
    "Elvas",
    "Vila Real de Santo António",
    "Estremoz",
    "Vizela",
    "Portalegre",
    "Loulé",
    "Vendas Novas",
    "Figueira da Foz",
    "Pombal",
    "Seixal",
    "Cantanhede",
    "Espinho",
    "Gouveia",
    "Cartaxo",
    "Águeda",
    "Ovar",
    "Caldas de Vizela",
    "Alcácer do Sal",
    "Almada",
    "Águeda",
    "Bragança",
    "Miranda do Douro",
    "Vila do Bispo",
    "Figueiró dos Vinhos",
    "Viana do Alentejo",
    "Palmela",
    "Vila Nova de Milfontes",
    "Redondo",
    "Lagos"
]

def generate_insert_queries(n):
    for i in range(n):
        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"
        lat = round(0.0000 + i * 0.0001, 4)
        lon = round(0.0000 - i * 0.0001, 4)
        entry = f"({address}, {lat}, {lon})"
        if i < n - 1:
            entry += ","
        print(entry)


print("-- workplace and offices/warehouse need to be populated in a transaction due to RI-2")
print("START TRANSACTION;")
print("SET CONSTRAINTS ALL DEFERRED;")
print("INSERT INTO workplace (address, lat, lon) VALUES")
generate_insert_queries(num_entries)
print(";")

def generate_address(start, end):
    for i in range(start, end + 1):
        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"
        if i < end:
            address += ","
        print(address)


print("INSERT INTO office (address) VALUES")
start_index = 1  # Specify the start index of the street names
end_index = int(num_entries / 2)  # Specify the end index of the street names
generate_address(start_index, end_index)
print(";")

print("INSERT INTO warehouse (address) VALUES")
start_index = int(num_entries / 2)  # Specify the start index of the street names
end_index = num_entries - 1  # Specify the end index of the street names
generate_address(start_index, end_index)
print(";")

print("\nCOMMIT;\n")


#------------------------------------------------------------------------------------------------------------------------

# List of employee departments
departments = [
    "Accounting",
    "Human Resources",
    "Marketing",
    "Sales",
    "Finance",
    "Operations",
    "Information Technology",
    "Research and Development",
    "Customer Service",
    "Product Management",
    "Purchasing",
    "Quality Assurance",
    "Supply Chain",
    "Logistics",
    "Administration",
    "Legal",
    "Training and Development",
    "Public Relations",
    "Business Development",
    "Strategic Planning",
    "Project Management",
    "Risk Management",
    "Corporate Communications",
    "Internal Audit",
    "Facilities Management",
    "Data Analytics",
    "Procurement",
    "Corporate Social Responsibility",
    "Safety and Security",
    "Engineering",
    "Design",
    "Architecture",
    "Consulting",
    "Health and Safety",
    "Media and Communications",
    "Business Intelligence",
    "Customer Success",
    "Partnerships",
    "Quality Control",
    "Regulatory Affairs",
    "Environmental Services",
    "Events Management",
    "Investor Relations",
    "Training",
    "Sales Operations",
    "Creative Services",
    "Market Research",
    "Compliance",
    "Product Development",
    "Public Affairs",
    "Sustainability",
    "Government Relations"
]

def print_departments(departments):
    print("INSERT INTO department (name)")
    print("VALUES")

    for department in departments:
        if department != departments[-1]: print(f"    ('{department}'),")
        else: print(f"    ('{department}')")

    print(";")

# Call the function
print_departments(departments)

# List of employee first names
first_names = [
    "John", "David", "Michael", "Sarah", "Jessica", "Jennifer", "James", "Robert", "Daniel", "Emma",
    "Emily", "William", "Joseph", "Matthew", "Olivia", "Sophia", "Jacob", "Andrew", "Ava", "Madison",
    "Noah", "Ethan", "Alexander", "Isabella", "Grace", "Logan", "Benjamin", "Mia", "Charlotte", "Lucas",
    "Henry", "Liam", "Jackson", "Samuel", "Sebastian", "Elijah", "Aiden", "Carter", "Abigail", "Harper",
    "Ella", "Sofia", "Avery", "Lily", "Chloe", "Evelyn", "Victoria", "Aria", "Scarlett", "Hannah",
    "Landon", "Gabriel", "Christopher", "David", "Andrew", "Lucas", "Joshua", "Nicholas", "Matthew",
    "Christopher", "Nathan", "Aaron", "Zachary", "Ryan", "Justin", "Jonathan", "Thomas", "Tyler",
    "Jason", "Brandon", "Christian", "Dylan", "Samuel", "Elijah", "Anthony", "Isaac", "Joseph",
    "Gavin", "Jackson", "Hunter", "Evan", "Jordan", "Adam", "Kevin", "Caleb", "Dylan"
]

# List of employee surnames
surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
    "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Young", "Walker", "Hall", "Allen", "Green",
    "Adams", "Baker", "Hill", "King", "Wright", "Lopez", "Scott", "Nguyen", "Gonzalez", "Carter",
    "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
    "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey",
    "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James",
    "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson"
]

from datetime import datetime, timedelta
#def generate_employee_entries(n):
#    ssn = 100000006
#    tin = 20005
#    bdate_start = '1950-01-01'
#    print("INSERT INTO employee (ssn, TIN, bdate, name)\nVALUES\n")
#    
#    for i in range(n):
#        ssn += 1
#        tin += 1
#        if (i%1000==0): bdate = (datetime.strptime(bdate_start, '%Y-%m-%d') + timedelta(days=i)).strftime('%Y-%m-%d')
#        random_first = random.choice(first_names)
#        random_sur = random.choice(surnames)
#        random_name = f'{random_first} {random_sur}'
#        entry = f"({ssn}, {tin}, '{bdate}', '{random_name}')"
#        if i < n - 1:
#            entry += ","
#        print(entry)
#
#    print(";")
#
#generate_employee_entries(num_entries)

# Generate a random date of birth between 18 and 60 years ago
def generate_date_of_birth():
    #current_year = datetime.datetime.now().year
    #start_year = current_year - 60
    #end_year = current_year - 18
    #birth_year = random.randint(start_year, end_year)
    #birth_month = random.randint(1, 12)
    #birth_day = random.randint(1, 28)
    #date_of_birth = datetime.date(birth_year, birth_month, birth_day)
    bdate_start = '1950-01-01'
    if (i%1000==0): bdate = (datetime.strptime(bdate_start, '%Y-%m-%d') + timedelta(days=i)).strftime('%Y-%m-%d')

    return bdate

# Generate a random employee name
def generate_name():
    first_name = random.choice(first_names)
    last_name = random.choice(surnames)
    return f"'{first_name} {last_name}'"

# Generate random employee data
def generate_employee_data(n):
    ssn = 100000006
    tin = 20005
    
    for i in range(1, n+1):
        ssn += 1
        tin += 1
        name = generate_employee_name()
        bdate = generate_date_of_birth()
        entry = f"({ssn}, {tin}, '{bdate}', '{name}')"
        if i < n:
            entry += ","
        print(entry)

# Generate INSERT queries for employee table
print("-- employee table")
print("INSERT INTO employee (ssn, tin, bdate, name) VALUES")
generate_employee_data(num_entries)
print(";")

# Generate random customer data
def generate_customer_data(n):

    for i in range(1, n+1):
        cust_no = 30 + i
        first_name = random.choice(first_names)
        last_name = random.choice(surnames)
        name = f"'{first_name} {last_name}'"
        email = f"'{first_name}@mail.com'"
        phone = random.randint(900000000, 999999999)
        phone_num = f"'(351){phone}"
        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"

        entry = f"({cust_no}, {name}, {email}, {phone_num}, {address})"
        if i < n:
            entry += ","
        print(entry)

# Generate INSERT queries for customer table
print("-- customer table")
print("INSERT INTO customer (name, address) VALUES")
generate_customer_data(num_entries)
print(";")

print("\nCOMMIT;\n")

products = [
    "Smartphone",
    "Laptop",
    "Headphones",
    "Smartwatch",
    "Wireless Earbuds",
    "Digital Camera",
    "Bluetooth Speaker",
    "Gaming Console",
    "Fitness Tracker",
    "Tablet",
    "Drone",
    "TV",
    "Portable Power Bank",
    "External Hard Drive",
    "Printer",
    "Home Security Camera",
    "Virtual Reality Headset",
    "Smart Home Hub",
    "Smart Thermostat",
    "Smart Lock",
    "Wireless Router",
    "Bluetooth Earphones",
    "Gaming Mouse",
    "Wireless Keyboard",
    "Smart Light Bulbs",
    "Robot Vacuum Cleaner",
    "Wireless Charging Pad",
    "Electric Toothbrush",
    "Air Purifier",
    "Coffee Machine",
    "Blender",
    "Electric Kettle",
    "Slow Cooker",
    "Food Processor",
    "Smart Scale",
    "Video Doorbell",
    "Car Dash Cam",
    "Bluetooth Car Kit",
    "GPS Navigation Device",
    "Wireless Gaming Controller",
    "Portable Bluetooth Projector",
    "External SSD",
    "Smart Mirror",
    "Smart Refrigerator",
    "Robot Lawn Mower",
    "Smart Pet Feeder",
    "Smart Garden System",
    "Wireless Bike Computer",
    "Portable Bluetooth Speaker",
    "Wireless Noise-Canceling Headphones",
    "Smart Home Security System",
    "Wireless Security Alarm",
    "Smart Door Lock",
    "Video Baby Monitor",
    "Wireless HDMI Transmitter",
    "Robotic Arm Kit",
    "Home Weather Station",
    "Solar Power Bank",
    "Bluetooth Tracker",
    "Wireless Charging Stand",
    "Portable Photo Printer",
    "Gaming Keyboard",
    "Mechanical Gaming Mouse",
    "Wireless Gaming Headset",
    "Smart Ceiling Fan",
    "Smart Window Blinds",
    "Smart Water Bottle",
    "Wireless Charging Car Mount",
    "Smart Sous Vide Cooker",
    "Electric Scooter",
    "Electric Bike",
    "VR Gaming Chair",
    "Smart Luggage",
    "Portable Espresso Maker",
    "Smart Bike Lock",
    "Wireless HDMI Adapter",
    "Smart Backpack",
    "Smart Mirrorless Camera",
    "Smart Home Speaker",
    "Wireless Charging Desk Lamp",
    "Smart Desk",
    "Smart Oven",
    "Smart Plant Pot",
    "Wireless Presentation Clicker",
    "Gaming Racing Wheel",
    "Smart Bike Helmet",
    "Smart Hiking Backpack",
    "Portable Solar Charger",
    "Wireless Charging Mouse Pad",
    "Smart Meditation Headband",
    "Smart Language Translator",
    "Electric Skateboard",
    "Robot Companion",
    "Smart Jump Rope",
    "Portable Air Conditioner",
    "Smart Wine Bottle Opener",
    "Smart Suitcase",
    "Wireless BBQ Thermometer",
    "Smart Piano",
    "Robot Window Cleaner"
]

price_ranges = {
    "Smartphone": (500, 1500),
    "Laptop": (800, 3000),
    "Headphones": (50, 500),
    "Smartwatch": (200, 1000),
    "Wireless Earbuds": (100, 400),
    "Digital Camera": (200, 1500),
    "Bluetooth Speaker": (50, 300),
    "Gaming Console": (300, 800),
    "Fitness Tracker": (50, 300),
    "Tablet": (200, 1000),
    "Drone": (200, 2000),
    "TV": (500, 5000),
    "Portable Power Bank": (20, 100),
    "External Hard Drive": (50, 500),
    "Printer": (100, 500),
    "Home Security Camera": (50, 300),
    "Virtual Reality Headset": (200, 800),
    "Smart Home Hub": (100, 300),
    "Smart Thermostat": (100, 300),
    "Smart Lock": (100, 300),
    "Wireless Router": (50, 200),
    "Bluetooth Earphones": (50, 300),
    "Gaming Mouse": (50, 200),
    "Wireless Keyboard": (50, 200),
    "Smart Light Bulbs": (10, 100),
    "Robot Vacuum Cleaner": (200, 800),
    "Wireless Charging Pad": (20, 100),
    "Electric Toothbrush": (50, 200),
    "Air Purifier": (100, 500),
    "Coffee Machine": (50, 300),
    "Blender": (50, 200),
    "Electric Kettle": (20, 100),
    "Slow Cooker": (50, 200),
    "Food Processor": (50, 300),
    "Smart Scale": (20, 100),
    "Video Doorbell": (100, 300),
    "Car Dash Cam": (50, 200),
    "Bluetooth Car Kit": (20, 100),
    "GPS Navigation Device": (100, 300),
    "Wireless Gaming Controller": (50, 200),
    "Portable Bluetooth Projector": (200, 800),
    "External SSD": (100, 500),
    "Smart Mirror": (200, 1000),
    "Smart Refrigerator": (500, 3000),
    "Robot Lawn Mower": (500, 2000),
    "Smart Pet Feeder": (50, 300),
    "Smart Garden System": (100, 500),
    "Wireless Bike Computer": (50, 200),
    "Portable Bluetooth Speaker": (50, 300),
    "Wireless Noise-Canceling Headphones": (100, 500),
    "Smart Home Security System": (200, 800),
    "Wireless Security Alarm": (100, 300),
    "Smart Door Lock": (100, 300),
    "Video Baby Monitor": (50, 200),
    "Wireless HDMI Transmitter": (50, 200),
    "Robotic Arm Kit": (100, 300),
    "Home Weather Station": (50, 200),
    "Solar Power Bank": (50, 200),
    "Bluetooth Tracker": (20, 100),
    "Wireless Charging Stand": (20, 100),
    "Portable Photo Printer": (100, 300),
    "Gaming Keyboard": (50, 200),
    "Mechanical Gaming Mouse": (50, 200),
    "Wireless Gaming Headset": (100, 300),
    "Smart Ceiling Fan": (200, 800),
    "Smart Window Blinds": (200, 800),
    "Smart Water Bottle": (20, 100),
    "Wireless Charging Car Mount": (50, 200),
    "Smart Sous Vide Cooker": (100, 300),
    "Electric Scooter": (200, 1000),
    "Electric Bike": (500, 2000),
    "VR Gaming Chair": (200, 800),
    "Smart Luggage": (100, 500),
    "Portable Espresso Maker": (50, 200),
    "Smart Bike Lock": (50, 200),
    "Wireless HDMI Adapter": (50, 200),
    "Smart Backpack": (50, 200),
    "Smart Mirrorless Camera": (500, 2000),
    "Smart Home Speaker": (50, 300),
    "Wireless Charging Desk Lamp": (50, 200),
    "Smart Desk": (200, 800),
    "Smart Oven": (500, 2000),
    "Smart Plant Pot": (20, 100),
    "Wireless Presentation Clicker": (20, 100),
    "Gaming Racing Wheel": (200, 800),
    "Smart Bike Helmet": (100, 300),
    "Smart Hiking Backpack": (100, 300),
    "Portable Solar Charger": (50, 200),
    "Wireless Charging Mouse Pad": (20, 100),
    "Smart Meditation Headband": (100, 300),
    "Smart Language Translator": (100, 300),
    "Electric Skateboard": (200, 800),
    "Robot Companion": (500, 2000),
    "Smart Jump Rope": (20, 100),
    "Portable Air Conditioner": (200, 1000),
    "Smart Wine Bottle Opener": (20, 100),
    "Smart Suitcase": (100, 500),
    "Wireless BBQ Thermometer": (50, 200),
    "Smart Piano": (500, 2000),
    "Robot Window Cleaner": (200, 800),
    # Add more price ranges for other products
}

def generate_insert_statements(products, price_ranges):
    insert_statements = []
    for i, product in enumerate(products):
        sku = f"A{i + 1:03}"
        name = product
        description = "Sample description for " + product
        price_range = price_ranges.get(product, (50, 500))
        price = random.uniform(price_range[0], price_range[1])
        #ean = f"1234567890{i + 1:03}"

        insert_statement = f"('{sku}', '{name}', '{description}', {price:.2f}, '{ean}')"
        insert_statements.append(insert_statement)

    # Join all insert statements with commas and add the header and footer
    insert_query = "INSERT INTO product (sku, name, description, price, ean)\nVALUES\n"
    insert_query += ",\n".join(insert_statements)
    insert_query += ";\n"

    return insert_query


# Generate the INSERT statements
insert_query = generate_insert_statements(products, price_ranges)

# Print the INSERT statements
print(insert_query)

suppliers = [
    "ABC Suppliers",
    "XYZ Company",
    "Global Distributors",
    "Best Deals Inc.",
    "Mega Supplies Corporation",
    "Reliable Sourcing Co.",
    "Prime Wholesale Suppliers",
    "Superior Imports Ltd.",
    "Quick Distribution Services",
    "Trade Connections International",
    "Elite Sourcing Solutions",
    "Value Merchandise Group",
    "Quality Trading Co.",
    "Direct Sourcing Ltd.",
    "Global Sourcing Partners",
    "Wholesale Express Inc.",
    "Premier Suppliers Ltd.",
    "Infinite Sourcing Solutions",
    "Top Notch Imports",
    "Trusted Trading Company",
    "Wholesale Direct Supplies",
    "Quality Merchandise Distributors",
    "Reliable Sourcing Solutions",
    "Mega Trade Co.",
    "Direct Importers Inc.",
    "Best Buy Wholesale",
    "Global Trade Connections",
    "Prime Sourcing Group",
    "Superior Wholesale Suppliers",
    "Quick Imports Ltd.",
    "Value Trading Co.",
    "Elite Imports Inc.",
    "Reliable Distribution Services",
    "Quality Suppliers Ltd.",
    "Global Merchandise Group",
    "Wholesale Connections International",
    "Premier Sourcing Solutions",
    "Infinite Trading Co.",
    "Top Quality Imports",
    "Trusted Wholesale Suppliers",
    "Direct Sourcing Solutions",
    "Global Express Inc.",
    "Prime Merchandise Distributors",
    "Superior Sourcing Ltd.",
    "Quick Trade Connections",
    "Value Wholesale Express",
    "Elite Suppliers Ltd.",
    "Reliable Notch Imports",
    "Quality Trading Company",
    "Global Direct Supplies",
    "Premier Merchandise Group",
    "Infinite Sourcing Partners",
    "Top Trade Express",
    "Trusted Suppliers Ltd.",
    "Direct Wholesale Connections",
    "Global Imports Inc.",
    "Prime Buy Wholesale",
    "Superior Trade Connections",
    "Quick Merchandise Distributors",
    "Value Sourcing Solutions",
    "Elite Wholesale Suppliers",
    "Reliable Direct Imports",
    "Quality Sourcing Solutions",
    "Global Distribution Services",
    "Premier Suppliers Ltd.",
    "Infinite Imports Inc.",
    "Top Notch Wholesale",
    "Trusted Importers Inc.",
    "Direct Trade Co.",
    "Global Wholesale Express",
    "Prime Connections International",
    "Superior Sourcing Group",
    "Quick Wholesale Suppliers",
    "Value Direct Imports",
    "Elite Trade Solutions",
    "Reliable Merchandise Distributors",
    "Quality Sourcing Ltd.",
    "Global Trading Co.",
    "Premier Direct Supplies",
    "Infinite Merchandise Group",
    "Top Connections International",
    "Trusted Sourcing Solutions",
    "Direct Wholesale Express",
    "Global Importers Inc.",
    "Prime Trade Connections",
    "Superior Wholesale Suppliers",
    "Quick Sourcing Solutions",
    "Value Distribution Services",
    "Elite Suppliers Ltd.",
    "Reliable Notch Imports",
    "Quality Trading Company",
    "Global Direct Supplies",
    "Premier Merchandise Group",
    "Infinite Sourcing Partners",
    "Top Trade Express",
    "Trusted Suppliers Ltd.",
    "Direct Wholesale Connections",
    "Global Imports Inc.",
    "Prime Buy Wholesale",
    "Superior Trade Connections",
    "Quick Sourcing Solutions",
    "Value Distribution Services",
    "Elite Suppliers Ltd.",
    "Reliable Notch Imports",
    "Quality Trading Company",
    "Global Direct Supplies",
    "Premier Merchandise Group",
    "Infinite Sourcing Partners",
    "Top Trade Express",
    "Trusted Suppliers Ltd.",
    "Direct Wholesale Connections",
    "Global Imports Inc.",
    "Prime Buy Wholesale",
    "Superior Trade Connections"
]

def print_supplier(suppliers):
    print("INSERT INTO supplier (TIN, name, address, sku)")
    print("VALUES")

    tin = 20005
    sku_count = 1

    for i in enumerate(suppliers):
        tin += 1
        sku = f"SKU{sku_count:03}"
        sku_count += 1

        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"

        name = random.choice(suppliers)

        if i < entries - 1:
            print(f"    ({tin}, '{name}', {address}, '{sku}'),")
        else:
            print(f"    ({tin}, '{name}', {address}, '{sku}')")

    print(";")

print_supplier(suppliers)


def print_delivery(entries):
    print("INSERT INTO delivery (address, TIN)")
    print("VALUES")

    tin = 20005

    for i in range(entries):
        tin += 1
        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"
        if i < entries - 1:
            print(f"    ({address}, {tin}),")
        else:
            print(f"    ({address}, {tin})")

    print(";")

print_delivery(num_entries)



#-------------------------------------------------------------------------------------

def generate_customers(n):
    for i in range(1, n + 1):
        cust_no = 30 + i
        first_name = random.choice(first_names)
        last_name = random.choice(surnames)
        name = f"'{first_name} {last_name}'"
        email = f"'{first_name}@mail.com'"
        phone = random.randint(900000000, 999999999)
        phone_num = f"'(351){phone}"
        random_numbers = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        random_street = random.choice(street_names)
        random_city = random.choice(city_names)
        address = f"'{random_street}, {random_numbers} {random_city}'"
        entry = (cust_no, name, email, phone_num, address)
        if i < n:
            print(f"    {entry},")
        else:
            print(f"    {entry};\n")

print("INSERT INTO customer (cust_no, name, email, phone, address)\nVALUES\n")
generate_customers(num_entries)



def generate_order_entries(num_entries):
    order_no = 10
    cust_no = 30

    for i in range(num_entries):
        order_no += 1
        cust_no += 1
        date = random_date()
        entry = (order_no, date, cust_no)
        if i < num_entries - 1: print(f"    {entry},")
        else: print(f"    {entry}")

    print(";")

def random_date():
    year = 2022
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    date = f"{year:04d}-{month:02d}-{day:02d}"
    return date

print(""" -- orders need to be in contains due to RI-3
START	TRANSACTION;
SET	CONSTRAINTS	ALL	DEFERRED;""")
      
print("""INSERT INTO order_ (order_no, date, cust_no)
VALUES""")
generate_order_entries(num_entries)



def generate_contains_entries(num_entries):

    order_no = 10
    sku_count = 1
    for i in range(num_entries):
        sku = f"SKU{sku_count:03}"
        sku_count += 1
        order_no += 1
        qty = random.randint(1, 10)

        entry = (sku, order_no, qty)
        if i < num_entries - 1: print(f"    {entry},")
        else: print(f"    {entry}")

    print(";")


print("""INSERT INTO contains (sku, order_no, qty)
VALUES""")
generate_contains_entries(num_entries)


print("COMMIT;")


print("""INSERT INTO pay (cust_no, order_no)
VALUES""")
def generate_pays(num_entries):
    cust_no = 30
    order_no = 10

    for i in range(int(num_entries/2)):
        cust_no += 1
        order_no += 1
        entry = (cust_no, order_no)
        if i < int(num_entries/2) - 1: print(f"    {entry},")
        else: print(f"    {entry}")

    print(";")

generate_pays(num_entries)



print("""INSERT INTO process (ssn, order_no)
VALUES""")
def generate_process(num_entries):
    ssn = 100000006
    order_no = 10

    for i in range(int(num_entries/2)):
        ssn += 1
        order_no += 1
        entry = (ssn, order_no)
        if i < int(num_entries/2) - 1: print(f"    {entry},")
        else: print(f"    {entry}")

    print(";")

generate_process(num_entries)