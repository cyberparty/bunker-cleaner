DROP DATABASE IF EXISTS bunkerbot;
CREATE DATABASE bunkerbot;
USE bunkerbot;

CREATE TABLE quotes(
	user_id BIGINT,
	quote_text TEXT,
	quote_id INT,
	grabber_id BIGINT,
	time_grabbed DATETIME,

	PRIMARY KEY (quote_id)
);

