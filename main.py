# Dataset for testing

# - About Dataset
#   Outlook :
#     |  Sunny       → 0
#     |  Overcast    → 1
#     |  Rain        → 2
#
#   Humidity :
#     |  High        → 0
#     |  Normal      → 1
#
#   Wind :
#     |  Weak        → 0
#     |  Strong      → 1

# - Header
#   | Outlook | Humidity | Wind | Play |

data_sample = [
  [0, 0, 0, 'No'],
  [0, 0, 1, 'No'],
  [1, 0, 0, 'Yes'],
  [2, 0, 0, 'Yes'],
  [2, 1, 0, 'Yes'],
  [2, 1, 1, 'No'],
  [1, 1, 1, 'Yes'],
  [0, 0, 0, 'No'],
  [0, 1, 0, 'Yes'],
  [2, 1, 0, 'Yes'],
  [0, 1, 1, 'Yes'],
  [1, 0, 1, 'Yes'],
  [1, 1, 0, 'Yes'],
  [2, 0, 1, 'No']
]





# | K-Nearest Neigbor | 
# |                   |
# |     Testing       |

from algorithm.knn import KNearestNeighbor

data_train = [0, 1, 1]

des = KNearestNeighbor(site=3)
print("KNN Prediction : ", des.predict(data_sample, data_train))

# |      Testing      |
# |                   |
# | K-Nearest Neigbor | 