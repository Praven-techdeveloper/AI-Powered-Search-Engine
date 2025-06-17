from sentence_transformers import SentenceTransformer
import numpy as np

print("Testing Sentence Transformers...")
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(["test sentence"])
print(f"Embeddings shape: {embeddings.shape}")
print("Test successful!")

print("\nTesting FAISS...")
import faiss
dimension = 384
index = faiss.IndexFlatL2(dimension)
index.add(np.random.rand(10, dimension).astype('float32'))
print(f"Index contains {index.ntotal} vectors")
print("FAISS test successful!")