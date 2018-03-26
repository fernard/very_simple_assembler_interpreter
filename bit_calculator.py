import sys

class BitCalculator:

    def __init__(self, bit_size):
        self.bit_size = bit_size

    @staticmethod
    def bit_to_integer(bits: str):
        try:
            return sum([int(bit) * (2 ** power)
                        if bit == "0" or bit == "1" else "raise Exception"
                        for power, bit in enumerate(bits[::-1])])
        except Exception as e:
            print("It's not a valid binary %r" % e)

    def decimal_to_binary(self, decimal: int):

        result = ''
        if decimal == 0:
            result = "0"
        if decimal < 0:
            decimal = self.bit_to_integer("1" * self.bit_size) + decimal
        while decimal > 0:
            result = str(decimal % 2) + result
            decimal = decimal // 2
        if len(result) <= self.bit_size:
            result = "0" * (self.bit_size - len(result)) + result
        else:
            alert = input("The register is too short to store such numbers. Want to exit? (y/n)")
            if alert == "y":
                sys.exit()
            else:
                raise BaseException("Exited!")
        return result

    def add(self, register:str):
        decimal = self.bit_to_integer(register) + 1
        return self.decimal_to_binary(decimal)

    def subtract(self, register:str):
        decimal = self.bit_to_integer(register) - 1
        return self.decimal_to_binary(decimal)

