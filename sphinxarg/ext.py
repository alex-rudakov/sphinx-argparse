from argparse import _HelpAction, _SubParsersAction
from docutils import nodes
from sphinx.util.compat import Directive
from sphinx.util.compat import make_admonition
from docutils.parsers.rst.directives import flag, unchanged, nonnegative_int
from sphinxarg.parser import parse_parser, parser_navigate


def map_nested_definitions(nested_content):

    if nested_content is None:
        raise Exception('Nested content should be iterable, not null')


    # build definition dictionary
    definitions = {}
    for item in nested_content:
        if isinstance(item, nodes.definition_list):
            for subitem in item:
                if isinstance(subitem, nodes.definition_list_item):
                    if len(subitem.children) > 0:
                        classifier = '@after'
                        idx = subitem.first_child_matching_class(nodes.classifier)
                        if not idx is None:
                            ci = subitem[idx]
                            if len(ci.children) > 0:
                                classifier = ci.children[0].astext()

                        if not classifier is None and not classifier in ('@replace', '@before', '@after'):
                            raise Exception('Unknown classifier: %s' % classifier)

                        idx = subitem.first_child_matching_class(nodes.term)
                        if not idx is None:
                            ch = subitem[idx]
                            if len(ch.children) > 0:
                                term = ch.children[0].astext()
                                idx = subitem.first_child_matching_class(nodes.definition)
                                if not idx is None:
                                    def_node = subitem[idx]
                                    def_node.attributes['classifier'] = classifier
                                    definitions[term] = def_node
    return definitions


def print_arg_list(data, nested_content):

    definitions = map_nested_definitions(nested_content)

    items = []

    if 'args' in data:
        for arg in data['args']:
            my_def = [nodes.paragraph(text=arg['help'])] if arg['help'] else []

            name = arg['name']

            my_def = apply_definition(definitions, my_def, name)

            if len(my_def) == 0:
                my_def.append(nodes.paragraph(text='Undocumented'))

            items.append(
                nodes.option_list_item('',
                    nodes.option_group('', nodes.option_string(text=name)),
                    nodes.description('', *my_def)
                )
            )

    return nodes.option_list('', *items) if items else None



def print_opt_list(data, nested_content):

    definitions = map_nested_definitions(nested_content)

    items = []

    if 'options' in data:
        for opt in data['options']:

            names = []

            my_def = [nodes.paragraph(text=opt['help'])] if opt['help'] else []

            for name in opt['name']:

                option_declaration = [nodes.option_string(text=name)]
                if not opt['default'] is None and opt['default'] != '==SUPPRESS==':
                    option_declaration += nodes.option_argument('', text='=' + str(opt['default']))

                names.append(nodes.option('', *option_declaration))

                my_def = apply_definition(definitions, my_def, name)


            if len(my_def) == 0:
                my_def.append(nodes.paragraph(text='Undocumented'))

            items.append(
                nodes.option_list_item('',
                    nodes.option_group('', *names),
                    nodes.description('', *my_def)
                )
            )

    return nodes.option_list('', *items) if items else None

def print_command_args_and_opts(arg_list, opt_list, sub_list=None):

    items = []

    if arg_list:
        items.append(nodes.definition_list_item('',
            nodes.term(text='Positional arguments:'),
            nodes.definition('', arg_list)
        ))

    if opt_list:
        items.append(nodes.definition_list_item('',
            nodes.term(text='Options:'),
            nodes.definition('', opt_list)
        ))

    if sub_list and len(sub_list):
        items.append(nodes.definition_list_item('',
            nodes.term(text='Sub-commands:'),
            nodes.definition('', sub_list)
        ))

    return nodes.definition_list('', *items)

def apply_definition(definitions, my_def, name):
    if name in definitions:
        definition = definitions[name]

        classifier = definition['classifier']

        if classifier == '@replace':
            return definition.children

        if classifier == '@after':
            return my_def + definition.children

        if classifier == '@before':
            return definition.children + my_def

        raise Exception('Unknown classifier: %s' % classifier)

    return my_def


def print_subcommand_list(data, nested_content):

    definitions = map_nested_definitions(nested_content)

    items = []

    if 'children' in data:
        for child in data['children']:

            my_def = [nodes.paragraph(text=child['help'])] if child['help'] else []
            name = child['name']
            nested_def = definitions[name] if name in definitions else []

            my_def = apply_definition(definitions, my_def, name)

            if len(my_def) == 0:
                my_def.append(nodes.paragraph(text='Undocumented'))

            my_def.append(nodes.literal_block(text=child['usage']))

            my_def.append(print_command_args_and_opts(
                print_arg_list(child, nested_content),
                print_opt_list(child, nested_content)
            ))

            items.append(
                nodes.definition_list_item(
                    '',
                    nodes.term('', '', nodes.strong(text=name)),
                    nodes.definition('', *my_def)
                )
            )

    return nodes.definition_list('', *items)



class ArgParseDirective(Directive):

    has_content = True

    option_spec = dict(module=unchanged, func=unchanged, prog=unchanged, path=unchanged)



    def run(self):

        mod = __import__(self.options['module'], globals(), locals(), [self.options['func']])
        func = getattr(mod, self.options['func'])

        parser = func()

        if not 'path' in self.options:
            self.options['path'] = ''
        path = str(self.options['path'])

        parser.prog = self.options['prog']

        result = parse_parser(parser)
        result = parser_navigate(result, path)

        nested_content = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, nested_content)
        nested_content = nested_content.children

        items = []

        # add common content between
        for item in nested_content:
            if not isinstance(item, nodes.definition_list):
                items.append(item)

        items.append(nodes.literal_block(text=result['usage']))

        items.append(print_command_args_and_opts(
            print_arg_list(result, nested_content),
            print_opt_list(result, nested_content),
            print_subcommand_list(result, nested_content)
        ))


        return items


def setup(app):
    app.add_directive('argparse', ArgParseDirective)
