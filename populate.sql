-- Insert sample data into customer table
INSERT INTO customer (cust_no, customer_name, email, phone, customer_address) 
VALUES 
    (1, 'Joao Silva',   'joao.silva@mail.com',      123456789, 'TagusPark, Oeiras'),
    (2, 'Maria Santos', 'maria.santos@mail.com',    987654321, 'Praca da Liberdade, Porto'),
    (3, 'Manuel Costa', 'manuel.costa@mail.com',    976455242, 'Rua do Peixe, Lisboa'),
    (4, 'Ana Pereira',  'ana.pereira@mail.com',     989765432, 'Avenida Brasil, Lisboa'),
    (5, 'Pedro Freitas','pedro.das@ldil.com',       918756463, 'Pontinha, Lisboa'),
    (6, 'Joao Trocado', 'joao.mainchar@mail.com',   911213432, 'Entrecampos, Lisboa'),
    (7, 'Marco Marques','marco.marquense@nokia.com',911003432, 'Marques de Pombal, Lisboa'),
    (8, 'Ernest Chad', 'ernest.giga@chad.com',      969420158, 'Giga Farm, Chad');

-- Insert sample data into "order" table
INSERT INTO "order" (order_no, order_date, cust_no)
VALUES 
    (1, '2023-05-01', 1),
    (2, '2023-04-05', 2),
    (3, '2023-12-02', 6),
    (4, '2022-01-01', 6),
    (5, '2024-11-13', 3),
    (6, '2020-11-13', 5),
    (7, '2023-01-03', 7),
    (8, '2023-01-03', 5),
    (9, '2023-01-03', 8);

-- Insert sample data into sale table
INSERT INTO sale (order_no)
VALUES (2), (3), (8), (9);

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, employee_name)
VALUES 
    (1001, 10001, '1945-09-02', 'Adolfo Chaplin'),
    (1002, 10002, '2001-09-11', 'Dwayne Johnson'),
    (1003, 10003, '1975-01-01', 'Xi JinPing'),
    (1004, 10004, '1911-05-23', 'Joao Bidao'),
    (1005, 10005, '1444-09-10', 'Tiago Pode'),
    (1006, 10006, '2020-01-01', 'Maria Pequena'),
    (1007, 10007, '2024-01-01', 'Joao Futuro'),
    (1008, 10008, '1983-01-15', 'Andre Fartura'),
    (1009, 10009, '1948-12-12', 'Marcel Rebel');


-- Insert sample data into department table
INSERT INTO department (department_name)
VALUES ('Sales'), ('Warehouse'), ('IT');

-- Insert sample data into workplace table
INSERT INTO workplace (workplace_address, lat, "long")
VALUES 
    ('Rua da Cafeina, PodeVille', -90.000, 45.000), -- Caffe
    ('Parque do Tejo, Oeiras', 38.737, -9.302),     -- Warehouse
    ('Avenida do Japao, Lisboa', 67.420, 40.000),   -- Office and Warehouse
    ('Rua do Piano, Lisboa', 76.787, 75.654);       -- Only Office


-- Insert sample data into office table
INSERT INTO office (office_address)
VALUES ('Rua do Piano, Lisboa'), ('Avenida do Japao, Lisboa');

-- Insert sample data into warehouse table
INSERT INTO warehouse (warehouse_address)
VALUES ('Avenida do Japao, Lisboa'), ('Parque do Tejo, Oeiras');

-- Insert sample data into product table
INSERT INTO product (sku, product_name, product_description, price)
VALUES 
    ('1A01', 'Banana',      'Generic Description', 0.50),
    ('1A02', 'TV 1K',       'Generic Description', 420.00),
    ('1A03', 'Fridge',      'Generic Description', 120.00),
    ('1A04', 'Apple',       'Generic Description', 0.70),
    ('1A05', 'Switch',      'Generic Description', 299.99),
    ('1A06', 'Water Bottle','Generic Description', 0.77),
    ('1A07', 'Air Bottle',  'Generic Description', 0.01),
    ('1A08', 'Jacket',      'Generic Description', 49.99),
    ('1A09', 'Nokia',       'Generic Description', 50.00),
    ('1A10', 'Bath Water',  'Generic Description', 51.69);

-- Insert sample data into ean_product table
INSERT INTO ean_product (sku, ean)
VALUES 
    ('1A07', 1234567890123),
    ('1A03', 2345678901234),
    ('1A09', 3456789012345),
    ('1A10', 4567890123456);

-- Insert sample data into supplier table
INSERT INTO supplier (TIN, supplier_name, supplier_address, sku, contract_date)
VALUES 
    (20001, 'Fnusk', 'Parque das Lagoas', '1A02', '2022-01-01'),
    (20002, 'Wusk', 'Parque das Lagoas', '1A03', '2022-01-01'),
    (20003, 'Wonfonusk', 'Parque das Lagoas', '1A05', '2022-01-01'),
    (20004, 'Ikusk', 'Parque das Lagoas', '1A09', '2022-01-01'),
    (20005, 'Cacem Bananas', 'Rua do Cacem, Cacem, TugaLand', '1A01', '2022-01-01'),
    (20006, 'Cacem Dealand', 'Rua do Cacem, Cacem, TugaLand', '1A04', '2022-01-01'),
    (20007, 'Cacem Legit Deals', 'Rua do Cacem, Cacem, TugaLand', '1A06', '2022-01-01'),
    (20008, 'Cacem Deals', 'Rua do Cacem, Cacem, TugaLand', '1A07', '2022-01-01'),
    (20009, 'Cacem Minus', 'Rua do Cacem, Cacem, TugaLand', '1A08', '2022-01-01'),
    (20010, 'Cacem Plus', 'Rua do Cacem, Cacem, TugaLand', '1A10', '2022-01-01');


-- Insert sample data into pay table
INSERT INTO pay (cust_no, order_no)
VALUES (2, 2), (6, 3), (5, 8), (8, 9);

-- Insert sample data into process table
INSERT INTO process (ssn, order_no)
VALUES (1004, 7), (1009, 7), (1001, 7), (1002, 7), (1003, 4), (1005, 7), (1006, 6), (1007, 5);

-- Insert sample data into contains table
INSERT INTO contains (order_no, sku, qty)
VALUES (1, '1A02', 1), (2, '1A03', 1), (3, '1A03', 1), 
       (3, '1A04', 10), (3, '1A01', 15), (4, '1A02', 1), 
       (5, '1A02', 1), (6, '1A02', 1), (7, '1A07', 100), 
       (8, '1A10', 3), (8, '1A04', 10), (9, '1A08', 1), 
       (9, '1A07', 2);

-- Insert sample data into works table
INSERT INTO works (ssn, department_name, workplace_address)
VALUES 
    (1004, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (1009, 'Warehouse', 'Parque do Tejo, Oeiras'),    
    (1003, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (1006, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (1007, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (1008, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (1001, 'IT', 'Rua do Piano, Lisboa'),
    (1002, 'Warehouse', 'Avenida do Japao, Lisboa'),
    (1005, 'Sales', 'Rua da Cafeina, PodeVille');


-- Insert sample data into delivery table
INSERT INTO delivery (sku, TIN, warehouse_address)
VALUES 
    ('1A09', 20004, 'Avenida do Japao, Lisboa'),
    ('1A10', 20010, 'Avenida do Japao, Lisboa');

