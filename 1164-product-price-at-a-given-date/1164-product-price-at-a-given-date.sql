
Select distinct product_id, new_price as price
From Products
Where (product_id, change_date) in (Select product_id, max(change_date) From Products where change_date<='2019-08-16' group by product_id)
union all
Select product_id, 10 as price
from products 
group by product_id
having min(change_date)>'2019-08-16'