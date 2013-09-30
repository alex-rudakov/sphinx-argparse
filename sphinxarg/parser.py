from argparse import _HelpAction, _SubParsersAction
from collections import defaultdict
import re
import sys


class NavigationException(Exception):
    pass


def parser_navigate(parser_result, path, current_path=None):

    if isinstance(path, str):
        if path == '':
            return parser_result
        path = re.split('\s+', path)

    current_path = current_path or []

    if len(path) == 0:
        return parser_result

    if not 'children' in parser_result:
        raise NavigationException('Current parser have no children elements. (path: %s)' % ' '.join(current_path))

    next_hop = path.pop(0)

    for child in parser_result['children']:
        if child['name'] == next_hop:
            current_path.append(next_hop)
            return parser_navigate(child, path, current_path)

    raise NavigationException('Current parser have no children element with name: %s  (path: %s)' % (
        next_hop, ' '.join(current_path)
    ))


def parse_parser(parser, data=None):

    if data is None:
        data = {'name': '', 'usage': parser.format_usage()}

    for action in parser._get_positional_actions():

        if isinstance(action, _HelpAction):
            continue

        if isinstance(action, _SubParsersAction):

            helps = {}
            for item in action._choices_actions:
                helps[item.dest] = item.help

            for name, subaction in action._name_parser_map.iteritems():
                subaction.prog = '%s %s' % (parser.prog, name)
                subdata = {
                    'name': name,
                    'help': helps[name] if name in helps else '',
                    'usage': subaction.format_usage()
                }
                parse_parser(subaction, subdata)

                if not 'children' in data:
                    data['children'] = []
                data['children'].append(subdata)

            continue

        if not 'args' in data:
            data['args'] = []

        data['args'].append({
            'name': action.dest,
            'help': action.help or ''
        })

    for action in parser._get_optional_actions():

        if isinstance(action, _HelpAction):
            continue

        if not 'options' in data:
            data['options'] = []

        data['options'].append({
            'name': action.option_strings,
            'default': action.default,
            'help': action.help or ''
        })

    return data
