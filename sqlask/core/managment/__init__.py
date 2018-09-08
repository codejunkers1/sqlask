"""
	Author = Venkata Sai Katepalli
"""

import sqlask
import sys
import os
import pkgutil

class Managment(object):

	def __init__(self, argv=None):
		self.argv = argv or sys.argv[:]


	def get_all_commands(self):
	    """
	    Given a path to a management directory, returns a list of all the command
	    names that are available.

	    Returns an empty list if no commands are defined.
	    """
	    command_dir = os.path.join(__path__[0], 'commands')
	    commands = [name for ins, name, is_pkg in pkgutil.iter_modules([command_dir])
	            if not is_pkg and not name.startswith('_')]
	    return commands


	def check_command(self, command):
		all_commands = self.get_all_commands()
		print(all_commands)
		if command in all_commands:
			print(command+" Processing. Please wait...")
		else:
			print('Invalid Command...:(')


	def process(self):
		# get the required operation command
		try:
			command = self.argv[1]
		except Exception as e:
			command = 'help'
		# if any operation requied or else help
		if command == 'help':
			print("Use some operations.")
		else:
			self.check_command(command)


def main(argv=None):
    print("Executing command")
    management = Managment(argv)
    management.process()