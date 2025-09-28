# | K-Nearest Neighbor | 
# |                   |
# |     Testing       |

from algorithm.knn import KNearestNeighborClasified
import pandas as pd

df = pd.read_csv('datasets/data.csv')
data_sample = df.values.tolist()
data_train = [2, 0, 1]

knn = KNearestNeighborClasified(site=3)
print("KNN Prediction : ", knn.predict(data_sample, data_train))

# |      Testing      |
# |                   |
# | K-Nearest Neighbor | 

