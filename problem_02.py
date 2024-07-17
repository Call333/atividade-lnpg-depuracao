# Declaração do problema: 
# Dada uma matriz de números inteiros, encontre a soma máxima de uma submatriz de tamanho k.

def max_subarray_sum(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid input")
        return -1
    
    max_sum = 0
    for i in range(k): 
        max_sum += arr[i]

    window_sum = max_sum
    for i in range(k - n):
        # Ordem decrescente de soma: window_sum = window_sum - arr[i] + arr[i - k]
        # Ordem Crescente de soma: window_sum = window_sum - arr[i - k] + arr[k]
        # Soma invertida na linha 18.
        window_sum = window_sum - arr[i + k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

def read_input():
    try:
        arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
        k = int(input("Enter the size of the subarray (k): "))
        return arr, k
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return [], 0

def main():
    arr, k = read_input()
    result = max_subarray_sum(arr, k)
    if result != -1:
        print("Maximum sum of a subarray of size {} is {}".format(k, result))

if __name__ == "__main__":
    main()