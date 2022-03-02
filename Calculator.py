# Program make a simple calculator

# This function adds two numbers
class Calculator:
    def add(self, x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(self, x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
        return x / y
    def power(self, x, y):
        return x**y
    def start(self):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Power")

        while True:
            # take input from the user
            choice = input("Enter choice(1/2/3/4): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4','5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print (num1, num2)
                    x = self.add(num1, num2)
                    print(num1, "+", num2, "=",x )

                elif choice == '2':
                    print(num1, "-", num2, "=", self.subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", self.multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", self.divide(num1, num2))
                elif choice == '5':
                    print(num1, "**", num2, "=", self.power(num1, num2))
                
                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                  break
            
            else:
                print("Invalid Input")

if __name__ == '__main__':
    calculator = Calculator()
    calculator.start()


