-- IC1 no triggers?

ALTER TABLE employee
ADD CONSTRAINT check_employee_age CHECK (AGE(bdate, CURRENT_DATE) >= INTERVAL '18 years');

-- IC 2

DROP TRIGGER IF EXISTS tg_check_mandatory_workplace_office_warehouse ON workplace;

CREATE OR REPLACE FUNCTION	check_mandatory_workplace_office_warehouse()
		RETURNS TRIGGER AS
$$
BEGIN
	IF NEW.address NOT IN (SELECT address FROM office UNION SELECT address FROM warehouse EXCEPT (SELECT address FROM office INTERSECT SELECT address FROM warehouse)) THEN
		RAISE EXCEPTION	'The workplace at %	must be either an office or warehouse.',	
        NEW.address;
	END IF;
	RETURN NEW;
END;
$$	LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER	tg_check_mandatory_workplace_office_warehouse
AFTER INSERT ON workplace DEFERRABLE                                                           --Maybe update? maybe after
FOR EACH ROW EXECUTE FUNCTION check_mandatory_workplace_office_warehouse();

-- IC 3

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

CREATE CONSTRAINT TRIGGER tg_contains_order
    AFTER INSERT ON "order" DEFERRABLE
    FOR EACH ROW
    EXECUTE FUNCTION check_contains_order();


--O uso de extensões procedimentais (Stored Procedures e Triggers) deve ser reservado a restrições de
--integridade que não podem ser implementadas usando outros mecanismos mais simples.




