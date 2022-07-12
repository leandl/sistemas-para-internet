def bubble_sort(_array):
  n = len(_array) # Tamanho do vetor
  
  for i in range ( n):
  # Executa a ordenacao ate o valor que ja esta
  # ordenado , por isso tem que usar (n - i) - 1 no range
    
    for j in range (0 , (n - i) - 1) :
    # Se o elemento da esquerda for maior que o da
    #direita , entao faz a troca dos valores
      if _array[j] > _array[j + 1]:
        temp =_array[j]
        _array[j] = _array[j + 1]
        _array[j + 1] = temp

  return _array