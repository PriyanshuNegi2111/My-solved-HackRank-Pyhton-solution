if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())   
    Tup = tuple(a)
    print(hash(Tup))
