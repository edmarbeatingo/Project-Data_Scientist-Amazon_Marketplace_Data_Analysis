# Project-Data_Scientist-Amazon_Marketplace_Data_Analysis
This project involves analyzing sales data to generate insights and visualizations. The analysis includes calculating return rates, analyzing sales trends, seasonal sales analysis, profitability analysis, sales performance by marketplace, anomaly detection, and sales performance by ASIN per month.


### Data Sources
The analysis is based on the following data sources:
1. [test_data.txt](test_data.txt): Contains the raw sales data.
2. [formatted_data.csv](formatted_data.csv): Contains the formatted sales data.
3. [updated_data.csv](updated_data.csv): Contains the updated sales data with additional processing
4. [cleaned_data.csv](cleaned_data.csv): Contains the cleaned sales data, ready for analysis.


### Scripts
1. [mapped_data.py](mapped_data.py): Python script for mapping and formatting the raw data.
2. [engineered_data.py](engineered_data.py): Python script for engineering additional features in the data.
3. [cleaning_data.py](cleaning_data.py): Python script for cleaning the data.
4. [analysis_data.py](analysis_data): Python script for performing the analysis and generating visualizations.
5. [README.md](README.md): This documentation file.


### Analysis and Visualizations
The analysis is performed using the [analysis_data.py](analysis_data) script, which generates the following visualizations:

1. #### Top 5 ASINs with the Highest Net Sales.
- Description: Identifies the top 5 ASINs with the highest net sales.
- Plot: A bar plot showing the top 5 ASINs with the highest net sales.
- File: [top_asins.png](top_asins.png)
- Insight: Highlights the ASINs that contribute the most to the overall sales.

2. #### ASINs with High Return Rates
- Description: Calculates the return rates for each ASIN and identifies products with return rates greater than 10%.
- Plot: A bar plot showing ASINs with high return rates.
- File: [high_return_rate_asins.png](high_return_rate_asins.png)
- Insight: Helps identify products with high return rates, indicating potential quality issues or customer dissatisfaction.

3. #### Sales Trend Over Time
- Description: Examines the sales trends over time by grouping the data by month and summing the net sales.
- Plot: A line plot showing the sales trend over time.
- File: [sales_trend.png](sales_trend.png)
- Insight: Provides a visual representation of how sales have changed over time, helping to identify trends and patterns.

4. #### Seasonal Sales Analysis
- Description: Identifies peak sales periods and seasonal trends by grouping net sales by month.
- Plot: A bar plot showing net sales by month.
- File: [seasonal_sales.png](seasonal_sales.png)
- Insight: Highlights seasonal variations in sales, helping to identify peak sales periods and plan for seasonal demand.

5. #### Profitability Analysis
- Description: Calculates the profitability of each ASIN by subtracting the net proceeds total from the net sales.
- Plot: A bar plot showing the top 5 ASINs by profit.
- File: [profitability.png](profitability.png)
- Insight: Helps identify the most profitable products, providing insights into which products contribute the most to the bottom line.

6. #### Sales Performance by Marketplace
- Description: Compares sales performance across different marketplaces.
- Plot: A bar plot showing net sales by Amazon store.
- File: [marketplace_performance.png](marketplace_performance.png)
- Insight: Provides a comparison of sales performance across different marketplaces, helping to identify the best-performing marketplaces.

7. #### Anomalies in Sales Data
- Description: Identifies anomalies in sales data by considering sales values that are more than 3 standard deviations from the mean.
- Plot: A bar plot showing anomalies in sales data.
- File: [anomalies.png](anomalies.png)
- Insight: Helps identify unusual sales values that may require further investigation.

8. #### Anomalies in Sales Data by Month
- Description: Groups anomalies by month and plots them.
- Plot: A bar plot showing anomalies in sales data by month.
- File: [anomalies_by_month.png](anomalies_by_month.png)
- Insight: Provides a monthly breakdown of anomalies, helping to identify specific periods with unusual sales values.

9. #### Sales Performance by ASIN per Month
- Description: Examines sales performance by ASIN per month by grouping the data by month and ASIN.
- Plot: A grouped bar plot showing sales performance by ASIN per month.
- File: [sales_performance_by_asin_month.png](sales_performance_by_asin_month.png)
- Insight: Provides a detailed view of how each ASIN performs on a monthly basis, helping to identify trends and patterns for individual products.
