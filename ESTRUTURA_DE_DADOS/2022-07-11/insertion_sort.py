def insertion_sort(_array):
  n = len(_array)

  for i in range (1 , n) : # Inicia na 2a posicao do _array
    marcado = _array[ i]

    j = i - 1
    # Faz comparacoes ate o inicio do _array(j >= 0) e
    # somente enquanto o valor marcado for menor que a
    # posicao do _array que esta sendo comparada
    while j >= 0 and marcado < _array[j]:
      _array[j + 1] = _array[j] # Copia o elemento uma posicao para frente
      j -= 1

    _array[j + 1] = marcado # Copia o elemento marcado na posicao correta

  return _array