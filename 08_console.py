from typing import List, Tuple


class Inst:
    def __init__(self, opcode, value):
        self.opcode = opcode
        self.value = int(value)


def run(instructions: List[Inst]) -> Tuple[bool, int]:
    """
    Run a boot code program.
    :param instructions: A list of Insts representing the program.
    :return: A tuple (success, accumulator)
    """
    pc = 0
    acc = 0
    visited = set()

    while pc not in visited and pc < len(instructions):
        visited.add(pc)
        inst = instructions[pc]
        if inst.opcode == "nop":
            pc += 1
        elif inst.opcode == "acc":
            acc += inst.value
            pc += 1
        else:
            pc += inst.value

    if pc in visited:
        return False, acc
    else:
        return True, acc


with open("inputs/8") as f:
    instructions = [Inst(*instr.split(" ")) for instr in
                    f.read().rstrip().split("\n")
                    ]


# Problem 1
print(run(instructions)[1])

for i in range(len(instructions)):
    inst = instructions[i]
    if inst.opcode == "acc":
        continue

    new_inst = Inst("jmp" if inst.opcode == "nop" else "nop", inst.value)
    instructions[i] = new_inst
    result = run(instructions)
    if result[0]:
        # Problem 2
        print(result[1])
        break

    instructions[i] = inst
