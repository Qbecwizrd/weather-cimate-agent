# 🌤️ Weather Journal API + 🌐 Climate Agent Module

A modular FastAPI backend that not only records weather journal entries but also includes an **LLM-powered climate research agent**. It reads, scrapes, embeds, and answers real-world climate questions like an intelligent assistant 🔍🧠

---

## 🚀 Features

### 📝 Weather Journal API
- Log daily weather entries (`location`, `temperature`, `description`)
- Fetch past weather logs
- Uses SQLite + SQLAlchemy for local DB storage

### 🌐 Climate Agent AI
- Ingests data from real web sources
- Embeds documents into a vector DB for search
- Uses LangChain + OpenAI/HuggingFace to answer climate questions
- Agentic reasoning with support for summaries, citations, and multi-step queries

---

## 📁 Folder Structure

