from FoodCategorizer import FoodCategorizer
from RestaurantData import RestaurantData


# Main program
def main():
    csv_file = 'fastfood.csv'
    db_file = 'food_database.db'

    restaurant_data = RestaurantData(csv_file, db_file)
    restaurant_data.store_in_database()
    analyzed_data = restaurant_data.analyze_data()
    restaurant_data.visualize_data(analyzed_data)

    food_categorizer = FoodCategorizer(analyzed_data)
    categorized_data = food_categorizer.categorize_food()
    sub_categorized_data = food_categorizer.sub_categorize_main()

    categorized_data_output = 'categorized_food.csv'
    sub_categorized_data_output = 'sub_categorized_food.csv'
    restaurant_data.export_to_csv(categorized_data, categorized_data_output)
    restaurant_data.export_to_csv(sub_categorized_data, sub_categorized_data_output)


if __name__ == '__main__':
    main()



