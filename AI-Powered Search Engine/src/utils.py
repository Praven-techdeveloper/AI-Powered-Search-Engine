import os
import numpy as np
import faiss

def normalize_vectors(vectors):
    """Normalize vectors for cosine similarity"""
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1e-10  # Avoid division by zero
    return vectors / norms

def save_faiss_index(index, path):
    """Save FAISS index with error handling"""
    try:
        faiss.write_index(index, path)
        return True
    except Exception as e:
        print(f"Error saving index: {e}")
        return False

def load_faiss_index(path):
    """Load FAISS index with error handling"""
    try:
        return faiss.read_index(path)
    except Exception as e:
        print(f"Error loading index: {e}")
        return None