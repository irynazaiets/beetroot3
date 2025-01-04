SELECT first_name, last_name, gender FROM patients WHERE gender='M';

SELECT first_name, last_name FROM patients WHERE allergies IS NULL;

SELECT DISTINCT first_name FROM patients WHERE first_name LIKE 'C%' ORDER BY first_name;

SELECT first_name, last_name FROM patients WHERE weight between 100 AND 120;

SELECT * FROM patients WHERE birth_date LIKE '%-02';

SELECT * FROM patients;