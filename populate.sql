-- Values are only for testing purposes and do not represent a final database --

-- Insert sample data into customer table
INSERT INTO customer (cust_no, "name", email, phone, "address") 
VALUES 
    (1, 'Joao Silva',    'joao.silva@mail.com',       '(555)123-4567', 'TagusPark, Oeiras'),                -- Orders 1 product above 50€
    (2, 'Maria Santos',  'maria.santos@mail.com',     '(555)987-6543', 'Praca da Liberdade, Porto'),        -- Orders and pays for 1 product above 50€
    (3, 'Manuel Costa',  'manuel.costa@mail.com',     '(555)976-4552', 'Rua do Peixe, Lisboa'),             -- Orders 1 product above 50€ in the wrong year
    (4, 'Ana Pereira',   'ana.pereira@mail.com',      '(555)289-7654', 'Avenida Brasil, Lisboa'),           -- Has no orders
    (5, 'Pedro Freitas', 'pedro.das@ldil.com',        '(555)918-7564', 'Pontinha, Lisboa'),                 -- Has one order on the wrong date and one sale on the right date, both above 50€
    (6, 'Joao Trocado',  'joao.mainchar@mail.com',    '(555)921-2134', 'Entrecampos, Lisboa'),              -- Has a large sale above 50€ and an order in the wrong year
    (7, 'Marco Marques', 'marco.marquense@nokia.com', '(555)411-0034', 'Marques de Pombal, Lisboa'),        -- Orders alot of small products, the sum is bellow 50€
    (8, 'Ernest Chad',   'ernest.giga@chad.com',      '(555)969-4201', 'Giga Farm, Chad'),                  -- Buys multiple product that together cost above 50€
    (9, 'Rui Because',   'because.rui@outlook.com',   '(555)694-2054', 'Rua com dois Mcdonalds, Massama');  -- Orders a product costing exactly 50€

-- Insert sample data into "order" table
INSERT INTO "order" (order_no, "date", cust_no)
VALUES 
    (1, '2023-05-01', 1),   -- not january
    (2, '2023-04-05', 2),   -- not january
    (3, '2023-12-02', 6),   -- not january
    (4, '2022-01-01', 6),   -- Year < 2023
    (5, '2024-11-13', 3),   -- Year > 2023 | not january
    (6, '2020-11-13', 5),   -- Year < 2023 | not january
    (7, '2023-01-03', 7),
    (8, '2023-01-12', 5),
    (9, '2023-01-03', 8),
    (10,'2023-01-30', 9);

-- Insert sample data into sale table
INSERT INTO sale (order_no)
VALUES (2), (3), (8), (9); -- Values: 120€ | 134.5€ | 162.07€ | 50.01€

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, "name")
VALUES 
    (100000001, '10001', '1945-09-02', 'Adolfo Chaplin'),        -- Works in an office, processes an order in jan 2023
    (100000002, '10002', '2001-09-11', 'Dwayne Johnson'),        -- Works in a warehouse and an office, processes an order in jan 2023 
    (100000003, '10003', '1975-01-01', 'Xi JinPing'),            -- Works in a warehouse, processes an order in jan (but 2022)
    (100000004, '10004', '1911-05-23', 'Joao Bidao'),            -- Works in a warehouse, processes an order in jan 2023
    (100000005, '10005', '1444-09-10', 'Tiago Pode'),            -- Works in a cafe probably selling coffee, processes an order in jan 2023 somehow 
    (100000006, '10006', '2020-01-01', 'Maria Pequena'),         -- Works in a warehouse, processes an order in 2023 (not in jan)
    (100000007, '10007', '2024-01-01', 'Joao Futuro'),           -- Works in a warehouse, processes an order (but 2024 and not in jan)
    (100000008, '10008', '1983-01-15', 'Andre Fartura'),         -- Works in a warehouse, doesn't do much
    (100000009, '10009', '1948-12-12', 'Marcel Rebel');          -- Works in a warehouse, processes an order in jan 2023

-- Insert sample data into department table
INSERT INTO department ("name")
VALUES ('Sales'), ('Warehouse'), ('IT');

-- Insert sample data into workplace table
INSERT INTO workplace ("address", lat, "long")
VALUES 
    ('Rua da Cafeina, PodeVille', -90.000, 45.000), -- Cafe
    ('Parque do Tejo, Oeiras', 38.737, -9.302),     -- Warehouse
    ('Avenida do Japao, Lisboa', 67.420, 40.000),   -- Office and Warehouse
    ('Rua do Piano, Lisboa', 76.787, 75.654);       -- Only Office

