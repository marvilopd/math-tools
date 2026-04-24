import math

def greeting():
    print("""    Hello user
    -Enter a base
    -Enter the growth factor
    -Enter the hours/days/week etc.""")
    

def main():
    greeting()
    Base = float(input("Enter a base: "))
    Growth_factor = float(input("Enter the growth factor: "))
    Time = int(input("Enter time: "))
    print(f"result is {calculate(Base, Growth_factor, Time)}")
    
    

def calculate(b, g, t):
   result = b * g ** t
   
   return result


if __name__ == "__main__":
    main()