

def collatz(number) -> object:
    if number % 2 == 0:
        print(number, "// 2 = ", number // 2)
        number = number // 2
        return number
    else:
        print("3 *", number, "+ 1 = ",  3 * number + 1)
        number = 3 * number + 1
        return number


print('Enter an integer: ')
userNumber = input()

while userNumber != 1:
    userNumber = collatz(int(userNumber))
