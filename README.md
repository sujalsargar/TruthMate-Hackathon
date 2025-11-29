# TruthMate –  News Detection System

TruthMate is a simple  News Detection System built using **HTML, CSS, JavaScript (Frontend)** and **Python + Flask (Backend)**.

Users can enter any news text, and the backend analyzes it to determine whether the news is **Real**, **Fake**, or **Unverified**, along with a confidence score and explanation.

---

## 📂 Project Structure

```
truthmate-app/
│
├── truthmate-frontend/
│   └── index.html        # Main UI (HTML + CSS + JS)
│
└── truthmate-backend/              # Flask backend folder (use your actual folder name)
    ├── app.py            # Flask server file
    ├── ...other .py files (logic, model, utilities)
```

---

## 🚀 How to Run the Project

TruthMate has **two parts** that must run together:  
1️⃣ Backend (Flask)  
2️⃣ Frontend (HTML/JS)

---

## 1️⃣ Start the Flask Backend

1. Open terminal and go to your backend folder:

```bash
cd truthmate-app/backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Flask server:

```bash
python app.py
```

Your backend will run at:

```
http://localhost:5000
```

---

## 2️⃣ Start the Frontend

Go to:

```
truthmate-frontend/index.html
```

You can open it in two ways:

### ✔ Option A – Open directly  
Double-click `index.html`.

### ✔ Option B – Open with VS Code Live Server (Recommended)

1. Open the folder in VS Code  
2. Install **Live Server**  
3. Right‑click `index.html` → **Open with Live Server**

Frontend will usually run at:

```
http://127.0.0.1:5500
```

---

## 🔌 Frontend → Backend Communication

Your JavaScript sends text to the Python backend:

```js
fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: userInput })
})
.then(response => response.json())
```

Flask backend returns a JSON response:

```json
{
  "status": "Fake / Real / Unverified",
  "confidence": 82,
  "message": "Detailed explanation of the result"
}
```

---

## 🎯 Features

- Detects Fake, Real, or Unverified news
- Confidence score from backend
- Lightweight and fast
- Simple frontend interface
- Easy to modify and extend

---

## 🛠 Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- Flask  

---

## 📝 Customization

### Change UI  
Edit:
```
truthmate-frontend/index.html
```

### Change backend logic  
Modify:
```
backend/app.py
backend/*.py
```

---

## 📄 License
This project is for educational and development use.

---

## 👍 Support
If you need:
- Deployment help  
- Mobile app conversion  
- Backend improvements  
- UI enhancements  

Just ask!
