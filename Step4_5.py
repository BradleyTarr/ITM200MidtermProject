import pandas as pd
import matplotlib.pyplot as plt

#step 4
df = pd.read_csv('Data.csv')

year21 = df.loc[df['Month'] == 2021].values.tolist()[0]
year22 = df.loc[df['Month'] == 2022].values.tolist()[0]

print(year21)
print(year22)

firstHalf21 = sum(year21[1:7])
firstHalf22 = sum(year22[1:7])

print(firstHalf21, firstHalf22)

diff = firstHalf22 - firstHalf21
sgr = diff / firstHalf22
print(sgr)
estimated22 = [round(year21[i+6] + year21[i+6]*sgr, 2) for i in range(6)]

with open('stats.txt', 'a') as f:
    f.write("\nEstimated Sales for the Last Six Months of 2022:\n")
    for i in range(6):
        sale = year21[i+6] + year21[i+6] * sgr
        f.write(f"Month {i+7}: {sale}\n")
    f.write(f"\nSGR: {sgr}")

# Step 5
months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.barh(months, estimated22)
plt.xlabel('Estimated Sales')
plt.ylabel('Month')
plt.title('Estimated Sales for Last Six Months of 2022')
plt.show()
