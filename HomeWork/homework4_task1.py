# Необходимо превратить собранное на семинаре дерево поиска в полноценное левостороннее красно-черное
# дерево. И реализовать в нем метод добавления новых элементов с балансировкой.
#
# Красно-черное дерево имеет следующие критерии:
# • Каждая нода имеет цвет (красный или черный)
# • Корень дерева всегда черный
# • Новая нода всегда красная
# • Красные ноды могут быть только левым ребенком
# • У краной ноды все дети черного цвета
#
# Соответственно, чтобы данные условия выполнялись, после добавления элемента в дерево необходимо
# произвести балансировку, благодаря которой все критерии выше станут валидными. Для балансировки
# существует 3 операции – левый малый поворот, правый малый поворот и смена цвета.

# class Node:
#     def init(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.is_red = True

# class LeftLeaningRedBlackTree:
#     def init(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#         self.root.is_red = False

#     def _insert(self, node, key):
#         if node is None:
#             return Node(key)

#         if key < node.key:
#             node.left = self._insert(node.left, key)
#         elif key > node.key:
#             node.right = self._insert(node.right, key)
#         else:
#             return node

#         if self._is_red(node.right) and not self._is_red(node.left):
#             node = self._rotate_left(node)
#         if self._is_red(node.left) and self._is_red(node.left.left):
#             node = self._rotate_right(node)
#         if self._is_red(node.left) and self._is_red(node.right):
#             self._flip_colors(node)

#         return node

#     def _is_red(self, node):
#         if node is None:
#             return False
#         return node.is_red

#     def _rotate_left(self, node):
#         x = node.right
#         node.right = x.left
#         x.left = node
#         x.is_red = node.is_red
#         node.is_red = True
#         return x

#     def _rotate_right(self, node):
#         x = node.left
#         node.left = x.right
#         x.right = node
#         x.is_red = node.is_red
#         node.is_red = True
#         return x

#     def _flip_colors(self, node):
#         node.is_red = True
#         node.left.is_red = False
#         node.right.is_red = False

# tree = LeftLeaningRedBlackTree()
# tree.insert(10)
# tree.insert(5)
# tree.insert(15)
# tree.insert(3)
# tree.insert(7)
# tree.insert(13)
# tree.insert(20)


def ex():
    tree = Tree()
    tree.add(1)
    tree.add(5)
    tree.add(8)
    tree.add(4)
    tree.add(3)
    tree.add(10)
    tree.add(7)
    tree.print()


class Node:
    def __init__(self):
        self.value: int = None
        self.isRed: bool = False
        self.left: Node = None
        self.right: Node = None


class Tree:
    def __init__(self):
        self.root: Node = None

    def print(self):
        self.print_node(self.root)

    def add(self, value: int):
        result = True

        if self.root is not None:
            result = self.add_note(self.root, value)
            self.root = self.rebalancing(self.root)
            self.root.isRed = False
        else:
            self.root = Node()
            self.root.isRed = False
            self.root.value = value

        return True

    def rebalancing(self, node) -> Node:
        result: Node = node
        need_rebalancing = True

        while need_rebalancing:

            need_rebalancing = False

            if (result.right is not None and result.right.isRed and
                    (result.left is None or not result.left.isRed)):
                need_rebalancing = True
                result = self.right_swap(result)

            if (result.left is not None and result.left.isRed and
                    result.left.left is not None and result.left.left.isRed):
                need_rebalancing = True
                result = self.left_swap(result)

            if (result.left is not None and result.left.isRed and
                    result.right is not None and result.right.isRed):
                need_rebalancing = True
                self.color_swap(result)

        return result

    def right_swap(self, node: Node) -> Node:
        right = node.right
        between = right.left
        right.left = node
        node.right = between
        right.isRed = node.isRed
        node.isRed = True
        return right

    def left_swap(self, node: Node) -> Node:
        left = node.left
        between = left.right
        left.right = node
        node.left = between
        left.isRed = node.isRed
        node.isRed = True
        return left

    def color_swap(self, node: Node):
        node.right.isRed = False
        node.left.isRed = False
        node.isRed = True

    def add_note(self, node: Node, value: int):

        if (node.value == value):
            return False

        result: bool = True

        if node.value > value:
            if node.left is not None:
                result = self.add_note(node.left, value)
                node.left = self.rebalancing(node.left)
            else:
                node.left = Node()
                node.left.isRed = True
                node.left.value = value
                result = True
        else:
            if (node.right is not None):
                result = self.add_note(node.right, value)
                node.right = self.rebalancing(node.right)
            else:
                node.right = Node()
                node.right.isRed = True
                node.right.value = value
                result = True

        return result

    def print_node(self, node: Node):
        if node is None:
            return
        self.print_node(node.left)
        print(node.value)
        self.print_node(node.right)


if __name__ == '__main__':
    ex()
