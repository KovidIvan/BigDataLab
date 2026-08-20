SELECT 
    first_name || ' ' || last_name AS full_name,
    country,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_amount
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name, c.country
HAVING 
    COUNT(o.order_id) >= 2                       -- условие 1: минимум 2 заказа
    AND EXISTS (                                 -- условие 2: хотя бы одна доставка со статусом 'Delivered'
        SELECT 1 
        FROM shippings s 
        WHERE s.customer = c.customer_id 
            AND s.status = 'Delivered'
    )
ORDER BY 
    full_name;