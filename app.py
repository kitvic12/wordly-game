from words import choose_word
from words import load_5letter_words


def get_guess(word_length):
    while True:
        guess = input(f"Введите слово из {word_length} букв: ").lower().strip()
        if len(guess) == word_length and guess.isalpha():
            return guess
        print(f"Пожалуйста, введите слово из {word_length} букв (только буквы).")

def check_guess(secret_word, guess):
    result = []
    secret = list(secret_word)
    guess_letters = list(guess)
    

    for i in range(len(secret)):
        if guess_letters[i] == secret[i]:
            result.append('🟩')
            secret[i] = None
            guess_letters[i] = None
    

    for i in range(len(guess_letters)):
        if guess_letters[i] is not None and guess_letters[i] in secret:
            result.append('🟨')
            secret[secret.index(guess_letters[i])] = None
        elif guess_letters[i] is not None:
            result.append('⬜')
    return result


def print_results(guesses):
    for guess in guesses:
        print(' '.join(guess))

def play_game():
    words = load_5letter_words()
    secret_word = choose_word(words)
    guesses = []
    
    print(f"\nУгадайте слово из 5 букв. У вас 6 попыток.")
    
    for attempt in range(1, 7):
        print(f"\nПопытка {attempt} из 6")
        try:
            guess = get_guess(5)
        except KeyboardInterrupt:
            print("\nИгра прервана пользователем.")
            return False
        
        if guess == secret_word:
            print("\nПоздравляем! Вы угадали слово!")
            print(f"Слово: {secret_word.upper()}")
            print(f"Попыток использовано: {attempt}")
            return True
        
        result = check_guess(secret_word, guess)
        guesses.append(result)
        print_results(guesses)
    
    print("\nИгра окончена! Вы не угадали слово.")
    print(f"Загаданное слово было: {secret_word.upper()}")
    return False

def main():
    print("Добро пожаловать в Wordle!")
    print("Попробуйте угадать слово из 5 букв.")
    print("🟩 - буква на правильном месте")
    print("🟨 - буква есть в слове, но не на этом месте")
    print("⬜ - буквы нет в слове")
    
    while True:
        play_game()
        if input("\nХотите сыграть ещё раз? (да/нет): ").lower() not in ['да', 'д', 'yes', 'y']:
            print("\nСпасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()