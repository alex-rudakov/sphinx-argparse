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


def _try_add_parser_attribute(data, parser, attribname):
    attribval = getattr(parser, attribname, None)
    if attribval is None:
        return

    if not isinstance(attribval, str):
        return

    if len(attribval) > 0:
        data[attribname] = attribval


def parse_parser(parser, data=None, **kwargs):
    if data is None:
        data = {'name': '', 'usage': parser.format_usage().strip()}

    _try_add_parser_attribute(data, parser, 'description')
    _try_add_parser_attribute(data, parser, 'epilog')

    for action in parser._get_positional_actions():

        if isinstance(action, _HelpAction):
            continue

        if isinstance(action, _SubParsersAction):

            helps = {}
            for item in action._choices_actions:
                helps[item.dest] = item.help

            for name, subaction in action._name_parser_map.items():
                subaction.prog = '%s %s' % (parser.prog, name)
                subdata = {
                    'name': name,
                    'help': helps[name] if name in helps else '',
                    'usage': subaction.format_usage().strip()
                }
                parse_parser(subaction, subdata, **kwargs)

                if not 'children' in data:
                    data['children'] = []
                data['children'].append(subdata)

            continue

        if not 'args' in data:
            data['args'] = []

        arg = {
            'name': action.dest,
            'help': action.help or ''
        }
        if action.choices:
            arg['choices'] = action.choices

        data['args'].append(arg)

    show_defaults = (not 'skip_default_values' in kwargs) or (kwargs['skip_default_values'] == False)

    for action in parser._get_optional_actions():

        #

        if isinstance(action, _HelpAction):
            continue

        if not 'options' in data:
            data['options'] = []

        option = {
            'name': action.option_strings,
            'default': action.default if show_defaults else '==SUPPRESS==',
            'help': action.help or ''
        }

        if action.choices:
            option['choices'] = action.choices

        data['options'].append(option)

    return data
