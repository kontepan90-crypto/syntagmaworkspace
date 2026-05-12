# Syntagma Workspace — Booking App

## Τοπική εκτέλεση

```bash
pip install -r requirements.txt
python app.py
# Άνοιξε http://localhost:5000
```

## Deploy στο Railway (δωρεάν)

1. Δημιούργησε λογαριασμό στο https://railway.app
2. "New Project" → "Deploy from GitHub"
3. Ανέβασε τα αρχεία σε GitHub repo
4. Το Railway ανιχνεύει αυτόματα Python + Procfile
5. Σε λίγα λεπτά έχεις live URL!

## Δες τις κρατήσεις (admin)

GET /admin/bookings  →  επιστρέφει JSON με όλες τις κρατήσεις

## Δομή project

```
syntagmaworkspace/
├── app.py              # Flask backend
├── templates/
│   └── index.html      # Frontend
├── requirements.txt
├── Procfile            # Για Railway/Render
└── bookings.db         # Δημιουργείται αυτόματα
```

## Επόμενα βήματα (προαιρετικά)

- Email επιβεβαίωσης με Flask-Mail
- Admin panel με password
- Export κρατήσεων σε Excel
- Ενοποίηση με Google Calendar
