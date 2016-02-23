/*
	THIS SCRIPT IS ONLY TO BE RUN ONCE ON NEW DATABASE
*/


INSERT INTO categories(name) VALUES('Soccer');
INSERT INTO categories(name) VALUES('Basketball');
INSERT INTO categories(name) VALUES('Baseball');
INSERT INTO categories(name) VALUES('Frisbee');
INSERT INTO categories(name) VALUES('Snowboarding');
INSERT INTO categories(name) VALUES('Rock Climbing');
INSERT INTO categories(name) VALUES('Foosball');
INSERT INTO categories(name) VALUES('Skating');
INSERT INTO categories(name) VALUES('Hockey');


INSERT INTO items(title, description, category_id) VALUES('Soccer Cleats', 'Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions. This does not happen in British English; the term "studs" is never used to refer to the shoes, which would instead be known as "football boots", "rugby boots", and so on.', (SELECT ID FROM categories WHERE name = 'Soccer') );
INSERT INTO items(title, description, category_id) VALUES('Jersey', 'Mostly refered as Kit, the kit in association football, as in a number of other sports, kit refers to the standard equipment and attire worn by players. The terms "kit", "strip", and in North American English "uniform" are used interchangeably.', (SELECT ID FROM categories WHERE name = 'Soccer') );
INSERT INTO items(title, description, category_id) VALUES('Bat', '', (SELECT ID FROM categories WHERE name = 'Baseball') );
INSERT INTO items(title, description, category_id) VALUES('Frisbee', '', (SELECT ID FROM categories WHERE name = 'Frisbee') );
INSERT INTO items(title, description, category_id) VALUES('Shinguards', '', (SELECT ID FROM categories WHERE name = 'Soccer') );
INSERT INTO items(title, description, category_id) VALUES('Two shinguards', '', (SELECT ID FROM categories WHERE name = 'Soccer') );
INSERT INTO items(title, description, category_id) VALUES('Snowboard', '', (SELECT ID FROM categories WHERE name = 'Snowboarding') );
INSERT INTO items(title, description, category_id) VALUES('Goggles', '', (SELECT ID FROM categories WHERE name = 'Snowboarding') );
INSERT INTO items(title, description, category_id) VALUES('Stick', '', (SELECT ID FROM categories WHERE name = 'Hockey') );