-- Insert sample data into office table
INSERT INTO office ("address")
VALUES ('Rua do Piano, Lisboa'), ('Avenida do Japao, Lisboa');

-- Insert sample data into warehouse table
INSERT INTO warehouse ("address")
VALUES ('Avenida do Japao, Lisboa'), ('Parque do Tejo, Oeiras');

-- Insert sample data into product table
INSERT INTO product (sku, "name", "description", price)
VALUES 
    ('1A01', 'Banana',      'Generic Description', 0.50),               -- most in a single sale
    ('1A02', 'TV 1K',       'Generic Description', 420.00),             -- most value ordered                   
    ('1A03', 'Fridge',      'Generic Description', 120.00),
    ('1A04', 'Apple',       'Generic Description', 0.70),               -- best seller
    ('1A05', 'Switch',      'Generic Description', 299.99),             
    ('1A06', 'Water Bottle','Generic Description', 0.77),               
    ('1A07', 'Air Bottle',  'Generic Description', 0.01),               -- most in a single order
    ('1A08', 'Jacket',      'Generic Description', 49.99),
    ('1A09', 'Unicorn pillow',  'mount of the robot overlord', 50.00),
    ('1A10', 'Bath Water',  'Generic Description', 51.69);              -- most value sold

-- Insert sample data into ean_product table
INSERT INTO ean_product (sku, ean)
VALUES 
    ('1A07', 1234567890123),
    ('1A03', 2345678901234),
    ('1A09', 3456789012345),
    ('1A10', 4567890123456);

-- Insert sample data into supplier table
INSERT INTO supplier (TIN, "name", "address", sku, "date")
VALUES 
    (20001, 'Fnusk', 'Parque das Lagoas', '1A02', '2022-01-01'),
    (20002, 'Wusk', 'Parque das Lagoas', '1A03', '2022-01-01'),
    (20003, 'Wonfonusk', 'Parque das Lagoas', '1A05', '2023-05-26'),
    (20004, 'IST Robotics', 'Parque do Tejo, Oeiras, Portugal', '1A09', '2022-01-01'),
    (20005, 'Cacem Bananas', 'Rua do Cacem, Cacem, TugaLand', '1A01', '2022-01-01'),
    (20006, 'Cacem Dealand', 'Rua do Cacem, Cacem, TugaLand', '1A04', '2022-01-01'),
    (20007, 'Cacem Legit Deals', 'Rua do Cacem, Cacem, TugaLand', '1A06', '2022-01-01'),
    (20008, 'Cacem Deals', 'Rua do Cacem, Cacem, TugaLand', '1A07', '2022-01-01'),
    (20009, 'Cacem Minus', 'Rua do Cacem, Cacem, TugaLand', '1A08', '2022-01-01'),
    (20010, 'Cacem Plus', 'Rua do Cacem, Cacem, Portugal', '1A10', '2022-01-01');

-- Insert sample data into pay table
INSERT INTO pay (cust_no, order_no)
VALUES (2, 2), (6, 3), (5, 8), (8, 9);

-- Insert sample data into process table
INSERT INTO process (ssn, order_no)
VALUES (100000004, 7), (100000009, 7), 
       (100000001, 7), (100000002, 7), 
       (100000003, 4), (100000005, 7), 
       (100000006, 1), (100000007, 5);

-- Insert sample data into contains table
INSERT INTO contains (order_no, sku, qty)
VALUES (1, '1A02', 1), (2, '1A03', 1), (3, '1A03', 1), 
       (3, '1A04', 10), (3, '1A01', 15), (4, '1A02', 1), 
       (5, '1A02', 1), (6, '1A02', 1), (7, '1A07', 100), 
       (8, '1A10', 3), (8, '1A04', 10), (9, '1A08', 1), 
       (9, '1A07', 2), (10, '1A09', 1);

-- Insert sample data into works table
INSERT INTO works (ssn, "name", "address")
VALUES 
    (100000004, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (100000009, 'Warehouse', 'Parque do Tejo, Oeiras'),    
    (100000003, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (100000006, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (100000007, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (100000008, 'Warehouse', 'Parque do Tejo, Oeiras'),
    (100000001, 'IT', 'Rua do Piano, Lisboa'),
    (100000002, 'Warehouse', 'Avenida do Japao, Lisboa'),
    (100000005, 'Sales', 'Rua da Cafeina, PodeVille');

-- Insert sample data into delivery table
INSERT INTO delivery (sku, TIN, "address")
VALUES 
    ('1A09', '20004', 'Avenida do Japao, Lisboa'),
    ('1A10', '20010', 'Avenida do Japao, Lisboa');
