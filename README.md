# Restaurant Nutrition Analysis

Restaurant Nutrition Analysis is a data analysis tool that reads nutrition information from an SQLite database, performs calculations and categorizations, and generates visualizations. It provides insights into the nutritional content of menu items from different restaurants.

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
3. Ensure you have an SQLite database file named `restaurant_data.db` containing the restaurant nutrition data. If you have a different database file name, update the `DATABASE_FILE` constant in the `database_manager.py` file.
4. Run the `main.py` file to execute the data analysis.

## Project Structure

The project consists of the following files:

- `main.py`: The entry point of the program. It initializes the database manager, performs the data analysis, and generates visualizations.
- `database_manager.py`: A class responsible for managing the SQLite database connection, executing queries, and retrieving nutrition data.
- `data_analyzer.py`: A class that performs the data analysis, including calculations and categorizations.
- `chart_generator.py`: A class that generates charts using the Matplotlib library to visualize the data.
- `food_cats.csv`: The output file containing the categorized food items.

## Usage

1. Ensure the SQLite database file `restaurant_data.db` is present in the project directory.
2. Run the `main.py` file using Python 3.
3. The program will read the nutrition data from the database and perform the analysis.
4. The results will be displayed in the console and saved in the `food_cats.csv` file.
5. A chart showing the statistics and rankings will be generated and saved as `nutrition_chart.png`.

## Customization

- If you want to categorize food items differently or add more sub-categories, you can modify the `categorize_food_items` method in the `DataAnalyzer` class.
- To change the chart style or customize the visualization, you can modify the `generate_chart` method in the `ChartGenerator` class.

## Dependencies

The project relies on the following dependencies, which can be installed using the provided `requirements.txt` file:

- Python 3
- SQLite3
- pandas
- matplotlib

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
