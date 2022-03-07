import requests


def diet_search(diet):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = ''
    app_key = ''
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(diet, app_id, app_key))
    data = result.json()
    return data['hits']

def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'd4c26f13'
    app_key = '519f29a1cb5dca4a4ff74ea48abcda68'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def calories_search(calories_to, calories_from):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'd4c26f13'
    app_key = '519f29a1cb5dca4a4ff74ea48abcda68'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(calories_to, calories_from, app_id, app_key))
    data = result.json()
    return data['hits']


def run():

    diet_list = ['Vegetarian', 'Vegan', 'Paleo', 'High-Fiber', 'High-Protein', 'High-Protein', 'Low-Carb', 'Low-Fat',
                    'Low-Sodium', 'Low-Sugar', 'Low-Sugar', 'Alcohol - Free']

    diet = input('Choose your diet: ')
    results_diet = recipe_search(diet)

    ingredient = input('Enter an ingredient: ')
    results = diet_search(ingredient)

    calory_from, calory_to = input('Enter the number of calories: ').split()
    results_calories = calories_search(calory_from, calory_to)

    for diet_result in results_diet: #to be checked
        if diet in diet_list:
            for result in results:
                #intoducing a list
                recipe_list = []
                # good_choice = 'good choice!'
                # bad_choice = 'ups, too many calories!'
                recipe = result['recipe']

                if calory_from > 0 and calory_from <= calory_to:
                    recipe_list.append('Calories: ')
                    recipe_list.append(calory_from)
                else:
                    print('Calories cannot be negative')

                print(recipe['label'])
                print(recipe_list)
                print(recipe['uri'])
                print()

        else:
            print("Wrong input, please check for typos")
run()