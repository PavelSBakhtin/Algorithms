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

class Node:
    def init(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.is_red = True

class LeftLeaningRedBlackTree:
    def init(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.is_red = False

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)
        
        return node

    def _is_red(self, node):
        if node is None:
            return False
        return node.is_red

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _flip_colors(self, node):
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False

tree = LeftLeaningRedBlackTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(20)
