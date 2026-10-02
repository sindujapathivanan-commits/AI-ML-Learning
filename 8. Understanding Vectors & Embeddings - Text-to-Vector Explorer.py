

#Display each word
words = ["Technology", "Food", "Animals", "Sports", "Vehicles"]

for word in words:
    print(word)

#Display its vector
data = {
    "Technology": [4, 3],
    "dog": [8, 4],
    "printer": [4, 5],
    "car": [1, 1],
    "bus": [8, 2],
    
    "Food": [8, 3],
    "violin": [5, 4],
    "book": [0, 5],
    "apple": [1, 1],
    "lunch": [6, 2],
    
    "Animals": [8, 3],
    "fan": [4, 4],
    "house": [7, 5],
    "clock": [3, 1],
    "notebook": [1, 2],
    
    "Sports": [0, 3],
    "dance": [2, 4],
    "study": [4, 7],
    "car": [8, 1],
    "book": [1, 2],
    
    "Vehicles": [4, 3],
        "pen": [3, 7],
        "laptop": [4, 2],
        "phone": [8, 1],
        "number": [8, 3],
   
}

for word, vector in data.items():
    print(word, "→", vector)
    
    #Display vector dimensions
    print(len(data))
    
    #Compare two vectors
Vehicles = [4, 3],
car = [4, 3],

# Compare the vectors
if Vehicles == car:
    print("Vectors are same")
else:
    print("Vectors are different")
    
    
Vehicles = [4, 3],
car = [7, 3],

if Vehicles == car:
    print("Vectors are same")
else:
    print("Vectors are different")
    
    #Calculate the distance between two vectors.
    import math

    Technology = [4, 3]
    Food = [8, 3]

    distance = math.dist(Technology, Food)

    print(distance)
    
    #Identify which vectors are closest
    import math
    
    Technology = [4, 3]
    Food = [8, 3]
    Animals = [8, 3]
    
               
    d1 = math.dist(Technology, Food)
    d2 = math.dist(Technology, Animals)
   

    if d1 < d2:
        print("Technology and food are closest")
    else :
        print("Technology and Animal are closest")


#Create a 2D visualization of the vectors using Matplotlib.
#2D Array

import numpy as NP

data1 = NP.array([
            [4, 3],
            [8, 3]   
])

print(data1)
    
import matplotlib.pyplot as plt
import numpy as np

x = np.array([4, 3])
y = np.array([8, 3])

plt.plot(x, y)
plt.show()
