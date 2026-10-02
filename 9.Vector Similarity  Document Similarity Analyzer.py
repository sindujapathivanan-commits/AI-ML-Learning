

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
    "Happy": [4, 4, 5, 8, 3],
    "house": [7, 5, 4, 8],
    "clock": [3, 1, 0, 4],
      
}
 #Accept the query vector
query = [4, 3, 9, 0]


#Convert the query to NumPy array
query = np.array(query)

#Compare query with every document
for name, vector in data.items():

    vector = np.array(vector)

    similarity = np.dot(query, vector) / (
        np.linalg.norm(query) * np.linalg.norm(vector)
    )

    print(name, similarity)
    
  