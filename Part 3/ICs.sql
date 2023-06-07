-- IC 1

DROP TRIGGER check_employee_age ON employee [IF EXISTS]

CREATE OR REPLACE FUNCTION check_age_employee()	
RETURNS TRIGGER AS
$$
BEGIN			
	IF AGE(NEW.bdate, CURRENT_DATE) < INTERVAL '18 years' THEN			
		RAISE EXCEPTION	'Underage alert | MINOR EXPLORATION'
	END IF;	
	RETURN NEW;
END;
$$	LANGUAGE plpgsql;

CREATE TRIGGER check_employee_age
BEFORE INSERT OR UPDATE ON employee
FOR EACH ROW
EXECUTE FUNCTION check_age_employee();

-- IC 2

DROP TRIGGER tg_check_mandatory_workplace_office_warehouse ON workplace [IF EXISTS]

CREATE OR REPLACE FUNCTION	check_mandatory_workplace_office_warehouse()
		RETURNS TRIGGER AS
$$
BEGIN
	IF NEW.address NOT IN (SELECT address FROM office UNION SELECT address FROM warehouse) THEN
		RAISE EXCEPTION	'The workplace at %	must be either an office or warehouse.',	
        NEW.address;
	END IF;
	RETURN NEW;
END;
$$	LANGUAGE plpgsql;

CREATE TRIGGER	tg_check_mandatory_workplace_office_warehouse
BEFORE INSERT ON workplace                                                           --Maybe update? maybe after
FOR EACH ROW EXECUTE PROCEDURE check_mandatory_workplace_office_warehouse();

--O uso de extensões procedimentais (Stored Procedures e Triggers) deve ser reservado a restrições de
--integridade que não podem ser implementadas usando outros mecanismos mais simples.

-- IC 3

CREATE TRIGGER check_contains_order
    BEFORE INSERT OR UPDATE ON "order"
    FOR EACH ROW
    EXECUTE FUNCTION check_contains_order();

-- Stored Procedure to check order existence in 'Contains'
CREATE OR REPLACE FUNCTION check_contains_order()
    RETURNS TRIGGER AS
$$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM contains WHERE order_no = NEW.order_no
    ) THEN
        RAISE EXCEPTION 'The order % must exist in "Contains".', NEW.order_no;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- IC1 no triggers?

ALTER TABLE employee
ADD CONSTRAINT check_employee_age CHECK (AGE(bdate, CURRENT_DATE) >= INTERVAL '18 years');

-- IC2 macacada

ALTER TABLE workplace
ADD COLUMN type VARCHAR(10) NOT NULL CHECK (type IN ('office', 'warehouse'));

-- IC3 no trigers?

ALTER TABLE "order"
ADD CONSTRAINT fk_contains_order_no
FOREIGN KEY (order_no)
REFERENCES contains (order_no);



