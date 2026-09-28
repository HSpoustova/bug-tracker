
-- One table for all bugs

Create table if not exists bugs (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT NOT NULL,
    steps TEXT,
    expected TEXT,
    actual TEXT,
    severity TEXT NOT NULL,
    priority TEXT NOT NULL,
    status    TEXT NOT NULL DEFAULT 'new',
    created TEXT NOT NULL,
    updated TEXT NOT NULL

);