# Script for importing a dataset and replacing min with max
import pandas as pd
df = pd.read_csv("~/Desktop/docs/names.csv")
df.head()
df = df['Status'].str.replace("min","max",regex=True)

# This script calculates the area of a rectangle

# Get input for length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Print the result with a comma separator and to 2 decimal places
print(f"The area of the rectangle is: {area:,.2f}")
