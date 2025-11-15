/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T1-oo-schema.sql

--Student ID: 35863900
--Student Name: Raveen Pieris 

/* drop table statements - do not remove*/



DROP TABLE address CASCADE CONSTRAINTS PURGE;

DROP TABLE manifest CASCADE CONSTRAINTS PURGE;

DROP TABLE passenger CASCADE CONSTRAINTS PURGE;

/* end of drop table statements*/

-- Task 1 Add Create table statements for the Missing TABLES below.
-- The columns/attributes must be in the same order as shown in the model.
-- Ensure all column comments, and constraints (other than FK's)are included.
-- FK constraints are to be added at the end of this script.

-- ADDRESS

CREATE TABLE address (
    address_id NUMERIC(6),
    address_street VARCHAR(50),
    address_town VARCHAR(30),
    address_pcode VARCHAR(10),
    country_code CHAR(3),
    CONSTRAINT address_pk PRIMARY KEY (address_id),
    CONSTRAINT address_uk UNIQUE (address_street,address_town,address_pcode,country_code)
);
-- MANIFEST
CREATE TABLE MANIFEST (
    manifest_id NUMERIC(8),
    passenger_id NUMERIC(6),
    cruise_id NUMERIC(6),
    manifest_board_datetime DATE,
    ship_code NUMERIC(4),
    cabin_no VARCHAR(5),
    CONSTRAINT manifest_pk PRIMARY KEY(manifest_id),
    CONSTRAINT manifest_passenger_cruise_ui UNIQUE(passenger_id,cruise_id)
);
-- PASSENGER
CREATE TABLE passenger(
    passenger_id NUMERIC(6),
    passenger_fname VARCHAR(25),
    passenger_lname VARCHAR(25),
    passenger_dob DATE,
    passenger_gender CHAR(1),
    passenger_contact VARCHAR(15),
    passenger_specialneed CHAR(1),
    address_id NUMERIC(6),
    guardian_id NUMERIC(6),
    CONSTRAINT passenger_pk PRIMARY KEY(passenger_id),
    CONSTRAINT passenger_gender_ck CHECK (passenger_gender IN ('M','F','X')),
    CONSTRAINT passenger_specialneed_ck CHECK (passenger_specialneed IN ('Y','N'))
);

-- Add all missing FK Constraints below here
-- You must use the default delete rule (i.e. no action/restrict) 
-- for all foreign keys.
ALTER TABLE address
ADD CONSTRAINT address_country_fk FOREIGN KEY (country_code)
REFERENCES COUNTRY(country_code);

ALTER TABLE passenger
ADD CONSTRAINT passenger_address_fk FOREIGN KEY(address_id)
REFERENCES address(address_id);

ALTER TABLE passenger
ADD CONSTRAINT passenger_guardian_fk FOREIGN KEY (guardian_id)
REFERENCES passenger(passenger_id);

ALTER TABLE manifest
ADD CONSTRAINT manifest_passenger_fk FOREIGN KEY (passenger_id)
REFERENCES passenger(passenger_id);

ALTER TABLE manifest
ADD CONSTRAINT manifest_cruise_fk FOREIGN KEY (cruise_id)
REFERENCES cruise(cruise_id);

ALTER TABLE manifest 
ADD CONSTRAINT manifest_cabin_fk FOREIGN KEY (ship_code, cabin_no)
REFERENCES cabin(ship_code, cabin_no);


