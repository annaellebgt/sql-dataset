import pickle
from grammarinator.runtime import UnlexerRule, UnparserRule


def print_tree(node, level=0):
    if isinstance(node, UnlexerRule):
        desc = f"UnlexerRule: name='{node.name}' : src='{node.src}'" 
    elif isinstance(node, UnparserRule):
        desc = f"UnparserRule: name='{node.name}'" 
    else:
        desc = "Unknown node type"
    print(" " * level + desc)
    for child in node.children:
        print_tree(child, level + 1)


if __name__=="__main__":
    with open("./populations/Basic/select_8.4504203c700f464b968bd3b2d4aea2aa.grt", "rb") as file:
        data = pickle.load(file)
        root = data.root
        print_tree(root)

