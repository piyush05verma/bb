sales = LOAD '/user/230968114/lab5/sales.csv'
USING PigStorage(',')
AS (order_id:int, product:chararray, category:chararray, amount:int);

sorted_sales = ORDER sales BY amount DESC;

top3 = LIMIT sorted_sales 3;

DUMP top3;
