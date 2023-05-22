DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS "order" CASCADE;
DROP TABLE IF EXISTS sale CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS department CASCADE;
DROP TABLE IF EXISTS workplace CASCADE;
DROP TABLE IF EXISTS office CASCADE;
DROP TABLE IF EXISTS warehouse CASCADE;
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS ean_product CASCADE;
DROP TABLE IF EXISTS supplier CASCADE;
DROP TABLE IF EXISTS pay CASCADE;
DROP TABLE IF EXISTS process CASCADE;
DROP TABLE IF EXISTS contains CASCADE;
DROP TABLE IF EXISTS works CASCADE;
DROP TABLE IF EXISTS delivery CASCADE;

-- Named constraints are global to the database.
-- Therefore, use the following naming rules:
--   1. pk_something for names of primary key constraints

CREATE TABLE customer (
    cust_no             INT             NOT NULL UNIQUE,
    customer_name       VARCHAR(255)    NOT NULL,
    email               VARCHAR(100)    NOT NULL UNIQUE,
    phone               INT             NOT NULL,
    customer_address    VARCHAR(255)    NOT NULL,
    CONSTRAINT pk_customer PRIMARY KEY (cust_no)
);


CREATE TABLE "order" (
    order_no            INT             NOT NULL UNIQUE,
    order_date          DATE            NOT NULL,
    cust_no             INT             NOT NULL,
    CONSTRAINT pk_order PRIMARY KEY (order_no),
    CONSTRAINT fk_order_customer FOREIGN KEY (cust_no) REFERENCES customer(cust_no)
);

CREATE TABLE sale (
    order_no            INT             NOT NULL,
    CONSTRAINT fk_sale_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE employee (
    ssn                 INT             NOT NULL UNIQUE,
    TIN                 INT             NOT NULL UNIQUE,
    bdate               DATE            NOT NULL,
    employee_name       VARCHAR(255)    NOT NULL,
    CONSTRAINT pk_employee PRIMARY KEY (ssn)
);

CREATE TABLE department (
    department_name     VARCHAR(255)    NOT NULL UNIQUE,
    CONSTRAINT pk_department PRIMARY KEY (department_name)
);

CREATE TABLE workplace (
    workplace_address   VARCHAR(255)    NOT NULL UNIQUE,
    lat                 FLOAT           NOT NULL UNIQUE,
    "long"              FLOAT           NOT NULL UNIQUE,
    CONSTRAINT pk_workplace PRIMARY KEY (workplace_address)
);

CREATE TABLE office (
    office_address      VARCHAR(255)    NOT NULL,
    CONSTRAINT fk_office_workplace FOREIGN KEY (office_address) REFERENCES workplace (workplace_address)
);

CREATE TABLE warehouse (
    warehouse_address   VARCHAR(255)    NOT NULL,
    CONSTRAINT fk_warehouse_workplace FOREIGN KEY (warehouse_address) REFERENCES workplace (workplace_address),
    CONSTRAINT fk_warehouse UNIQUE (warehouse_address)
);

CREATE TABLE product (
    sku                 INT             NOT NULL UNIQUE,
    product_name        VARCHAR(255)    NOT NULL,
    product_description VARCHAR(255)    NOT NULL,
    price               FLOAT           NOT NULL CHECK (price > 0),
    CONSTRAINT pk_product PRIMARY KEY (sku)
);

CREATE TABLE ean_product (
    sku                 INT             NOT NULL,
    ean                 BIGINT          NOT NULL,
    CONSTRAINT fk_ean_product FOREIGN KEY (sku) REFERENCES product (sku)
);

CREATE TABLE supplier (
    TIN                 INT             NOT NULL UNIQUE,
    supplier_name       VARCHAR(255)    NOT NULL,
    supplier_address    VARCHAR(255)    NOT NULL,
    sku                 INT             NOT NULL,
    contract_date       DATE            NOT NULL,
    CONSTRAINT pk_supplier PRIMARY KEY (TIN),
    CONSTRAINT fk_supplier_product FOREIGN KEY (sku) REFERENCES product (sku),
    CONSTRAINT uc_supplier_sku_tin UNIQUE (sku, TIN)
);

CREATE TABLE pay (
    cust_no             INT             NOT NULL,
    order_no            INT             NOT NULL,
    CONSTRAINT fk_pay_customer FOREIGN KEY (cust_no) REFERENCES customer (cust_no),
    CONSTRAINT fk_pay_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE process (
    ssn                 INT             NOT NULL,
    order_no            INT             NOT NULL,
    CONSTRAINT fk_process_employee FOREIGN KEY (ssn) REFERENCES employee (ssn),
    CONSTRAINT fk_process_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE contains (
    order_no            INT             NOT NULL,
    sku                 INT             NOT NULL,
    qty                 INT             NOT NULL,
    CONSTRAINT fk_contains_product FOREIGN KEY (sku) REFERENCES product (sku),
    CONSTRAINT fk_contains_order FOREIGN KEY (order_no) REFERENCES "order" (order_no),
    CONSTRAINT uc_contains_order_no_sku UNIQUE (order_no, sku)                              --idk
);

CREATE TABLE works (
    ssn                 INT             NOT NULL,
    department_name     VARCHAR(255)    NOT NULL,
    workplace_address   VARCHAR(255)    NOT NULL,
    CONSTRAINT fk_works_employee FOREIGN KEY (ssn) REFERENCES employee (ssn),
    CONSTRAINT fk_works_workplace FOREIGN KEY (workplace_address) REFERENCES workplace (workplace_address),
    CONSTRAINT fk_works_department FOREIGN KEY (department_name) REFERENCES department (department_name)
);

CREATE TABLE delivery (
    sku                 INT             NOT NULL,
    TIN                 INT             NOT NULL,
    warehouse_address   VARCHAR(255)    NOT NULL,
    CONSTRAINT fk_delivery_supplier FOREIGN KEY (sku, TIN) REFERENCES supplier (sku, TIN),
    CONSTRAINT fk_delivery_warehouse FOREIGN KEY (warehouse_address) REFERENCES warehouse (warehouse_address)
);
