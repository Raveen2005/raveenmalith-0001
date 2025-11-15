/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T6-oo-json.sql

--Student ID: 35863900
--Student Name: Raveen Pieris 



-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer
select
   json_object(
      '_id' value p.passenger_id,
               'passenger_name' value trim(p.passenger_fname
                                           || ' ' || p.passenger_lname),
               'passenger_dob' value to_char(
         p.passenger_dob,
         'dd-mm-yyyy'
      ),
               'passenger_contact' value nvl(
         p.passenger_contact,
         '-'
      ),
               'guardian_name' value nvl(
         g.passenger_fname
         || ' '
         || g.passenger_lname,
         '-'
      ),
               'address' value
         json_object(
            'street' value nvl(
               ad.address_street,
               '-'
            ),
                     'town' value nvl(
               ad.address_town,
               '-'
            ),
                     'postcode' value nvl(
               ad.address_pcode,
               '-'
            ),
                     'country' value nvl(
               co.country_name,
               '-'
            )
         ),
               'no_of _cruises' value count(m.cruise_id),
               'cruises' value
         case
            when count(m.cruise_id) = 0 then
               json_array()
            else
               json_arrayagg(
                  json_object(
                     'cruise_id' value nvl(to_char(cr.cruise_id),'-'),
                              'cruise_name' value nvl(to_char(cr.cruise_name),'-'),
                              'board_date_time' value nvl(to_char(
                        m.manifest_board_datetime,
                        'DD-MM-YYYY HH24:MI'),'-'
                     ),
                              'cabin_no' value nvl(
                        m.cabin_no,
                        '-'
                     ),
                              'cabin_class' value nvl(
                        ca.cabin_class,
                        '-'
                     )
                  )
               )
         end
   )
as passenger_json
  from passenger p
  join address ad
on p.address_id = ad.address_id
  join country co
on ad.country_code = co.country_code
  left join passenger g
on p.guardian_id = g.passenger_id
  left join manifest m
on p.passenger_id = m.passenger_id
  left join cruise cr
on m.cruise_id = cr.cruise_id
  left join cabin ca
on m.cabin_no = ca.cabin_no
 group by p.passenger_id,
          p.passenger_fname,
          p.passenger_lname,
          p.passenger_dob,
          p.passenger_contact,
          g.passenger_fname,
          g.passenger_lname,
          ad.address_street,
          ad.address_town,
          ad.address_pcode,
          co.country_name;
   SET PAGESIZE 100