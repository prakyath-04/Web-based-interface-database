CREATE OR REPLACE PROCEDURE insertcustomer (
fname_ IN pm_custmr.fname%TYPE,
mname_ IN pm_custmr.mname%TYPE DEFAULT NULL,
lname_ IN pm_custmr.lname%TYPE,
street_ IN pm_custmr.street%TYPE,
h_no_ IN pm_custmr.h_no%TYPE,
apt_no_ IN pm_custmr.apt_no%TYPE DEFAULT NULL,
city_ IN pm_custmr.city%TYPE,
state_ IN pm_custmr.STATE%TYPE,
country_ IN pm_custmr.country%TYPE,
zip_ IN pm_custmr.zip%TYPE,
gender_ IN pm_custmr.gender%TYPE DEFAULT NULL,
mart_status_ IN pm_custmr.mart_status%TYPE)
IS
BEGIN
INSERT INTO pm_custmr VALUES ((SELECT MAX(cid)+1 FROM pm_custmr),fname_,mname_,lname_,street_,h_no_,apt_no_,city_,state_,country_,zip_,gender_,mart_status_);
COMMIT;
END;
/

--DELETE FROM PM_CUSTMR WHERE CID = 3213213214;
--COMMIT;
-- EXEC insertcustomer('PETER','STINSON','UNION STREET',13,'A1','MANHATTAN','NEW YORK','USA',11211,'M','S');



CREATE OR REPLACE PROCEDURE insertinsurance (
ins_type IN pm_insrnce.ins_type%TYPE,
prem_amt IN pm_insrnce.prem_amt%TYPE,
status_ IN pm_insrnce.status%TYPE,

start_date IN pm_cust_insr.start_date%TYPE,
end_date IN pm_cust_insr.end_date%TYPE,
cid_ IN pm_cust_insr.cid%TYPE)

IS
BEGIN
INSERT INTO pm_insrnce VALUES ((SELECT MAX(ins_no)+1 FROM pm_insrnce),ins_type,status_,prem_amt);
COMMIT;
INSERT INTO pm_cust_insr VALUES (start_date,end_date,cid_,(SELECT MAX(ins_no) FROM pm_insrnce));
IF ins_type = 'H' THEN
    INSERT INTO pm_in_home VALUES ((SELECT MAX(ins_no) FROM pm_insrnce));
ELSE
    INSERT INTO pm_in_auto VALUES ((SELECT MAX(ins_no) FROM pm_insrnce));
END IF;

COMMIT;
END;
/

-- EXEC insertinsurance('H',1500,'C',sysdate,sysdate + numtoyminterval(5,'year'),3213213214);



CREATE OR REPLACE PROCEDURE insertvehicle (
ins_type IN pm_insrnce.ins_type%TYPE,
prem_amt IN pm_insrnce.prem_amt%TYPE,
status_ IN pm_insrnce.status%TYPE,

start_date IN pm_cust_insr.start_date%TYPE,
end_date IN pm_cust_insr.end_date%TYPE,
cid_ IN pm_cust_insr.cid%TYPE)

IS
BEGIN
INSERT INTO pm_insrnce VALUES ((SELECT MAX(ins_no)+1 FROM pm_insrnce),ins_type,status_,prem_amt);
COMMIT;
INSERT INTO pm_cust_insr VALUES (start_date,end_date,cid_,(SELECT MAX(ins_no) FROM pm_insrnce));
IF ins_type = 'H' THEN
    INSERT INTO pm_in_home VALUES ((SELECT MAX(ins_no) FROM pm_insrnce));
ELSE
    INSERT INTO pm_in_auto VALUES ((SELECT MAX(ins_no) FROM pm_insrnce));
END IF;

COMMIT;
END;
/


-- EXEC insertinsurance('A',3500,'C',sysdate,sysdate + numtoyminterval(5,'year'),3213213213);



CREATE OR REPLACE PROCEDURE insertvehicle (
vin IN pm_vehcle.vin%TYPE,
vmake IN pm_vehcle.vmake%TYPE,
vmodel IN pm_vehcle.vmodel%TYPE,
model_yr IN pm_vehcle.model_yr%TYPE,
status IN pm_vehcle.status%TYPE,
ins_no IN pm_vehcle.ins_no%TYPE)

IS
BEGIN
INSERT INTO pm_vehcle VALUES (vin,vmake,vmodel,model_yr,status,ins_no);
COMMIT;
END;
/

-- EXEC insertvehicle(661312,'toyota','corolla',2021,'L',1000000041);

