def anonymizer_transformer(root):
    def delete_children(node):
        for child in node.children:
            child.parent = None
        node.children = []
        assert node.children == []

    def _walk(node):
        nonlocal idx

        if node.name == "table_ref":
            for child in node.children:
                if child.name == "Identifier":
                    child.src = "table_name"
                    delete_children(child)
        elif node.name == "columnref":
            for child in node.children:
                if child.name == "Identifier":
                    child.src = "column_name"
                    delete_children(child)
        elif node.name == "collabel":
            for child in node.children:
                if child.name == "Identifier":
                    child.src = "column_label"
                    delete_children(child)

        elif node.name == "sortby":
            for child in node.children:
                if child.name == "Identifier":
                    child.src = "column_name"
                    delete_children(child)

        for child in node.children:
            _walk(child)

    idx = 0
    _walk(root)
    return root
