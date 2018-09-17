def organize(l):
    print(l)
    for p in range(len(l)-1):
        for i in range(0,len(l)-1-p):
            if l[i] > l[i+1]:
                t = l[i]
                l[i] = l[i+1]
                l[i+1] = t

    print(l)

if __name__ == '__main__':
    l = [54,26,93,17,77,31,44,55,20]
    organize(l)

