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

                register = self.registers.get(reg)
                if register and register != ("0" * self.bit_size):
                    index += int(val)
                elif register is None:
                    if int(reg) != 0:
                        index += int(val)
                    else:
                        index += 1
                else:
                    index += 1
            else:
                index += 1
                if name == "mov":
                    try:
                        value = int(val)
                        self.registers[reg] = self.bit_calculator.decimal_to_binary(value)
                    except:
                        self.registers[reg] = self.registers[val]
                elif name == "inc":
                    self.registers[reg] = self.bit_calculator.add(self.registers[reg])

                elif name == "dec":
                    self.registers[reg] = self.bit_calculator.subtract(self.registers[reg])

        for k,v in sorted(self.registers.items()):
            print(f'Register {k}: {self.registers[k]}')
