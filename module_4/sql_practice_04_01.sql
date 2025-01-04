SELECT * FROM hr_db.employees;

SELECT first_name, last_name, phone_number FROM hr_db.employees;

SELECT DISTINCT first_name FROM hr_db.employees;

SELECT COUNT(*) FROM hr_db.employees;

SELECT COUNT(DISTINCT first_name) FROM hr_db.employees;

SELECT * FROM hr_db.employees WHERE first_name = 'David';

SELECT * FROM hr_db.employees WHERE salary >= 10000;

SELECT * FROM hr_db.employees WHERE salary BETWEEN 5000 AND 10000;

SELECT first_name, last_name, phone_number FROM hr_db.employees WHERE hire_date 
BETWEEN '1987-06-01' AND '1987-06-30'; 

SELECT * FROM hr_db.employees WHERE 
job_id IN ('IT_PROG', 'FI_ACCOUNT') 
AND hire_date BETWEEN '1987-06-20' AND '1987-06-25';

SELECT * FROM hr_db.employees WHERE phone_number LIKE '515%';

SELECT * FROM hr_db.employees WHERE 
manager_id = 104 OR manager_id = 105 OR manager_id = 103;

SELECT * FROM hr_db.employees WHERE email IS NOT NULL;

SELECT * FROM hr_db.employees ORDER BY salary DESC;

SELECT SUM(salary) FROM hr_db.employees 
WHERE first_name = 'David';