
INSERT INTO categories (name) VALUES ('Ноутбуки') ON CONFLICT DO NOTHING;
INSERT INTO categories (name) VALUES ('Аксессуары') ON CONFLICT DO NOTHING;


INSERT INTO items (category_id, name, description, price) VALUES
((SELECT id FROM categories WHERE name='Ноутбуки'), 'Ноутбук A', 'Игровой ноутбук', 80000.00),
((SELECT id FROM categories WHERE name='Ноутбуки'), 'Ноутбук B', 'Ультрабук', 120000.00),
((SELECT id FROM categories WHERE name='Аксессуары'), 'Мышь', 'Оптическая мышь', 1500.00)
ON CONFLICT DO NOTHING;

