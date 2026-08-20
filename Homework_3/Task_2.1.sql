SELECT 
    first_name,
    last_name,
    item,
    amount
FROM 
    Orders
JOIN 
    Customers ON orders.customer_id = customers.customer_id;