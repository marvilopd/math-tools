import math 
from math import radians 


def main():
    print(" sin: to find the sine of your given angle\n cos: to find the cosine of your given angle\n tan: to find the tangent of your given angle")
    try:
        Function = input("Enter trig. function: ")
        Value = float(input("Enter the angle in degrees: "))
    
        if Function.upper() == "SIN":
            Value = radians(Value)
            print(round(math.sin(Value), 10))
        elif Function.upper() == "COS":
            Value = radians(Value)
            print(round(math.cos(Value), 10))
        elif Function.upper() == "TAN":
            if round(Value % 180) == 90:
                print("Undefined")
            else:
                Value = radians(Value)
                print(round(math.tan(Value), 10))
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()