from FoodCategorizer import FoodCategorizer
from RestaurantData import RestaurantData


# Main program
def main():

    # csv file path
    csv_file = 'CSV_input_file/fastfood.csv'
    # database file path
    db_file = 'Database_folder/food_database.db'

    # Getting data from CSV file and retrieve them in to database
    restaurant_data = RestaurantData(csv_file, db_file)

    # Storing data in to database
    restaurant_data.store_in_database()

    # Calculating the average, minimum, and maximum calories for each restaurant
    # and ranking the restaurants by the least amount of carbs on average
    analyzed_data = restaurant_data.analyze_data()

    # Show this data for the Top 5 restaurants as a chart using any Python visualization library
    restaurant_data.visualize_data(analyzed_data)

    # Categorizing and sub-categorizing data
    categorization_data = restaurant_data.categorize_data()

    # Analyzing the food items based on the analyzed data
    food_Analyser = FoodCategorizer(analyzed_data)
    analyzed_food = food_Analyser.analyze_food()

    # Categorizing the food items based on the categorization data
    food_categorizer = FoodCategorizer(categorization_data)
    categorized_data = food_categorizer.categorize_food()

    # Create two csv files for Top 5 restaurant and categories.
    analyzed_data_output = 'CSV_output_file/analyzed_food.csv'
    sub_categorized_data_output = 'CSV_output_file/categorized_food.csv'

    # export two csv file for Top 5 restaurant and categories.
    restaurant_data.export_to_csv(analyzed_food, analyzed_data_output)
    restaurant_data.export_to_csv(categorized_data, sub_categorized_data_output)


if __name__ == '__main__':
    main()
