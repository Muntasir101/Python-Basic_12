class Calculate:

    def summation(self, number1, number2):
        return number1 + number2

    def subtract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        return number1 / number2


if __name__ == '__main__':
    obj = Calculate()
    print(obj.summation(10, 200))
    print(obj.subtract(20, 200))
    print(obj.multiply(30, 300))
    print(obj.divide(30, 300))
