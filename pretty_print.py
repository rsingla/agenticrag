import json

from pygments import highlight, lexers, formatters


def pretty_print(data):
    # parse JSON
    parsed_json = json.loads(data.replace("'", '"'))

    # pretty print JSON with syntax highlighting
    formatted_json = json.dumps(parsed_json, indent=4)
    colorful_json = highlight(formatted_json,
                          lexers.JsonLexer(),
                          formatters.TerminalFormatter())

    return colorful_json

## Do NOT modify this class.
class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def link_nodes(self, node1, node2):
        node1.next = node2
        node2.prev = node1
        return node1, node2

    def traverse(self):
        visited = []
        current = self.head
        while current:
            visited.append(current)
            current = current.next
            if current == self.head:
                break
        return visited

    def add_node(self, data):
        my_node = Node(data)
        if not self.head:
            self.head = my_node
            self.tail = my_node
        else:
            self.tail.next = my_node
            my_node.prev = self.tail
            self.tail = my_node
        return my_node
