from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
print("************************************")
print(iris.target)
print("************************************")
print(iris.target_names)
print("************************************")
print(type(iris.target))
print("************************************")
print(iris.data.shape)
print("************************************")
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
x = iris.data
y = iris.target
knn.fit(x,y)
print(knn.predict( [ [5.9, 3,  5.1, 1.8] ] ))