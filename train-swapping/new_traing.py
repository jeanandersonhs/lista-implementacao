def merge (arr, left, mid, right):
    top_left = left
    top_right = mid + 1
    temp = []
    count = 0
    
    while top_left <= mid and top_right <= right:
        # se o elemento da esquerda for menor ou igual ao da direita
        if arr[top_left] <= arr[top_right]:
            temp.append(arr[top_left])
            top_left += 1
        else:
            temp.append(arr[top_right])
            top_right += 1
            count += mid - top_left + 1
    # se ainda houver elementos na metade esquerda
    while top_left <= mid:
        temp.append(arr[top_left])
        top_left += 1
    # se ainda houver elementos na metade direita
    while top_right <= right:
        temp.append(arr[top_right])
        top_right += 1
        
    for top_left in range(len(temp)):
        arr[left + top_left] = temp[top_left]
        
    return count

def count_swaps(arr, left, right):
    """
    Implementação do merge sort modificado para contar inversões
    """
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += count_swaps(arr, left, mid)  
        count += count_swaps(arr, mid + 1, right) 
        count += merge(arr, left, mid, right)  # conta inversões durante a mesclagem
      
    return count

def main():
    numero_testes = int(input())
    result = []
    
    for _ in range(numero_testes):
        comprimento_trem = int(input())
        trens = list(map(int, input().split()))
        trens_copy = trens.copy()
        swaps = count_swaps(trens_copy, 0, comprimento_trem - 1)
        result.append(f'Optimal train swapping takes {swaps} swaps.')
    
    for linha in result:
        print(linha)

if __name__ == '__main__':
    main()