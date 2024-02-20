# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:09:10 2023

@author: Marko
"""

def process_memory_instructions(instructions, memory_state):
    for instruction in instructions:
        operation, address1, address2 = instruction

        if operation == "move":
            memory_state[address2] = memory_state[address1]
        elif operation == "store":
            memory_state[address1] = address2

    return {hex(address): hex(value) for address, value in memory_state.items()}

memory_instructions = [
    ("move", 0x03, 0x00),
    ("store", 0x01, 0x02),
    ("move", 0x01, 0x03)
]

memory_state = {
    0x00: 0xAB,
    0x01: 0x53,
    0x02: 0xD6,
    0x03: 0x02
}

result = process_memory_instructions(memory_instructions, memory_state)
print(result)