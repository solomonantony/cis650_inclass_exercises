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
    start_time  TEXT NOT NULL,          -- 'YYYY-MM-DD HH:MM'
    end_time    TEXT NOT NULL,
    attendees   INTEGER NOT NULL CHECK (attendees > 0),
    status      TEXT NOT NULL DEFAULT 'booked' CHECK (status IN ('booked','cancelled')),
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
