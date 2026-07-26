
import os
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

print(API_KEY) 

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_store(chunks):
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, chunks


def get_answer(question, index, chunks):
    question_embedding = model.encode([question])

    distance, indices = index.search(
        np.array(question_embedding), k=1
    )

    answer = chunks[indices[0][0]]

    return answer