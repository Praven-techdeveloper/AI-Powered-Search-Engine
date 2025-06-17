import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_NAME = "all-MiniLM-L6-v2"
DEFAULT_DATASET = os.path.join(BASE_DIR, "data", "knowledge_base.csv")
EMBEDDINGS_PATH = os.path.join(BASE_DIR, "data", "embeddings.npy")
INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.bin")
BATCH_SIZE = 128
TOP_K_RESULTS = 10