# Experiment 5: Hadoop Streaming – Sales Data Analysis

## Aim
To perform Hadoop Streaming using Python Mapper and Reducer programs to analyze sales data.

## Objective
- To understand Hadoop Streaming.
- To write Mapper and Reducer programs in Python.
- To execute a Hadoop MapReduce job.
- To calculate the total sales for each city.

## Software Used
- Ubuntu 24.04
- Hadoop 3.4.1
- Python 3
- Java 11

## Input
A CSV file containing sales records with:
- Date
- Product
- Price
- City
- Customer ID
- Quantity

## Procedure
1. Generate the sales dataset.
2. Create the Mapper program.
3. Create the Reducer program.
4. Test the programs locally.
5. Upload the dataset to HDFS.
6. Run the Hadoop Streaming job.
7. View and analyze the output.

## Files
- generate_sales.py
- mapper_city_sales.py
- reducer_city_sales.py
- sales_data.csv
- city_sales_results.txt

## Output
The program generates the total sales and transaction count for each city.

## Result
The Hadoop Streaming program was executed successfully, and the city-wise sales report was generated successfully.
