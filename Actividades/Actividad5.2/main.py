# imports
from src.make_data import make_data
from src.knn import euclidean_distance, manhattan_distance, cosine_distance, KNNRegressor
import matplotlib.pyplot as plt

# get data
X, y = make_data(n_features=2, n_pts=300, noise=0.1)

# separate into training and test
X_train = X[5:]
y_train = y[5:]
X_test = X[:5]
y_test = y[:5]

# perform a KNN Regression using multiple distance functions

fig,ax=plt.subplots()
plt.scatter(list(range(0,len(y_test))),y_test,label='actual')
for f in [euclidean_distance, manhattan_distance, cosine_distance]:
    knn = KNNRegressor(k=3, distance=f)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    plt.scatter(list(range(0,len(y_pred))),y_pred,label=f.__name__)

    print(f.__name__)
    print("Compare our predictions to the actual values. Are our predictions similar?")
    print("Predictions", y_pred)
    print("Actual", y_test)
    print('*' * 50)

plt.legend()