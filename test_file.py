# from MizuQuruma.KNearestNeighbours import KNN

# model = KNN()

# X_train, y_train, X_test, y_test = model.generate_dataset(n_classes=2)

# model.fit(X_train, y_train)

# prediction = model.predict([[10, 10], [70, 50]])
# print(prediction)

# evaluation = model.evaluate(X_test, y_test)
# print(evaluation)

# model.save_model()

# model = model.load_model()
# evaluation = model.evaluate(X_test, y_test)
# print(evaluation)


# my_plot = model.plot_data(X_test, y_test)
# my_plot.show()

# # ---

# import requests


# def get_crypto_price(symbol):
#     url = (
#         f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
#     )
#     response = requests.get(url)
#     data = response.json()
#     return data[symbol]["usd"]


# bitcoin_price = get_crypto_price("bitcoin")
# print("Bitcoin Price:", bitcoin_price)


from MizuQuruma.Regression import StochasticLinearRegression
from icecream import ic
import numpy as np


model = StochasticLinearRegression()
X_train, y_train, X_test, y_test = model.generate_dataset(
    coeff=[2], intercept=5, n_features=1, n_samples=150
)
# ic(X_train)
# ic(y_train)

model.fit(X_train, y_train, num_iterations=200, verbosity=2)
# ic(coeff, intercept, loss)
