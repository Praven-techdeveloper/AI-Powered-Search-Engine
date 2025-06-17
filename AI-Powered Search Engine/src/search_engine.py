import os
import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from .utils import normalize_vectors, save_faiss_index, load_faiss_index
from .data_loader import load_or_create_dataset
from config import MODEL_NAME, DEFAULT_DATASET, EMBEDDINGS_PATH, INDEX_PATH, BATCH_SIZE

class SemanticSearchEngine:
    def __init__(self):
        # Create directories if missing
        os.makedirs(os.path.dirname(EMBEDDINGS_PATH), exist_ok=True)
        os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
        
        # Load dataset
        self.df = load_or_create_dataset(DEFAULT_DATASET)
        self.texts = self.df['title'] + ". " + self.df['content']
        
        # Initialize model
        self.model = SentenceTransformer(MODEL_NAME)
        
        # Load or create embeddings
        self.embeddings = self._load_or_create_embeddings()
        
        # Load or create index
        self.index = self._load_or_create_index()

    def _load_or_create_embeddings(self):
        """Load embeddings from file or generate new"""
        if os.path.exists(EMBEDDINGS_PATH):
            try:
                return np.load(EMBEDDINGS_PATH)
            except:
                print("Error loading embeddings, regenerating...")
        
        print("Generating embeddings...")
        embeddings = []
        
        # Process in batches for memory efficiency
        for i in tqdm(range(0, len(self.texts), BATCH_SIZE), desc="Embedding documents"):
            batch = self.texts.iloc[i:i+BATCH_SIZE].tolist()
            embeddings.append(self.model.encode(batch))
        
        embeddings = np.vstack(embeddings)
        np.save(EMBEDDINGS_PATH, embeddings)
        return embeddings

    def _load_or_create_index(self):
        """Load FAISS index or build new"""
        index = load_faiss_index(INDEX_PATH)
        if index:
            return index
        
        print("Building FAISS index...")
        dimension = self.embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)  # Inner Product for cosine similarity
        
        # Normalize embeddings
        normalized_embeddings = normalize_vectors(self.embeddings)
        index.add(normalized_embeddings)
        
        if save_faiss_index(index, INDEX_PATH):
            print("Index saved successfully")
        return index

    def search(self, query, top_k=TOP_K_RESULTS, category_filter=None):
        """Perform semantic search with optional filtering"""
        # Encode query
        query_embedding = self.model.encode([query])
        query_embedding = normalize_vectors(query_embedding)
        
        # Search index
        scores, indices = self.index.search(query_embedding, top_k)
        
        # Format results with optional filtering
        results = []
        for i in range(top_k):
            idx = indices[0][i]
            if idx < 0:  # FAISS returns -1 for invalid indices
                continue
                
            doc = self.df.iloc[idx]
            
            # Apply category filter
            if category_filter and doc['category'] != category_filter:
                continue
                
            results.append({
                "id": doc['id'],
                "title": doc['title'],
                "content": doc['content'][:300] + "..." if len(doc['content']) > 300 else doc['content'],
                "category": doc['category'],
                "score": float(scores[0][i])
            })
        
        return results

    def add_document(self, title, content, category="General"):
        """Add new document and update index"""
        # Add to dataset
        success, new_id = add_document_to_dataset(title, content, category)
        if not success:
            return False, "Failed to add to dataset"
        
        # Generate embedding
        text = f"{title}. {content}"
        new_embedding = self.model.encode([text])
        new_embedding = normalize_vectors(new_embedding)
        
        # Update embeddings array
        self.embeddings = np.vstack([self.embeddings, new_embedding])
        np.save(EMBEDDINGS_PATH, self.embeddings)
        
        # Update index
        self.index.add(new_embedding)
        save_faiss_index(self.index, INDEX_PATH)
        
        return True, new_id

    def get_categories(self):
        """Get unique categories for filtering"""
        return self.df['category'].unique().tolist()