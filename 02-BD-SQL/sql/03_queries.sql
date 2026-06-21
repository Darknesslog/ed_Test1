SELECT * FROM categories;


SELECT * FROM items;


SELECT i.id, i.name, c.name AS category, i.price, i.created_at
FROM items i
JOIN categories c ON i.category_id = c.id;


SELECT c.name AS category, COUNT(i.id) AS items_count, ROUND(AVG(i.price),2) AS avg_price
FROM categories c
LEFT JOIN items i ON i.category_id = c.id
GROUP BY c.name
ORDER BY c.name;


INSERT INTO items (category_id, name, description, price)
VALUES ((SELECT id FROM categories WHERE name='Аксессуары'), 'Коврик для мыши', 'Большой коврик', 700.00);


UPDATE items SET price = price * 0.95 WHERE name ILIKE '%ноутбук%';


DELETE FROM items WHERE name = 'Коврик для мыши';

