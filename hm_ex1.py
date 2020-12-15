def cook_book():
     with open('recipes.txt', encoding='utf8') as f:
        cook_book_dic = {}
        while True:
            dish = f.readline().strip('\n')
            cook_book_dic[dish] = []
            inc_list = []
            a = int(f.readline())
            while a != 0:
                ingredient = f.readline().split('|')
                dict_ingredients = {'ingredient_name': ingredient[0].strip(' '),
                                    'quantity': int(ingredient[1].strip(' ')),
                                    'measure': ingredient[2].strip(' \n')}
                inc_list.append(dict_ingredients)
                a -= 1
            cook_book_dic[dish] = inc_list
            if not f.readline():
                break
        return cook_book_dic


# print(cook_list())


def get_shop_list_by_dishes(dishes, person_count):
    cook_dic = cook_book()
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_dic.keys():
            for a in cook_dic.get(dish):
                if a.get('ingredient_name') not in shop_list_by_dishes:
                    shop_list_by_dishes.setdefault(a.get('ingredient_name'), {'quantity': a.get('quantity') * int(person_count), 'measure': a.get('measure')})
                else:
                    shop_list_by_dishes[dish['ingredient_name']]['quantity'] += dish['quantity'] * person_count
        else:
            print('такого блюда нет')
    return shop_list_by_dishes



print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))













