from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, index_path, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.read_index(index_path)
    
    def retrieve(self, query, k=5):
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(query_vector.astype('float32'), k)
        return indices[0]