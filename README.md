
AI Semantic Search Engine 🔍
https://img.shields.io/badge/python-3.8%252B-blue
https://img.shields.io/badge/license-MIT-green

An AI-powered semantic search engine that understands the meaning behind your queries. Built with Sentence-BERT for embeddings and FAISS for efficient similarity search.

Features ✨
Semantic Understanding: Finds documents based on meaning, not just keywords

Web Interface: Modern, responsive UI for searching and adding documents

Category Filtering: Filter results by custom categories

Document Management: Add new documents through the web interface

Persistent Storage: Automatically saves embeddings and indexes

Scalable Architecture: Ready for deployment to production environments

Tech Stack 🛠️
Natural Language Processing: Sentence-BERT (all-MiniLM-L6-v2)

Vector Search: FAISS (Facebook AI Similarity Search)

Web Framework: Flask

Frontend: HTML5, CSS3, JavaScript

Data Handling: Pandas, NumPy


Installation 💻
Prerequisites
Python 3.8+

pip package manager

Steps
Clone the repository:

bash
git clone https://github.com/your-username/ai-semantic-search.git
cd ai-semantic-search
Create and activate a virtual environment:

bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Set up the knowledge base:

bash
# Create data directory
mkdir data

# Create sample dataset
echo "id,title,content,category" > data/knowledge_base.csv
echo '1,"Quantum Computing","Quantum computers use qubits instead of classical bits...","AI"' >> data/knowledge_base.csv
echo '2,"Neural Networks","Neural networks are computational models inspired by the human brain...","ML"' >> data/knowledge_base.csv
echo '3,"Transformers","Transformer architecture revolutionized NLP with attention mechanisms...","NLP"' >> data/knowledge_base.csv
Run the application:

bash
cd src
python api.py
Access the web interface at: http://localhost:5000

Usage 🚀
Web Interface
Search: Enter any query in natural language

Filter: Use category dropdown to filter results

Add Documents: Click "Add New Document" to expand knowledge base

View Results: See relevant documents with similarity scores

API Endpoints
GET /search?q=query&category=filter: Search endpoint

json
{
  "query": "machine learning models",
  "category_filter": "ML",
  "processing_time": "0.215s",
  "results": [
    {
      "id": 2,
      "title": "Neural Networks",
      "content": "Neural networks are computational models...",
      "category": "ML",
      "score": 0.872
    }
  ]
}
POST /add-document: Add new document

json
{
  "title": "New Document Title",
  "content": "Document content...",
  "category": "New Category"
}
