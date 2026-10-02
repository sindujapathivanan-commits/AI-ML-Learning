
from sentence_transformers import SentenceTransformer
import numpy as np

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

print(sentences)

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print("\n===== Generate embeddings =====")
embeddings = model.encode(sentences)

print("Done. Embeddings shape:", embeddings.shape)
print("Embeddings created!")
print("Number of embeddings:", len(embeddings))


# Display a few embedding details
print("\n===== Top 5 matches =====")
print("\nTop 5 matches:")
for sentence, vector in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding size:", len(vector))
    print()
   