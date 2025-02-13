SELECT 
    ROUND(
        (SUM(CASE WHEN customer_pref_delivery_date = order_date THEN 1 ELSE 0 END) / 
        COUNT(*)) * 100, 
    2) AS immediate_percentage
FROM 
    Delivery
WHERE 
    (customer_id, order_date) IN (
        SELECT 
            customer_id, 
            MIN(order_date) AS first_order_date
        FROM 
            Delivery
        GROUP BY 
            customer_id
    );