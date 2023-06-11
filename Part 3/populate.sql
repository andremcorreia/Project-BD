-- Values are only for testing purposes and do not represent a final database --

-- Insert sample data into customer table
INSERT INTO customer (cust_no, name, email, phone, address) 
VALUES 
    (1, 'Pobre', 'pobre@mail.com', NULL, NULL),       -- no orders 
    (2, 'Maria Santos',  'maria.santos@mail.com', '(351)911111111', 'Praca da Liberdade, 1360-490 Porto'),      -- some paid (not top), unpaid excede top
    (3, 'Rico', 'rico@mail.com', NULL, 'Avenida da Liberdade, 1660-491 Lisboa'),       -- top by single sale
    (4, 'Rico V2', 'rico.v2@mail.com', NULL, 'Casino Estoril, 2060-495 Cascais'),     -- top by multiple sales
    (5, 'Pedro Pobre', 'pedro.pobre@mail.com', NULL, NULL);     -- doesn't pay

-- Insert sample data into product table
INSERT INTO product (SKU, name, description, price, ean)
VALUES 
    ('1A01', 'Banana', NULL, 0.50, 1234567890001),
    ('1A02', 'TV 1K',  NULL, 499.00, NULL),
    ('1A03', 'Switch',  NULL, 299.00, NULL),
    ('1A04', 'BMW', NULL, 5485.00, NULL);

START	TRANSACTION;
SET	CONSTRAINTS	ALL	DEFERRED;
INSERT INTO "order" (order_no, cust_no, date)
VALUES 
    (1, 2, '2022-01-08'),
    (2, 2, '2022-01-30'),
    (3, 2, '2022-02-02'),
    (4, 3, '2022-03-01'),
    (5, 4, '2023-04-12'),
    (6, 4, '2022-06-23'),
    (7, 5, '2022-06-05'),
    (8, 5, '2023-07-10');

INSERT INTO contains (order_no, SKU, qty)
VALUES
    (1, '1A01', 25), (2, '1A03', 2), (3, '1A04', 2),
    (4, '1A04', 1), (5, '1A02', 5), (6, '1A03', 10),
    (7, '1A04', 1), (8, '1A02', 2);

COMMIT;	

INSERT INTO "order" (order_no, cust_no, date)
VALUES (99, 1, '2023-01-01');                -- check not in contains IC

-- Insert sample data into sale table
INSERT INTO pay (order_no, cust_no)
VALUES
    (1, 2), (2, 2), (4, 3),
    (5, 4), (6, 4);

-- Insert sample data into employee table
INSERT INTO employee (ssn, TIN, bdate, name)
VALUES 
    --(100000001, '10001', '1945-09-02', 'Cafe Dead'),
    --(100000002, '10002', '1975-03-23', 'Actually Man'),
    (100000005, '10006', '2022-01-01', 'Minor');        -- check age < 18 IC

-- Insert sample data into process table
--INSERT INTO process (ssn, order_no)
--VALUES
    --(100000001, 1), (100000002, 2);

-- Insert sample data into department table
INSERT INTO department (name)
VALUES
    ('Sales'), ('Logistics'), ('IT');

START	TRANSACTION;
SET	CONSTRAINTS	ALL	DEFERRED;
    -- Insert sample data into workplace table
    INSERT INTO workplace (address, lat, long)
    VALUES 
        ('Rua do Poder, 6290-500 PodeVille', 0.000, 45.000),
        ('Parque do Tejo, 2340-123 Oeiras', 38.737, -9.302);

    INSERT INTO office (address)
    VALUES
        ('Parque do Tejo, 2340-123 Oeiras');

    -- Insert sample data into warehouse table
    INSERT INTO warehouse (address)
    VALUES
        ('Rua do Poder, 6290-500 PodeVille');

COMMIT;	

START	TRANSACTION;
SET	CONSTRAINTS	ALL	DEFERRED;
    -- Insert sample data into workplace table
    INSERT INTO workplace (address, lat, long)
    VALUES 
        ('Rua Ambos, 5555-555 AmbosLand', 45.000, 45.000);      -- check both IC

    INSERT INTO office (address)
    VALUES
        ('Rua Ambos, 5555-555 AmbosLand');      -- for both IC

    -- Insert sample data into warehouse table
    INSERT INTO warehouse (address)
    VALUES
        ('Rua Ambos, 5555-555 AmbosLand');      -- for both IC

COMMIT;	

-- Insert sample data into workplace table
INSERT INTO workplace (address, lat, long)
VALUES 
    ('Rua do Cafe, 1111-111 CafeLand', 0.000, 0.000);       -- check none IC

-- Insert sample data into works table
--INSERT INTO works (ssn, name, address)
--VALUES 
    --(100000001, 'Sales', 'Parque do Tejo, 2340-123 Oeiras'),
    --(100000002, 'Logistics', 'Rua do Poder, 6290-500 PodeVille');

-- Insert sample data into supplier table
INSERT INTO supplier (TIN, name, address, SKU, date)
VALUES 
    (20001, 'Bausk', 'Parque das Lagoas, 5350-250 Lagoa', '1A01', '2021-01-01'),
    (20002, 'Tvusk', NULL, '1A02', '2021-01-01'),
    (20003, 'Swusk', NULL, '1A03', '2021-01-01'),
    (20004, 'Causk', NULL, '1A04', '2021-01-01');

-- Insert sample data into delivery table
INSERT INTO delivery (address, TIN)
VALUES 
    ('Rua do Poder, 6290-500 PodeVille', 20001),
    ('Rua do Poder, 6290-500 PodeVille', 20002),
    ('Rua do Poder, 6290-500 PodeVille', 20003),
    ('Rua do Poder, 6290-500 PodeVille', 20004);
