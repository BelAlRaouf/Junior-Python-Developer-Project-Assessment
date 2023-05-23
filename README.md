# Restaurant Nutrition Analysis

This program analyzes restaurant data from a CSV file, stores it in a SQLite database, and performs various operations on the data such as calculating average, minimum, and maximum calories for each restaurant, ranking restaurants based on the least amount of carbs, categorizing and sub-categorizing food items, and visualizing the data using a Python visualization library.

## Dependencies

The project relies on the following dependencies, which can be installed using the provided `requirements.txt` file:

- Python 3.10
- SQLite3
- pandas
- matplotlib

## Features

- Read nutrition data from an SQLite database.
- Calculate statistics such as average, minimum, and maximum calories for each restaurant.
- Rank restaurants based on the average amount of carbs in their menu items.
- Categorize food items as Main, Side, Dessert, and Other based on their names and nutritional information.
- Further sub-categorize Main food items into Chicken, Beef, Seafood, Pork, Other.
- Generate a chart to visualize the statistics and rankings.

## Setup

1. Clone the repository or download the project files to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Ensure you have an CSV file named `fast_food.csv` containing the restaurant nutrition data.
4. Run the `main.py` file to execute the program.

## Project Structure

The project consists of the following files:

- `main.py`: The main program file that orchestrates the entire analysis process.
- `RestaurantData.py`: A module that handles reading the CSV file, storing data in the database, retrieving analyzed data, Show the data for the Top 5 restaurants as a chart, and exporting data to CSV files.
- `FoodCategorizer.py`: A module that categorizes and sub-categorizes food items based on keywords.
- `CSV_input_file/fastfood.csv`: The input CSV file containing the restaurant data.
- `CSV_output_file/analyzed_food.csv`: Store the average, minimum and maximum calories for each restaurant and rank the restaurants by those that have the least amount of carbs on average.
- `CSV_output_file/sub_categorized_food.csv`: Store the data that Categorized the food items as Main, Side, Dessert, and Other based on their names and nutritional information. Further sub-categorize Main food items into Chicken, Beef, Seafood, Pork, Other.
- `Database_folder/food_database.db`: The SQLite database file for storing the restaurant data.
- `Restaurant_chart/5-Top-Restaurant-chart.png`: Contain a png picture that Show the data for the Top 5 restaurants as a chart.

## Usage

1. Place the CSV file containing the restaurant data in the same directory as the code files.
2. Update the `csv_file` and `db_file` variables in the `main()` function of the `main.py` file to specify the file names for the CSV and database files, respectively.
3. Run the program by executing the following command: `python main.py`
4. The program will perform the following steps:
- Read the data from the CSV file and store it in the SQLite database.
- Analyze the data to calculate average, minimum, and maximum calories for each restaurant and rank the restaurants based on the least amount of carbs.
- Visualize the data for the top 5 restaurants as a bar chart using matplotlib.
- Categorize and sub-categorize the food items based on certain keywords.
- Export the analyzed food data and categorized data to CSV files.
5.The program will generate the following output files:
- `analyzed_food.csv`: Contains the analyzed food data, including average, minimum, and maximum calories for each restaurant.
- `sub_categorized_food.csv`: Contains the categorized and sub-categorized food data.


## Customization

- If you want to categorize food items differently or add more sub-categories, you can modify the `_categorize_food_item`, `_sub_categorize_main_item`, and `categorize_food` method in the `FoodCategorizer.py` class.
- To change the chart style or customize the visualization, you can modify the `visualize_data` method in the `RestaurantData.py` class.


## What's Next

IIt has possibility to work on improving the categorization pattern for better accuracy, especially when dealing with larger datasets. While the current pattern works well with fewer keywords, it may not be as effective for big data scenarios.
To enhance the categorization process, we can explore alternative approaches such as:

- Implementing machine learning algorithms for automatic classification based on textual features.

By implementing more advanced techniques, we can aim to achieve higher accuracy and efficiency in categorizing and sub-categorizing food items.



Belal Raouf