![image](https://user-images.githubusercontent.com/83235640/137639717-092320bf-283e-4516-b25a-12ee181f0b57.png)

![image](https://user-images.githubusercontent.com/83235640/137673224-635acf8a-9505-41e4-8340-d70227c0e19b.png)

```
--Table Roles creating
CREATE TABLE roles (
	id SERIAL PRIMARY KEY,
	role_title VARCHAR(50) NOT NULL
);

--Table Salary creating
CREATE TABLE salary (
	id SERIAL PRIMARY KEY,
	monthly_salary int
);

--Table Employees_roles creating
CREATE TABLE employees_roles (
	id SERIAL PRIMARY KEY,
	id_role int NOT NULL REFERENCES roles(id),
	id_employee int NOT NULL
);

--Table Roles_salary creating
CREATE TABLE roles_salary (
	id SERIAL PRIMARY KEY,
	id_role int,
	id_salary int,
	FOREIGN KEY (id_salary) REFERENCES salary(id)
);

--Table Service creating
CREATE TABLE service (
	id SERIAL PRIMARY KEY,
	service_title VARCHAR(50) NOT NULL,
	price int NOT NULL
);

--Table Materials creating
CREATE TABLE materials (
	id SERIAL PRIMARY KEY,
	material_title VARCHAR(50),
	amount int,
	price int
);

--Table Employees creating
CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	employee_name VARCHAR(50) NOT NULL
);

--Table Claim creating
CREATE TABLE claim (
	id SERIAL PRIMARY KEY,
	service_id int REFERENCES service(id),
	employee_id int REFERENCES employees(id),
	material_id int REFERENCES materials(id),
	claim_date date,
	sales_manager int REFERENCES employees(id)
);

--Adding constraints
ALTER TABLE roles_salary
ADD FOREIGN KEY (id_role) REFERENCES roles(id);

ALTER TABLE employees_roles
ADD FOREIGN KEY (id_employee) REFERENCES employees(id);

--Adding data
INSERT INTO roles (role_title)
VALUES ('Accountant');
SELECT *
FROM roles;

INSERT INTO salary (monthly_salary)
VALUES (7000);
SELECT *
FROM salary;

INSERT INTO employees_roles (id_role, id_employee)
VALUES (10, 6);
SELECT *
FROM employees_roles;

INSERT INTO roles_salary (id_role, id_salary)
VALUES (11, 5);
SELECT *
FROM roles_salary;

INSERT INTO service (service_title, price)
VALUES ('Consulting', 500);
SELECT *
FROM service;

INSERT INTO materials (material_title, amount, price)
VALUES ('Media label', 12, 4);
SELECT *
FROM materials;

INSERT INTO employees (employee_name)
VALUES ('Leo');
SELECT *
FROM employees;

INSERT INTO claim (service_id, employee_id, material_id, claim_date, sales_manager)
VALUES (14, 10, 10, '2021-10-08', 8);
SELECT *
FROM claim;

--Adding new table Suppliers
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
```
