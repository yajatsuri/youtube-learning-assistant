<div align="center">

# 🎓 YouTube Learning Assistant

**Transform any YouTube video into structured learning material — powered by Gemini AI**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)

[![Live Demo]](https://youtube-learning-assistant-frontend-c92b.onrender.com)

</div>

---

## 🌐 Live Demo

**[youtube-learning-assistant-frontend-c92b.onrender.com](https://youtube-learning-assistant-frontend-c92b.onrender.com)**

> ⚠️ Hosted on Render's free tier — may take 30–60 seconds to wake up on first load.

---

## 🧠 What It Does

Paste a YouTube URL → get back three things instantly:

| Output | Description |
|---|---|
| 📋 Executive Summary | Concise overview of the entire video |
| 📝 Detailed Notes | Structured, topic-wise breakdown of the content |
| 💡 Key Takeaways | Bullet-point insights for quick revision |

All results are persisted to PostgreSQL so you can revisit notes without re-processing.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js, TypeScript, Tailwind CSS |
| **Backend** | FastAPI, Python, Pydantic, SQLAlchemy |
| **AI Model** | Gemini 2.5 Flash (Google AI) |
| **Transcripts** | Supadata API |
| **Database** | PostgreSQL |
| **DevOps** | Docker |

---

## 🏗️ Architecture

```
User (Browser)
      │
      ▼
Next.js Frontend
      │  REST API calls
      ▼
FastAPI Backend
      ├──► Supadata API        →  Extract transcript + video metadata
      ├──► Gemini 2.5 Flash   →  Generate Summary / Notes / Takeaways
      └──► PostgreSQL (ORM)   →  Persist and retrieve results
```

---

## 📂 Project Structure

```
youtube-learning-assistant/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   │   └── youtube.py
│   ├── services/
│   │   ├── transcript_service.py   # Supadata API integration
│   │   ├── llm_service.py          # Gemini prompt-engineered calls
│   │   └── notes_service.py
│   ├── schemas/
│   │   ├── notes_schema.py
│   │   └── video_schema.py
│   ├── models/                     # SQLAlchemy ORM models
│   ├── database/
│   └── Dockerfile
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── lib/
│
├── docker-compose.yml
└── README.md
```

---


## 🔮 Roadmap

- [ ] **Chat with Video** — conversational Q&A using RAG over transcripts
- [ ] **Quiz Generation** — auto-generate MCQs for active recall
- [ ] **PDF Export** — download notes as formatted PDF
- [ ] **User Authentication** — personal note libraries
- [ ] **pgvector Integration** — semantic search over past videos

---

<div align="center">
Built by <a href="https://github.com/yajatsuri">Yajat Suri</a>
</div>
