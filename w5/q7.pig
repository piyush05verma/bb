sales = LOAD '/user/230968114/lab5/sales.csv'
USING PigStorage(',')
AS (order_id:int, product:chararray, category:chararray, amount:int);

filtered = FILTER sales BY amount > 5000;

STORE filtered INTO '/user/230968114/lab5/output5' USING PigStorage(',');
