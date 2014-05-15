import argparse

parser = argparse.ArgumentParser()

parser.add_subparsers()



parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers()

my_command1 = subparsers.add_parser('apply', help='Execute provision script, collect all resources and apply them.')

my_command1.add_argument('path', help='Specify path to provision script. provision.py in current'
                                             'directory by default. Also may include url.', default='provision.py')
my_command1.add_argument('-r', '--rollback', action='store_true', default=False, help='If specified will rollback all'
                                                                               'resources applied.')
my_command1.add_argument('--tree', action='store_true', default=False, help='Print resource tree')
my_command1.add_argument('--dry', action='store_true', default=False, help='Just print changes list')
my_command1.add_argument('--force', action='store_true', default=False, help='Apply without confirmation')


my_command2 = subparsers.add_parser('game')
my_command2.add_argument('move', choices=['rock', 'paper', 'scissors'], help='Choices for argument example')
my_command2.add_argument('--opt', choices=['rock', 'paper', 'scissors'], help='Choices for option example')


