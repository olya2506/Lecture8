file_name = 'recipes.txt'

def file_worker(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        dish = 'str'
        while dish:
            dish = file.readline().strip()
            if dish != '':
                number_of_ingredients = file.readline().strip()
                ingredients_list = []
                for line in range(int(number_of_ingredients)):
                    ingredients_list.append(file.readline().strip())
                empty_line = file.readline().strip()
                for i in range(len(ingredients_list)):
                    ingredients = ingredients_list[i].split(' | ')
                    ingredients_list[i] = {'ingredient_name': ingredients[0], 'quantity': ingredients[1],
                                           'measure': ingredients[2]}
                cook_book[dish] = ingredients_list
    return cook_book


cook_book = file_worker(file_name)
print(cook_book)
print('---')


def get_shop_list_by_dishes(dishes, person_count):
    dict = {}
    for dish, ingredients_list in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients_list:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity']) * person_count

                if ingredient_name not in dict:
                    measure_and_quantity = {'measure': measure, 'quantity': quantity}
                    dict[ingredient_name] = measure_and_quantity
                else:
                    measure_and_quantity = {'measure': measure, 'quantity': ((dict[ingredient_name])['quantity']) + quantity}
                    dict[ingredient_name] = measure_and_quantity
    return dict


dict = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1)
print(dict)
print('---')


