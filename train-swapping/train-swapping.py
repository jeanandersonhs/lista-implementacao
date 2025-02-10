import numpy as np
import sys 


# tempo limite excedido ta em n²

def train_swaping(n, arr):
    count = 0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count




def main():
    numero_testes = int(input())
    result = []
    for _ in np.arange(numero_testes):
        comprimento_trem = int(input())
        trens = np.array(list(map(int, input().split())))
        result.append(f'Optimal train swapping takes {train_swaping(comprimento_trem, trens)} swaps.')

    for i in result:
        print(i)

if __name__ == '__main__':
    main()