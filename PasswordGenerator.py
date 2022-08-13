import random


def create_word_list():



def pull_words():
    samples = ['Tetrarchy','Pontifex','Coliseum','Boudicca','Centurion','Augustus','Gracchus','Gaius']
    final_string='' 
    words = 0
    while words < 3:
        final_string=f'{final_string}{random.choice(samples)}'
        words+=1
    return final_string


def pull_digits(existing_password):
    numbers=[*range(1,100,1)]
    return f'{existing_password}{random.choice(numbers)}'


if __name__ == '__main__':
    password=pull_words()
    password=pull_digits(password)
    print(password)     