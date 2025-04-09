def anonymizer_transformer(root):
    def _walk(node):
        nonlocal idx

        if node.name == 'table_ref':
            for child in node.children:
                if child.name=="Identifier":
                    child.src="table_name"
        elif node.name=="columnref":
            for child in node.children:
                if child.name=="Identifier":
                    child.src="column_name"
        elif node.name=="collabel":
            for child in node.children:
                if child.name=="Identifier":
                    child.src="column_label"

        for child in node.children:
            _walk(child)

    idx = 0
    _walk(root)
    return root

