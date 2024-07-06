def fix_me(nested_list):
    final_list = []
    for idx, a_list in enumerate(nested_list):
        partial_sum = sum(a_list)

        if idx % 2 != 0:
            partial_sum *= -1

        final_list.append(partial_sum)

    return final_list

# Ejemplos de uso
entrada1 = {'nested_list': [[1, 2], [3, 4]]}
entrada2 = {'nested_list': [[1, 2], [3, 4], [-1, -4]]}

resultado1 = fix_me(entrada1['nested_list'])
resultado2 = fix_me(entrada2['nested_list'])

print(resultado1)  # Salida esperada: [3, -7]
print(resultado2)  # Salida esperada: [3, -7, -5]
