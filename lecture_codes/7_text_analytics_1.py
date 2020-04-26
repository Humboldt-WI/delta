# Codes used in examples of Section 7 Text Analytics Part I

# Word Embeddings
from typing import Any, Union

import numpy as np
hotel = np.zeros((1, 10))
hotel[0, -3] = 1

motel = np.zeros((1, 10))
motel[0, 2] = 1

num = np.dot(hotel, motel.T)
denom = np.linalg.norm(hotel) * np.linalg.norm(motel)

cos_theta = num.item()/denom
