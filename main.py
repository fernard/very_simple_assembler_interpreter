from assember_interpreter import AssemblerInterpreter

# Ask user for file with instructions and register length
program_name = input("Enter the name of the file with its relative path: \n")
bit_size = int(input("Enter the the size of register in bits: \n"))

# Create new instances of interpreter and calculator
assembler_interpreter = AssemblerInterpreter(bit_size)

if __name__ == "__main__":
    assembler_interpreter.read(program_name)
