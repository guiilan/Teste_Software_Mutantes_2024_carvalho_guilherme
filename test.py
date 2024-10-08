import copy
import pytest
import random

from RobotSimulator import Direction, RobotSimulator

test1 = '''PLACE 0,0,NORTH
MOVE
REPORT'''

test2 = '''PLACE 0,0,NORTH
LEFT
REPORT'''

test3 = '''PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT'''


@pytest.mark.parametrize("input, expected", [(test1, '0,1,NORTH'), (test2, '0,0,WEST'), (test3, '3,3,NORTH')])
def test_given(input, expected, capfd):
	robot_simulator = RobotSimulator()
	robot_simulator.process_input(input)
	captured = capfd.readouterr()
	assert captured.out.strip() == expected


def generate_command(table_width, table_length):
	command = random.choice(verifyArray(['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT']))
	if command == 'PLACE':
		x = random.randint(0, int(1.5 * table_width))
		y = random.randint(0, int(1.5 * table_length))
		dir = random.choice(list(Direction))
		command += ' {},{},{}'.format(x, y, dir.name)

	return command

def verifyArray(ar):
    valid_commands = ['PLACE', 'MOVE', 'REPORT', 'LEFT', 'RIGHT']
    if all(command in valid_commands for command in ar):
        return ar
    else:
        return []

@pytest.mark.parametrize('execution_number', range(100))
def test_random(capfd, execution_number):
	robo_sim = RobotSimulator()
	is_valid = False

	# with capfd.disabled():
	# 	print()

	for _ in range(1_000):
		prev_robo_sim = copy.deepcopy(robo_sim)

		command = generate_command(robo_sim.table_width, robo_sim.table_length)
		robo_sim.parse_command(command)

		params = command.strip().split()
		operation = params[0]

		if not is_valid and operation != 'PLACE':
			continue

		# with capfd.disabled():
		# 	print(command)

		if operation == 'PLACE':
			x, y, dir = params[1].split(',')
			if robo_sim.is_valid_position(int(x), int(y)):
				is_valid = True
				assert robo_sim.robot_x == int(x)
				assert robo_sim.robot_y == int(y)
				assert robo_sim.robot_direction == Direction[dir.upper()]
			elif is_valid:
				assert robo_sim == prev_robo_sim
		elif operation == 'MOVE':
			prev_dir = prev_robo_sim.robot_direction
			new_x, new_y = prev_robo_sim.robot_x, prev_robo_sim.robot_y
			if (prev_dir == Direction.EAST):
				new_x += 1
			elif (prev_dir == Direction.WEST):
				new_x -= 1
			elif (prev_dir == Direction.NORTH):
				new_y += 1
			else:
				new_y -= 1

			if robo_sim.is_valid_position(new_x, new_y):
				assert robo_sim.robot_x == new_x
				assert robo_sim.robot_y == new_y
			else:
				assert robo_sim == prev_robo_sim
		elif operation == 'REPORT':
			captured = capfd.readouterr()
			x, y, dir = captured.out.strip().split('\n')[-1].split(',')
			assert robo_sim.robot_x == int(x)
			assert robo_sim.robot_y == int(y)
			assert robo_sim.robot_direction == Direction[dir.upper()]
		elif operation == 'LEFT':
			assert robo_sim.robot_direction.value == ((prev_robo_sim.robot_direction.value - 1) % 4)
		elif operation == 'RIGHT':
			assert robo_sim.robot_direction.value == ((prev_robo_sim.robot_direction.value + 1) % 4)

		assert robo_sim._is_valid_command == is_valid


test_with_err1 = '''PLACE 0,0,NORTH
	PLACE 3,0,3rR03
	REPORT'''
test_with_err2 = '''PLACE l337,n00b,NORTH
	REPORT
'''
test_with_err3 = '''PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
WRIGHT
REPORT'''


@pytest.mark.parametrize("input, expected",
                         [(test_with_err1, '0,0,NORTH'), (test_with_err2, ''), (test_with_err3, '3,3,NORTH')])
def test_exceptions(input, expected, capfd):
	robo_sim = RobotSimulator()
	robo_sim.process_input(input)
	captured = capfd.readouterr()
	assert captured.out.strip() == expected