import random

eng_words = ["puppy", "kitten", "happy"]

answer = random.choice(eng_words)
guess_letters = list("_" * len(answer))
life = 3
game_over = False

while not game_over:
    print(f"残りの機会: {'❤' * life}回")
    user_guess = input("一文字ずつ推測してみてください >>>  ").lower()

    if len(user_guess) == 1 and user_guess.isalpha():
        for i in range(len(answer)):
            if answer[i] == user_guess:
                guess_letters[i] = user_guess
        print(guess_letters)
        print()

        if "_" not in guess_letters:
            game_over = True

            print("成功！おめでとう！")

        if user_guess not in answer:
            life -= 1
            if life == 0:
                game_over = True
                print(f"失敗! 正解は{answer}です。")
    else:
        print("英文を一文字ずつ入力してください")