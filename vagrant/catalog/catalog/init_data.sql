/*
	THIS SCRIPT IS ONLY TO BE RUN ONCE ON NEW DATABASE
*/


INSERT INTO categories(name) VALUES('Baseball');
INSERT INTO categories(name) VALUES('Basketball');
INSERT INTO categories(name) VALUES('Foosball');
INSERT INTO categories(name) VALUES('Frisbee');
INSERT INTO categories(name) VALUES('Hockey');
INSERT INTO categories(name) VALUES('Rock Climbing');
INSERT INTO categories(name) VALUES('Skating');
INSERT INTO categories(name) VALUES('Snowboarding');
INSERT INTO categories(name) VALUES('Soccer');


INSERT INTO items(user_id, category_id, title, description) VALUES(1, 1, 'Bat', '') );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 1, 'Ball', '') );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 2, 'Ball', 'Baseket ball') );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 2, 'Hoops', '') );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 3, 'Ball', '') );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 4, 'Frisbee', '' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Stick', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Puck', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Shoes', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Gloves', '' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Rope', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Shoes', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Gloves', '' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 7, 'Shoes', '' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Snowboard', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Shoes', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Gloves', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Goggles', '' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Two shinguards', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Jersey', 'Mostly refered as Kit, the kit in association football, as in a number of other sports, kit refers to the standard equipment and attire worn by players. The terms "kit", "strip", and in North American English "uniform" are used interchangeably.');
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Shinguards', '' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Soccer Cleats', 'Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions. This does not happen in British English; the term "studs" is never used to refer to the shoes, which would instead be known as "football boots", "rugby boots", and so on.') );

