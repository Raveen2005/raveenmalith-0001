/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T2-oo-insert.sql

--Student ID: 35863900
--Student Name: Raveen Pieris 

/* GenAI Acknowledgement and Prompts:
Sample values for this Task were generated using GEN AI. It was generated 
inside the scafold of FIT2094 assignment 2 requirments. 
*/

-- Task 2 Load the ADDRESS, PASSENGER and MANIFEST tables with your own
-- test data following the data requirements expressed in the brief

-- =======================================
-- ADDRESS 
-- =======================================

INSERT INTO ADDRESS VALUES (1,'12 Seashell ST', 'Coral Bay','3000', 'ABW');
INSERT INTO address VALUES (2,'44 Wharf Road','Harbourtown','3001','AFG');
INSERT INTO address VALUES (3,'7 Lighthouse Ave','Portside','3002','AGO');
INSERT INTO address VALUES (4,'18 Palm Grove','Marina City','3003','ABW');
INSERT INTO address VALUES (5,'5 Coral Crescent','Reefville','3004','AFG');
INSERT INTO address VALUES (6,'91 Ocean View','Shelly Beach','3005','AGO');
INSERT INTO address VALUES (7,'2 Sand Dune Dr','Bayview','3006','ABW');
INSERT INTO address VALUES (8,'77 Pier Parade','Harbourton','3007','AFG');
INSERT INTO address VALUES (9,'9 Anchor Lane','Jetty Hills','3008','AGO');
INSERT INTO address VALUES (10,'31 Marina Quay','Seacliff','3009','ABW');
INSERT INTO address VALUES (11,'6 Pelican Row','Gull Point','3010','AFG');
INSERT INTO address VALUES (12,'55 Beacon Road','Wavecrest','3011','AGO');

INSERT INTO address VALUES (13,'45 Sunset Pier','Bayview','3012','ABW');   
INSERT INTO address VALUES (14,'88 Reef Sands','Coral Bay','3013','AFG'); 
INSERT INTO address VALUES (15, '23 Ocean Road', 'Perth', '6000', 'AUS');
INSERT INTO address VALUES (16, '77 Forest Lane', 'Auckland', '1010', 'NZL');


-- =======================================
-- PASSENGER
-- =======================================

INSERT INTO passenger VALUES (1,'Maya','Fern',TO_DATE('1988-04-13','YYYY-MM-DD'),'F','0400111222','N',14,NULL);
INSERT INTO passenger VALUES (2,'Ethan','Rao',TO_DATE('1995-02-17','YYYY-MM-DD'),'M','0400333444','Y',2,NULL);
INSERT INTO passenger VALUES (3,'Ari','Lee',TO_DATE('1992-11-30','YYYY-MM-DD'),'X','0400555666','N',3,NULL);
INSERT INTO passenger VALUES (4,'Noah','Khan',TO_DATE('1985-08-09','YYYY-MM-DD'),'M','0400777888','N',4,NULL);
INSERT INTO passenger VALUES (5,'Zoe','Park',TO_DATE('1990-06-22','YYYY-MM-DD'),'F','0400999000','Y',5,NULL);
INSERT INTO passenger VALUES (6,'Olivia','Chan',TO_DATE('1987-01-14','YYYY-MM-DD'),'F','0401100200','N',6,NULL);

INSERT INTO passenger VALUES (7,'Leo','Martin',TO_DATE('1984-03-02','YYYY-MM-DD'),'M','0401300400','N',13,NULL);
INSERT INTO passenger VALUES (8,'Ava','Martin',TO_DATE('2010-05-12','YYYY-MM-DD'),'F',NULL,'N',13,7);
INSERT INTO passenger VALUES (9,'Mia','Martin',TO_DATE('2012-09-03','YYYY-MM-DD'),'F',NULL,'Y',13,7);
INSERT INTO passenger VALUES (10,'Kai','Martin',TO_DATE('2009-12-29','YYYY-MM-DD'),'M',NULL,'N',13,7);

INSERT INTO passenger VALUES (11,'Riya','Das',TO_DATE('1998-10-05','YYYY-MM-DD'),'F','0401500600','N',8,NULL);
INSERT INTO passenger VALUES (12,'Ben','Ng',TO_DATE('1989-07-21','YYYY-MM-DD'),'M','0401700800','N',9,NULL);
INSERT INTO passenger VALUES (13,'Imani','Osei',TO_DATE('1993-02-02','YYYY-MM-DD'),'F','0401900100','N',10,NULL);
INSERT INTO passenger VALUES (14,'Tom','Evans',TO_DATE('1986-05-17','YYYY-MM-DD'),'M','0402100300','N',11,NULL);
INSERT INTO passenger VALUES (15,'Sara','Kim',TO_DATE('1991-03-28','YYYY-MM-DD'),'F','0402300500','N',12,NULL);

