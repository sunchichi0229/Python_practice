class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("おはよう! 私は" + self.name)

    def introduce(self):
        print("私の名前は" + self.name + "。そして、私は" + str(self.age) + "歳です。")


class Police(Person):
    def arrest(self, to_arrest):
        print("お前は逮捕だ。" + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("次は何を作ろうかな？あ！これを作ろう: " + to_program)

sunchichi = Person("スンちゃん", 33)
jenny = Police("ジェニー", 22)
michael = Programmer("マイクル", 30)

sunchichi.introduce()
jenny.introduce()
jenny.arrest("スンちゃん")
michael.introduce()
michael.program("ECサイト")
