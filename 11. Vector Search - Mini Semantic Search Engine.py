from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Our documents
documents = [
"Python Basics — variables, data types, input/output"
"Python Conditions — if, elif, else, comparison operators"
"Python Loops — for, while, range()"
"Python Lists & Dictionaries — storing and accessing employee/student data"
"Python Functions & Modules — reusable code and importing libraries"
"NumPy Arrays — 1D, 2D, 3D arrays"
"Array Indexing & Slicing — rows, columns, elements"
"Array Shape, Size & Dimensions — shape, size, ndim, dtype"
"NumPy Data Cleaning — missing/invalid values and filtering"
"NumPy AI Data Preprocessing — feature selection, normalization, reshaping"
"Pandas Series & DataFrame"
"Reading & Writing CSV/Excel Files"
"Selecting & Filtering Data"
"Data Cleaning with Pandas — missing values, duplicates, incorrect data"
"Pandas Employee Analytics — salary, department, performance analysis"
"What is Machine Learning? — AI vs ML vs Deep Learning"
"Features & Target — X and y"
"Training & Testing Data — train_test_split"
"Regression — predicting employee salary"
"Classification — predicting employee performance/pass/fail"
"What is Artificial Intelligence?"
"AI, ML, Deep Learning & Generative AI"
"Vectors & Embeddings — converting text into numbers"
"Semantic Similarity & Search — comparing documents with a query"
"AI Assistant Project — documents → embeddings → similarity search → answer"
]

# 1. Load embedding model
model1 = SentenceTransformer("all-MiniLM-L6-v2")

#Generate embeddings
print("\n===== Generate embeddings =====")
embeddings = model1.encode(documents)

print("Done. Embeddings shape:", embeddings.shape)
print("Embeddings created!")
print("Number of embeddings:", len(embeddings))

## Print sentence + embedding
for i, documents in enumerate(documents):
    print(i, documents)
    print("Vector (first 5):", embeddings[i][:5])
    
print("Done. Embeddings shape:", embeddings.shape)
print("Embeddings created!")
print("Number of embeddings:", len(embeddings))

print("\n===== each embedded sentence =====")
print(embeddings)

#store the embedding
print("\n===== 2. Store the embedding =====")
import numpy as np
np.save("embeddings.npy", embeddings)
embeddings = np.load("embeddings.npy")
print(embeddings)

#Generate query embedding
print("\n====3. Generate query embedding ===")
query = "What is NumPy used for?"
query_embedding = model1.encode([query])

#compare query with every documenty
print("\n====4.Compare query with every document====")
for i, documents in enumerate(documents):
 print(i, documents)
 print("vector (first 5):", embeddings[0][:5])  
 print()   

#Calculate similarity
print("\n=====Calculate similarity===========")
similarities = np.dot(embeddings, query_embedding.T)
print("similarities shape:", similarities.shape)
print("similarities", similarities)

   
#Rank results
print("\n===== Rank results=====")
results = list(zip(documents, similarities[0]))
results.sort(key=lambda x: x[1], reverse=True)

for rank, result in enumerate(results):
    print(rank, result[0], result)
    
    
    
#Sorts from highest → lowest.  
print("\n=====highest → lowest=====")
for rank, (documents, score) in enumerate(results, 1):
    print(rank, score, documents)
    
# Display Top 5 relevant documents

print("\n==== Top 5 Relevant Documents ====")    #np.argsort(similarities) → sorts scores

# Sort similarity scores from highest to lowest
similarities = np.asarray(similarities).ravel()

# Indices of the 5 highest scores, best first
top_5 = np.argsort(similarities)[::-1][:5]

for i in top_5:
    print(documents[int(i)], similarities[i])







