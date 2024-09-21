immutable_var = (5, "Hello", 3.14, True)
# Если мы попробуем изменить нам выдомс ошибку посколько это не изменяемый тип
print(immutable_var)
mutable_list = [5, "Hello", 3.14, True]
mutable_list.append('Modified')
mutable_list.remove(3.14)
mutable_list[1] = 'Привет'
print(mutable_list)