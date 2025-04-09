
from grammarinator.runtime import *
def simple_space_serializer(root):
    
    def _walk(node):
        nonlocal src

        if isinstance(node, UnlexerRule):
            if node.name=='DOT':
                src = src[:-1]
            if node.src:
                src += node.src
            if node.name!='DOT':
                src += ' '
        else:
            for child in node.children:
                _walk(child)
        

    src = ''
    _walk(root)
    return src