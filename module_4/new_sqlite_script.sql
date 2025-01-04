-- SQLite Database Schema

-- Regions Table
CREATE TABLE regions (
  region_id INTEGER PRIMARY KEY,
  region_name TEXT NOT NULL
);

-- Countries Table
CREATE TABLE countries (
  country_id TEXT PRIMARY KEY,
  country_name TEXT NOT NULL,
  region_id INTEGER NOT NULL,
  FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- Locations Table
CREATE TABLE locations (
  location_id INTEGER PRIMARY KEY,
  street_address TEXT NOT NULL,
  postal_code TEXT,
  city TEXT NOT NULL,
  state_province TEXT,
  country_id TEXT,
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Departments Table
CREATE TABLE departments (
  department_id INTEGER PRIMARY KEY,
  depart_name TEXT NOT NULL,
  manager_id INTEGER,
  location_id INTEGER,
  FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Jobs Table
CREATE TABLE jobs (
  job_id TEXT PRIMARY KEY,
  job_title TEXT NOT NULL,
  min_salary REAL,
  max_salary REAL
);

-- Employees Table
CREATE TABLE employees (
  employee_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  phone_number TEXT,
  hire_date TEXT,
  job_id TEXT NOT NULL,
  salary REAL,
  commission_pct REAL,
  manager_id INTEGER,
  department_id INTEGER,
  Avg_Salary REAL,
  FOREIGN KEY (job_id) REFERENCES jobs(job_id),
  FOREIGN KEY (department_id) REFERENCES departments(department_id),
  FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Job History Table
CREATE TABLE job_history (
  employee_id INTEGER NOT NULL,
  start_date TEXT NOT NULL,
  end_date TEXT NOT NULL,
  job_id TEXT NOT NULL,
  department_id INTEGER NOT NULL,
  PRIMARY KEY (employee_id, start_date),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id),
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Product Master Table
CREATE TABLE prod_mast (
  prod_id INTEGER PRIMARY KEY,
  prod_name TEXT,
  prod_rate INTEGER,
  prod_qc TEXT DEFAULT 'OK'
);

-- Product Backup Table
CREATE TABLE prod_backup (
  prod_id INTEGER PRIMARY KEY,
  prod_name TEXT,
  prod_rate INTEGER,
  prod_qc TEXT DEFAULT 'OK'
);

-- Orders Table
CREATE TABLE orders (
  ord_no INTEGER PRIMARY KEY,
  item_id INTEGER,
  item_name TEXT,
  ord_qty INTEGER,
  cost INTEGER
);

-- Test Table
CREATE TABLE tb1 (
  c1 INTEGER,
  c2 TEXT,
  c3 REAL
);

-- Minimum Salary Table
CREATE TABLE MIN_SALARY (
  job_id TEXT,
  MIN_SALARY REAL,
  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

-- Disable foreign key constraints to allow data insertion
PRAGMA foreign_keys = OFF;

-- 1. Regions Data
INSERT INTO regions (region_id, region_name) VALUES 
(1, 'Europe'),
(2, 'Americas'),
(3, 'Asia'),
(4, 'Middle East and Africa'),
(999, 'MONE_999');

-- 2. Jobs Data
INSERT INTO jobs (job_id, job_title, min_salary, max_salary) VALUES 
('AD_PRES', 'President', 20000, 40000),
('AD_VP', 'Administration Vice President', 15000, 30000),
('AD_ASST', 'Administration Assistant', 3000, 6000),
('FI_MGR', 'Finance Manager', 8200, 16000),
('FI_ACCOUNT', 'Accountant', 4200, 9000),
('AC_MGR', 'Accounting Manager', 8200, 16000),
('AC_ACCOUNT', 'Public Accountant', 4200, 9000),
('SA_MAN', 'Sales Manager', 10000, 20000),
('SA_REP', 'Sales Representative', 6000, 12000),
('PU_MAN', 'Purchasing Manager', 8000, 15000),
('PU_CLERK', 'Purchasing Clerk', 2500, 5500),
('ST_MAN', 'Stock Manager', 5500, 8500),
('ST_CLERK', 'Stock Clerk', 2000, 5000),
('SH_CLERK', 'Shipping Clerk', 2500, 5500),
('IT_PROG', 'Programmer', 4000, 10000),
('MK_MAN', 'Marketing Manager', 9000, 15000),
('MK_REP', 'Marketing Representative', 4000, 9000),
('HR_REP', 'Human Resources Representative', 4000, 9000),
('PR_REP', 'Public Relations Representative', 4500, 10500);

-- 3. Countries Data
INSERT INTO countries (country_id, country_name, region_id) VALUES 
('AR', 'Argentina', 2),
('AU', 'Australia', 3),
('BE', 'Belgium', 1),
('BR', 'Brazil', 2),
('CA', 'Canada', 2),
('CH', 'Switzerland', 1),
('CN', 'China', 3),
('DE', 'Germany', 1),
('DK', 'Denmark', 1),
('EG', 'Egypt', 4),
('FR', 'France', 1),
('HK', 'HongKong', 3),
('IL', 'Israel', 4),
('IN', 'India', 3),
('IT', 'Italy', 1),
('JP', 'Japan', 3),
('KW', 'Kuwait', 4),
('MX', 'Mexico', 2),
('NG', 'Nigeria', 4),
('NL', 'Netherlands', 1),
('SG', 'Singapore', 3),
('UK', 'United Kingdom', 1),
('US', 'United States of America', 2),
('ZM', 'Zambia', 4),
('ZW', 'Zimbabwe', 4);

-- 4. Locations Data
INSERT INTO locations (location_id, street_address, postal_code, city, state_province, country_id) VALUES 
(1000, '1297 Via Cola di Rie', '989', 'Roma', '', 'IT'),
(1100, '93091 Calle della Testa', '10934', 'Venice', '', 'IT'),
(1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP'),
(1300, '9450 Kamiya-cho', '6823', 'Hiroshima', '', 'JP'),
(1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US'),
(1500, '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US'),
(1600, '2007 Zagora St', '50090', 'South Brunswick', 'New Jersey', 'US'),
(1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US'),
(1800, '147 Spadina Ave', 'M5V 2L7', 'Toronto', 'Ontario', 'CA'),
(1900, '6092 Boxwood St', 'YSW 9T2', 'Whitehorse', 'Yukon', 'CA'),
(2000, '40-5-12 Laogianggen', '190518', 'Beijing', '', 'CN'),
(2100, '1298 Vileparle (E)', '490231', 'Bombay', 'Maharashtra', 'IN'),
(2200, '12-98 Victoria Street', '2901', 'Sydney', 'New South Wales', 'AU'),
(2300, '198 Clementi North', '540198', 'Singapore', '', 'SG'),
(2400, '8204 Arthur St', '', 'London', '', 'UK'),
(2500, 'Magdalen Centre, The Oxford Science Park', 'OX9 9ZB', 'Oxford', 'Oxford', 'UK'),
(2600, '9702 Chester Road', '9629850293', 'Stretford', 'Manchester', 'UK'),
(2700, 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE'),
(2800, 'Rua Frei Caneca 1360', '01307-002', 'Sao Paulo', 'Sao Paulo', 'BR'),
(2900, '20 Rue des Corps-Saints', '1730', 'Geneva', 'Geneve', 'CH'),
(3000, 'Murtenstrasse 921', '3095', 'Bern', 'BE', 'CH'),
(3100, 'Pieter Breughelstraat 837', '3029SK', 'Utrecht', 'Utrecht', 'NL'),
(3200, 'Mariano Escobedo 9991', '11932', 'Mexico City', 'Distrito Federal,', 'MX');

-- 5. Departments Data (initially with NULL managers)
INSERT INTO departments (department_id, depart_name, manager_id, location_id) VALUES 
(90, 'Executive', NULL, 1700),
(60, 'IT', NULL, 1400),
(100, 'Finance', NULL, 1700),
(30, 'Purchasing', NULL, 1700),
(50, 'Shipping', NULL, 1500),
(80, 'Sales', NULL, 2500),
(10, 'Administration', NULL, 1700),
(20, 'Marketing', NULL, 1800),
(40, 'Human Resources', NULL, 2400),
(70, 'Public Relations', NULL, 2700),
(110, 'Accounting', NULL, 1700),
(120, 'Treasury', NULL, 1700),
(130, 'Corporate Tax', NULL, 1700),
(140, 'Control And Credit', NULL, 1700),
(150, 'Shareholder Services', NULL, 1700),
(160, 'Benefits', NULL, 1700),
(170, 'Manufacturing', NULL, 1700),
(180, 'Construction', NULL, 1700),
(190, 'Contracting', NULL, 1700),
(200, 'Operations', NULL, 1700),
(210, 'IT Support', NULL, 1700),
(220, 'NOC', NULL, 1700),
(230, 'IT Helpdesk', NULL, 1700),
(240, 'Government Sales', NULL, 1700),
(250, 'Retail Sales', NULL, 1700),
(260, 'Recruiting', NULL, 1700),
(270, 'Payroll', NULL, 1700);

-- Complete Employees Data
INSERT INTO employees (
    employee_id, first_name, last_name, email, phone_number, 
    hire_date, job_id, salary, commission_pct, manager_id, department_id, Avg_Salary
) VALUES 
(100, 'Steven', 'King', 'SKING', '515.123.4567', '1987-06-17', 'AD_PRES', 24000, NULL, NULL, 90, NULL),
(101, 'Neena', 'Kochhar', 'NKOCHHAR', '515.123.4568', '1987-06-18', 'AD_VP', 17000, NULL, 100, 90, NULL),
(102, 'Lex', 'De Haan', 'LDEHAAN', '515.123.4569', '1987-06-19', 'AD_VP', 17000, NULL, 100, 90, NULL),
(103, 'Alexander', 'Hunold', 'AHUNOLD', '590.423.4567', '1987-06-20', 'IT_PROG', 9000, 0, 102, 60, NULL),
(104, 'Bruce', 'Ernst', 'BERNST', '590.423.4568', '1987-06-21', 'IT_PROG', 6000, 0, 103, 60, NULL),
(105, 'David', 'Austin', 'DAUSTIN', '590.423.4569', '1987-06-22', 'IT_PROG', 4800, 0, 103, 60, NULL),
(106, 'Valli', 'Pataballa', 'VPATABAL', '590.423.4560', '1987-06-23', 'IT_PROG', 4800, 0, 103, 60, NULL),
(107, 'Diana', 'Lorentz', 'DLORENTZ', '590.423.5567', '1987-06-24', 'IT_PROG', 4200, 0, 103, 60, NULL),
(108, 'Nancy', 'Greenberg', 'NGREENBE', '515.124.4569', '1987-06-25', 'FI_MGR', 12000, 0, 101, 100, NULL),
(109, 'Daniel', 'Faviet', 'DFAVIET', '515.124.4169', '1987-06-26', 'FI_ACCOUNT', 9000, 0, 108, 100, NULL),
(110, 'John', 'Chen', 'JCHEN', '515.124.4269', '1987-06-27', 'FI_ACCOUNT', 8200, 0, 108, 100, NULL),
(111, 'Ismael', 'Sciarra', 'ISCIARRA', '515.124.4369', '1987-06-28', 'FI_ACCOUNT', 7700, 0, 108, 100, NULL),
(112, 'Jose Manuel', 'Urman', 'JMURMAN', '515.124.4469', '1987-06-29', 'FI_ACCOUNT', 7800, 0, 108, 100, NULL),
(113, 'Luis', 'Popp', 'LPOPP', '515.124.4567', '1987-06-30', 'FI_ACCOUNT', 6900, 0, 108, 100, NULL),
(114, 'Den', 'Raphaely', 'DRAPHEAL', '515.127.4561', '1987-07-01', 'PU_MAN', 11000, 0, 100, 30, NULL),
(115, 'Alexander', 'Khoo', 'AKHOO', '515.127.4562', '1987-07-02', 'PU_CLERK', 3100, 0, 114, 30, NULL),
(116, 'Shelli', 'Baida', 'SBAIDA', '515.127.4563', '1987-07-03', 'PU_CLERK', 2900, 0, 114, 30, NULL),
(117, 'Sigal', 'Tobias', 'STOBIAS', '515.127.4564', '1987-07-04', 'PU_CLERK', 2800, 0, 114, 30, NULL),
(118, 'Guy', 'Himuro', 'GHIMURO', '515.127.4565', '1987-07-05', 'PU_CLERK', 2600, 0, 114, 30, NULL),
(119, 'Karen', 'Colmenares', 'KCOLMENA', '515.127.4566', '1987-07-06', 'PU_CLERK', 2500, 0, 114, 30, NULL),
(120, 'Matthew', 'Weiss', 'MWEISS', '650.123.1234', '1987-07-07', 'ST_MAN', 8000, 0, 100, 50, NULL),
(121, 'Adam', 'Fripp', 'AFRIPP', '650.123.2234', '1987-07-08', 'ST_MAN', 8200, 0, 100, 50, NULL),
(122, 'Payam', 'Kaufling', 'PKAUFLIN', '650.123.3234', '1987-07-09', 'ST_MAN', 7900, 0, 100, 50, NULL),
(123, 'Shanta', 'Vollman', 'SVOLLMAN', '650.123.4234', '1987-07-10', 'ST_MAN', 6500, 0, 100, 50, NULL),
(124, 'Kevin', 'Mourgos', 'KMOURGOS', '650.123.5234', '1987-07-11', 'ST_MAN', 5800, 0, 100, 50, NULL),
(125, 'Julia', 'Nayer', 'JNAYER', '650.124.1214', '1987-07-12', 'ST_CLERK', 3200, 0, 120, 50, NULL),
(126, 'Irene', 'Mikkilineni', 'IMIKKILI', '650.124.1224', '1987-07-13', 'ST_CLERK', 2700, 0, 120, 50, NULL),
(127, 'James', 'Landry', 'JLANDRY', '650.124.1334', '1987-07-14', 'ST_CLERK', 2400, 0, 120, 50, NULL),
(128, 'Steven', 'Markle', 'SMARKLE', '650.124.1434', '1987-07-15', 'ST_CLERK', 2200, 0, 120, 50, NULL),
(129, 'Laura', 'Bissot', 'LBISSOT', '650.124.5234', '1987-07-16', 'ST_CLERK', 3300, 0, 121, 50, NULL),
(130, 'Mozhe', 'Atkinson', 'MATKINSO', '650.124.6234', '1987-07-17', 'ST_CLERK', 2800, 0, 121, 50, NULL),
(131, 'James', 'Marlow', 'JAMRLOW', '650.124.7234', '1987-07-18', 'ST_CLERK', 2500, 0, 121, 50, NULL),
(132, 'TJ', 'Olson', 'TJOLSON', '650.124.8234', '1987-07-19', 'ST_CLERK', 2100, 0, 121, 50, NULL),
(133, 'Jason', 'Mallin', 'JMALLIN', '650.127.1934', '1987-07-20', 'ST_CLERK', 3300, 0, 122, 50, NULL),
(134, 'Michael', 'Rogers', 'MROGERS', '650.127.1834', '1987-07-21', 'ST_CLERK', 2900, 0, 122, 50, NULL),
(135, 'Ki', 'Gee', 'KGEE', '650.127.1734', '1987-07-22', 'ST_CLERK', 2400, 0, 122, 50, NULL),
(136, 'Hazel', 'Philtanker', 'HPHILTAN', '650.127.1634', '1987-07-23', 'ST_CLERK', 2200, 0, 122, 50, NULL),
(137, 'Renske', 'Ladwig', 'RLADWIG', '650.121.1234', '1987-07-24', 'ST_CLERK', 3600, 0, 123, 50, NULL),
(138, 'Stephen', 'Stiles', 'SSTILES', '650.121.2034', '1987-07-25', 'ST_CLERK', 3200, 0, 123, 50, NULL),
(139, 'John', 'Seo', 'JSEO', '650.121.2019', '1987-07-26', 'ST_CLERK', 2700, 0, 123, 50, NULL),
(140, 'Joshua', 'Patel', 'JPATEL', '650.121.1834', '1987-07-27', 'ST_CLERK', 2500, 0, 123, 50, NULL),
(141, 'Trenna', 'Rajs', 'TRAJS', '650.121.8009', '1987-07-28', 'ST_CLERK', 3500, 0, 124, 50, NULL),
(142, 'Curtis', 'Davies', 'CDAVIES', '650.121.2994', '1987-07-29', 'ST_CLERK', 3100, 0, 124, 50, NULL),
(143, 'Randall', 'Matos', 'RMATOS', '650.121.2874', '1987-07-30', 'ST_CLERK', 2600, 0, 124, 50, NULL),
(144, 'Peter', 'Vargas', 'PVARGAS', '650.121.2004', '1987-07-31', 'ST_CLERK', 2500, 0, 124, 50, NULL),
(145, 'John', 'Russell', 'JRUSSEL', '011.44.1344.429268', '1987-08-01', 'SA_MAN', 14000, 0.4, 100, 80, NULL),
(146, 'Karen', 'Partners', 'KPARTNER', '011.44.1344.467268', '1987-08-02', 'SA_MAN', 13500, 0.3, 100, 80, NULL),
(147, 'Alberto', 'Errazuriz', 'AERRAZUR', '011.44.1344.429278', '1987-08-03', 'SA_MAN', 12000, 0.3, 100, 80, NULL),
(148, 'Gerald', 'Cambrault', 'GCAMBRAU', '011.44.1344.619268', '1987-08-04', 'SA_MAN', 11000, 0.3, 100, 80, NULL),
(149, 'Eleni', 'Zlotkey', 'EZLOTKEY', '011.44.1344.429018', '1987-08-05', 'SA_MAN', 10500, 0.2, 100, 80, NULL),
(150, 'Peter', 'Tucker', 'PTUCKER', '011.44.1344.129268', '1987-08-06', 'SA_REP', 10000, 0.3, 145, 80, NULL),
(151, 'David', 'Bernstein', 'DBERNSTE', '011.44.1344.345268', '1987-08-07', 'SA_REP', 9500, 0.25, 145, 80, NULL),
(152, 'Peter', 'Hall', 'PHALL', '011.44.1344.478968', '1987-08-08', 'SA_REP', 9000, 0.25, 145, 80, NULL),
(153, 'Christopher', 'Olsen', 'COLSEN', '011.44.1344.498718', '1987-08-09', 'SA_REP', 8000, 0.2, 145, 80, NULL),
(154, 'Nanette', 'Cambrault', 'NCAMBRAU', '011.44.1344.987668', '1987-08-10', 'SA_REP', 7500, 0.2, 145, 80, NULL),
(155, 'Oliver', 'Tuvault', 'OTUVAULT', '011.44.1344.486508', '1987-08-11', 'SA_REP', 7000, 0.15, 145, 80, NULL),
(156, 'Janette', 'King', 'JKING', '011.44.1345.429268', '1987-08-12', 'SA_REP', 10000, 0.35, 146, 80, NULL),
(157, 'Patrick', 'Sully', 'PSULLY', '011.44.1345.929268', '1987-08-13', 'SA_REP', 9500, 0.35, 146, 80, NULL),
(158, 'Allan', 'McEwen', 'AMCEWEN', '011.44.1345.829268', '1987-08-14', 'SA_REP', 9000, 0.35, 146, 80, NULL),
(159, 'Lindsey', 'Smith', 'LSMITH', '011.44.1345.729268', '1987-08-15', 'SA_REP', 8000, 0.3, 146, 80, NULL),
(160, 'Louise', 'Doran', 'LDORAN', '011.44.1345.629268', '1987-08-16', 'SA_REP', 7500, 0.3, 146, 80, NULL),
(161, 'Sarath', 'Sewall', 'SSEWALL', '011.44.1345.529268', '1987-08-17', 'SA_REP', 7000, 0.25, 146, 80, NULL),
(162, 'Clara', 'Vishney', 'CVISHNEY', '011.44.1346.129268', '1987-08-18', 'SA_REP', 10500, 0.25, 147, 80, NULL),
(163, 'Danielle', 'Greene', 'DGREENE', '011.44.1346.229268', '1987-08-19', 'SA_REP', 9500, 0.15, 147, 80, NULL),
(164, 'Mattea', 'Marvins', 'MMARVINS', '011.44.1346.329268', '1987-08-20', 'SA_REP', 7200, 0.10, 147, 80, NULL),
(165, 'David', 'Lee', 'DLEE', '011.44.1346.529268', '1987-08-21', 'SA_REP', 6800, 0.10, 147, 80, NULL),
(166, 'Sundar', 'Ande', 'SANDE', '011.44.1346.629268', '1987-08-22', 'SA_REP', 6400, 0.10, 147, 80, NULL),
(167, 'Amit', 'Banda', 'ABANDA', '011.44.1346.729268', '1987-08-23', 'SA_REP', 6200, 0.10, 147, 80, NULL),
(168, 'Lisa', 'Ozer', 'LOZER', '011.44.1343.929268', '1987-08-24', 'SA_REP', 11500, 0.25, 148, 80, NULL),
(169, 'Harrison', 'Bloom', 'HBLOOM', '011.44.1343.829268', '1987-08-25', 'SA_REP', 10000, 0.20, 148, 80, NULL),
(170, 'Tayler', 'Fox', 'TFOX', '011.44.1343.729268', '1987-08-26', 'SA_REP', 9600, 0.20, 148, 80, NULL),
(171, 'William', 'Smith', 'WSMITH', '011.44.1343.629268', '1987-08-27', 'SA_REP', 7400, 0.15, 148, 80, NULL),
(172, 'Elizabeth', 'Bates', 'EBATES', '011.44.1343.529268', '1987-08-28', 'SA_REP', 7300, 0.15, 148, 80, NULL),
(173, 'Sundita', 'Kumar', 'SKUMAR', '011.44.1343.329268', '1987-08-29', 'SA_REP', 6100, 0.10, 148, 80, NULL),
(174, 'Ellen', 'Abel', 'EABEL', '011.44.1644.429267', '1987-08-30', 'SA_REP', 11000, 0.30, 149, 80, NULL),
(175, 'Alyssa', 'Hutton', 'AHUTTON', '011.44.1644.429266', '1987-08-31', 'SA_REP', 8800, 0.25, 149, 80, NULL),
(176, 'Jonathon', 'Taylor', 'JTAYLOR', '011.44.1644.429265', '1987-09-01', 'SA_REP', 8600, 0.20, 149, 80, NULL),
(177, 'Jack', 'Livingston', 'JLIVINGS', '011.44.1644.429264', '1987-09-02', 'SA_REP', 8400, 0.20, 149, 80, NULL),
(178, 'Kimberely', 'Grant', 'KGRANT', '011.44.1644.429263', '1987-09-03', 'SA_REP', 7000, 0.15, 149, NULL, NULL),
(179, 'Charles', 'Johnson', 'CJOHNSON', '011.44.1644.429262', '1987-09-04', 'SA_REP', 6200, 0.10, 149, 80, NULL),
(180, 'Winston', 'Taylor', 'WTAYLOR', '650.507.9876', '1987-09-05', 'SH_CLERK', 3200, NULL, 120, 50, NULL),
(181, 'Jean', 'Fleaur', 'JFLEAUR', '650.507.9877', '1987-09-06', 'SH_CLERK', 3100, NULL, 120, 50, NULL),
(182, 'Martha', 'Sullivan', 'MSULLIVA', '650.507.9878', '1987-09-07', 'SH_CLERK', 2500, NULL, 120, 50, NULL),
(183, 'Girard', 'Geoni', 'GGEONI', '650.507.9879', '1987-09-08', 'SH_CLERK', 2800, NULL, 120, 50, NULL),
(184, 'Nandita', 'Sarchand', 'NSARCHAN', '650.509.1876', '1987-09-09', 'SH_CLERK', 4200, NULL, 121, 50, NULL),
(185, 'Alexis', 'Bull', 'ABULL', '650.509.2876', '1987-09-10', 'SH_CLERK', 4100, NULL, 121, 50, NULL),
(186, 'Julia', 'Dellinger', 'JDELLING', '650.509.3876', '1987-09-11', 'SH_CLERK', 3400, NULL, 121, 50, NULL),
(187, 'Anthony', 'Cabrio', 'ACABRIO', '650.509.4876', '1987-09-12', 'SH_CLERK', 3000, NULL, 121, 50, NULL),
(188, 'Kelly', 'Chung', 'KCHUNG', '650.505.1876', '1987-09-13', 'SH_CLERK', 3800, NULL, 122, 50, NULL),
(189, 'Jennifer', 'Dilly', 'JDILLY', '650.505.2876', '1987-09-14', 'SH_CLERK', 3600, NULL, 122, 50, NULL),
(190, 'Timothy', 'Gates', 'TGATES', '650.505.3876', '1987-09-15', 'SH_CLERK', 2900, NULL, 122, 50, NULL),
(191, 'Randall', 'Perkins', 'RPERKINS', '650.505.4876', '1987-09-16', 'SH_CLERK', 2500, NULL, 122, 50, NULL),
(192, 'Sarah', 'Bell', 'SBELL', '650.501.1876', '1987-09-17', 'SH_CLERK', 4000, NULL, 123, 50, NULL),
(193, 'Britney', 'Everett', 'BEVERETT', '650.501.2876', '1987-09-18', 'SH_CLERK', 3900, NULL, 123, 50, NULL),
(194, 'Samuel', 'McCain', 'SMCCAIN', '650.501.3876', '1987-09-19', 'SH_CLERK', 3200, NULL, 123, 50, NULL),
(195, 'Vance', 'Jones', 'VJONES', '650.501.4876', '1987-09-20', 'SH_CLERK', 2800, NULL, 123, 50, NULL),
(196, 'Alana', 'Walsh', 'AWALSH', '650.507.9811', '1987-09-21', 'SH_CLERK', 3100, NULL, 124, 50, NULL),
(197, 'Kevin', 'Feeney', 'KFEENEY', '650.507.9822', '1987-09-22', 'SH_CLERK', 3000, NULL, 124, 50, NULL),
(198, 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '1987-09-23', 'SH_CLERK', 2600, NULL, 124, 50, NULL),
(199, 'Douglas', 'Grant', 'DGRANT', '650.507.9844', '1987-09-24', 'SH_CLERK', 2600, NULL, 124, 50, NULL),
(200, 'Jennifer', 'Whalen', 'JWHALEN', '515.123.4444', '1987-09-25', 'AD_ASST', 4400, NULL, 101, 10, NULL),
(201, 'Michael', 'Hartstein', 'MHARTSTE', '515.123.5555', '1987-09-26', 'MK_MAN', 13000, NULL, 100, 20, NULL),
(202, 'Pat', 'Fay', 'PFAY', '603.123.6666', '1987-09-27', 'MK_REP', 6000, NULL, 201, 20, NULL),
(203, 'Susan', 'Mavris', 'SMAVRIS', '515.123.7777', '1987-09-28', 'HR_REP', 6500, NULL, 101, 40, NULL),
(204, 'Hermann', 'Baer', 'HBAER', '515.123.8888', '1987-09-29', 'PR_REP', 10000, NULL, 101, 70, NULL),
(205, 'Shelley', 'Higgins', 'SHIGGINS', '515.123.8080', '1987-09-30', 'AC_MGR', 12000, NULL, 101, 110, NULL),
(206, 'William', 'Gietz', 'WGIETZ', '515.123.8181', '1987-10-01', 'AC_ACCOUNT', 8300, NULL, 205, 110, NULL);

-- Update departments with managers
UPDATE departments SET manager_id = 200 WHERE department_id = 10;
UPDATE departments SET manager_id = 201 WHERE department_id = 20;
UPDATE departments SET manager_id = 114 WHERE department_id = 30;
UPDATE departments SET manager_id = 203 WHERE department_id = 40;
UPDATE departments SET manager_id = 121 WHERE department_id = 50;
UPDATE departments SET manager_id = 103 WHERE department_id = 60;
UPDATE departments SET manager_id = 204 WHERE department_id = 70;
UPDATE departments SET manager_id = 145 WHERE department_id = 80;
UPDATE departments SET manager_id = 100 WHERE department_id = 90;
UPDATE departments SET manager_id = 108 WHERE department_id = 100;
UPDATE departments SET manager_id = 205 WHERE department_id = 110;

-- 7. Job History
INSERT INTO job_history (employee_id, start_date, end_date, job_id, department_id) VALUES 
(102, '1993-01-13', '1998-07-24', 'IT_PROG', 60),
(101, '1989-09-21', '1993-10-27', 'AC_ACCOUNT', 110),
(101, '1993-10-28', '1997-03-15', 'AC_MGR', 110),
(201, '1996-02-17', '1999-12-19', 'MK_REP', 20),
(200, '1987-09-17', '1993-06-17', 'AD_ASST', 90);

-- 8. Product Master
INSERT INTO prod_mast (prod_id, prod_name, prod_rate, prod_qc) VALUES 
(1, 'Pancakes', 75, 'OK'),
(2, 'Gulha', 55, 'OK'),
(3, 'Pakora', 48, 'OK'),
(4, 'Pizza', 200, 'OK'),
(5, 'Fudge', 100, 'OK'),
(6, 'Candy', 95, 'OK'),
(7, 'Chocolate', 150, 'OK');

-- 9. Product Backup
INSERT INTO prod_backup (prod_id, prod_name, prod_rate, prod_qc) VALUES 
(1, 'Pancakes', 75, 'OK'),
(2, 'Gulha', 55, 'Problems'),
(3, 'Pakora', 48, 'OK'),
(4, 'Pizza', 200, 'OK'),
(5, 'Fudge', 100, 'OK'),
(6, 'Candy', 95, 'Not OK'),
(7, 'Chocolate', 150, 'OK');

-- 10. Orders
INSERT INTO orders (ord_no, item_id, item_name, ord_qty, cost) VALUES 
(1, 5, 'Fudge', 100, 10000),
(2, 2, 'Gulha', 95, 5225),
(3, 1, 'Pancakes', 150, 11250),
(4, 2, 'Gulha', 250, 13750),
(5, 2, 'Gulha', 300, 16500),
(6, 10, NULL, 100, NULL),
(7, 8, NULL, 95, NULL);

-- 11. Test Table
INSERT INTO tb1 (c1, c2, c3) VALUES 
(2, '2', 2.0),
(3, '3', 3.0);

-- 12. Minimum Salary
INSERT INTO MIN_SALARY (job_id, MIN_SALARY) VALUES 
('AD_PRES', 24000),
('AD_VP', 17000),
('FI_ACCOUNT', 6900),
('IT_PROG', 4200),
('PU_CLERK', 2500),
('SA_REP', 7000),
('ST_CLERK', 2100),
('ST_MAN', 5800);

-- Re-enable foreign key constraints
PRAGMA foreign_keys = ON;