-- IC 1

DROP TRIGGER check_employee_age ON employee [IF EXISTS]

CREATE OR REPLACE FUNCTION chk_age_employee()	
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
EXECUTE FUNCTION chk_age_employee();

-- IC 2

DROP TRIGGER tg_chk_mandatory_workplace_office_warehouse ON workplace [IF EXISTS]

CREATE OR REPLACE FUNCTION	chk_mandatory_workplace_office_warehouse()
		RETURNS TRIGGER AS
$$
BEGIN
	IF NEW.address NOT IN (SELECT address FROM office JOIN warehouse p ON ct.sku = p.sku) THEN
		RAISE EXCEPTION	'The workplace at %	must be either an office or warehouse.',	
        NEW.address;
	END IF;
	RETURN NEW;
END;
$$	LANGUAGE plpgsql;

CREATE TRIGGER	tg_chk_mandatory_workplace_office_warehouse
AFTER INSERT ON workplace
FOR EACH ROW EXECUTE PROCEDURE chk_mandatory_workplace_office_warehouse();
