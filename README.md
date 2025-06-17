
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


Configuration ⚙️
Edit config.py to customize:

python
MODEL_NAME = "all-MiniLM-L6-v2"       # Sentence-BERT model
DEFAULT_DATASET = "data/knowledge_base.csv"
EMBEDDINGS_PATH = "data/embeddings.npy"
INDEX_PATH = "data/faiss_index.bin"
BATCH_SIZE = 128                      # Embedding generation batch size
TOP_K_RESULTS = 10                    # Default number of results
Adding Your Data 📊
Supported Formats
CSV Files: Must contain columns: id, title, content, category

JSON Files: Array of objects with same fields

PDF Documents: Automatically convert using included utility

Dataset Sources
Wikipedia Dataset

Arxiv Papers

BBC News Summary

Your custom documents (PDF, TXT, DOCX)

Convert PDF to CSV
python
from PyPDF2 import PdfReader
import pandas as pd

def pdf_to_csv(pdf_path, csv_path):
    reader = PdfReader(pdf_path)
    data = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text().replace('\n', ' ')
        data.append({"id": i+1, "title": f"Page {i+1}", "content": text, "category": "PDF"})
    pd.DataFrame(data).to_csv(csv_path, index=False)



Deployment 🚢
Docker
bash
docker build -t semantic-search .
docker run -p 5000:5000 semantic-search
Cloud Platforms
AWS:

bash
eb init -p python-3.10 semantic-search
eb create prod-env
Google Cloud Run:

bash
gcloud run deploy semantic-search --source .
Azure App Service:

bash
az webapp up --runtime PYTHON:3.10 --sku F1
Troubleshooting 🐛
Issue	Solution
ModuleNotFoundError	Run pip install -r requirements.txt
FAISS load error	Reinstall with pip install faiss-cpu --no-cache
No results	Check dataset path in config.py
Slow performance	Use GPU version: pip install faiss-gpu
Port conflict	Change port in api.py: app.run(port=5001)


Future Enhancements 🔮
User authentication system

Real-time collaborative editing

Multi-language support

Automated dataset crawling

Search history and analytics

Hybrid keyword-semantic search



Contributing 🤝
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -am 'Add some feature')

Push to the branch (git push origin feature/your-feature)

Open a pull request



License 📄
This project is licensed under the MIT License - see the LICENSE file for details.








Built with ❤️ by [PRAVEN] | GitHub Profile






