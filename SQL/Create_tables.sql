CREATE TABLE employees_roles (
	id SERIAL PRIMARY KEY,
	id_role int NOT NULL REFERENCES roles(id),
	id_employee int NOT NULL
);
INSERT INTO employees_roles (id_role, id_employee)
VALUES (10, 6);
SELECT *
FROM employees_roles;


CREATE TABLE roles (
	id SERIAL PRIMARY KEY,
	role_title VARCHAR(50) NOT NULL
);
INSERT INTO roles (role_title)
VALUES ('Accountant');
SELECT *
FROM roles;


ALTER TABLE employees_roles
ADD FOREIGN KEY (id_employee) REFERENCES employees(id);

CREATE TABLE salary (
	id SERIAL PRIMARY KEY,
	monthly_salary int
);
INSERT INTO salary (monthly_salary)
VALUES (7000);
SELECT *
FROM salary;


CREATE TABLE roles_salary (
	id SERIAL PRIMARY KEY,
	id_role int,
	id_salary int,
	FOREIGN KEY (id_salary) REFERENCES salary(id)
);
INSERT INTO roles_salary (id_role, id_salary)
VALUES (11, 5);
SELECT *
FROM roles_salary;

--ALTER TABLE roles_salary
--DROP CONSTRAINT id_role;

CREATE TABLE service (
	id SERIAL PRIMARY KEY,
	service_title VARCHAR(50) NOT NULL,
	price int NOT NULL
);
INSERT INTO service (service_title, price)
VALUES ('Consulting', 500);
SELECT *
FROM service;


CREATE TABLE materials (
	id SERIAL PRIMARY KEY,
	material_title VARCHAR(50),
	amount int,
	price int
);
INSERT INTO materials (material_title, amount, price)
VALUES ('Media label', 12, 4);
SELECT *
FROM materials;

CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	employee_name VARCHAR(50) NOT NULL
);
INSERT INTO employees (employee_name)
VALUES ('Leo');
SELECT *
FROM employees;

CREATE TABLE claim (
	id SERIAL PRIMARY KEY,
	service_id int REFERENCES service(id),
	employee_id int REFERENCES employees(id),
	material_id int REFERENCES materials(id),
	claim_date date,
	sales_manager int REFERENCES employees(id)
);
INSERT INTO claim (service_id, employee_id, material_id, claim_date, sales_manager)
VALUES (14, 10, 10, '2021-10-08', 8);
SELECT *
FROM claim;

CREATE TABLE suppliers (
	id SERIAL PRIMARY KEY,
	"name" VARCHAR(50)
);
INSERT INTO suppliers ("name")
VALUES ('A-ha');
SELECT *
FROM suppliers;

ALTER TABLE materials ADD COLUMN supplier_id INT;
ALTER TABLE materials
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(id);

ALTER TABLE employees ADD COLUMN surname VARCHAR(50);
ALTER TABLE salary ADD COLUMN currency VARCHAR(7);