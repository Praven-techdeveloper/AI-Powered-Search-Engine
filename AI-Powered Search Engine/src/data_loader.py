import pandas as pd
import os
from config import DEFAULT_DATASET

def load_or_create_dataset(path=DEFAULT_DATASET):
    """Load dataset or create sample if none exists"""
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            print(f"Loaded dataset with {len(df)} documents")
            return df
        except Exception as e:
            print(f"Error loading dataset: {e}")
    
    # Create sample dataset
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'title': [
            "Quantum Computing Basics",
            "Introduction to Neural Networks",
            "Transformer Models Explained",
            "Reinforcement Learning Fundamentals",
            "Generative AI Overview"
        ],
        'content': [
            "Quantum computers use qubits instead of classical bits to perform calculations...",
            "Neural networks are computational models inspired by the human brain's structure...",
            "Transformer architecture revolutionized NLP with its attention mechanism...",
            "Reinforcement learning involves agents learning to make decisions through rewards...",
            "Generative AI creates new content by learning patterns from existing data..."
        ],
        'category': ["AI", "ML", "NLP", "ML", "AI"]
    }
    
    df = pd.DataFrame(sample_data)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
        print(f"Created sample dataset at {path}")
    except Exception as e:
        print(f"Error creating dataset: {e}")
    
    return df

def add_document_to_dataset(title, content, category="General", path=DEFAULT_DATASET):
    """Add new document to dataset"""
    try:
        df = pd.read_csv(path)
        new_id = df['id'].max() + 1 if not df.empty else 1
        new_row = pd.DataFrame([{
            'id': new_id,
            'title': title,
            'content': content,
            'category': category
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(path, index=False)
        return True, new_id
    except Exception as e:
        print(f"Error adding document: {e}")
        return False, None