import numpy as np

data=np.array([1,2,3,4,5])
media=np.mean(data)
#print(media)
# print(np.median(data))
# print(np.var(data))
# print(np.std(data))

arr=np.array([10,20,30])
probabilitati=[0.9,0.09,0.01]
alegere=np.random.choice(arr,p=probabilitati)
print(alegere)

