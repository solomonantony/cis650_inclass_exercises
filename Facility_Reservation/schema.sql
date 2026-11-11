CREATE TABLE IF NOT EXISTS customers (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS reservations (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    room        TEXT NOT NULL,
    request_date  date NOT NULL,          -- 'YYYY-MM-DD HH:MM'
    assigned_date date TEXT,
    attendees   INTEGER NOT NULL CHECK (attendees > 0),
    status      TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
