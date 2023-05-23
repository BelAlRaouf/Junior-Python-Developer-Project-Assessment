import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os


class RestaurantData:
    def __init__(self, csv_file, db_file):
        self.csv_file = csv_file
        self.db_file = db_file

    def read_csv(self):
        # Read the CSV file using pandas
        return pd.read_csv(self.csv_file)

    def store_in_database(self):
        data = self.read_csv()
        conn = sqlite3.connect(self.db_file)
        # Store the data in the database table 'food_items'
        # If the table already exists, replace it.
        data.to_sql('food_items', conn, if_exists='replace', index=False)
        # close the database connection.
        conn.close()

    def analyze_data(self):
        # Connect to the database
        conn = sqlite3.connect(self.db_file)
        # Execute the query to calculate the average, minimum, and maximum calories
        # for each restaurant and order the results by average carbs in ascending order
        # Limit the results to the top 5 restaurants
        query = "SELECT restaurant, AVG(calories) AS avg_calories, MIN(calories) AS min_calories, MAX(calories) AS " \
                "max_calories, AVG(total_carb) AS avg_carbs FROM food_items GROUP BY restaurant ORDER BY avg_carbs " \
                "ASC LIMIT 5 "
        # Execute the query and retrieve the results into a pandas DataFrame
        result = pd.read_sql_query(query, conn)
        conn.close()
        #return the analyzed data
        return result

    def categorize_data(self):
        conn = sqlite3.connect(self.db_file)
        # Execute the query to retrieve the restaurant and food item data
        query = "SELECT restaurant, item AS Food_Items FROM food_items"
        result = pd.read_sql_query(query, conn)
        conn.close()
        # Return the categorized data
        return result

    def visualize_data(self, data):
        # Set the figure size for the plot
        plt.figure(figsize=(10, 8))
        # Create a bar plot of the average calories for each restaurant
        plt.bar(data['restaurant'], data['avg_calories'])
        # set x-axis label
        plt.xlabel('Restaurants')
        # set y-axis label
        plt.ylabel('Average Calories')
        # set the title of the chart
        plt.title('Average Calories for Top 5 Restaurants')
        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)

        # Create an output folder for the chart if it doesn't exist
        output_folder = 'Restaurant_chart'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Save the chart in the output folder
        output_file = os.path.join(output_folder, '5-Top-Restaurant-chart.png')
        plt.savefig(output_file)
        plt.show()

    def export_to_csv(self, data, csv_file):
        # Export the data to a CSV file
        data.to_csv(csv_file, index=False)
