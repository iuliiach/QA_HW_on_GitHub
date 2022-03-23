--Short database description "Computer firm":

--The database scheme consists of four tables:
--Product(maker, model, type)
--PC(code, model, speed, ram, hd, cd, price)
--Laptop(code, model, speed, ram, hd, screen, price)
--Printer(code, model, color, type, price)
--The Product table contains data on the maker, model number, and type of product ('PC', 'Laptop', or 'Printer'). It is assumed that model numbers in the Product table are unique for all makers and product types. Each personal computer in the PC table is unambiguously identified by a unique code, and is additionally characterized by its model (foreign key referring to the Product table), processor speed (in MHz) – speed field, RAM capacity (in Mb) - ram, hard disk drive capacity (in Gb) – hd, CD-ROM speed (e.g, '4x') - cd, and its price. The Laptop table is similar to the PC table, except that instead of the CD-ROM speed, it contains the screen size (in inches) – screen. For each printer model in the Printer table, its output type (‘y’ for color and ‘n’ for monochrome) – color field, printing technology ('Laser', 'Jet', or 'Matrix') – type, and price are specified.

--Exercise: 1 
--Find the model number, speed and hard drive capacity for all the PCs with prices below $500.
--Result set: model, speed, hd.

select model,speed, hd
from PC
where price < 500;

--Exercise: 2 
--List all printer makers. Result set: maker.

select distinct maker
from Product
where type = 'Printer';

--Exercise: 3 
Find the model number, RAM and screen size of the laptops with prices over $1000.

select model number, ram, screen
from Laptop
where price > 1000;

--Exercise: 4 
--Find all records from the Printer table containing data about color printers.

select *
from Printer
where color = 'y';

--Exercise: 5 
--Find the model number, speed and hard drive capacity of PCs cheaper than $600 having a 12x or a 24x CD drive.

select model, speed, hd
from PC
where price < 600 and (cd = '12x' or cd = '24x');

--Exercise: 6 
For each maker producing laptops with a hard drive capacity of 10 Gb or higher, find the speed of such laptops. Result set: maker, speed.

select distinct maker, speed
from product
join laptop
on product.model = laptop.model
where hd >= 10.0;
