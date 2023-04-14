import matplotlib.pyplot as plt
import pandas as pd

#Step 1
df = pd.read_csv('Data.CSV')

#Step 2
df_total = df.sum(axis=1)

df_stats = pd.DataFrame({'Month': df['Month'], 'Total Vehicles Sold': df_total})

with open('stats.txt', 'w') as f:
    f.write(df_stats.to_string(index=False))

#step 3
df_stats = pd.DataFrame({'Year': df['Month'], 'Total Vehicles Sold': df_total})

# Plot the total sales for each year using a bar plot
df_stats.plot(kind='bar', x='Year', y='Total Vehicles Sold')
plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Vehicles Sold')
plt.show()
plt.show()
