--****PLEASE ENTER YOUR DETAILS BELOW****
--T4-oo-mods.sql

--Student ID: 35863900
--Student Name: Raveen Pieris 


--(a)

CREATE TABLE maintenance (
    maintenance_id NUMERIC(6),
    ship_code NUMERIC(4),
    scheduled_start DATE,
    scheduled_end DATE,
    actual_start DATE,
    actual_end DATE,
    maintenance_type VARCHAR2(30),
    CONSTRAINT maintenance_pk PRIMARY KEY (maintenance_id)
);

ALTER TABLE maintenance
ADD CONSTRAINT maintenance_fk FOREIGN KEY ( ship_code)
REFERENCES ship(ship_code);

ALTER TABLE maintenance
ADD CONSTRAINT maintenance_type_ch CHECK(maintenance_type IN (
    'Preventive Maintenance',
    'Breakdown Maintenance',
    'Condition-Based Maintenance'
));

COMMENT ON COLUMN maintenance.maintenance_id IS 'Unique identifier for maintenance record';
COMMENT ON COLUMN maintenance.ship_code IS 'Ship that is undergoing maintenance';
COMMENT ON COLUMN maintenance.scheduled_start IS 'Planned maintenance start date';
COMMENT ON COLUMN maintenance.scheduled_end IS 'Planned maintenance end date';
COMMENT ON COLUMN maintenance.actual_start IS 'Actual maintenance start date';
COMMENT ON COLUMN maintenance.actual_end IS 'Actual maintenance end date';
COMMENT ON COLUMN maintenance.maintenance_type IS 'Type of maintenance';

DESC maintenance;

--(b)
CREATE TABLE need_category(
    category_id NUMERIC(4),
    category_name VARCHAR2(30),
    CONSTRAINT need_category_pk PRIMARY KEY (category_id),
    CONSTRAINT need_category_uk UNIQUE (category_name)
);

COMMENT ON COLUMN need_category.category_id IS 'Unique identifier for need_category';
COMMENT ON COLUMN need_category.category_name IS 'Unique Name for need in need_category';



CREATE TABLE passenger_need (
    passenger_id NUMERIC(6),
    category_id NUMERIC(4),
    need_details VARCHAR2(200),
    CONSTRAINT passenger_need_pk PRIMARY KEY(passenger_id,category_id)
);

ALTER TABLE passenger_need
ADD CONSTRAINT passenger_need_passenger_fk FOREIGN KEY (passenger_id)
REFERENCES passenger(passenger_id);

ALTER TABLE passenger_need
ADD CONSTRAINT passenger_need_category_fk FOREIGN KEY (category_id)
REFERENCES need_category(category_id);

COMMENT ON COLUMN passenger_need.need_details IS 'Describing on the special need with more information';

INSERT INTO need_category VALUES (1,'General');
INSERT INTO need_category VALUES (2,'Mobility');
INSERT INTO need_category VALUES (3,'Hearing');
INSERT INTO need_category VALUES (4,'Visual');
INSERT INTO need_category VALUES (5,'Other');

INSERT INTO passenger_need( passenger_id, category_id,need_details)
SELECT passenger_id, 1, NULL
FROM PASSENGER
WHERE PASSENGER.PASSENGER_SPECIALNEED = 'Y';

COMMIT;

DESC need_category;
DESC passenger_need;

SELECT * FROM need_category ORDER by CATEGORY_ID;
SELECT passenger_id, category_id, need_details 
FROM passenger_need 
ORDER BY passenger_id;
