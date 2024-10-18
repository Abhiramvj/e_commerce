drop database bookstore;
create database bookstore;
use bookstore;
CREATE TABLE Customers (customer_id INT PRIMARY KEY,name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL UNIQUE);
CREATE TABLE Books (book_id INT PRIMARY KEY,title VARCHAR(255) NOT NULL,author VARCHAR(255) NOT NULL,price DECIMAL(10, 2) NOT NULL);
CREATE TABLE Orders (order_id INT PRIMARY KEY,customer_id INT,order_date DATE NOT NULL,FOREIGN KEY (customer_id) REFERENCES Customers(customer_id));
CREATE TABLE OrderDetails (order_id INT,book_id INT,quantity INT NOT NULL,PRIMARY KEY (order_id, book_id),FOREIGN KEY (order_id) REFERENCES Orders(order_id),FOREIGN KEY (book_id) REFERENCES Books(book_id));
INSERT INTO Customers (customer_id, name, email)
VALUES (1, 'John', 'john@gmail.com'),
       (2, 'Jane', 'jane@gmail.com'),
       (3, 'Alice', 'alice@gmail.com'),
       (4, 'Michael', 'michael@gmail.com'),
       (5, 'Emily', 'emily@gmail.com'),
       (6, 'Daniel', 'daniel@gmail.com'),
       (7, 'Sophia', 'sophia@gmail.com'),
       (8, 'James', 'james@gmail.com'),
       (9, 'Isabella', 'isabella@gmail.com'),
       (10, 'William', 'william@gmail.com');
INSERT INTO Books (book_id, title, author, price)
VALUES (1, 'To Kill a Mockingbird', 'Harper Lee', 12.99),
       (2, '1984', 'George Orwell', 15.50),
       (3, 'The Great Gatsby', 'F. Scott Fitzgerald', 10.75),
       (4, 'Pride and Prejudice', 'Jane Austen', 8.99),
       (5, 'The Catcher in the Rye', 'J.D. Salinger', 13.45),
       (6, 'Moby Dick', 'Herman Melville', 9.80),
       (7, 'War and Peace', 'Leo Tolstoy', 18.99),
       (8, 'Ulysses', 'James Joyce', 14.60),
       (9, 'The Odyssey', 'Homer', 11.20),
       (10, 'Crime and Punishment', 'Fyodor Dostoevsky', 16.75);
INSERT INTO Orders (order_id, customer_id, order_date)
VALUES (1, 1, '2023-01-15'),
       (2, 2, '2023-01-17'),
       (3, 3, '2023-01-19'),
       (4, 1, '2023-02-02'),
       (5, 4, '2023-02-10'),
       (6, 5, '2023-03-05'),
       (7, 2, '2024-03-11'),
       (8, 3, '2024-04-09'),
       (9, 5, '2024-04-12'),
       (10, 4, '2024-05-01'); 
-- Insert 10 sample order details into the OrderDetails table
INSERT INTO OrderDetails (order_id, book_id, quantity)
VALUES (1, 1, 2),  
       (1, 2, 1),  
       (2, 1, 1),  
       (2, 3, 4),  
       (3, 2, 3),  
       (4, 3, 23),  
       (5, 1, 33),  
       (6, 2, 2),  
       (7, 3, 3),  
       (8, 1, 2);  
select * from books;
select* from customers;
select * from orders;
select * from orderdetails;
Select c.customer_id,c.name,sum(od.quantity) as total_quantity from customers c join orders o on c.customer_id=o.customer_id join orderdetails od on o.order_id=od.order_id
where  o.order_date >= NOW() - interval 1 year group by c.customer_id, c.name order by total_quantity desc limit 5;
select b.author,sum(od.quantity*b.price) as total_revenue from books b join orderdetails od on b.book_id=od.book_id join orders o on od.order_id=o.order_id group by 
b.author order by total_revenue desc;
select b.book_id,b.title,b.author,sum(od.quantity) as total_quantity_ordered from Books b join OrderDetails od on b.book_id = od.book_id group by b.book_id, b.title, b.author
having SUM(od.quantity) > 10;


 

