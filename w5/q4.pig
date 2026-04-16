sales = LOAD '/user/230968114/lab5/sales.csv'
USING PigStorage(',')
AS (order_id:int, product:chararray, category:chararray, amount:int);

grp = GROUP sales BY category;

total = FOREACH grp GENERATE group AS category, SUM(sales.amount) AS total_sales;

DUMP total;
