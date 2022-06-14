def main(lock1, lock2) :
    for i in range(0, 10000) :
        if lock1 == i and i%2 == 0 :
            print(1)
            exit()
        if lock2 == i and i%2 == 1 :
            print(1)
            exit()
    print(0)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    main(a, b)

