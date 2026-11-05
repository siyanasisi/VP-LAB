def scale_recipe(recipe_ingredients, original_servings, target_servings):
    if original_servings <= 0 or target_servings <= 0:
        return { }

    scaled_recipe = {}
    for ingredient, quantity in recipe_ingredients.items():
        new_quantity = quantity * (target_servings / original_servings)
        scaled_recipe[ingredient] = round(new_quantity, 2)
    return scaled_recipe

recipe_ingredients = {
    "flour": 200,
    "sugar": 100,
    "eggs": 2,
    "milk": 250
}

result = scale_recipe(recipe_ingredients, 4, 6)
print(result)