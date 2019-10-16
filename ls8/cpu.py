"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 255
        self.pc = 0
        self.register = [0] * 8
        self.running = True
        self.garbage = []

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def load_management(self, filename):
        try:
            address = 0

            with open(filename) as f:
                for line in f:
                    # ignore comments
                    comment_split = line.split("#")

                    # Convert from binary to int
                    num = comment_split[0].strip()
                    
                    #try:
                        
                    print(comment_split)
                    if len(num) == 8:
                        print(f'{type(num)}: {len(num)} {num} FOOBAR')
                        val = int(num, 2)
                        print(f'{val} TEST TEST')
                        self.ram[address] = val
                        address += 1
                    else:
                        self.garbage.append(num)
                    #except ValueError:
                        #continue
                    
                    #print(f"{val:08b}: {val:d}: {val}")
            print(self.garbage)
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)
            
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.register[i], end='')

        print()

    def run(self):
        #ir = self.ram[self.pc]
        operand_a = self.ram_read(self.pc+1)
        print(f'{operand_a} foo')
        operand_b = self.ram_read(self.pc+2)
        print(f'{operand_b} bar')
        self.trace()
        #print(self.ram[self.pc+1])
        #print(self.ram[self.pc+2])
        print(self.ram)
        while self.running:
            command = self.ram[self.pc]
            #print(f'{command} this is the command')
            #LDI - set value of register to integer
            if command == 130:
                self.register[operand_a] = operand_b
                #print(self.pc)
                #print(ir)
                #print(f'{self.ram} NAME')
                self.pc += 3
                #print(f'{self.pc} FOOOOO')
            #HLT - stops the program
            elif command == 1:
                self.running = False
                self.pc += 1
            #PRN - prints next digit in register
            elif command == 71:
                num = print(self.ram[self.pc+1])
                self.pc += 2
    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
