import re
raw = str(input())
program = []
memory_table = []
cycle_sort_pattern = r'\[(.*?)\]'
cycles_table  = re.findall(cycle_sort_pattern,raw)
cycle_number = 0
serving_cycle = 0

for letter in raw:
    if letter in ",.<>[]+-":
        program.append(letter)
program.append("END")
for i in range (30000):
    memory_table.append(0)
def process():
    global cycle_number
    bus_pos = 0
    i = 0
    while True:
        if program[i] == "+":
            memory_table[bus_pos] += 1
        elif program[i] == "-":
            memory_table[bus_pos] -= 1
        elif program[i] == "<":
            bus_pos -= 1
        elif program[i] == ">":
            bus_pos += 1
        elif program[i] == "END":
            input("Задача завершена. ")
            break
        elif program[i] == ".":
            print(chr(memory_table[bus_pos]))
        elif program[i] == ",":
            memory_table[bus_pos] = int(input())
        elif program[i] == "[":
            serving_cycle = list(cycles_table[cycle_number])
            while memory_table[bus_pos] > 1:
                for j in range(len(serving_cycle)):
                    if serving_cycle[j] == "+":
                        memory_table[bus_pos] += 1
                    elif serving_cycle[j] == "-":
                        memory_table[bus_pos] -= 1
                    elif serving_cycle[j] == "<":
                        bus_pos -= 1
                    elif serving_cycle[j] == ">":
                        bus_pos += 1
                    elif program[i] == ".":
                        print(chr(memory_table[bus_pos]))
                    elif program[i] == ",":
                        memory_table[bus_pos] = int(input())
            cycle_number += 1
        i += 1
#print("Приняты следующие инструкции: ", program, sep="")  
process()
