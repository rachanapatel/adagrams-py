from random import randint

letter_dist = [{"A":9}, {"B":2}, {"C": 2}, {"D": 4}, {"E": 12}, {"F": 2}, 
               {"G": 3}, {"H": 2}, {"I" : 9}, {"J": 1}, {"K": 1}, {"L": 4},
               {"M": 2}, {"N": 6}, {"O": 8}, {"P": 2}, {"Q": 1}, {"R": 6}, 
               {"S": 4}, {"T": 6}, {"U": 4}, {"V": 2}, {"W": 2}, {"X": 1}, 
               {"Y": 2}, {"Z": 1}]


score_chart = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G") :2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}

# adding comment to test



def draw_letters():
    #use the dictionary generated_dict to keep track of the frequency of each letter
    generated_dict = {}


    while len(generated_dict.keys()) < 10:
        sp_letter = letter_dist[randint(0, len(letter_dist)-1)]
        for char, max_allowed in sp_letter.items():
            if char not in generated_dict.keys():
                random_letter = char
                generated_dict[random_letter] = 1
            else:
                if max_allowed > generated_dict[random_letter]:
                    generated_dict[random_letter] += 1


    print(generated_dict.keys())
    return generated_dict.keys()



def uses_available_letters(word, letter_bank):
    word = word.upper()

    # for elem in letter_bank:
    word_list = []

    for char in word:
        word_list.append(char)

    word_list_dict = create_letter_freq_dict(word_list)
    bank_dict = create_letter_freq_dict(letter_bank)


    for letter, freq in word_list_dict.items():
        if letter not in bank_dict.keys() or freq > bank_dict[letter]:
            return False

    
    return True




 

def score_word(word):
    word = word.upper()
    total_score = 0
    if len(word) > 6:
        total_score += 8
    for letter in word:
        for group, points in score_chart.items():
            if letter in group:
                total_score += points

    return total_score


def get_highest_word_score(word_list: list) -> tuple[str, int]:
    score_tracker = {} 
    for given_word in word_list:
        score_for_item = score_word(given_word)
        score_tracker[given_word] = score_for_item

    highest = 0
    highest_word = ""
    ties: list[str] = []

# get highest value or add values to ties list
    for word_item, points in score_tracker.items():
        if points > highest:
            highest = points
            highest_word = word_item
        elif points == highest:
            # add the earlier value first to preserve index order
            ties.append(highest_word)
            ties.append(word_item)
    highest = highest
    highest_word = highest_word




    shortest_word = None

    for tied_words in ties:
        shortest_word = ties[0]
        if len(tied_words) == 10:
            highest_word = tied_words
            highest = score_tracker[highest_word]
            break
        else:
            if len(tied_words) < len(shortest_word):
                shortest_word = tied_words
                highest_word = shortest_word
                print("picked shorter word")
                break
            if len(tied_words) == len(shortest_word): 
                print("equal lengths")
                if word_list.index(tied_words) < word_list.index(shortest_word):
                    highest_word = tied_words
                else:
                    highest_word = shortest_word

    print(highest_word, highest)
    return (highest_word, highest)
    






def create_letter_freq_dict(letter_bank):
    letter_count = {}
    for elem in letter_bank:
        if elem in letter_count:
            letter_count[elem] += 1
        else:
            letter_count[elem] = 1
    return letter_count

