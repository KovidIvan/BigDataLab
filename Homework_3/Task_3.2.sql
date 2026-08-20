SELECT
	item,
	count (*) as item_count,
	avg(amount) as avg_amount
FROM 
	orders
GROUP BY 
	item