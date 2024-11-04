def find_tovar(tov_list,tov_name, i=-1, ind=0):

    for current_tov in tov_list:
        i += 1
        if current_tov == tov_name:
            ind = i
            break
        else: ind = None



    return ind


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_tovar(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
