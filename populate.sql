INSERT INTO tweets_action_type (id, name) VALUES (1, 'reply');
INSERT INTO tweets_action_type (id, name) VALUES (2, 'retweet');
INSERT INTO tweets_action_type (id, name) VALUES (3, 'like');
INSERT INTO tweets_action_type (id, name) VALUES (4, 'share');
INSERT INTO tweets_action_type (id, name) VALUES (5, 'follow');
INSERT INTO tweets_action_type (id, name) VALUES (6, 'block');
INSERT INTO tweets_action_type (id, name) VALUES (7, 'make_a_post');
INSERT INTO tweets_post (id, content) VALUES (1, 'Nope. The COVID-19 vaccine does not contain fetal cells. A fetal cell line, or copies of a primary cell dating back to an abortion or miscarriage in 1973, was used in testing the efficacy of the vaccine.');
INSERT INTO tweets_post (id, content) VALUES (2, 'False. A viral message spread primarily through WhatsApp claimed that an image file with the name “Mexico did it” was about to be shared online and was a vehicle for malware that would quickly wreak havoc on users’ cellphones.');
INSERT INTO tweets_post (id, content) VALUES (3, ' False. What the legislation does is significantly lower the threshold for reporting taxable transactions made using cash apps like Venmo, PayPal, or Zelle for goods and services to the IRS.');

INSERT INTO tweets_configuration (id, configName, space_for_comment, space_for_creat_post, user_picture, reply_button, like_button, share_button, block_button, follow_button, retweet_button,posts_number, lower_limit_interaction, upper_limit_interaction) VALUES (1, 'default', 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,2, 20,50);
INSERT INTO tweets_environment (id, configuration_id) VALUES (1, 1);

INSERT INTO tweets_hashtag (id, hashtag, post_id) VALUES (1, 'Fake', 1 );
INSERT INTO tweets_hashtag (id, hashtag, post_id) VALUES (2, 'FAKE', 1 );

INSERT INTO tweets_hashtag (id, hashtag, post_id) VALUES (3, 'fake-new', 2 );
INSERT INTO tweets_hashtag (id, hashtag, post_id) VALUES (4, 'FAKE-NEW', 2 );

INSERT INTO tweets_image (id, imagepath, post_id) VALUES (1, 'twitter.jpg', 2 );
