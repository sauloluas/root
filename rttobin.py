import re
import sys
from binmap import *

instructions = [
    'nop', '.', 'loads', 'keeps', 'stores', 'copies', 'is',
    '+', '-', '*', '/', '%', 'not', 'and', 'or', 'xor',
    'store:sums', 'load:sums', 'keep:sums', 'copy:sums', 'assign:sums', 
    'store:mults', 'load:mults',
    'keep:not'
]

registers = ['reg', 'regB', 'cell']

def parse_code_source(source):
    if source[-1] == 'h':
        return source[:-1]
    elif source in registers:
        return register[source]
    else:
        return str(int(source, 16))

def rttobin(filename):
    filename = filename.replace('.rt', '')

    with open(f'{filename}.rt', 'r') as file:    
        while True:
            line = file.readline()

            # print(line)

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
                        b = 'nop'
                        a = None
                        # break 
                    case 'keep:not':
                        # 'not',  'b' -> 'b', 'not', ''
                        a, b = b, a
                        c = None
                        # break
                    case '.':
                        b = '.'
                        a = None
                        # break
            elif a[-1] == 'h':
                pass        # op type detection

            if b not in instructions:
                print(f'Instrução inválida: "{b}"', file=sys.stderr)
                print(line)

            if (a != None) and (a[-1] != 'h') and (a not in registers):
                print(f'Destino inválido: "{a}"', file=sys.stderr)
                print(line)

            if (c != None) and (c[-1] != 'h') and (c not in registers) and (not c.isnumeric()):
                print(f'Origem inválida: {c}', file=sys.stderr)
                print(line)

            instruction = b
            target = a
            source = c

            
            code_target = '00' if target is None else code_target

            code_instruction = operation[instruction]
            # print(target[:-1])
            code_target = target[:-1].rjust(2, '0') if target[-1] == 'h' else register[target]
            code_source = parse_code_source(source).rjust(2, '0') if (source is not None) else '00'


            code = code_instruction + code_target + code_source
            print(code)