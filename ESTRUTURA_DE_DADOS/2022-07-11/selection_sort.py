def selection_sort(_array):
  n = len(_array)

  for i in range (n): # Cada iteracao indica uma rodada
    id_minimo = i # Posicao onde esta o menor valor

    for j in range (i + 1, n): # Parte de i + 1 porque os
    # elementos ordenados nao precisam ser percorridos
    # novamente e eles estao na posicao inicial do _array
      if _array[id_minimo] > _array[j]:
        id_minimo = j 
        # Se o valor comparado for menor,
        # sua posicao passa a ser a nova posicao de id_minimo
        # Ao final faz a troca do valores

    temp = _array[i]
    _array[i] = _array[id_minimo]
    _array[id_minimo] = temp

  return _array
