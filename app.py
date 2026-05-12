from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DB_PATH = "bookings.db"

# --- Database setup ---
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            package TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            notes TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    required = ["name", "email", "package", "start_date"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Το πεδίο '{field}' είναι υποχρεωτικό."}), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO bookings (name, email, phone, package, start_date, end_date, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data.get("phone", ""),
        data["package"],
        data["start_date"],
        data.get("end_date", ""),
        data.get("notes", "")
    ))
    booking_id = c.lastrowid
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "booking_id": booking_id,
        "message": f"Η κράτησή σου #{booking_id} καταχωρήθηκε! Θα επικοινωνήσουμε σύντομα."
    }), 201

# Admin: δες όλες τις κρατήσεις (προστάτεψε με password αν θες)
@app.route("/admin/bookings")
def admin_bookings():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM bookings ORDER BY created_at DESC")
    rows = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    init_db()
    if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
