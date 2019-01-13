import random
import sys

file = open(sys.argv[1], 'r')
contents = file.readlines()
seed = int(contents[0])
maxint = int(contents[1])
program = "".join(contents[2:])
random.seed(seed)

tape = [random.randint(-maxint, maxint) for i in range(random.randint(1,maxint))]

# Thou slimey space kraken! You are as dumb as the Kerbals and as smart as paint! Thou equivalency to a space kraken is more than the one of an ostrich!

accumulator = random.randint(-maxint, maxint)
pointer = 0
instructions = random.sample([chr(i) for i in range(32, 127)], 6)
pos = 0


while pos < len(program):
	if program[pos] == instructions[0]:
		try:
			sys.stdout.write(chr(tape[pointer]))
		except:
			pass
	elif program[pos] == instructions[1]:
		accumulator = ord(sys.stdin.read(1)) * random.randint(-maxint, maxint)
	elif program[pos] == instructions[2]:
		accumulator = random.randint(-maxint, maxint)
	elif program[pos] == instructions[3]:
		tape[pointer] = accumulator
	elif program[pos] == instructions[4]:
		pointer += 1 if pointer < len(tape) - 1 else 0
	elif program[pos] == instructions[5]:
		pos = tape[pointer]
	pos += 1


