import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned CSV data
df = pd.read_csv('C:/Users/Edmar Beatingo/Downloads/cleaned_data.csv')

# Convert date columns to datetime format
df['Start date'] = pd.to_datetime(df['Start date'], errors='coerce')
df['End date'] = pd.to_datetime(df['End date'], errors='coerce')

# Top 5 ASINs with the highest net sales
top_asins = df.groupby('ASIN')['Net sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 ASINs with the highest net sales:")
print(top_asins)

# Plot top 5 ASINs with the highest net sales
plt.figure(figsize=(10, 6))
top_asins.plot(kind='bar', color='skyblue')
plt.title('Top 5 ASINs with the Highest Net Sales')
plt.xlabel('ASIN')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/top_asins.png')
plt.show()

# Calculate return rates
df['Return rate'] = df['Units returned'] / df['Units sold']
high_return_rate_asins = df[df['Return rate'] > 0.1][['ASIN', 'Return rate']].drop_duplicates()
print("\nASINs with high return rates (greater than 10%):")
print(high_return_rate_asins)

# Plot ASINs with high return rates
plt.figure(figsize=(10, 6))
high_return_rate_asins.set_index('ASIN')['Return rate'].plot(kind='bar', color='salmon')
plt.title('ASINs with High Return Rates (Greater than 10%)')
plt.xlabel('ASIN')
plt.ylabel('Return Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/high_return_rate_asins.png')
plt.show()

# Analyze sales trends over time
sales_trend = df.groupby(df['Start date'].dt.to_period('M'))['Net sales'].sum()
print("\nSales trend over time:")
print(sales_trend)

# Plot sales trend over time
plt.figure(figsize=(14, 8))
sales_trend.plot(kind='line', marker='o', color='green')
plt.title('Sales Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/sales_trend.png')
plt.show()

# Seasonal Sales Analysis: Identify peak sales periods and seasonal trends
seasonal_sales = df.groupby(df['Start date'].dt.month)['Net sales'].sum()
print("\nSeasonal Sales Analysis (Net sales by month):")
print(seasonal_sales)

# Plot seasonal sales analysis
plt.figure(figsize=(10, 6))
seasonal_sales.plot(kind='bar', color='purple')
plt.title('Seasonal Sales Analysis (Net Sales by Month)')
plt.xlabel('Month')
plt.ylabel('Net Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/seasonal_sales.png')
plt.show()

# Profitability Analysis: Calculate the profitability of each ASIN
df['Profit'] = df['Net sales'] - df['Net proceeds total']
profitability = df.groupby('ASIN')['Profit'].sum().sort_values(ascending=False)
print("\nProfitability Analysis (Top 5 ASINs by profit):")
print(profitability.head(5))

# Plot profitability analysis
plt.figure(figsize=(10, 6))
profitability.head(5).plot(kind='bar', color='blue')
plt.title('Top 5 ASINs by Profit')
plt.xlabel('ASIN')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/profitability.png')
plt.show()

# Sales Performance by Marketplace: Compare sales performance across different marketplaces
marketplace_performance = df.groupby('Amazon store')['Net sales'].sum().sort_values(ascending=False)
print("\nSales Performance by Marketplace:")
print(marketplace_performance)

# Plot sales performance by marketplace
plt.figure(figsize=(10, 6))
marketplace_performance.plot(kind='bar', color='orange')
plt.title('Sales Performance by Marketplace')
plt.xlabel('Amazon Store')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/marketplace_performance.png')
plt.show()

# Anomaly Detection: Identify any anomalies in sales data
# For simplicity, we'll consider sales values that are more than 3 standard deviations from the mean as anomalies
mean_sales = df['Net sales'].mean()
std_sales = df['Net sales'].std()
anomalies = df[(df['Net sales'] > mean_sales + 3 * std_sales) | (df['Net sales'] < mean_sales - 3 * std_sales)]
print("\nAnomalies in Sales Data:")
print(anomalies[['ASIN', 'Net sales']])

# Plot anomalies in sales data
plt.figure(figsize=(10, 6))
anomalies.set_index('ASIN')['Net sales'].plot(kind='bar', color='red')
plt.title('Anomalies in Sales Data')
plt.xlabel('ASIN')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/anomalies.png')
plt.show()

# Plot anomalies in sales data by month
anomalies_by_month = anomalies.groupby(anomalies['Start date'].dt.to_period('M'))['Net sales'].sum()
print("\nAnomalies in Sales Data by Month:")
print(anomalies_by_month)

# Plot anomalies in sales data by month (separate bars with equal value)
plt.figure(figsize=(14, 8))
anomalies_by_month.plot(kind='bar', color='red')
plt.title('Anomalies in Sales Data by Month')
plt.xlabel('Month')
plt.ylabel('Net Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/anomalies_by_month.png')
plt.show()

# Sales Performance by ASIN per Month
sales_performance_by_asin_month = df.groupby([df['Start date'].dt.to_period('M'), 'ASIN'])['Net sales'].sum().unstack()
print("\nSales Performance by ASIN per Month:")
print(sales_performance_by_asin_month)

# Plot sales performance by ASIN per month (grouped bars)
sales_performance_by_asin_month.plot(kind='bar', figsize=(14, 8))
plt.title('Sales Performance by ASIN per Month')
plt.xlabel('Month')
plt.ylabel('Net Sales')
plt.legend(title='ASIN', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/Edmar Beatingo/Downloads/sales_performance_by_asin_month.png')
plt.show()

# Save the analysis results to CSV files
top_asins.to_csv('C:/Users/Edmar Beatingo/Downloads/top_asins.csv', header=True)
high_return_rate_asins.to_csv('C:/Users/Edmar Beatingo/Downloads/high_return_rate_asins.csv', index=False)
sales_trend.to_csv('C:/Users/Edmar Beatingo/Downloads/sales_trend.csv', header=True)
seasonal_sales.to_csv('C:/Users/Edmar Beatingo/Downloads/seasonal_sales.csv', header=True)
profitability.to_csv('C:/Users/Edmar Beatingo/Downloads/profitability.csv', header=True)
marketplace_performance.to_csv('C:/Users/Edmar Beatingo/Downloads/marketplace_performance.csv', header=True)
anomalies.to_csv('C:/Users/Edmar Beatingo/Downloads/anomalies.csv', index=False)
sales_performance_by_asin_month.to_csv('C:/Users/Edmar Beatingo/Downloads/sales_performance_by_asin_month.csv', header=True)