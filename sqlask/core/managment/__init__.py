import sqlask
import sys
import os

class Managment(object):

	def __init__(self, argv=None):
		self.argv = argv or sys.argv[:]
		self.command_arg0 = os.path.basename(self.argv[0])
		self.command_arg1 = os.path.basename(self.argv[1]) or None

	def process(self):
		print("You Entered")
		print(self.command_arg0)
		print(self.command_arg1)

def main(argv=None):
    print("Executing command")
    management = Managment(argv)
    management.process()