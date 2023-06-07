-- Values are only for testing purposes and do not represent a final database --

-- Insert sample data into customer table
INSERT INTO customer (cust_no, name, email, phone, address) 
VALUES 
    (1, 'Joao Silva',    'joao.silva@mail.com',   '(351)911111111', 'Avenida Brasil, 2650-325 Lisboa'),        
    (2, 'Maria Santos',  'maria.santos@mail.com', '(351)922222222', 'Praca da Liberdade, 1360-490 Porto');     

-- Insert sample data into order table
INSERT INTO order (order_no, cust_no, date)
VALUES 
    (1, 1, '2022-01-01'),
    (2, 2, '2022-01-01');

-- Insert sample data into sale table
INSERT INTO pay (order_no, cust_no)
VALUES
    (1, 1);

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, name)
VALUES 
    (100000001, '10001', '1945-09-02', 'Cafe Dead'),
    (100000002, '10002', '1975-03-23', 'Actually Man');

-- Insert sample data into process table
INSERT INTO process (ssn, order_no)
VALUES
    (100000001, 1), (100000002, 2);

-- Insert sample data into department table
INSERT INTO department (name)
VALUES
    ('Sales'), ('Logistics'), ('IT');

-- Insert sample data into workplace table
INSERT INTO workplace (address, lat, long)
VALUES 
    ('Rua da Cafeina, 6290-500 PodeVille', 0.000, 45.000),
    ('Parque do Tejo, 2340-123 Oeiras', 38.737, -9.302);

-- Insert sample data into office table
INSERT INTO office (address)
VALUES
    ('Parque do Tejo, 2340-123 Oeiras');

-- Insert sample data into warehouse table
INSERT INTO warehouse (address)
VALUES
    ('Rua da Cafeina, 6290-500 PodeVille');

-- Insert sample data into works table
INSERT INTO works (ssn, name, address)
VALUES 
    (100000001, 'Sales', 'Parque do Tejo, 2340-123 Oeiras'),
    (100000002, 'Logistics', 'Rua da Cafeina, 6290-500 PodeVille');

-- Insert sample data into product table
INSERT INTO product (SKU, name, description, price, ean)
VALUES 
    ('1A01', 'Banana', 'Generic Description', 0.50, 1234567890001),
    ('1A02', 'TV 1K',  'Generic Description', 499.00);

-- Insert sample data into contains table
INSERT INTO contains (order_no, SKU, qty)
VALUES
    (1, '1A01', 25), (2, '1A01', 5), (2, '1A02', 1);

-- Insert sample data into supplier table
INSERT INTO supplier (TIN, name, address, SKU, date)
VALUES 
    (20001, 'Bnusk', 'Parque das Lagoas, 5350-250 Lagoa', '1A01', '2022-01-01'),
    (20002, 'Tusk', 'Parque das Lagoas, 5350-250 Lagoa', '1A02', '2022-01-01');

-- Insert sample data into delivery table
INSERT INTO delivery (address, TIN)
VALUES 
    ('Rua da Cafeina, 6290-500 PodeVille', 20001),
    ('Rua da Cafeina, 6290-500 PodeVille', 20002);
