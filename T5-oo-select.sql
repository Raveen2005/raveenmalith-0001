/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T5-oo-select.sql

--Student ID:35863900
--Student Name:Raveen Pieris 


/* (a) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

select co.country_code,
       co.country_name,
       count(p.passenger_id) as number_of_passengers,
       round(
          (count(p.passenger_id) /(
             select count(*)
               from passenger
          )) * 100,
          2
       )
       || '%' as percent_passengers
  from passenger p
  join address ad
on p.address_id = ad.address_id
  join country co
on co.country_code = ad.country_code
 group by co.country_code,
          co.country_name
having count(p.passenger_id) = (
   select max(count(p2.passenger_id))
     from passenger p2
     join address ad2
   on p2.address_id = ad2.address_id
    group by ad2.country_code
)
 order by co.country_code;
/* (b) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

select cruise_id,
       cruise_name,
       cruise_depart_dt as departure_date_time,
       ship_details,
       gender_category,
       passenger_count
  from (
   select cr.cruise_id,
          cr.cruise_name,
          cr.cruise_depart_dt,
          cr.ship_code
          || ' - '
          || s.ship_name as ship_details,
          case
             when upper(p.passenger_gender) = 'M' then
                'MALE'
             when upper(p.passenger_gender) = 'F' then
                'FEMALE'
             else
                'OTHER'
          end as gender_category,
          count(*) as passenger_count
     from manifest m
     join passenger p
   on p.passenger_id = m.passenger_id
     join cruise cr
   on cr.cruise_id = m.cruise_id
     join ship s
   on cr.ship_code = s.ship_code
    group by cr.cruise_id,
             cr.cruise_name,
             cr.cruise_depart_dt,
             cr.ship_code
             || ' - '
             || s.ship_name,
             case
                when upper(p.passenger_gender) = 'M' then
                   'MALE'
                when upper(p.passenger_gender) = 'F' then
                   'FEMALE'
                else
                   'OTHER'
             end
   union all
   select cr.cruise_id,
          cr.cruise_name,
          cr.cruise_depart_dt,
          cr.ship_code
          || ' - '
          || s.ship_name as ship_details,
          'Total Count' as gender_category,
          count(*) as passenger_count
     from manifest m
     join passenger p
   on p.passenger_id = m.passenger_id
     join cruise cr
   on cr.cruise_id = m.cruise_id
     join ship s
   on cr.ship_code = s.ship_code
    group by cr.cruise_id,
             cr.cruise_name,
             cr.cruise_depart_dt,
             cr.ship_code
             || ' - '
             || s.ship_name
)
 order by cruise_id,
          case gender_category
             when 'MALE'        then
                1
             when 'FEMALE'      then
                2
             when 'OTHER'       then
                3
             when 'Total Count' then
                4
          end;

/* (c) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

select cr.cruise_id
       || ':'
       || cr.cruise_name as cruise,
       floor(cr.cruise_arrive_dt - cr.cruise_depart_dt)
       || ' days '
       || floor((cr.cruise_arrive_dt - cr.cruise_depart_dt) * 24 - floor(cr.cruise_arrive_dt - cr.cruise_depart_dt) * 24)
       || ' hours' as cruise_duration,
       count(m.passenger_id) as total_passengers,
       sum(
          case
             when p.guardian_id is not null then
                1
             else
                0
          end
       ) as minors,
       round(
          avg((cr.cruise_depart_dt - p.passenger_dob) / 365),
          1
       ) as avg_age,
       count(distinct ad.country_code) as countries,
       to_char(
          cr.cruise_cost_pp,
          '$99999.99'
       ) as cruise_cost,
       s.ship_name as ship_name,
       o.oper_comp_name as opr_comp_name,
       s.country_code as ship_country
  from cruise cr
  join manifest m
on cr.cruise_id = m.cruise_id
  join passenger p
on p.passenger_id = m.passenger_id
  join address ad
on ad.address_id = p.address_id
  join ship s
on s.ship_code = cr.ship_code
  join operator o
on s.oper_id = o.oper_id
 group by cr.cruise_id,
          cr.cruise_name,
          cr.cruise_depart_dt,
          cr.cruise_arrive_dt,
          cr.cruise_cost_pp,
          s.ship_name,
          o.oper_comp_name,
          s.country_code
having count(m.passenger_id) > (
   select avg(cnt)
     from (
      select count(*) as cnt
        from manifest
       group by cruise_id
   )
)
 order by total_passengers desc,
          cr.cruise_id;

