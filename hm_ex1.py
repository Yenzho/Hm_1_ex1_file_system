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
    shop_dic_by_dishes = {}
    for dish in dishes:
        if dish in cook_dic.keys():
            for b in cook_dic[dish]:
                if b.get('ingredient_name') not in shop_dic_by_dishes:
                    shop_dic_by_dishes.setdefault(b.get('ingredient_name'),
                                                 {'quantity': int(b.get('quantity') * int(person_count)),
                                                  'measure': b.get('measure')})
                else:
                    shop_dic_by_dishes[b['ingredient_name']]['quantity'] += b['quantity'] * int(person_count)
        else:
            print('Одно или несколько блюд отсутсвует в списке')
    return shop_dic_by_dishes



print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))













