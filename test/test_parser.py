import argparse
import json
from pprint import pprint
from sphinxarg.parser import parse_parser, parser_navigate


def test_parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', default=False, help='foo help')
    parser.add_argument('--bar', action='store_true', default=False)

    data = parse_parser(parser)

    assert data['options'] == [
        {
            'name': ['--foo'],
            'default': False,
            'help': 'foo help'
        }, {
            'name': ['--bar'],
            'default': False,
            'help': ''
        },
    ]


def test_parse_positional():
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', default=False, help='foo help')
    parser.add_argument('bar', default=False)

    data = parse_parser(parser)

    assert data['args'] == [
        {
            'name': 'foo',
            'help': 'foo help'
        }, {
            'name': 'bar',
            'help': ''
        },
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
            'help': 'foo help'
        }, {
            'name': 'bar',
            'help': ''
        },
    ]

    assert data['children'] == [
        {
            'name': 'install',
            'help': 'install help',
            'usage': 'usage: py.test install [-h] [--upgrade] ref\n',
            'args': [
                {
                    'name': 'ref',
                    'help': 'foo1 help'
                },
            ],
            'options': [
                {
                    'name': ['--upgrade'],
                    'default': False,
                    'help': 'foo2 help'
                },
            ]
        },
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
            'help': 'foo help'
        }, {
            'name': 'bar',
            'help': ''
        },
    ]

    data2 = parser_navigate(data, 'level1 level2')
    assert data2['children'] == [
                {
                    'name': 'level3',
                    'help': '',
                    'usage': 'usage: py.test level1 level2 level3 [-h] foo bar\n',
                    'args': [
                        {
                            'name': 'foo',
                            'help': 'foo help'
                        },
                        {
                            'name': 'bar',
                            'help': ''
                        },
                    ],
                }
            ]

    assert data == parser_navigate(data, '')