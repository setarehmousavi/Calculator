class Calculater:
    def __init__(self):
        """initialize history list"""
        self.history = []

    def calculate(self,num1,op,num2):
        try:
            if op == "+" :
                result = num1 + num2 
            elif op == "-":
                result = num1 - num2 
            elif op == "*":
                result = num1 * num2 
            elif op == "/":
                if num2 == 0:
                    result = "error division"
                else: 
                    result = num1 / num2
            elif op == "**":
                result = num1 ** num2
            else : 
                result = "invalid operator"

            #store data in history
            self.history.append(f"{num1} {op} {num2} = {result}")
            return result
        except ValueError:
            return "invalid input , please try again!"

    def show_history(self):
        print ("\n--- calculation history ---") 
        for entry in self.history:
            print(entry)

if __name__ == "__main__":
    cal = Calculater()


    while True :
        try:
            num1 = float(input("enter first number: "))
            op = input ("enter operator(+ ,- ,* , / , **): ")
            num2 = float(input("enter second number: "))

            result = cal.calculate(num1,op,num2)
            print(f"Result : {result}")
        except ValueError:
            print ("invalid input , please try again!")

        cont = input ("do you want to continue? (y/n): ").lower()
        if cont != "y":
            print ("thanks,Bye.")
            break

    cal.show_history()

  
  
  
  
  
  
  
  

