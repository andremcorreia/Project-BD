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
--   1. pk_table for names of primary key constraints
--   2. fk_table_another for names of foreign key constraints
--   3. uc_table_atributes for constraints of key pairs

CREATE TABLE customer (
    cust_no             NUMERIC(9),
    "name"              VARCHAR(80)     NOT NULL,
    email               VARCHAR(254)    NOT NULL UNIQUE,
    phone               VARCHAR(15)     NOT NULL,
    "address"           VARCHAR(255)    NOT NULL,
    CONSTRAINT pk_customer PRIMARY KEY (cust_no)
);


CREATE TABLE "order" (
    order_no            NUMERIC(9),
    "date"              DATE            NOT NULL,
    cust_no             NUMERIC(9)      NOT NULL,
    CONSTRAINT pk_order PRIMARY KEY (order_no),
    CONSTRAINT fk_order_customer FOREIGN KEY (cust_no) REFERENCES customer(cust_no),
    CONSTRAINT uc_order_cust_no UNIQUE (order_no, cust_no)
    -- Every order (order_no) must participate in the contains association
);

CREATE TABLE sale (
    order_no            NUMERIC(9),
    CONSTRAINT pk_sale PRIMARY KEY (order_no),
    CONSTRAINT fk_sale_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE employee (
    ssn                 NUMERIC(11),
    TIN                 VARCHAR(20)     NOT NULL UNIQUE,
    bdate               DATE            NOT NULL,
    "name"              VARCHAR(80)     NOT NULL,
    CONSTRAINT pk_employee PRIMARY KEY (ssn)
    -- Every employee (ssn) must participate in the works association
);

CREATE TABLE department (
    "name"              VARCHAR(200),
    CONSTRAINT pk_department PRIMARY KEY ("name")
);

CREATE TABLE workplace (
    "address"           VARCHAR(255),
    lat                 NUMERIC(8,6)    NOT NULL,
    "long"              NUMERIC(9,6)    NOT NULL,
    CONSTRAINT pk_workplace PRIMARY KEY ("address"),
    CONSTRAINT uc_lat_long UNIQUE (lat, "long")
);

CREATE TABLE office (
    "address"           VARCHAR(255),
    CONSTRAINT pk_office PRIMARY KEY ("address"),
    CONSTRAINT fk_office_workplace FOREIGN KEY ("address") REFERENCES workplace ("address")
);

CREATE TABLE warehouse (
    "address"   VARCHAR(255),
    CONSTRAINT pk_warehouse PRIMARY KEY ("address"),
    CONSTRAINT fk_warehouse_workplace FOREIGN KEY ("address") REFERENCES workplace ("address")
);

CREATE TABLE product (
    sku                 VARCHAR(10),
    "name"              VARCHAR(50)     NOT NULL,
    "description"       TEXT            NOT NULL,
    price               NUMERIC(16,4)   NOT NULL CHECK (price > 0),
    CONSTRAINT pk_product PRIMARY KEY (sku)
    -- Every product (sku) must participate in the supplier relation
);

CREATE TABLE ean_product (
    sku                 VARCHAR(10),
    ean                 NUMERIC(13)     NOT NULL,
    CONSTRAINT pk_ean_product PRIMARY KEY (sku),
    CONSTRAINT fk_ean_product FOREIGN KEY (sku) REFERENCES product (sku)
);

CREATE TABLE supplier (
    TIN                 VARCHAR(20),
    "name"              VARCHAR(80)     NOT NULL,
    "address"           VARCHAR(255)    NOT NULL,
    sku                 VARCHAR(10)     NOT NULL,
    "date"              DATE            NOT NULL,
    CONSTRAINT pk_supplier PRIMARY KEY (TIN),
    CONSTRAINT fk_supplier_product FOREIGN KEY (sku) REFERENCES product (sku),
    CONSTRAINT uc_supplier_sku_tin UNIQUE (sku, TIN)
);

CREATE TABLE pay (
    cust_no             NUMERIC(9)      NOT NULL,
    order_no            NUMERIC(9),
    CONSTRAINT pk_pay PRIMARY KEY (order_no),
    CONSTRAINT fk_pay_customer FOREIGN KEY (cust_no) REFERENCES customer (cust_no),
    CONSTRAINT fk_pay_order FOREIGN KEY (order_no) REFERENCES "order" (order_no),
    CONSTRAINT fk_pay_customer_order FOREIGN KEY (cust_no, order_no) REFERENCES "order" (cust_no, order_no)
);

CREATE TABLE process (
    ssn                 NUMERIC(11),
    order_no            NUMERIC(9),
    CONSTRAINT pk_process PRIMARY KEY (ssn, order_no),
    CONSTRAINT fk_process_employee FOREIGN KEY (ssn) REFERENCES employee (ssn),
    CONSTRAINT fk_process_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE contains (
    order_no            NUMERIC(9),
    sku                 VARCHAR(10),
    qty                 SMALLINT        NOT NULL CHECK (qty > 0),
    CONSTRAINT pk_contains PRIMARY KEY (order_no, sku),                      
    CONSTRAINT fk_contains_product FOREIGN KEY (sku) REFERENCES product (sku),
    CONSTRAINT fk_contains_order FOREIGN KEY (order_no) REFERENCES "order" (order_no)
);

CREATE TABLE works (
    ssn                 NUMERIC(11),
    "name"              VARCHAR(200),
    "address"           VARCHAR(255),
    CONSTRAINT pk_works PRIMARY KEY (ssn, "name", "address"),
    CONSTRAINT fk_works_employee FOREIGN KEY (ssn) REFERENCES employee (ssn),
    CONSTRAINT fk_works_workplace FOREIGN KEY ("address") REFERENCES workplace ("address"),
    CONSTRAINT fk_works_department FOREIGN KEY ("name") REFERENCES department ("name")
);

CREATE TABLE delivery (
    sku                 VARCHAR(10),
    TIN                 VARCHAR(20),
    "address"           VARCHAR(255),
    CONSTRAINT pk_delivery PRIMARY KEY (sku, TIN, "address"),
    CONSTRAINT fk_delivery_supplier FOREIGN KEY (sku, TIN) REFERENCES supplier (sku, TIN),
    CONSTRAINT fk_delivery_warehouse FOREIGN KEY ("address") REFERENCES warehouse ("address")
);
