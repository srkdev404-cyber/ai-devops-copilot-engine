import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

memory = []

def store_vector(vector, text):
    index.add(np.array([vector]).astype("float32"))
    memory.append(text)

def search(vector, k=2):
    D, I = index.search(np.array([vector]).astype("float32"), k)
    return [memory[i] for i in I[0] if i < len(memory)]
