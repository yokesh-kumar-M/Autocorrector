# 📝 Django AutoCorrector

A simple Django-based web application that automatically corrects spelling mistakes in user input using the **TextBlob** library.

---

## 🔍 Features

- ✅ Takes input from a text area
- ✅ Applies automatic spelling correction
- ✅ Displays corrected output on the same page
- ✅ Simple and clean interface
- ✅ Built with Django & TextBlob

---

## 🛠️ Tech Stack

- **Backend:** Django (Python Web Framework)
- **Spell Correction:** TextBlob
- **Frontend:** HTML (basic Django templates)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Autocorrector.git
cd Autocorrector
python -m venv .venv
.venv\Scripts\activate  # Windows

# or

source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python -m textblob.download_corpora
python manage.py runserver

autocorrector/
├── autocorrector/        # Django project settings
├── corrector/            # Main app
│   ├── templates/
│   │   └── corrector/
│   │       └── home.html
├── manage.py
├── requirements.txt
└── README.md
```

