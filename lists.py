# Replace the "ANSWER HERE" with your answer

def remove_elements (lista):
	len_lista= len(lista)

	if len_lista == 6:
		new_lista = [lista[1], lista[2], lista[3]]

	elif len_lista >= 4:
		new_lista = [lista[1], lista[2], lista[3]]

	else:
		new_lista = []

	return new_lista


def add_elements (list_add):
	list_add.append('Yellow')
	list_add.insert(0,'Pink')
	return list_add


def is_empty(lista):
	if len(lista) == 0:
		return 'True'
	else:
		return 'false'

def check_lists (list_to_check1, list_to_check2):
	list_to_check1 = list_to_check[0]
	list_to_check2 = list_to_check[1]

	if list_to_check1[2] == list_to_check2[2]:
		return 'True'
	else:
		return 'False'


def list_of_lists(lists_of_lists_to_modify):
	list0 = lists_of_lists_to_modify[0]
	list1 = lists_of_lists_to_modify[1]
	list2 = lists_of_lists_to_modify[2]

	if len(list0) > 2:
		list0_new = [list0[0], list0[1]]
	else:
		list0_new = list0


	len2 = len(list1)

	if len2 ==2:
		list1_new = [list1[1]]
	elif len2 ==3:
		list1_new = [list1[1], list1[2]]
	elif len2 >= 4:
		list1_new = [list1[1], list1[2], list1[3]]
	else:
		list2_new = []

	len3 = len(list2)

	if len3 == 1:
		list2_new = [list2[0]]
	elif len3 >= 2:
		list2_new = [list2[-2], list2[-1]]

	else:
		list2_new = []


	return [list0_new, list1_new, list2_new]

