# | K-Nearest Neighbor | 
# |                    |
# |     Testing        |

from algorithm.knn import KNearestNeighborClassified
from algorithm.csv_reader import CSVReader

# Format: [Glucose, BMI, Age, Outcome]
csv = CSVReader('datasets/data.csv')
data_sample = csv.read()
data_train = [120, 30.1, 41]

knn = KNearestNeighborClassified(site=3)
print("KNN Prediction : ", knn.predict(data_sample, data_train))

# |      Testing       |
# |                    |
# | K-Nearest Neighbor | 

