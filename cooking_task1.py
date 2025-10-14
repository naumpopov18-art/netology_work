with open("recipes.txt", 'r', encoding='UTF-8') as recipes:
    current_recipe = None 
    ingredients_count = 0 
    current_ingredients = []
    recipes_book = {}
    recipes_read = recipes.readlines()
    for i in recipes_read:
        line = i.strip()
        
        if not line:
            if current_recipe and current_ingredients:
                recipes_book[current_recipe] = current_ingredients
            current_recipe = None
            current_ingredients = []
            continue
        if line.isdigit():
            ingredients_count = int(line)
        elif '|' in line:
            parts = line.split(' | ')      
            ingridient = {
                'ingredient_name': parts[0],
                'quantity': int(parts[1]),
                'measure': parts[2]
            }
            current_ingredients.append(ingridient)
        else:
            current_recipe = line

print(recipes_book)