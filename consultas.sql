SELECT item_id, Count(*) FROM app_inventario
GROUP BY item_id
HAVING Count(*) > 1;

SELECT Count(*) FROM app_inventario WHERE aferidores LIKE '%ana%';


SELECT Count(*) FROM app_dependenciasetor WHERE bloco_id != '';

delete FROM app_dependenciasetor WHERE bloco_id != '';

