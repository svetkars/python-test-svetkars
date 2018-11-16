from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_no_argument(parser):
    """
    Without a specified path, the parser will exit with an error.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_succeeds_with_a_path(parser):
    """
    The parser will not exit if it receives a path as
    an argument.
    """
    args = parser.parse_args(['/some/path'])
    assert args.destination == '/some/path'

def test_parser_export_flag(parser):
    """
    The `export` value should default to False, but set
    to True when passed to the parser.
    """
    args = parser.parse_args(['/some/path'])
    assert args.export == False

    args = parser.parse_args(['--export', '/some/path'])
    assert args.export == True
