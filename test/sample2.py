import argparse


def blah():
    parser = argparse.ArgumentParser(description="""
### Example of MarkDown inside programs

[I'm a link](http://www.google.com)
""")
    parser.add_argument('cmd', help='execute a `command`')
    return parser
