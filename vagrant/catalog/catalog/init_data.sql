/*
	THIS SCRIPT IS ONLY TO BE RUN ONCE ON NEW DATABASE
*/
INSERT INTO user(name, email, picture) VALUES('Robo Barista', 'tinnyTim@udacity.com', 'https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png');


INSERT INTO categories(name) VALUES('Baseball');
INSERT INTO categories(name) VALUES('Basketball');
INSERT INTO categories(name) VALUES('Foosball');
INSERT INTO categories(name) VALUES('Frisbee');
INSERT INTO categories(name) VALUES('Hockey');
INSERT INTO categories(name) VALUES('Rock Climbing');
INSERT INTO categories(name) VALUES('Skating');
INSERT INTO categories(name) VALUES('Snowboarding');
INSERT INTO categories(name) VALUES('Soccer');


INSERT INTO items(user_id, category_id, title, description) VALUES(1, 1, 'Bat', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.');
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 1, 'Ball', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.');

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 2, 'Ball', 'Baseket ball');
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 2, 'Hoops', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.');

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 3, 'Ball', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.');

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 4, 'Frisbee', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Stick', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Puck', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Shoes', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 5, 'Gloves', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Rope', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Shoes', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 6, 'Gloves', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 7, 'Shoes', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Snowboard', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Shoes', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Gloves', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 8, 'Goggles', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );

INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Two shinguards', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Jersey', 'Mostly refered as Kit, the kit in association football, as in a number of other sports, kit refers to the standard equipment and attire worn by players. The terms "kit", "strip", and in North American English "uniform" are used interchangeably.');
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Shinguards', 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.' );
INSERT INTO items(user_id, category_id, title, description) VALUES(1, 9, 'Soccer Cleats', 'Cleats or studs are protrusions on the sole of a shoe, or on an external attachment to a shoe, that provide additional traction on a soft or slippery surface. In American English the term cleats is used synecdochically to refer to shoes featuring such protrusions. This does not happen in British English; the term "studs" is never used to refer to the shoes, which would instead be known as "football boots", "rugby boots", and so on.');

