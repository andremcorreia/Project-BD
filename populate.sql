-- Insert sample data into customer table
INSERT INTO customer (cust_no, customer_name, email, phone, customer_address) 
VALUES 
    (1, 'João Silva', 'joao.silva@mail.com', 123456789, 'Rua A, Lisboa'),
    (2, 'Maria Santos', 'maria.santos@mail.com', 987654321, 'Avenida B, Lisboa'),
    (3, 'Manuel Costa', 'manuel.costa@mail.com', 555555555, 'Rua C, Lisboa'),
    (4, 'Ana Pereira', 'ana.pereira@mail.com', 999999999, 'Avenida D, Lisboa');

-- Insert sample data into order table
INSERT INTO "order" (order_no, order_date, cust_no)
VALUES 
    (1, '2023-05-01', 1),
    (2, '2023-01-15', 2),
    (3, '2023-03-10', 3),
    (4, '2023-06-20', 4);

-- Insert sample data into sale table
INSERT INTO sale (order_no)
VALUES (1), (2), (3), (4);

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, employee_name)
VALUES 
    (1001, 10001, '1980-01-01', 'José Fonseca'),
    (1002, 10002, '1990-02-02', 'Sofia Gomes'),
    (1003, 10003, '1985-06-15', 'António Martins');

-- Insert sample data into department table
INSERT INTO department (department_name)
VALUES ('Sales'), ('Warehouse'), ('HR');

-- Insert sample data into workplace table
INSERT INTO workplace (workplace_address, lat, "long")
VALUES 
    ('Rua X, Lisboa', 38.7223, -9.1393),
    ('Avenida Y, Lisboa', 38.7369, -9.1424),
    ('Rua Z, Lisboa', 38.7216, -9.1257);

-- Insert sample data into office table
INSERT INTO office (office_address)
VALUES ('Rua X, Lisboa'), ('Avenida Y, Lisboa');

-- Insert sample data into warehouse table
INSERT INTO warehouse (warehouse_address)
VALUES ('Rua Z, Lisboa');

-- Insert sample data into product table
INSERT INTO product (sku, product_name, product_description, price)
VALUES 
    (1001, 'Product A', 'Description A', 49.99),
    (1002, 'Product B', 'Description B', 59.99),
    (1003, 'Product C', 'Description C', 99.99),
    (1004, 'Product D', 'Description D', 74.99);

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
    (10004, 'Supplier D', 'Supplier Address D', 1004, '2022-04-01');

-- Insert sample data into pay table
INSERT INTO pay (cust_no, order_no)
VALUES (1, 1), (2, 2), (3, 3), (4, 4);

-- Insert sample data into process table
INSERT INTO process (ssn, order_no)
VALUES (1001, 1), (1002, 2), (1003, 3), (1001, 4);

-- Insert sample data into contains table
INSERT INTO contains (order_no, sku, qty)
VALUES (1, 1001, 1), (1, 1002, 2), (2, 1003, 1), (3, 1004, 3), (4, 1001, 2);

-- Insert sample data into works table
INSERT INTO works (ssn, department_name, workplace_address)
VALUES 
    (1001, 'Warehouse', 'Rua Z, Lisboa'),
    (1002, 'Sales', 'Rua X, Lisboa'),
    (1003, 'HR', 'Avenida Y, Lisboa');

-- Insert sample data into delivery table
INSERT INTO delivery (sku, TIN, warehouse_address)
VALUES 
    (1001, 10001, 'Rua Z, Lisboa'),
    (1002, 10002, 'Rua Z, Lisboa'),
    (1003, 10003, 'Rua Z, Lisboa'),
    (1004, 10004, 'Rua Z, Lisboa');
