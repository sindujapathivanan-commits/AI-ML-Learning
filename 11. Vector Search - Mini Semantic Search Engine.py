from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Our documents
documents = [
    "Python is a programming language.",
    "NumPy is used for numerical calculations.",
    "Pandas is used for data analysis.",
    "Machine learning learns patterns from data.",
    "Artificial intelligence makes machines intelligent."
]

print(documents)

# 1. Load embedding model
model1 = SentenceTransformer("all-MiniLM-L6-v2")

#Generate embeddings
print("\n===== Generate embeddings =====")
embeddings = model1.encode(documents)

print("Done. Embeddings shape:", embeddings.shape)
print("Embeddings created!")
print("Number of embeddings:", len(embeddings))

# Convert documents to embeddings
documents_vectors = model1.encode(documents)

# 4. User query
query = "What is NumPy used for?"

# 5. Convert query to embedding
query_vector = model1.encode([query])
