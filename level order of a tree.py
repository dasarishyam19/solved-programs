level = []
        if not root:
            return level
        def fun(node,l):
            if len(level) == l:
                level.append([])
                level[l].append(node.val)
            if node.left:
                fun(node.left,l+1)
            if node.right:
                fun(node.right,l+1)
        fun(root,0)
        return level