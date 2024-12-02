import numpy as np
import pandas as pd
# matrix = np.array([[1,2,3], [4,5,6]])
# print("Matrix: ")
# print(matrix)

# random_numbers = np.random.randint(1, 100, size = 10)
# print("slumpmässiga tal: ", random_numbers)

# average = np.mean(random_numbers)
# print("medelvärdet: ", average)

data = {
    "namn": ["Anna", "Björn", "Cecilia"],
    "Ålder": [22, 34, 29],
    "Stad": ["Stockholm", "Göteborg", "Malmö"]
}

df = pd.DataFrame(data)

print("DataFrame: ")
print(df)

filtered_df = df[df["Ålder"] > 25]
print("\nPersoner över 25 år:")
print(filtered_df)