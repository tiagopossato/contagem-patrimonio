SELECT item_id, Count(*) FROM app_inventario
GROUP BY item_id
HAVING Count(*) > 1;
