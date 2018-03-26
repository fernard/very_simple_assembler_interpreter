from bit_calculator import  BitCalculator


class AssemblerInterpreter:

    def __init__(self, bit_size):
        self.bit_size = bit_size
        self.program_list = []
        self.registers = dict()
        self.bit_calculator = BitCalculator(bit_size)

    def read(self, program_name: str):
        with open(program_name, 'r') as program:
            for line in program:
                instruction = line.strip('\n').split(" ")
                self.program_list.append(instruction)

        self.run_program(self.program_list)

    def run_program(self, program_list: list):
        index = 0
        while index < len(program_list):
            current_instruction = program_list[index]
            name, reg, val = (current_instruction + [0])[:3]

            if name == "jnz":

                ''' We consider two scenarios: Either the register's name is present in the dictionary and if
                    it doesn't equal 0, we jump accordingly in the program. The other option is that the register 
                    is not in the dictionary, which means it is a constant
                '''
                if (
                    reg in self.registers and self.registers[reg] != ("0" * self.bit_size)
                    or
                    reg not in self.registers and int(reg) != 0
                ):

                    index += int(val) - 1

            elif name == "mov":

                    ''' If the value exists on the dictionary, it means that it is one of the registers
                        and we assign its value to the current register. Otherwise we set the value of the register
                        to the number
                    '''

                    if val in self.registers:
                        self.registers[reg] = self.registers[val]
                    else:
                        value = int(val)
                        self.registers[reg] = self.bit_calculator.decimal_to_binary(value)

            elif name == "inc":
                    self.registers[reg] = self.bit_calculator.add(self.registers[reg])

            elif name == "dec":
                    self.registers[reg] = self.bit_calculator.subtract(self.registers[reg])

            index += 1

        for k,v in sorted(self.registers.items()):
            print(f'Register {k}: {self.registers[k]}')
