CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT,
    email TEXT,
    level INTEGER,
    confirmed BOOLEAN,
    teacher BOOLEAN,
    admin BOOLEAN
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    level INTEGER,
    max INTEGER,
    time DATETIME,
    active BOOLEAN
);

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    valid DATETIME
);