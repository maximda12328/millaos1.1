import random
import time
import psutil



print ("hi user")
while True:
    aCommand = (input("enter the operations command "))
    if aCommand == "calc":
            # Function to add two numbers
        def add(x, y):
            return x + y

        # Function to subtract two numbers
        def subtract(x, y):
            return x - y

        # Function to multiply two numbers
        def multiply(x, y):
            return x * y

        # Function to divide two numbers
        def divide(x, y):
            return x / y

        # Main function to run the calculator
        def main():
            print("Select operation.")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = input("Enter choice (1/2/3/4): ")

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                if num2 == 0:
                    print("Error: cannot divide by 0")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
            
            else:
                print("Invalid input")

        # Run the calculator
        main()

    if aCommand == "random":
        random_number = random.randint(1, 110)
        print("Random number:", random_number)

    if aCommand == "timer":
        start = time.time()  # Запустить секундомер

        while True:
            elapsed_time = time.time() - start
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs))
            print(timer, end='\r')




    

    if aCommand == "pip admin"  :
        adminCommand = input("pip adminCommand: ")
        if adminCommand == "memory-":
            process = psutil.Process()
            memory = process.memory_info().rss
            print("Memory busy:", memory, "byte")
        if adminCommand == "memory+":
                        # Get system memory information
            mem = psutil.virtual_memory()

            # Print the amount of free memory in megabytes
            print(f"Free memory: {mem.available / 1024 / 1024:.2f} MB")

        

            


