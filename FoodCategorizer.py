class FoodCategorizer:
    def __init__(self, data):
        self.data = data

    def analyze_food(self):
        # Perform food analysis on the data
        categorized_data = self.data.copy()
        return categorized_data

    def categorize_food(self):
        # Categorize the food items based on predefined patterns
        categorized_data = self.data.copy()
        categorized_data['food_category'] = categorized_data['Food_Items'].str.lower().apply(self._categorize_food_item)
        categorized_data['food_sub_category'] = categorized_data['Food_Items'].str.lower().apply(self._sub_categorize_main_item)

        return categorized_data

    def _categorize_food_item(self, food_name):
        # Categorize a food item into a main, dessert, side, and other categories.
        if any(keyword in food_name for keyword in ['burger', 'sandwich', 'tenders', 'beef', 'taco']):
            return 'Main'
        elif any(keyword in food_name for keyword in ['fries', 'onion rings', 'salad']):
            return 'Side'
        elif any(keyword in food_name for keyword in ['ice cream', 'dessert']):
            return 'Dessert'
        else:
            return 'Other'

    def _sub_categorize_main_item(self, food_name):
        # Sub-categorize a main food item into specific sub-categories
        sub_categories = []
        main_category = self._categorize_food_item(food_name)

        if main_category == 'Main':
            if 'chicken' in food_name:
                sub_categories.append('Chicken')
            if 'beef' in food_name:
                sub_categories.append('Beef')
            if 'seafood' in food_name:
                sub_categories.append('Seafood')
            if 'pork' in food_name:
                sub_categories.append('Pork')
            else:
                sub_categories.append('Other')
        else:
            sub_categories.append('Other')

        return ', '.join(sub_categories)
