from inspect import stack


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return len(nodes)

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.data)
        return " -> ".join(str(x) for x in nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            for node in self:
                pass
            node.next = new_node
        return self

    def insert_after(self, previous_node, new_node):
        if self.head is None:
            return "List is empty"
        for node in self:
            if node == previous_node:
                new_node.next = previous_node.next
                previous_node.next = new_node
                return self
        return "Node does not exist in list"

    def insert_before(self, next_node, new_node):
        if self.head == next_node:
            self.head = new_node
            new_node.next = next_node
        else:
            for node in self:
                if node == next_node:
                    previous_node.next = new_node
                    new_node.next = next_node
                    return self
                previous_node = node
        return "Node does not exist in list"


    def remove(self, new_node):
        previous_node = self.head
        for node in self:
            if node == new_node:
                previous_node.next = new_node.next
                return self
            previous_node = node
        return "Node does not exist in list"

        
node1 = Node(5)
node2 = Node('Phiona')
node3 = Node('Bas')
node4 = Node('Rach')
node5 = Node('Log')
node6 = Node('Josh')
node7 = Node('Tumu')

# linked_list = LinkedList()
# linked_list.append(node1)
# linked_list.append(node2)
# linked_list.append(node3)
# linked_list.insert_after(node2, node4)
# linked_list.append(node6)

# print(linked_list)

# linked_list.insert_before(node1, node5)

# print(linked_list)

# linked_list.insert_before(node6, node7)

# print(linked_list)

# linked_list.remove(node3)
# print(linked_list)

# linked_list2 = LinkedList()
# linked_list2.append(node6)

# print(linked_list2.insert_after(node3, node1))
# print(len(linked_list))


class Stack:
    def __init__(self) -> None:
        self.list = LinkedList()
        self.count = 0

    def push(self, val):
        self.list.append(val)

    def __iter__(self):
        node = self.list.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        return self.list.__repr__()

    def pop(self):
        node = self.list.head
        while node is not None:
            if node.next is None:
                self.list.remove(node)
                return self.list
            node = node.next

    def peek(self):
        node = self.list.head
        while node is not None:
            if node.next is None:
                return node.data
            node = node.next


stack1 = Stack()
stack1.push(node1)
stack1.push(node2)
stack1.push(node3)
stack1.push(node4)
stack1.push(node5)
print(stack1)
# for item in stack1:
#     print(item.data)
print(stack1.peek())

print(stack1.pop())
