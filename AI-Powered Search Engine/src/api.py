# Add to the top of api.py
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request, jsonify, render_template, redirect, url_for
from .search_engine import SemanticSearchEngine
import time

app = Flask(__name__)
engine = SemanticSearchEngine()

@app.route('/')
def home():
    return render_template('search.html', categories=engine.get_categories())

@app.route('/search')
def search():
    query = request.args.get('q', '')
    category = request.args.get('category', '')
    start_time = time.time()
    
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    results = engine.search(query, category_filter=category if category else None)
    search_time = time.time() - start_time
    
    return jsonify({
        "query": query,
        "category_filter": category,
        "processing_time": f"{search_time:.3f}s",
        "results": results
    })

@app.route('/add-document', methods=['GET', 'POST'])
def add_document():
    if request.method == 'POST':
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        category = request.form.get('category', 'General')
        
        if not title or not content:
            return render_template('add_document.html', 
                                  error="Title and content are required",
                                  categories=engine.get_categories())
        
        success, doc_id = engine.add_document(title, content, category)
        if success:
            return redirect(url_for('document_added', doc_id=doc_id))
        else:
            return render_template('add_document.html', 
                                  error="Failed to add document",
                                  categories=engine.get_categories())
    
    return render_template('add_document.html', 
                          categories=engine.get_categories(),
                          error=None)

@app.route('/document-added/<int:doc_id>')
def document_added(doc_id):
    return render_template('document_added.html', doc_id=doc_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)