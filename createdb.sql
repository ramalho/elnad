CREATE DATABASE company;
CREATE USER 'student'@'localhost' IDENTIFIED BY 'puffpuff';
GRANT ALL PRIVILEGES ON company.* TO 'student'@'localhost';
CREATE DATABASE test_company;
GRANT ALL PRIVILEGES ON test_company.* TO 'student'@'localhost';
