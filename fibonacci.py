def fibonacci_series(val):
    assert val > 0
    firstnum=0
    secondnum=1
    finallist = []
    finallist.append(firstnum)
    finallist.append(secondnum)
    while True:
        fib=firstnum+secondnum
        firstnum=secondnum
        secondnum=fib
        if secondnum < val :
            finallist.append(fib)
            continue
        else:
            break
    fibonacci=str(finallist)
    print(fibonacci[1:-1])

def main():
    range=int(input("Enter the number till you want fibonacci series: "))
    fibonacci_series(range)

if __name__ == '__main__':
    main()
