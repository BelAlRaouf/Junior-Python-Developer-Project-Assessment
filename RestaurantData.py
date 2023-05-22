import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


class RestaurantData:
    def __init__(self, csv_file, db_file):
        self.csv_file = csv_file
        self.db_file = db_file

    def read_csv(self):
        return pd.read_csv(self.csv_file)

    def store_in_database(self):
        data = self.read_csv()
        conn = sqlite3.connect(self.db_file)
        data.to_sql('food_items', conn, if_exists='replace', index=False)
        conn.close()

    def analyze_data(self):
        conn = sqlite3.connect(self.db_file)
        query = "SELECT restaurant, AVG(calories) AS avg_calories, MIN(calories) AS min_calories, MAX(calories) AS " \
                "max_calories, AVG(total_carb) AS avg_carbs FROM food_items GROUP BY restaurant ORDER BY avg_carbs " \
                "ASC LIMIT 5 "
        result = pd.read_sql_query(query, conn)
        conn.close()
        return result

    def visualize_data(self, data):
        plt.bar(data['restaurant'], data['avg_calories'])
        plt.xlabel('Restaurants')
        plt.ylabel('Average Calories')
        plt.title('Average Calories for Top 5 Restaurants')
        plt.xticks(rotation=45)
        plt.show()

    def export_to_csv(self, data, csv_file):
        data.to_csv(csv_file, index=False)
