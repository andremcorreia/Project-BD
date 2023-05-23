-- Insert sample data into customer table
INSERT INTO customer (cust_no, customer_name, email, phone, customer_address) 
VALUES 
    (1, 'Joao Silva', 'joao.silva@mail.com', 123456789, 'Rua A, Lisboa'),
    (2, 'Maria Santos', 'maria.santos@mail.com', 987654321, 'Avenida B, Lisboa'),
    (3, 'Manuel Costa', 'manuel.costa@mail.com', 555555555, 'Rua C, Lisboa'),
    (4, 'Ana Pereira', 'ana.pereira@mail.com', 999999999, 'Avenida D, Lisboa'),
    (5, 'Pedro Freitas', 'pedro.sad@lidl.com', 555550555, 'Casal, Lisboa'),
    (6, 'Joao Trocado', 'joao.mainchar@mail.com', 999099999, 'Rich Land, Lisboa');

-- Insert sample data into "order" table
INSERT INTO "order" (order_no, order_date, cust_no)
VALUES 
    (1, '2023-05-01', 1),
    (2, '2023-01-15', 2),
    (3, '2023-03-10', 3),
    (4, '2023-06-20', 4),
    (5, '2022-03-10', 6),
    (6, '2024-06-20', 6);

-- Insert sample data into sale table
INSERT INTO sale (order_no)
VALUES (1), (2), (3), (4), (6);

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, employee_name)
VALUES 
    (1001, 10001, '1980-01-01', 'José Fonseca'),
    (1002, 10002, '1990-02-02', 'Sofia Gomes'),
    (1003, 10003, '1985-06-15', 'António Martins'),
    (1004, 10004, '1990-02-02', 'to ze cacem'),
    (1005, 10005, '2023-05-23', 'not lasagna');

-- Insert sample data into department table
INSERT INTO department (department_name)
VALUES ('Sales'), ('Warehouse'), ('HR'), ('Banana'), ('Unemployment');

-- Insert sample data into workplace table
INSERT INTO workplace (workplace_address, lat, "long")
VALUES 
    ('Rua X, Lisboa', 38.7223, -9.1393),
    ('Avenida Y, Lisboa', 38.7369, -9.1424),
    ('Rua Z, Lisboa', 38.7216, -9.1257),
    ('cacem park, Taguspark', 38.7598, -9.2742),
    ('Rua Oriente, Lisboa', 38.7256, -9.1265);

-- Insert sample data into office table
INSERT INTO office (office_address)
VALUES ('Rua X, Lisboa'), ('Avenida Y, Lisboa'), ('cacem park, Taguspark');

-- Insert sample data into warehouse table
INSERT INTO warehouse (warehouse_address)
VALUES ('Rua Z, Lisboa'), ('Rua Oriente, Lisboa');

-- Insert sample data into product table
INSERT INTO product (sku, product_name, product_description, price)
VALUES 
    (1001, 'Product A', 'Description A', 49.99),
    (1002, 'Product B', 'Description B', 59.99),
    (1003, 'Suspicious Object', 'Description C', 99.99),
    (1004, 'Product D', 'Description D', 74.99),
    (1005, 'Banana', 'Description C', 5.55),
    (1006, 'Tiago', 'Description D', 0.01);

-- Insert sample data into ean_product table
INSERT INTO ean_product (sku, ean)
VALUES 
    (1001, 1234567890123),
    (1002, 2345678901234),
    (1003, 3456789012345),
    (1004, 4567890123456);

-- Insert sample data into supplier table
INSERT INTO supplier (TIN, supplier_name, supplier_address, sku, contract_date)
VALUES 
    (10001, 'Supplier A', 'Supplier Address A', 1001, '2022-01-01'),
    (10002, 'Supplier B', 'Supplier Address B', 1002, '2022-02-01'),
    (10003, 'Supplier C', 'Supplier Address C', 1003, '2022-03-01'),
    (10004, 'Supplier D', 'Supplier Address D', 1004, '2022-04-01'),
    (10005, 'Monke', 'Jungle, aka alameda', 1006, '2001-04-02'),
    (10006, 'coreia', 'Supplier D', 1005, '2020-08-01');

-- Insert sample data into pay table
INSERT INTO pay (cust_no, order_no)
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (6, 6);

-- Insert sample data into process table
INSERT INTO process (ssn, order_no)
VALUES (1001, 1), (1002, 2), (1003, 3), (1001, 4), (1005, 6);

-- Insert sample data into contains table
INSERT INTO contains (order_no, sku, qty)
VALUES (1, 1001, 1), (1, 1002, 2), (2, 1003, 1), (3, 1004, 3), (4, 1001, 2), (6, 1006, 20), (6, 1005, 5), (6, 1004, 1), (5, 1006, 100), (5, 1003, 100);

-- Insert sample data into works table
INSERT INTO works (ssn, department_name, workplace_address)
VALUES 
    (1001, 'Warehouse', 'Rua Z, Lisboa'),
    (1004, 'Banana', 'cacem park, Taguspark'),
    (1002, 'Banana', 'Rua Oriente, Lisboa'),
    (1005, 'Unemployment', 'Rua Oriente, Lisboa'),
    (1003, 'HR', 'Avenida Y, Lisboa');

-- Insert sample data into delivery table
INSERT INTO delivery (sku, TIN, warehouse_address)
VALUES 
    (1001, 10001, 'Rua Z, Lisboa'),
    (1002, 10002, 'Rua Z, Lisboa'),
    (1003, 10003, 'Rua Z, Lisboa'),
    (1004, 10004, 'Rua Z, Lisboa'),
    (1006, 10005, 'Rua Oriente, Lisboa');
