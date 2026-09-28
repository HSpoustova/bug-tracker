import sqlite3
from datetime import datetime
from pathlib import Path

SCHEMA = Path(__file__).parent / "schema.sql"


class BugRepository:

    def __init__(self, path):
        self.path = path
        with self._connect() as db:
            db.executescript(SCHEMA.read_text(encoding="utf-8"))

    def _connect(self):
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        return db

    @staticmethod
    def _now():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add(self, data):
        now = self._now()
        with self._connect() as db:
            cursor = db.execute(
                "INSERT INTO bugs (name, steps, expected, actual, severity, priority, status, created, updated)"
                " VALUES (?, ?, ?, ?, ?, ?, 'new', ?, ?)",
                (
                    data["name"].strip(),
                    data.get("steps", ""),
                    data.get("expected", ""),
                    data.get("actual", ""),
                    data["severity"],
                    data["priority"],
                    now,
                    now,
                ),
            )

        return cursor.lastrowid