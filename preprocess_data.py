from os import listdir
from os.path import isfile, join
import numpy as np

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å', ' ' ]


def noise_maker(sentence, threshold, depth = 3):
    '''Relocate, remove, or add characters to create spelling mistakes'''

    noisy_sentence = []
    i = 0
    while i < len(sentence):
        random = np.random.uniform(0, 1, 1)
        # Most characters will be correct since the threshold value is high
        if random < threshold:
            noisy_sentence.append(sentence[i])
        else:
            new_random = np.random.uniform(0, 1, 1)
            # ~33% chance characters will swap locations
            if new_random > 0.75:
                if i == (len(sentence) - 1):
                    # If last character in sentence, it will not be typed
                    continue
                else:
                    # if any other character, swap order with following character
                    noisy_sentence.append(sentence[i + 1])
                    noisy_sentence.append(sentence[i])
                    i += 1
            # ~33% chance an extra lower case letter will be added to the sentence
            elif new_random > 0.50:
                random_letter = np.random.choice(letters, 1)[0]
                noisy_sentence.append(random_letter)
                noisy_sentence.append(sentence[i])
            # chance the wrong character is typed
            elif new_random > 0.25:
                random_letter = np.random.choice(letters, 1)[0]
                noisy_sentence.append(random_letter)
            # chance a character will not be typed
            else:
                pass
        i += 1
    if depth <= 0:
        return "".join(noisy_sentence)
    return noise_maker(noisy_sentence, threshold, depth - 1)

def load_text(path):
    input_file = join(path)
    with open(input_file, encoding="utf-8") as f:
        with open('texts.txt', 'a', encoding="utf-8") as texts_file:
            with open('texts_noisy.txt', 'a', encoding="utf-8") as texts_noisy_file:
                for line in f:
                    texts_file.write(line.rstrip() + '\n')
                    texts_noisy_file.write(noise_maker(line.rstrip(), .98) + '\n')

                    #print(line.rstrip())
                    #print(noise_maker(line, .98))



text_files = [f for f in listdir("texts") if isfile(join("texts", f))]

print(text_files)

for text_file in text_files:
    load_text("texts/" + text_file)
