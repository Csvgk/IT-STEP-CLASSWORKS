class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return self.items == []


class Player:
    def __init__(self,name):
        self.name = name
        self.x = 0
        self.y = 0

        self.history = Stack()

    def show_position(self):
        print(f"{self.name}: ({self.x} , {self.y})")

    def move(self,dx,dy):
        self.history.push((self.x,self.y))

        self.x += dx
        self.y += dy

        print(f"{self.name} moved!")
        self.show_position()

    def undo_move(self):
        old_position = self.history.pop()
        if old_position is None:
            print("No more moves")
            return

        self.x , self.y = old_position
        print("Last move canceled")
        self.show_position()

#player = Player("Max")
#player.show_position()
#player.move(1,3)
#player.move(2,4)
#player.move(6,7)

#print("----UNDO----")

#player.undo_move()
#player.undo_move()
#player.undo_move()
#player.undo_move()

class BracketChecker:
    def __init__(self):
        self.stack = Stack()

    def check(self,text):
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }


#        for symbol in text:
#
#            if symbol in pairs.values():
#                self.stack.push(symbol)
#
#            elif symbol in pairs.keys():
#                if self.stack.is_empty():
#                    return False
#                if self.stack.peek() != pairs[symbol]:
#                    return False
#
#                self.stack.pop()
#
#        return self.stack.is_empty()

        for symbol in text:

            if symbol in pairs.values():
                self.stack.push(symbol)

            elif symbol in pairs.keys():
                if self.stack.is_empty():
                    return False, f"Зайва закриваюча дужка '{symbol}'"

                top = self.stack.peek()
                if top != pairs[symbol]:
                    return False, f"Очікувалася відповідна дужка до '{top}', а зустріто '{symbol}'"

                self.stack.pop()

        if not self.stack.is_empty():
            return False, f"Помилка: не закрита дужка '{self.stack.peek()}'"

        return True, "Дужки розставлені правильно!"

checker = BracketChecker()
text = input("Введіть текст: ")

print(checker.check(text))
