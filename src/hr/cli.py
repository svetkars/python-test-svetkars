import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Manage users on a server based JSON inventory file.
    """)
    parser.add_argument('path', help='the path to the inventory file (JSON).')
    parser.add_argument('--export', action='store_true', help='export current settings to the inventory file')
    return parser
