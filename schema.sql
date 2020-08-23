CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    level INTEGER,
    confirmed BOOLEAN,
    role INTEGER
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    level INTEGER,
    max INTEGER NOT NULL,
    date DATE NOT NULL,
    time INTEGER NOT NULL,
    teacher_id INTEGER REFERENCES users(id)
);

CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    times INTEGER,
    bought DATE,
    user_id INTEGER REFERENCES users(id)
);

CREATE TABLE users_lessons (
    user_id INTEGER REFERENCES users(id),
    lesson_id INTEGER REFERENCES lessons(id)
);