

#Create 10 short documents
data = {
    "Technology": [4, 3, 9, 0],
    "dog": [8, 4, 9, 3],
    "printer": [4, 5, 7, 8],
    "violin": [5, 4, 7, 4],
    "book": [0, 5, 3, 2],
    "apple": [1, 1, 5, 6],
    "lunch": [6, 2, 5, 5],
    "Happy": [4, 4, 5, 8, 3],
    "house": [7, 5, 4, 8],
    "clock": [3, 1, 0, 4],
      
}
for data in data:
  print(data) 

#Represent each document using numerical vectors

import numpy as np

vectors = {
     "Technology": [4, 3, 9, 0],
        "dog": [8, 4, 9, 3],
        "printer": [4, 5, 7, 8],
        "violin": [5, 4, 7, 4],
        "book": [0, 5, 3, 2],
        "apple": [1, 1, 5, 6],
        "lunch": [6, 2, 5, 5],
        "Happy": [4, 4, 5, 8, 3],
        "house": [7, 5, 4, 8],
        "clock": [3, 1, 0, 4],            
}
print(vectors)

# similarity calculation to know which vectors are closest.

print("\n===== similarity calculation to know which vectors are closest, Calculate similarity.=====")


from sklearn.metrics.pairwise import cosine_similarity

vectors1 = [
     [4, 3, 9, 0],
     [8, 4, 9, 3],
     [4, 5, 7, 8],
     [5, 4, 7, 4],
     [0, 5, 3, 2],
     [1, 1, 5, 6],
     [6, 2, 5, 5],
     [4, 4, 5, 8],
     [7, 5, 4, 8],
     [3, 1, 0, 4]     
]
# Calculate similarity
similarity = cosine_similarity(vectors)

print(similarity)

#Rank documents from most similar to least similar.

print("\n===== Rank documents from most similar to least similar.=====")


for i in range(len(similarity)):
    print(similarity)
    
    #Display the top 3 results.
    print("\n===== Display the top 3 results=====")

results = list(zip(vectors1, data))

results.sort(reverse=True)

print(results[:3])


for vectors1, data in results[:3]:
    print(data, vectors1)