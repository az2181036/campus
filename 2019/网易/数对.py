
def main():
    n, k = map(int, input().strip().split())
    sum = 0
    if n <= k:
        return sum
    if k == 0:
        return n * n
    for i in range(k+1,n+1):
        sum += n // i  * (i - k) + max(0, n%i-k+1)
    return sum

if __name__ == "__main__":
    print(main())