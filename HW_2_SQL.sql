--1. Создать таблицу employees
-- id. serial,  primary key,
-- employee_name. Varchar(50), not null

create table employees(
	id serial primary key,
	employee_name varchar(50) not null
);

--2. Наполнить таблицу employee 70 строками.

insert into employees(employee_name)
values ('Catherine_Humphrey'),
('Stephanie_Hernandez'),
('Lisa_Drake'),
('Susan_Gordon'),
('Dylan_Ellis'),
('Mary_Brown'),
('Mark_Wheeler'),
('Jack_Briggs'),
('Stephanie_Williams'),
('Patricia_White'),
('Tara_Olsen'),
('Julia_Jones'),
('Dennis_Powell'),
('Juan_Brown'),
('Jonathan_Heath'),
('Patricia_Bradley'),
('Dale_Cox'),
('Frances_Lewis'),
('Jim_Murphy'),
('James_Powell'),
('Hannah_Fuentes'),
('Alexander_Graham'),
('Billy_Schneider'),
('Jamie_Armstrong'),
('Thomas_Martinez'),
('Jacob_Osborne'),
('Lisa_Myers'),
('Brenda_Taylor'),
('Samantha_Robinson'),
('Julie_Evans'),
('Brittney_Hayes'),
('Jonathan_Nash'),
('Robert_Mann'),
('Mary_Snyder'),
('Julie_Ellis'),
('Virginia_Patterson'),
('Kevin_Miles'),
('Timothy_Hubbard'),
('Derek_Wilson'),
('Ashlee_Gibson'),
('Brittany_Dodson'),
('Timothy_Walsh'),
('Timothy_Willis'),
('James_Ayers'),
('Kevin_Smith'),
('John_Turner'),
('Stephanie_Ryan'),
('Tamara_Lawrence'),
('Nancy_Lozano'),
('Kevin_Schmidt'),
('Rose_Thomas'),
('Shelly_Parker'),
('Susan_Mitchell'),
('Andrea_Scott'),
('Ruben_Myers'),
('Brett_Watson'),
('Christopher_Anderson'),
('Nicholas_Bruce'),
('Monique_Reynolds'),
('Brittany_Mullins'),
('Rebecca_Richard'),
('Ryan_Knox'),
('Norma_Payne'),
('Stephanie_Zamora'),
('Iuliia_Ekkart'),
('Kathleen_Castillo'),
('Jack_Williams'),
('Russell_Brooks'),
('John_Ferguson'),
('Mary_Moore');

--3. Создать таблицу salary
-- id. Serial  primary key,
-- monthly_salary. Int, not null

create table salary(
	id serial primary key,
	monthly_salary int not null
)

--4. Наполнить таблицу salary 15 строками

insert into salary(monthly_salary)
values (1000),
(1100),
(1200),
(1300),
(1400),
(1500),
(1600),
(1700),
(1800),
(1900),
(2000),
(2100),
(2200),
(2300),
(2400);

--5. Создать таблицу employee_salary
-- id. Serial  primary key,
-- employee_id. Int, not null, unique
-- salary_id. Int, not null

create table employee_salary(
	id serial primary key,
	employee_id int not null unique,
	salary_id int not null
);

--6. Наполнить таблицу employee_salary 40 строками:
-- в 10 строк из 40 вставить несуществующие employee_id

insert into employee_salary(employee_id, salary_id)
values (1, 15),
(2, 14),
(3, 13),
(4, 12),
(5, 11),
(6, 10),
(7, 9),
(8, 8),
(9, 7),
(10, 6),
(11, 5),
(12, 4),
(13, 3),
(14, 2),
(15, 1),
(71, 15),
(82, 14),
(93, 13),
(72, 12),
(83, 11),
(16, 10),
(17, 9),
(18, 8),
(19, 7),
(20, 6),
(21, 5),
(22, 4),
(23, 3),
(24, 2),
(25, 1),
(65, 15),
(66, 14),
(67, 13),
(68, 12),
(55, 11),
(77, 10),
(85, 9),
(79, 8),
(88, 7),
(99, 6);

--7. Создать таблицу roles
-- id. Serial  primary key,
-- role_name. int, not null, unique

create table roles(
	id serial primary key,
	role_name int not null unique
);

--8. Поменять тип столба role_name с int на varchar(30)

alter table roles
alter column role_name type varchar(30) using role_name:: varchar(30);

--9. Наполнить таблицу roles 20 строками

insert into roles(role_name)
values ('Junior Python developer'),
('Middle Python developer'),
('Senior Python developer'),
('Junior Java developer'),
('Middle Java developer'),
('Senior Java developer'),
('Junior JavaScript developer'),
('Middle JavaScript developer'),
('Senior JavaScript developer'),
('Junior Manual QA engineer'),
('Middle Manual QA engineer'),
('Senior Manual QA engineer'),
('Project Manager'),
('Designer'),
('HR'),
('CEO'),
('Sales manager'),
('Junior Automation QA engineer'),
('Middle Automation QA engineer'),
('Senior Automation QA engineer');


--10. Создать таблицу roles_employee
-- id. Serial  primary key,
-- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
-- role_id. Int, not null (внешний ключ для таблицы roles, поле id)

create table roles_employee(
	id serial primary key,
	employee_id int not null unique,
	role_id int not null,
	foreign key (employee_id)
		references employees (id),
	foreign key (role_id)
		references roles (id)
);

--11. Наполнить таблицу roles_employee 40 строками

insert into roles_employee (employee_id, role_id)
values (1, 10),
(11, 18),
(21, 16),
(31, 14),
(41, 12),
(51, 10),
(61, 18),
(2, 6),
(12, 4),
(22, 2),
(32, 2),
(42, 8),
(52, 1),
(62, 4),
(3, 2),
(13, 1),
(23, 8),
(33, 6),
(43, 4),
(53, 2),
(63, 1),
(4, 3),
(14, 5),
(24, 7),
(34, 9),
(54, 11),
(64, 13),
(5, 15),
(15, 17),
(25, 19),
(35, 2),
(45, 3),
(44, 5),
(55, 7),
(65, 9),
(6, 3),
(16, 13),
(26, 15),
(36, 17),
(46, 3);
