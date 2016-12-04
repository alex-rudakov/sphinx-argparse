import argparse
from sphinxarg.parser import parse_parser, parser_navigate


def test_parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', default=False, help='foo help')
    parser.add_argument('--bar', action='store_true', default=False)

    data = parse_parser(parser)

    assert data['action_groups'][0]['options'] == [
        {
            'name': ['--foo'],
            'default': False,
            'help': 'foo help'
        }, {
            'name': ['--bar'],
            'default': False,
            'help': ''
        }
    ]


def test_parse_default():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default='123')

    data = parse_parser(parser)

    assert data['action_groups'][0]['options'] == [
        {
            'name': ['--foo'],
            'default': '"123"',
            'help': ''
        }
    ]


def test_parse_arg_choices():
    parser = argparse.ArgumentParser()
    parser.add_argument('move', choices=['rock', 'paper', 'scissors'])

    data = parse_parser(parser)

    assert data['args'] == [
        {
            'name': 'move',
            'help': '',
            'choices': ['rock', 'paper', 'scissors'],
            'metavar': None
        }
    ]


def test_parse_opt_choices():
    parser = argparse.ArgumentParser()
    parser.add_argument('--move', choices=['rock', 'paper', 'scissors'])

    data = parse_parser(parser)

    assert data['action_groups'][0]['options'] == [
        {
            'name': ['--move'],
            'default': None,
            'help': '',
            'choices': ['rock', 'paper', 'scissors']
        }
    ]


def test_parse_default_skip_default():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', default='123')

    data = parse_parser(parser, skip_default_values=True)

    assert data['action_groups'][0]['options'] == [
        {
            'name': ['--foo'],
            'default': '==SUPPRESS==',
            'help': ''
        }
    ]


def test_parse_positional():
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', default=False, help='foo help')
    parser.add_argument('bar', default=False)

    data = parse_parser(parser)

    assert data['args'] == [
        {
            'name': 'foo',
            'help': 'foo help',
            'metavar': None
        }, {
            'name': 'bar',
            'help': '',
            'metavar': None
        }
    ]


def test_parse_description():
    parser = argparse.ArgumentParser(description='described', epilog='epilogged')
    parser.add_argument('foo', default=False, help='foo help')
    parser.add_argument('bar', default=False)

    data = parse_parser(parser)

    assert data['description'] == 'described'

    assert data['epilog'] == 'epilogged'

    assert data['args'] == [
        {
            'name': 'foo',
            'help': 'foo help',
            'metavar': None
        }, {
            'name': 'bar',
            'help': '',
            'metavar': None
        }
    ]


def test_parse_nested():
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', default=False, help='foo help')
    parser.add_argument('bar', default=False)

    subparsers = parser.add_subparsers()

    subparser = subparsers.add_parser('install', help='install help')
    subparser.add_argument('ref', type=str, help='foo1 help')
    subparser.add_argument('--upgrade', action='store_true', default=False, help='foo2 help')

    data = parse_parser(parser)

    assert data['args'] == [
        {
            'name': 'foo',
            'help': 'foo help',
            'metavar': None
        }, {
            'name': 'bar',
            'help': '',
            'metavar': None
        }
    ]

    assert data['children'] == [
        {
            'name': 'install',
            'help': 'install help',
            'usage': 'usage: py.test install [-h] [--upgrade] ref',
            'bare_usage': 'py.test install [-h] [--upgrade] ref',
            'args': [
                {
                    'name': 'ref',
                    'help': 'foo1 help',
                    'metavar': None
                },
            ],
            'action_groups': [
                {
                    'description': None,
                    'title': 'optional arguments',
                    'options': [
                        {
                            'name': ['--upgrade'],
                            'default': False,
                            'help': 'foo2 help'
                        },
                    ]
                }
            ]
        }
    ]


def test_parse_nested_traversal():
    parser = argparse.ArgumentParser()

    subparsers1 = parser.add_subparsers()
    subparser1 = subparsers1.add_parser('level1')

    subparsers2 = subparser1.add_subparsers()
    subparser2 = subparsers2.add_parser('level2')

    subparsers3 = subparser2.add_subparsers()
    subparser3 = subparsers3.add_parser('level3')

    subparser3.add_argument('foo', help='foo help')
    subparser3.add_argument('bar')

    data = parse_parser(parser)

    data3 = parser_navigate(data, 'level1 level2 level3')

    assert data3['args'] == [
        {
            'name': 'foo',
            'help': 'foo help',
            'metavar': None
        }, {
            'name': 'bar',
            'help': '',
            'metavar': None
        }
    ]

    data2 = parser_navigate(data, 'level1 level2')
    assert data2['children'] == [
        {
            'name': 'level3',
            'help': '',
            'usage': 'usage: py.test level1 level2 level3 [-h] foo bar',
            'bare_usage': 'py.test level1 level2 level3 [-h] foo bar',
            'args': [
                {
                    'name': 'foo',
                    'help': 'foo help',
                    'metavar': None
                },
                {
                    'name': 'bar',
                    'help': '',
                    'metavar': None
                }
            ]
        }
    ]

    assert data == parser_navigate(data, '')


def test_fill_in_default_prog():
    """
    Ensure that %(default)s and %(prog)s are getting properly filled in inside help=''
    """
    parser = argparse.ArgumentParser(prog='test_fill_in_default_prog')
    parser.add_argument('bar', default='foo', help='%(prog)s (default: %(default)s)')
    data = parse_parser(parser)

    assert data['args'] == [
        {
            'metavar': None,
            'name': 'bar',
            'help': 'test_fill_in_default_prog (default: foo)'
        }
    ]


def test_string_quoting():
    """
    If an optional argument has a string type and a default, then the default should be in quotes.
    This prevents things like '--optLSFConf=-q short' when '--optLSFConf="-q short"' is correct.
    """
    parser = argparse.ArgumentParser(prog='test_string_quoting_prog')
    parser.add_argument('--bar', default='foo bar', help='%(prog)s (default: %(default)s)')
    data = parse_parser(parser)

    assert data['action_groups'][0]['options'] == [
        {
            'default': '"foo bar"',
            'name': ['--bar'],
            'help': 'test_string_quoting_prog (default: "foo bar")'
        }
    ]


def test_parse_groups():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', default=False, help='foo help')
    parser.add_argument('--bar', action='store_true', default=False)
    optional = parser.add_argument_group('Group 1')
    optional.add_argument("--option1", help='option #1')
    optional.add_argument("--option2", help='option #2')

    data = parse_parser(parser)
    assert data['action_groups'] == [
        {
            'description': None,
            'options': [
                {'default': False, 'help': 'foo help', 'name': ['--foo']},
                {'default': False, 'help': '', 'name': ['--bar']}],
            'title': 'optional arguments'},
        {
            'description': None,
            'options': [
                {'default': None, 'help': 'option #1', 'name': ['--option1']},
                {'default': None, 'help': 'option #2', 'name': ['--option2']}],
            'title': 'Group 1'
        }
    ]
