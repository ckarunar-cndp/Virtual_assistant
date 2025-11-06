# 🤖 Virtual Assistant — AI-Powered Multi-Tab Streamlit App

An AI-powered **Virtual Assistant** built with Streamlit to automate tasks like OCR-based document parsing, email support, data visualization, and intelligent summarization.  
Designed for startups and data teams looking for an all-in-one productivity and analytics solution.

---

## 🚀 Key Features

### 🧾 OCR Tab
- Upload invoices, receipts, or notes in `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`, or `.webp`
- Automatically extract store name, date, subtotal, tax, total, and line items
- Supports two OCR modes:
  - **EasyOCR** — lightweight and fast
  - **Hugging Face TrOCR** — transformer-based OCR for higher accuracy
- Download extracted and structured data as `.txt` or JSON

### ✉️ Email Drafting Tab
- Generate well-structured email drafts from short prompts
- Supports tone, audience, and formatting customization
- One-click copy/export

### 🧠 Summarization Tab
- Upload `.txt`, `.pdf`, or `.docx` files
- Generate short or detailed AI summaries
- Download summarized text instantly

### ✍️ Editorial Support Tab
- AI-powered rewriting, paraphrasing, and grammar enhancement
- Upload documents and get refined, professional versions ready to use

### Coming soon--------------------------
### 📊 Dashboard Tab
- Visualize metrics and trends with **Plotly**, **Matplotlib**, and **Seaborn**
- Compare KPIs and explore data interactively

### 💬 Chatbot & FAQ Tabs
- In-app **virtual assistant** for general or contextual Q&A
- Dynamic **FAQ** section with collapsible answers
- Optional backend integration via FastAPI for expansion

---

## 🧩 Tech Stack

| Layer | Tools / Libraries |
|-------|--------------------|
| Frontend | Streamlit |
| OCR | EasyOCR, Hugging Face TrOCR |
| ML/NLP | Transformers, Scikit-learn |
| Visualization | Plotly, Matplotlib, Seaborn |
| Document Handling | Pillow, OpenCV, pdf2image |
| Backend (optional) | FastAPI, Docker |
| Cloud (future) | Azure / GCP / Snowflake Integration |

---

## 🗂️ Folder Structure

