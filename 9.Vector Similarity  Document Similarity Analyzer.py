

#Create 10 short documents

import numpy as np

data = {
    "Technology": [4, 3, 9, 0],
    "dog": [8, 4, 9, 3],
    "printer": [4, 5, 7, 8],
    "violin": [5, 4, 7, 4],
    "book": [0, 5, 3, 2],
    "apple": [1, 1, 5, 6],
    "lunch": [6, 2, 5, 5],
    "Happy": [4, 4, 5, 8,],
    "house": [7, 5, 4, 8],
    "clock": [3, 1, 0, 4],
      
}
 #Accept the query vector
query = [4, 3, 9, 0]


#Convert the query to NumPy array
query = np.array(query)

#Compare query with every document
for name, vector in data.items():
      print(name, vector)

vector = np.array(vector)

#vector length = length of the document vector
vector_length = np.linalg.norm(vector)
print(vector_length)
    
#Query length = length of the query vector
query_length = np.linalg.norm(query)
print(query_length)

#Calculate similarity = vector length + Query length
similarity = np.dot(query, vector) / ( # both compared
    np.linalg.norm(query) * np.linalg.norm(vector)
)
print(name, similarity) 

#find the similarity value for each vector
results = []

for name, vector in data.items():

    similarity = np.dot(query, vector) / (
        np.linalg.norm(query) * np.linalg.norm(vector)
    )

    results.append((name, similarity))

print(results)

#rank documents:
results.sort(key=lambda x: x[1], reverse=True)

for rank, result in enumerate(results, 1):
    print(rank, result[0], result[1])
    
    
  #Sorts from highest → lowest.  
    results = [
    ("Technology", 0.9999999999999999),
    ("dog", 0.9311778132380596),
    ("violin", 0.8962264150943395),
    ("lunch", 0.7678688960424389),
    ("printer", 0.7357233853694374),
    ("book", 0.6617661662464172),
    ("Happy", 0.6445806177461844),
    ("apple", 0.6363266851191053),
    ("house", 0.6183207174913357),
    ("clock", 0.2857272441597973)
]

results.sort(reverse=True) #Display the top 3 results.

print("Rank 1:", results[0])
print("Rank 2:", results[1])
print("Rank 3:", results[2])
print("Rank 4:", results[3])