class Node:
    def __init__(self,value) -> None:
        self._value = value
        self._node = []
    
    def __repr__(self) -> str:
        return f'Node({self._value})'
    
    def add_children(self,node:'Node') -> 'Node':
        self._node.append(node)
    
    def __iter__(self):
        return iter(self._node)

    def dfs(self):
        yield self
        for i in self:
            yield from i.dfs()
root = Node(0)
children1 = Node(1)
children2 = Node(2)
root.add_children(children1)
root.add_children(children2)
children1.add_children(Node(3))
children1.add_children(Node(4))
children11 = Node(5)
children2.add_children(children11)
children11.add_children(Node(6))
for c in root.dfs():
    print(c)