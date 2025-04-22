# 🩺 Medical Chatbot - Generative AI

An end-to-end conversational AI assistant built using **LangChain**, **OpenAI GPT**, **Pinecone**, and **Flask** — tailored for medical domain interactions. It intelligently understands and answers user queries by leveraging LLMs and vector search.

---

## 🚀 Features

- Chatbot powered by GPT (via OpenAI)
- Embedding-based document retrieval with Pinecone
- Flask backend for web deployment
- Supports custom medical knowledge base
- Built with LangChain for modular and powerful LLM chaining

---

## 🧰 Tech Stack

- **Python 3.10**
- **LangChain**
- **OpenAI GPT-3.5 / GPT-4**
- **Pinecone Vector DB**
- **Flask** (Web server)
- **Conda** (for virtual environment)

---

## 📦 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Medical-Chatbot-Gen-AI.git
cd Medical-Chatbot-Gen-AI

### ✅ Step 2: Create and Activate Conda Environment

Run the following command to **create a new environment**:

```bash
conda create -n medbot python=3.10 -y


### 📥 Step 3: Install Requirements

```bash
pip install -r requirements.txt

### 🔐 Step 4: Set Up Environment Variables

OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

### 🧠 Step 5: Generate and Store Embeddings in Pinecone

```bash
python store_index.py

This script:

Loads your data (from the data/ folder)

Converts it into embeddings

Stores it in Pinecone vector DB

### 🚀 Step 6: Run the Application

```bash
python app.py

Once the server is running, open your browser and go to:
http://localhost:5000



    
