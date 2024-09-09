from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Indexer:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.index = None

    def create_index(self, texts):
        # 确保所有的文本都是非空的字符串
        valid_texts = [text for text in texts if isinstance(text, str) and text.strip()]
        if not valid_texts:
            raise ValueError("No valid texts to index. Please check your data.")
        
        embeddings = self.model.encode(valid_texts)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def save_index(self, path):
        faiss.write_index(self.index, path)
    
    def load_index(self, path):
        self.index = faiss.read_index(path)