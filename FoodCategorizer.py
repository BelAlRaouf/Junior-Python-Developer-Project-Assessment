class FoodCategorizer:
    def __init__(self, data):
        self.data = data

    def categorize_food(self):
        categorized_data = self.data.copy()
        categorized_data['food_category'] = categorized_data.apply(self._categorize_food_item, axis=1)
        return categorized_data

    def _categorize_food_item(self, row):
        food_name = row.get('item', '').lower()
        if 'burger' in food_name or 'sandwich' in food_name:
            return 'Main'
        elif 'fries' in food_name or 'onion rings' in food_name:
            return 'Side'
        elif 'nuggets' in food_name or 'tenders' in food_name:
            return 'Main'
        elif 'salad' in food_name:
            return 'Side'
        elif 'ice cream' in food_name or 'dessert' in food_name:
            return 'Dessert'
        else:
            return 'Other'

    def sub_categorize_main(self):
        sub_categorized_data = self.data.copy()
        sub_categorized_data['food_sub_category'] = sub_categorized_data.apply(self._sub_categorize_main_item, axis=1)
        return sub_categorized_data

    def _sub_categorize_main_item(self, row):
        food_name = row.get('item', '').lower()
        sub_categories = []
        if 'chicken' in food_name:
            sub_categories.append('Chicken')
        if 'beef' in food_name:
            sub_categories.append('Beef')
        if 'seafood' in food_name:
            sub_categories.append('Seafood')
        if 'pork' in food_name:
            sub_categories.append('Pork')
        if not sub_categories:
            sub_categories.append('Other')
        return ', '.join(sub_categories)
