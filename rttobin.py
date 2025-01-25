import re

instructions = ['nop', '.', 'loads', 'keeps', 'stores', 'copies', 'is', '+', '-', '*', '/', '%', 'not', 'and', 'or', 'xor']

def rttobin(filename):
    filename = filename.replace('.rt', '')

    with open(f'{filename}.rt', 'r') as file:    
        while True:
            line = file.readline()
            
            if not line:
                break

            if line == '\n':
                continue

            line = line.strip('\n') # remove newline character
            
            splitted = re.split(r'\s+', line) # split line by whitespace

            a = splitted[0]
            b = splitted[1] if len(splitted) > 1 else None
            c = splitted[2] if len(splitted) > 2 else None

            if a in instructions:
                match a:
                    case '-':
                        a = 'nop'
                        break 
                    case 'not':
                        # 'not',  'b' -> 'b', 'not', ''
                        a, b = b, a
                        c = None