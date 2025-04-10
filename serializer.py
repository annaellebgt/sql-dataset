from grammarinator.runtime import *


def simple_space_serializer(root):

    def _walk(node, add_space=True):
        nonlocal src

        if isinstance(node, UnlexerRule):
            if node.name == "DOT":
                src = src.rstrip()  # remove whitespace before dots
            if node.src:
                src += node.src
            # only add spaces if the node is not a dot
            if add_space and node.name != "DOT":
                src += " "
        if node.name in {"Identifier", "Integral", "Digits", "Numeric"}:
            add_space = False
        for child in node.children:
            _walk(child, add_space)

    src = ""
    _walk(root)
    return src
