sales = LOAD '/user/230968114/lab5/sales.csv'
USING PigStorage(',')
AS (order_id:int, product:chararray, category:chararray, amount:int);

customers = LOAD '/user/230968114/lab5/customers.csv'
USING PigStorage(',')
AS (order_id:int, name:chararray, city:chararray);

joined = JOIN sales BY order_id, customers BY order_id;

DUMP joined;
