from ast import Compare

from sentence_transformers import SentenceTransformer
import numpy as np
from torch import embedding

# Data to encode
sentences = [
    "Code tells a computer what to do.",
    "A bug is a mistake in a program.",
    "Python is easy to learn.",
    "Good code is neat and clear.",
    "Programmers test their work often.",
    "Apps are made with code.",
    "AI can learn from data.",
    "Robots use AI to do tasks.",
    "Chatbots answer simple questions.",
    "AI can help doctors find illness.",
    "Some AI can write and draw.",
    "People must use AI in a safe way.",
    "Students go to school to learn.",
    "Teachers help us understand new things.",
    "Reading every day is a good habit.",
    "Practice helps us get better.",
    "Online classes are easy to join.",
    "Learning never really ends.",
    "A business sells things or services.",
    "Happy customers come back again.",
    "Good teams work well together.",
    "Every company needs money to grow.",
    "Advertising helps people find a product.",
    "A good boss listens to the team.",
    "Many people travel on holiday.",
    "A passport is needed to visit other countries.",
    "Planes are the fastest way to travel far.",
    "Tourists take photos of new places.",
    "Local food is fun to try.",
    "Pack a small bag for a short trip."
]

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print("\n=====1. Generate embeddings =====")
embeddings = model.encode(sentences)

 
## Print sentence + embedding
for i, sentence in enumerate(sentences):
    print(i, sentence)
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
print("\n===== 3. Generate query embedding =====")
query = "I want to learn artificial intelligence"
query_embedding = model.encode([query])

#Compare query with every document
print("\n===== 4.Compare query with every document =====")
for i, sentence in enumerate(sentences):
    print(i, sentence)
    print("Vector (first 5):", embeddings[i][:5])
    print("Sentence:", sentence)
    print("Embedding:", query_embedding)
    print()
       
  #Calculate similarity
print("\n===== 5.Calculate similarity.=====")
similarities = np.dot(embeddings, query_embedding.T)
print("Similarities shape:", similarities.shape)
print("Similarities:", similarities)

#See sentence + similarity
print("\n===== See sentence + similarity=====")
for sentence, score in zip(sentences, similarities[0]):
    print(sentence, score)
    
#Rank results
print("\n===== Rank results=====")
results = list(zip(sentences, similarities[0]))
results.sort(key=lambda x: x[1], reverse=True)

for rank, result in enumerate(results):
    print(rank, result[0], result)
    
    
    
#Sorts from highest → lowest.  
print("\n=====highest → lowest=====")
for rank, (sentence, score) in enumerate(results, 1):
    print(rank, score, sentence)
    
    
     #Sorts from highest → lowest.  
    print("\n===== highest → lowest.  =====")

    results = [
[ 0.08537271],
 [ 0.45389223],
 [ 0.14538074], 
 [ 0.25042123],
 [ 0.15567026],
 [ 0.5750976 ],
 [ 0.51353896],
 [ 0.34531987],
 [ 0.41015667],
 [ 0.46220583],
 [ 0.42885435],
 [ 0.25020683],
 [ 0.26424855],
 [ 0.20763919],
 [ 0.22541118],
 [ 0.24709435],
 [ 0.34952235],
 [-0.00473217],
 [ 0.01293283],
 [ 0.05705832],
 [ 0.03177438],
 [ 0.06963825],
 [ 0.0787719 ],
 [-0.00808025],
 [ 0.02237052],
 [ 0.07976358],
 [-0.03394672],
 [ 0.01613097],
 [ 0.01323562]]

    
    results.sort(reverse=True) #Display the top 3 results.
    
    print("Rank 1:", results[0])
    print("Rank 2:", results[1])
    print("Rank 3:", results[2])
    print("Rank 4:", results[3])