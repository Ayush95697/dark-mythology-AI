# 🧙 Dark Myth Explorer AI

Unveil the secrets of **dark mythology, folklore, and occult traditions** with this AI-powered exploration tool.  
Built with **Streamlit** and a custom **RAG (Retrieval-Augmented Generation)** backend, this app allows you to ask deep questions about ancient myths, supernatural beings, and esoteric wisdom.

---

## ✨ Features

- 💬 **Interactive Chat** – Ask questions about mythology, folklore, and occult knowledge.  
- 📖 **Source-Aware Responses** – See which texts your answers are derived from.  
- 🎨 **Custom Dark UI** – Aesthetic design with collapsible source sections.  
- ⚙️ **Configurable Settings** – Adjust chunk size, retrieval count, and temperature.  
- 🧹 **Clear Chat History** – Reset conversations anytime.  
- 📚 **Knowledge Base** – Includes mythological texts, folklore collections, and occult sources.  

---

## 🚀 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** Custom RAG pipeline (LLM + Vector Database)  
- **Language:** Python 3.10+  
- **Embeddings & Retrieval:** FAISS / ChromaDB (configurable)  
- **LLM:** OpenAI / Groq / HuggingFace (pluggable backend)  

---

## 📂 Project Structure

```
Dark-Myth-Explorer-AI/
│
├── backend.py # Handles LLM + RAG logic
├── main.py # Streamlit frontend
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

---

## ⚡ Installation

Clone the repository:

```
bash
git clone https://github.com/Ayush95697/dark-myth-explorer-ai.git
cd dark-myth-explorer-ai
```
## Install dependencies:
```
pip install -r requirements.txt

```
## Run the app:
```
Run the app:
```
## 🛠️ Configuration

You can tweak the following settings in the sidebar:

* Chunk Size: Controls text chunking for retrieval.

* Retrieval Count (k): Number of passages to retrieve.

* Temperature: Controls creativity of the LLM output.

## 🎨 UI Preview

<img width="2472" height="1536" alt="image" src="https://github.com/user-attachments/assets/d7e2bce6-b09d-435b-b09e-9c0b0c443155" />
## 📜 Roadmap

* Save/Export Chat History

* Multi-theme support (Dark/Light)

* Knowledge Base Expansion (upload PDFs, URLs)

* Fine-tuned models for mythology-specific QA

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## 📜 License

MIT License © 2025 Ayush Mishra
