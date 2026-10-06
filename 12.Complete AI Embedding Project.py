import numpy as np
import pandas as pd
import sentence_transformers

#1.Python reads the documents
print("\n==== 1.Python reads the documents ====") 
from pypdf import PdfReader

pdf = PdfReader("12. Complete AI Embedding Project document - AI Knowledge Base Dataset_Simple.pdf")

for page in pdf.pages:
    text = page.extract_text()
    print(text)


#2.Clean the text
print("\n==== 2.Clean the text====") 
text = " ".join(text.split()) #Remove messy spaces → put words together neatly with one space
print("cleaned")# Display cleaned text

#3.Simple chunking code(Separating data)
print("\n==== 3.Simple chunking code(Separating data)====") 
# Create chunks
words = text.split()
chunks = []

for i in range(0, len(words), 100):
    chunk = " ".join(words[i:i + 100])
    chunks.append(chunk)

print("Total chunks:", len(chunks))
print(chunks[0])

#4.Generate Embeddings
print("\n====4. Generate Embeddings====") 
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
text = "Python is a programming language."
embedding = model.encode(text)
print(embedding)

#5.Store the vectors
print("\n====5.Store the vectors====") 
np.save("embeddings.npy", embedding)
np.save("chunks.npy", chunks)
print("Saved!")

#6.Ask the Question
print("\n====6.Ask the Question====") 
query = input("What happens if I miss my training session?")
q = model.encode(query)
scores = [np.dot(q, x) for x in embedding]
best = np.argmax(scores)
print(chunks[best])

#7.Convert question to numbers
print("\n====7.Convert question to numbers====") 
query_embedding = model.encode(query)

#8.Calculate similarity
print("\n====8.Calculate similarity====")
similarities = []

for embedding in embedding:

    score = np.dot(query_embedding, embedding) / (
        np.linalg.norm(query_embedding) *
        np.linalg.norm(embedding)
    )
similarities.append(score)

# Convert to NumPy array
similarities = np.array(similarities)
# Get indexes from highest score to lowest
sorted_indexes = np.argsort(similarities)[::-1]
# Show Top 5
print("\n===== TOP 5 RESULTS =====")
for rank, index in enumerate(sorted_indexes[:5], start=1):
    print("\nRank:", rank)
    print("Similarity Score:", round(similarities[index], 2))
    print("Text:", chunks[index])