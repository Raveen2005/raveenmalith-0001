--****PLEASE ENTER YOUR DETAILS BELOW****
--T3-oo-dm.sql

--Student ID: 35863900
--Student Name: Raveen Pieris 

--(a)
drop sequence address_seq;
drop sequence passenger_seq;
drop sequence manifest_seq;

create sequence address_seq start with 500 increment by 5;

create sequence passenger_seq start with 500 increment by 5;

create sequence manifest_seq start with 500 increment by 5;
--(b)
insert into address (
   address_id,
   address_street,
   address_town,
   address_pcode,
   country_code
) values ( address_seq.nextval,
           '23 Banksia Avenue',
           'Melbourne',
           '3000',
           'AUS' );
-- Adding father Dominik 
insert into passenger (
   passenger_id,
   passenger_fname,
   passenger_lname,
   passenger_dob,
   passenger_gender,
   passenger_contact,
   passenger_specialneed,
   address_id,
   guardian_id
) values ( passenger_seq.nextval,
           'Dominik',
           'Kohl',
           to_date('1980-01-01','YYYY-MM-DD'),
           'M',
           '+61493336312',
           'N',
           (
              select address_id
                from address
               where address_street = '23 Banksia Avenue'
                 and address_town = 'Melbourne'
           ),
           null );
-- Adding child stella 
insert into passenger (
   passenger_id,
   passenger_fname,
   passenger_lname,
   passenger_dob,
   passenger_gender,
   passenger_contact,
   passenger_specialneed,
   address_id,
   guardian_id
) values ( passenger_seq.nextval,
           'Stella',
           'Kohl',
           to_date('2012-05-10','yyyy-mm-dd'),
           'F',
           null,
           'N',
           (
              select address_id
                from address
               where address_street = '23 Banksia Avenue'
                 and address_town = 'Melbourne'
           ),
           (
              select passenger_id
                from passenger
               where passenger_fname = 'Dominik'
                 and passenger_lname = 'Kohl'
           ) );
-- Adding Child Poppy 
insert into passenger (
   passenger_id,
   passenger_fname,
   passenger_lname,
   passenger_dob,
   passenger_gender,
   passenger_contact,
   passenger_specialneed,
   address_id,
   guardian_id
) values ( passenger_seq.nextval,
           'Poppy',
           'Kohl',
           to_date('2015-03-22','yyyy-mm-dd'),
           'F',
           null,
           'N',
           (
              select address_id
                from address
               where address_street = '23 Banksia Avenue'
                 and address_town = 'Melbourne'
           ),
           (
              select passenger_id
                from passenger
               where passenger_fname = 'Dominik'
                 and passenger_lname = 'Kohl'
           ) );
insert into manifest (
   manifest_id,
   passenger_id,
   cruise_id,
   manifest_board_datetime,
   ship_code,
   cabin_no
)
   select manifest_seq.nextval,
          p.passenger_id,
          s.cruise_id,
          ( s.cruise_depart_dt - ( 6 / 24 ) ),
          s.ship_code,
          '8035'
     from cruise s
     join passenger p
   on p.address_id = (
      select address_id
        from address
       where address_street = '23 Banksia Avenue'
         and address_town = 'Melbourne'
   )
    where upper(s.cruise_name) = 'MELBOURNE TO SINGAPORE';
COMMIT;
--(c)
DELETE FROM MANIFEST
WHERE PASSENGER_ID IN (
   SELECT PASSENGER_ID
   FROM PASSENGER
   WHERE passenger_fname = 'Stella' and passenger_lname = 'Kohl'
);

UPDATE MANIFEST
SET CABIN_NO = '9015'
WHERE passenger_id IN(
   SELECT passenger_id
   FROM PASSENGER
   WHERE Passenger_lname = 'Kohl' and passenger_fname IN ('Dominik', 'Poppy')
);
COMMIT;

--(d)

DELETE FROM MANIFEST
WHERE PASSENGER_ID IN (
      SELECT passenger_id
      FROM PASSENGER
      WHERE passenger_lname = 'Kohl'
      and Passenger_fname IN ('Dominik', 'Poppy')
);
COMMIT;