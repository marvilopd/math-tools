mport math
l = []

def greet():
    return """This is a programm to find all the prime numbers from lower intervall to the upper intervall its inspired by the Sieve of Eratosthenes algorhitm"""
    

def var():
    while True:
            try:
                lower_interval = int(input("Lower interval: "))
                upper_interval = int(input("Upper interval: "))
                break
            except ValueError:
                print("Please enter an Int")

    prime_number_checker(lower_interval, upper_interval)



def main():
    print(greet())
    var()
    print(l)
   


def prime_number_checker(m, n):
    try:
        for num in range(m, n+1):
            is_prime = True
            for divider in range(2, int(math.sqrt(num)+1)):
                if num % divider == 0:
                    is_prime = False
                    pass
            if is_prime and num != 0 and num != 1:
                l.append(num)
    except ValueError:
        print("Please enter an integer")


if __name__ == "__main__":
    main()
