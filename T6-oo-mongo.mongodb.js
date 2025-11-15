// *****PLEASE ENTER YOUR DETAILS BELOW*****
// T6-oo-mongo.mongodb.js

// Student ID:35863900
// Student Name:Raveen Pieris 
// ====================================================================================
// DO NOT modify or relocate any of the comments below (items marked with //)
// You are required to add additional comments as described on page five of this brief.
// ====================================================================================

// Use (connect to) your database - you MUST update xyz001
// with your authcate username

use("rdaj0001");
// (b)
// PLEASE PLACE REQUIRED MONGODB COMMAND TO CREATE THE COLLECTION HERE
// YOU MAY PICK ANY COLLECTION NAME
// ENSURE that your statement is formatted and has a semicolon
// (;) at the end of each MongoDB statement

// Drop collection
db.oo.drop();

// Create collection and insert documents

db.oo.insertMany(
  [
{"_id":1,"passenger_name":"Maya Fern","passenger_dob":"13-04-1988","passenger_contact":"0400111222","guardian_name":" ","address":{"street":"88 Reef Sands","town":"Coral Bay","postcode":"3013","country":"Afghanistan"},"no_of _cruises":3,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"01-06-2025 22:00","cabin_no":"1001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"16-06-2025 00:00","cabin_no":"110","cabin_class":"O"},{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"06-07-2025 18:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":2,"passenger_name":"Ethan Rao","passenger_dob":"17-02-1995","passenger_contact":"0400333444","guardian_name":" ","address":{"street":"44 Wharf Road","town":"Harbourtown","postcode":"3001","country":"Afghanistan"},"no_of _cruises":3,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"02-06-2025 04:00","cabin_no":"1001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"16-06-2025 02:00","cabin_no":"110","cabin_class":"O"},{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"-","cabin_no":"1001","cabin_class":"I"}]},
{"_id":3,"passenger_name":"Ari Lee","passenger_dob":"30-11-1992","passenger_contact":"0400555666","guardian_name":" ","address":{"street":"7 Lighthouse Ave","town":"Portside","postcode":"3002","country":"Angola"},"no_of _cruises":2,"cruises":[{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"06-07-2025 22:00","cabin_no":"1001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"16-06-2025 03:00","cabin_no":"110","cabin_class":"O"}]},
{"_id":4,"passenger_name":"Noah Khan","passenger_dob":"09-08-1985","passenger_contact":"0400777888","guardian_name":" ","address":{"street":"18 Palm Grove","town":"Marina City","postcode":"3003","country":"Aruba"},"no_of _cruises":3,"cruises":[{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"15-06-2025 21:00","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"15-06-2025 23:00","cabin_no":"110","cabin_class":"O"},{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"15-06-2025 21:00","cabin_no":"2001","cabin_class":"O"}]},
{"_id":5,"passenger_name":"Zoe Park","passenger_dob":"22-06-1990","passenger_contact":"0400999000","guardian_name":" ","address":{"street":"5 Coral Crescent","town":"Reefville","postcode":"3004","country":"Afghanistan"},"no_of _cruises":3,"cruises":[{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"-","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"-","cabin_no":"110","cabin_class":"O"},{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"-","cabin_no":"2001","cabin_class":"O"}]},
{"_id":6,"passenger_name":"Olivia Chan","passenger_dob":"14-01-1987","passenger_contact":"0401100200","guardian_name":" ","address":{"street":"91 Ocean View","town":"Shelly Beach","postcode":"3005","country":"Angola"},"no_of _cruises":2,"cruises":[{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 02:00","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 02:00","cabin_no":"2001","cabin_class":"O"}]},
{"_id":7,"passenger_name":"Leo Martin","passenger_dob":"02-03-1984","passenger_contact":"0401300400","guardian_name":" ","address":{"street":"45 Sunset Pier","town":"Bayview","postcode":"3012","country":"Aruba"},"no_of _cruises":1,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"02-06-2025 00:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":8,"passenger_name":"Ava Martin","passenger_dob":"12-05-2010","passenger_contact":"-","guardian_name":"Leo Martin","address":{"street":"45 Sunset Pier","town":"Bayview","postcode":"3012","country":"Aruba"},"no_of _cruises":1,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"02-06-2025 00:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":9,"passenger_name":"Mia Martin","passenger_dob":"03-09-2012","passenger_contact":"-","guardian_name":"Leo Martin","address":{"street":"45 Sunset Pier","town":"Bayview","postcode":"3012","country":"Aruba"},"no_of _cruises":1,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"02-06-2025 00:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":10,"passenger_name":"Kai Martin","passenger_dob":"29-12-2009","passenger_contact":"-","guardian_name":"Leo Martin","address":{"street":"45 Sunset Pier","town":"Bayview","postcode":"3012","country":"Aruba"},"no_of _cruises":1,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"02-06-2025 00:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":11,"passenger_name":"Riya Das","passenger_dob":"05-10-1998","passenger_contact":"0401500600","guardian_name":" ","address":{"street":"77 Pier Parade","town":"Harbourton","postcode":"3007","country":"Afghanistan"},"no_of _cruises":2,"cruises":[{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 03:00","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 03:00","cabin_no":"2001","cabin_class":"O"}]},
{"_id":12,"passenger_name":"Ben Ng","passenger_dob":"21-07-1989","passenger_contact":"0401700800","guardian_name":" ","address":{"street":"9 Anchor Lane","town":"Jetty Hills","postcode":"3008","country":"Angola"},"no_of _cruises":2,"cruises":[{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 01:00","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"2","cruise_name":"Melbourne to Sydney","board_date_time":"16-06-2025 01:00","cabin_no":"2001","cabin_class":"O"}]},
{"_id":13,"passenger_name":"Imani Osei","passenger_dob":"02-02-1993","passenger_contact":"0401900100","guardian_name":" ","address":{"street":"31 Marina Quay","town":"Seacliff","postcode":"3009","country":"Aruba"},"no_of _cruises":4,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 04:30","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"O"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 04:30","cabin_no":"2001","cabin_class":"O"}]},
{"_id":14,"passenger_name":"Tom Evans","passenger_dob":"17-05-1986","passenger_contact":"0402100300","guardian_name":" ","address":{"street":"6 Pelican Row","town":"Gull Point","postcode":"3010","country":"Afghanistan"},"no_of _cruises":4,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 05:30","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"O"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 05:30","cabin_no":"2001","cabin_class":"O"}]},
{"_id":15,"passenger_name":"Sara Kim","passenger_dob":"28-03-1991","passenger_contact":"0402300500","guardian_name":" ","address":{"street":"55 Beacon Road","town":"Wavecrest","postcode":"3011","country":"Angola"},"no_of _cruises":2,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"O"}]},
{"_id":16,"passenger_name":"Niko Fern","passenger_dob":"04-04-2011","passenger_contact":"-","guardian_name":"Maya Fern","address":{"street":"88 Reef Sands","town":"Coral Bay","postcode":"3013","country":"Afghanistan"},"no_of _cruises":1,"cruises":[{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"06-07-2025 17:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":17,"passenger_name":"Ivy Fern","passenger_dob":"18-08-2013","passenger_contact":"-","guardian_name":"Maya Fern","address":{"street":"88 Reef Sands","town":"Coral Bay","postcode":"3013","country":"Afghanistan"},"no_of _cruises":1,"cruises":[{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"06-07-2025 17:00","cabin_no":"1001","cabin_class":"I"}]},
{"_id":18,"passenger_name":"Noel Chan","passenger_dob":"10-10-2010","passenger_contact":"-","guardian_name":"Olivia Chan","address":{"street":"91 Ocean View","town":"Shelly Beach","postcode":"3005","country":"Angola"},"no_of _cruises":0,"cruises":[]},
{"_id":19,"passenger_name":"Arjun Patel","passenger_dob":"12-12-1988","passenger_contact":"0402500700","guardian_name":" ","address":{"street":"77 Pier Parade","town":"Harbourton","postcode":"3007","country":"Afghanistan"},"no_of _cruises":4,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"O"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"O"}]},
{"_id":20,"passenger_name":"Lena Schultz","passenger_dob":"09-09-1987","passenger_contact":"0402700900","guardian_name":" ","address":{"street":"9 Anchor Lane","town":"Jetty Hills","postcode":"3008","country":"Angola"},"no_of _cruises":4,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"O"},{"cruise_id":"10","cruise_name":"New Zealand Christmas Sail","board_date_time":"-","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"08-07-2025 06:30","cabin_no":"2001","cabin_class":"O"}]},
{"_id":21,"passenger_name":"Liam Walker","passenger_dob":"15-02-1990","passenger_contact":"0412002334","guardian_name":" ","address":{"street":"23 Ocean Road","town":"Perth","postcode":"6000","country":"Australia"},"no_of _cruises":3,"cruises":[{"cruise_id":"1","cruise_name":"Australian Circumnavigation","board_date_time":"31-10-2025 11:31","cabin_no":"1001","cabin_class":"I"},{"cruise_id":"4","cruise_name":"Queensland Islands","board_date_time":"31-10-2025 11:31","cabin_no":"1001","cabin_class":"I"},{"cruise_id":"3","cruise_name":"New Zealand Delight","board_date_time":"31-10-2025 11:31","cabin_no":"110","cabin_class":"O"}]},
{"_id":22,"passenger_name":"Emily Moana","passenger_dob":"08-09-1987","passenger_contact":"0213309090","guardian_name":" ","address":{"street":"77 Forest Lane","town":"Auckland","postcode":"1010","country":"New Zealand"},"no_of _cruises":2,"cruises":[{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"31-10-2025 11:31","cabin_no":"2001","cabin_class":"I"},{"cruise_id":"5","cruise_name":"Brisbane to Hobart","board_date_time":"31-10-2025 11:31","cabin_no":"2001","cabin_class":"O"}]},
{"_id":500,"passenger_name":"Dominik Kohl","passenger_dob":"01-01-1980","passenger_contact":"+61493336312","guardian_name":" ","address":{"street":"23 Banksia Avenue","town":"Melbourne","postcode":"3000","country":"Australia"},"no_of _cruises":0,"cruises":[]},
{"_id":505,"passenger_name":"Stella Kohl","passenger_dob":"10-05-2012","passenger_contact":"-","guardian_name":"Dominik Kohl","address":{"street":"23 Banksia Avenue","town":"Melbourne","postcode":"3000","country":"Australia"},"no_of _cruises":0,"cruises":[]},
{"_id":510,"passenger_name":"Poppy Kohl","passenger_dob":"22-03-2015","passenger_contact":"-","guardian_name":"Dominik Kohl","address":{"street":"23 Banksia Avenue","town":"Melbourne","postcode":"3000","country":"Australia"},"no_of _cruises":0,"cruises":[]},
  ]
)
// List all documents you added
db.oo.find();
// (c)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer
db.oo.find(
  { "address.country": {$in:["Australia", "New Zealand"]}, 
  "no_of_cruises" : {$gt:2}
  }, 
  {"_id":1,
    "passenger_name": 1,
    "passenger_contact":1,
    "address":1
  }
);
// (d)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your statement is formatted and has a semicolon
// (;) at the end of each MongoDB statement
// (i) Add new passenger and first booking
db.oo.insertOne(
  {
    "_id": "1000",
    "passenger_name": "Kiera Meier",
    "passenger_dob": "30-10-1976",
    "passenger_contact": "0424675687",
    "guardian_name": "-",
    "address":{
      "street": "Pinewood Dr",
      "town": "Mount Waverly",
      "postcode": "3142",
      "country": "Australia"
    },
    "no_of_cruises": 1,
    "cruises":[
      {
        "cruise_id": "9", 
        "cruise_name": "Queensland Islands",
        "board_date_time": "05-08-2025 14:00",
        "cabin_no": "2022",
        "cabin_class":"Balcony"
      }
    ]
  }
)
// Illustrate/confirm changes made
db.oo.find({
  "_id":"1000"
});
// (ii) Add second booking
db.oo.updateOne({"_id":"1000"},
    {"$push": {"cruises":{
        "cruise_id": "10",
        "cruise_name":"New Zealand Christmas Sail",
        "board_date_time":"25-12-2025 00:00",
        "cabin_no": "4004",
        "cabin_class": "Suite"
    }}}
)
// Illustrate/confirm changes made
db.oo.find({
  "_id":"1000"
});

/* (iii) Write a reflection of the difference
between inserting the passenger and booking data
into the Oracle versus MongoDB.

<<write your reflection here>>
<<
The process of inserting passengers passengers and booking data in Oracale is a structured process which 
involves working across multiple related tables. In oracle, passenger details, cabin bookings, and cruise information are stored seperately 
using primary and foreign keys in different tables. When adding a new passenger with a new booking, we must 
insert a row first into passenger table, then insert another seperate row to the MANIFEST table to record 
the booking. This requires ensuring referencal integirity, correct foreign key values and matching data types. 
This process is more controled but slower, because one change in a table may result in an another few table's rows to be changed. 
Also changes usually require multiple SQL statements and must follow the database schema strictly. 

In contrast, MongoDb allows both the passenger and their bookings to be stored in a single document. Adding a 
new passenger with bookings can be done in one insertOne() command operation and adding further bookings can be done 
using updateone() and "$push" and if we want to delete we can use "$pull". There is no ned for joins or foreign
key constraints, which makes the process faster and more flexible but this flexibility means the data reliesd more
on the application logic. If incorrect or inconsistent values are inserted, MongoDB will still accept them because it does 
not enforce relational contraints. 

Overall, Oracle emphasizes data integrity and structure while MongoDB emphasizes flexiblity and ease of 
data manipulation. 

>>

*/