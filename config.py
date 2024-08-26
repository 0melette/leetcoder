from common.parsers import *

PARSER_MAPPING = {
    'postorderTraversal': tree_parser,
    'postorder': nary_tree_parser,
}

DEFAULT_PARSER = json_parser