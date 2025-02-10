

def merge_sort(lista, inicio=0, fim=None):
   if fim is None:
        fim = len(lista)
   
   count = 0 
   if (fim - inicio > 1):
      meio = (inicio + fim) // 2 
      count += merge_sort(lista, inicio, meio)
      count += merge_sort(lista, meio, fim)
      count += merge(lista, inicio, meio, fim)
   return count

def merge(lista, inicio, meio, fim):
   left = lista[inicio:meio] # pega elementos desde o inicio até o meio
   right = lista[meio:fim] # pega elementos desde o meio até o fim
   top_left,top_right = 0,0
   count = 0

   for _ in range(inicio, fim):
      if top_left >= len(left):
          lista[_] = right[top_right]
          top_right += 1
      elif top_right >= len(right):
         lista[_] = left[top_left]
         top_left += 1
      elif left[top_left] <= right[top_right]:
         lista[_] = left[top_left]
         top_left += 1
      else:
        lista[_] = right[top_right]
        top_right += 1
        count += len(left) - top_left 
        print("CONTAGEM",count)
   

   return count


def train_swaping():
    
    numero_testes = int(input())
    result = []
    
    for _ in range(numero_testes):
        comprimento_trem = int(input())
        trens = list(map(int, input().split()))
        trens_copy = trens.copy()
        swaps = merge_sort(trens_copy, 0, comprimento_trem)
        result.append(f'Optimal train swapping takes {swaps} swaps.')
    
    for linha in result:
        print(linha)

if __name__ == '__main__':
    train_swaping()