CREATE OR REPLACE PROCEDURE insertdriver(
licence IN pm_driver.licence%TYPE,
d_fname IN pm_driver.d_fname%TYPE,
d_lname IN pm_driver.d_lname%TYPE,
d_mname IN pm_driver.d_mname%TYPE DEFAULT NULL,
birthdate IN pm_driver.birthdate%TYPE,
vin IN pm_driver.vin%TYPE)

IS
BEGIN
INSERT INTO pm_driver VALUES (licence,d_fname,d_lname,d_mname,birthdate,vin);
COMMIT;
END;
/

-- EXEC insertdriver(6613126666,'asdf',';lkj',NULL,'13-FEB-1989',661312);

CREATE OR REPLACE PROCEDURE inserthome(
pur_date IN pm_home.pur_date%TYPE,
pur_value IN pm_home.pur_value%TYPE,
area IN pm_home.area%TYPE,
htype IN pm_home.htype%TYPE,
auto_fire_n IN pm_home.auto_fire_n%TYPE,
home_security IN pm_home.home_security%TYPE,
basement IN pm_home.basement%TYPE,
swim_pool IN pm_home.swim_pool%TYPE,
ins_no IN pm_home.ins_no%TYPE)

IS
BEGIN
INSERT INTO pm_home VALUES ((SELECT MAX(pm_home.house_id)+1 FROM pm_home),pur_date,pur_value,area,htype,auto_fire_n,home_security,basement,swim_pool,ins_no);
COMMIT;
END;
/

-- EXEC inserthome('22-FEB-16',1050000,2400,'S',0,0,1,'I',1000000042);


CREATE OR REPLACE PROCEDURE SelectCustomer(
fname_ IN pm_custmr.fname%TYPE,
lname_ in pm_custmr.lname%TYPE)
IS
BEGIN
SELECT * FROM pm_custmr WHERE pm_custmr.fname=fname_ and pm_custmr.lname=lname_;
END;
/

--
-- exec SelectCustomer('MARK','STINSON');
--
--
-- select * from (select * from pm_insrnce a join (select b.start_date,b.end_date,b.cid,b.ins_no from pm_cust_insr b join pm_custmr c on b.cid = c.cid where c.cid = 1023456789) d on a.ins_no=d.ins_no)
--
--
-- select * from pm_home natural join (select * from pm_in_home natural join (select * from pm_cust_insr natural join pm_insrnce))
--
-- select * from pm_driver natural join (select * from pm_vehcle a join (select * from pm_in_auto natural join (select * from pm_cust_insr natural join pm_insrnce)) b on a.ins_no=b.ins_no)


CREATE OR REPLACE PROCEDURE UPDATEcustomer (
fname_ IN pm_custmr.fname%TYPE,
mname_ IN pm_custmr.mname%TYPE DEFAULT NULL,
lname_ IN pm_custmr.lname%TYPE,
street_ IN pm_custmr.street%TYPE,
h_no_ IN pm_custmr.h_no%TYPE,
apt_no_ IN pm_custmr.apt_no%TYPE DEFAULT NULL,
city_ IN pm_custmr.city%TYPE,
state_ IN pm_custmr.STATE%TYPE,
country_ IN pm_custmr.country%TYPE,
zip_ IN pm_custmr.zip%TYPE,
gender_ IN pm_custmr.gender%TYPE DEFAULT NULL,
mart_status_ IN pm_custmr.mart_status%TYPE)
IS
BEGIN
UPDATE pm_custmr SET NAME=p_name, GENDER=p_gender, ADDRESS=p_address WHERE NAME=p_name;
COMMIT;
END;
/



CREATE OR REPLACE PROCEDURE DeleteCustomer (
fname_ IN pm_custmr.fname%TYPE,
lname_ IN pm_custmr.lname%TYPE
)
IS
BEGIN
UPDATE pm_insrnce SET Status='P' WHERE ins_no in (select ins_no from pm_cust_insr natural join (select * from pm_custmr where fname = fname_ and lname = lname_));
DELETE FROM pm_cust_insr WHERE cid = (select cid from pm_custmr where fname = fname_ and lname = lname_);
Delete from pm_custmr where cid = (select cid from pm_custmr where fname = fname_ and lname = lname_);
commit;
END;
/

-- exec deletecustomer('2','2');
--
-- UPDATE pm_insrnce SET Status='C' WHERE ins_no in (select ins_no from pm_cust_insr natural join (select * from pm_custmr where fname = '2' and lname = '2'));
-- commit;
