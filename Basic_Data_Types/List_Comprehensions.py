if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final_list =[]
    for i in range(1+x):
        for j in range(y+1):
            for k in range(1+z):
                if i+j+k!=n:
                    temp=[i,j,k]
                    final_list.append(temp)
                else:
                    continue
    print(final_list)

    # In List_Comprehensions
    # print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
