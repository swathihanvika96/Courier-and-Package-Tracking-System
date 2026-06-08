CREATE DATABASE courier1_db;

USE courier1_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Kavitha', '9876543210', 'Bangalore'),
(2, 'Prakash', '9876543211', 'Hyderabad');

CREATE TABLE shipments (
    shipment_id INT PRIMARY KEY,
    customer_id INT,
    package_name VARCHAR(100),
    shipment_date DATE,
    delivery_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) 
    REFERENCES customers(customer_id)
);

INSERT INTO shipments VALUES
(101, 1, 'Electronics', '2025-05-01', '2025-05-04', 'Delivered'),
(102, 1, 'Clothes', '2025-05-05', '2025-05-08', 'Delivered'),
(103, 2, 'Books', '2025-05-10', NULL, 'Pending');

SELECT c.customer_id,
       c.customer_name,
       COUNT(s.shipment_id) AS total_shipments
FROM customers c
JOIN shipments s
ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_shipments DESC;

SELECT COUNT(*) AS total_delivered_packages
FROM shipments
WHERE status = 'Delivered';

SELECT shipment_id,
       package_name,
       shipment_date,
       status
FROM shipments
WHERE status = 'Pending';

SELECT DATE_FORMAT(shipment_date, '%Y-%m') AS month,
       COUNT(*) AS total_shipments
FROM shipments
GROUP BY DATE_FORMAT(shipment_date, '%Y-%m')
ORDER BY month;

SELECT AVG(DATEDIFF(delivery_date, shipment_date))
       AS avg_delivery_days
FROM shipments
WHERE status = 'Delivered';

SELECT
    c.customer_id,
    c.customer_name,
    COUNT(s.shipment_id) AS shipment_count,
    RANK() OVER (
        ORDER BY COUNT(s.shipment_id) DESC
    ) AS customer_rank
FROM customers c
JOIN shipments s
ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name;