if __name__ == '__main__':
    # n = int(input())
    # integer_list = map(int, input().split())
    n = int(input())
    ints = input().split()
    t = tuple(int(i) for i in ints)
    print(hash(t))
    