INSERT INTO passenger VALUES (16,'Niko','Fern',TO_DATE('2011-04-04','YYYY-MM-DD'),'M',NULL,'N',14,1);
INSERT INTO passenger VALUES (17,'Ivy','Fern',TO_DATE('2013-08-18','YYYY-MM-DD'),'F',NULL,'N',14,1);
INSERT INTO passenger VALUES (18,'Noel','Chan',TO_DATE('2010-10-10','YYYY-MM-DD'),'X',NULL,'Y',6,6);

INSERT INTO passenger VALUES (21,'Liam','Walker',TO_DATE('1990-02-15','YYYY-MM-DD'),'M','0412002334','N',15,NULL);


INSERT INTO passenger VALUES (22,'Emily','Moana',TO_DATE('1987-09-08','YYYY-MM-DD'),'F','0213309090','N',16,NULL);



-- More adults
INSERT INTO passenger VALUES (19,'Arjun','Patel',TO_DATE('1988-12-12','YYYY-MM-DD'),'M','0402500700','N',8,NULL);
INSERT INTO passenger VALUES (20,'Lena','Schultz',TO_DATE('1987-09-09','YYYY-MM-DD'),'F','0402700900','N',9,NULL);

-- =======================================
-- MANIFEST
-- =======================================

INSERT INTO manifest VALUES (1,1,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(12/24),101,'1001');
INSERT INTO manifest VALUES (2,2,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(6/24),101,'1001');
INSERT INTO manifest VALUES (3,7,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(10/24),101,'1001');
INSERT INTO manifest VALUES (4,8,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(10/24),101,'1001');
INSERT INTO manifest VALUES (5,9,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(10/24),101,'1001');
INSERT INTO manifest VALUES (6,10,1,TO_DATE('02/06/2025 10:00','DD/MM/YYYY HH24:MI')-(10/24),101,'1001');

INSERT INTO manifest VALUES (7,1,4,TO_DATE('07/07/2025 02:00','DD/MM/YYYY HH24:MI')-(8/24),101,'1001');
INSERT INTO manifest VALUES (8,2,4,NULL,101,'1001');
INSERT INTO manifest VALUES (9,3,4,TO_DATE('07/07/2025 02:00','DD/MM/YYYY HH24:MI')-(4/24),101,'1001');
INSERT INTO manifest VALUES (10,16,4,TO_DATE('07/07/2025 02:00','DD/MM/YYYY HH24:MI')-(9/24),101,'1001');
INSERT INTO manifest VALUES (11,17,4,TO_DATE('07/07/2025 02:00','DD/MM/YYYY HH24:MI')-(9/24),101,'1001');

INSERT INTO manifest VALUES (12,4,2,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(12/24),102,'2001');
INSERT INTO manifest VALUES (13,5,2,NULL,102,'2001');
INSERT INTO manifest VALUES (14,6,2,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(7/24),102,'2001');
INSERT INTO manifest VALUES (15,11,2,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(6/24),102,'2001');
INSERT INTO manifest VALUES (16,12,2,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(8/24),102,'2001');

INSERT INTO manifest VALUES (17,13,5,TO_DATE('08/07/2025 10:30','DD/MM/YYYY HH24:MI')-(6/24),102,'2001');
INSERT INTO manifest VALUES (18,14,5,TO_DATE('08/07/2025 10:30','DD/MM/YYYY HH24:MI')-(5/24),102,'2001');
INSERT INTO manifest VALUES (19,15,5,TO_DATE('08/07/2025 10:30','DD/MM/YYYY HH24:MI')-(4/24),102,'2001');
INSERT INTO manifest VALUES (20,19,5,TO_DATE('08/07/2025 10:30','DD/MM/YYYY HH24:MI')-(4/24),102,'2001');
INSERT INTO manifest VALUES (21,20,5,TO_DATE('08/07/2025 10:30','DD/MM/YYYY HH24:MI')-(4/24),102,'2001');

INSERT INTO manifest VALUES (22,1,3,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(9/24),103,'110');
INSERT INTO manifest VALUES (23,2,3,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(7/24),103,'110');
INSERT INTO manifest VALUES (24,3,3,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(6/24),103,'110');
INSERT INTO manifest VALUES (25,4,3,TO_DATE('16/06/2025 09:00','DD/MM/YYYY HH24:MI')-(10/24),103,'110');
INSERT INTO manifest VALUES (26,5,3,NULL,103,'110');

INSERT INTO manifest VALUES (27,13,10,NULL,102,'2001');
INSERT INTO manifest VALUES (28,14,10,NULL,102,'2001');
INSERT INTO manifest VALUES (29,19,10,NULL,102,'2001');
INSERT INTO manifest VALUES (30,20,10,NULL,102,'2001');
INSERT INTO manifest VALUES (31,21,1,SYSDATE,101,'1001');
INSERT INTO manifest VALUES (32,21,3,SYSDATE,103,'110');
INSERT INTO manifest VALUES (33,21,4,SYSDATE,101,'1001');
INSERT INTO manifest VALUES (34,22,5,SYSDATE,102,'2001');
COMMIT;