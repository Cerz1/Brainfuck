class BrainfuckInterpreter:
    def __init__(self, file_path):
        # Open the file in read mode and save the content in self.brainfuck_code
        with open(file_path, 'r') as file:
            self.brainfuck_code = file.read()
        # Initialize an array of zeros of length 30000 (as per Brainfuck specifications)
        self.array = [0] * 30000
        # The array pointer initially points to position 0
        self.ptr = 0

    def interpret(self):
        # Initialize an empty string for the translation
        translation = ''
        i = 0
        # Iterate over each symbol in the Brainfuck code
        while i < len(self.brainfuck_code):
            symbol = self.brainfuck_code[i]

            if symbol == '>':
                # If the symbol is '>', increment the pointer
                self.ptr += 1
            elif symbol == '<':
                # If the symbol is '<', decrement the pointer
                self.ptr -= 1
            elif symbol == '+':
                # If the symbol is '+', increment the value at the position pointed by the pointer
                self.array[self.ptr] = (self.array[self.ptr] + 1) % 256
            elif symbol == '-':
                # If the symbol is '-', decrement the value at the position pointed by the pointer
                self.array[self.ptr] = (self.array[self.ptr] - 1) % 256
            elif symbol == '.':
                # If the symbol is '.', add the character corresponding to the ASCII value at the position pointed by the pointer to the translation
                translation += chr(self.array[self.ptr])
            elif symbol == '[':
                # If the symbol is '[', and the value at the position pointed by the pointer is 0, skip ahead to the corresponding ']'
                if self.array[self.ptr] == 0:
                    open_brackets, close_brackets = 1, 0
                    while open_brackets != close_brackets:
                        i += 1
                        if self.brainfuck_code[i] == '[':
                            open_brackets += 1
                        elif self.brainfuck_code[i] == ']':
                            close_brackets += 1
            elif symbol == ']':
                # If the symbol is ']', and the value at the position pointed by the pointer is not 0, skip back to the corresponding '['
                open_brackets, close_brackets = 1, 0
                while open_brackets != close_brackets:
                    i -= 1
                    if self.brainfuck_code[i] == '[':
                        open_brackets -= 1
                    elif self.brainfuck_code[i] == ']':
                        close_brackets += 1
                i -= 1

            i += 1

        # Return the translation
        return translation

# Create an instance of the interpreter with the name of the Brainfuck file
interpreter = BrainfuckInterpreter('TestBrainfuck.txt')

# Print the translation of the Brainfuck code
print(interpreter.interpret())