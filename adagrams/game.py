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


def draw_letters():
    #use dictionary generated_dict to keep track of the frequency of each letter
    generated_dict = {}
    #use randint to access a random dictionary in list letter_dist
    count = 0
    while count < 10:
        char_max_dict = letter_dist[randint(0, len(letter_dist)-1)]
        for char, max_allowed in char_max_dict.items():
            if char not in generated_dict:
                generated_dict[char] = 1
                count += 1
            else:
                if max_allowed > generated_dict[char]:
                    generated_dict[char] += 1
                    count += 1
    generated_hand = [k for k, v in generated_dict.items() for _ in range(v)]

    return generated_hand



def uses_available_letters(word, letter_bank):
    word = word.upper()
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


def get_highest_word_score(word_list):
    score_tracker = {} 
    for given_word in word_list:
        score_for_item = score_word(given_word)
        score_tracker[given_word] = score_for_item
    
    winning_score = -1
    winning_word = ""
    ties = []

# get highest value or add values to ties list
    for word_item, points in score_tracker.items():

        if points > winning_score:
            winning_score = points
            winning_word = word_item
            
            if len(ties) > 0:
                ties.clear()

        elif points == winning_score:
            # add the earlier value to ties list first to preserve word order from word_list in ties list
            ties.append(winning_word)
            ties.append(word_item)


    #use tiebreaker func if there are ties
    if len(ties) > 0:
        winning_word = tiebreaker(ties)
        # winning_score = score_tracker[winning_word]

    return (winning_word, winning_score)


def tiebreaker(tied_list):
    # shortest_len_word = None
    shortest_word = tied_list[0]

    for tied_words in tied_list:
        # shortest_word = None
        
        #even if there are multiples w length of 10, the first in the list will be the winner
        if len(tied_words) == 10:
            winner = tied_words
            break
        else:
            if len(tied_words) < len(shortest_word):
                shortest_word = tied_words
                winner = shortest_word
                # break
            if len(tied_words) == len(shortest_word): 
                if tied_list.index(tied_words) < tied_list.index(shortest_word):
                    winner = tied_words
                else:
                    winner = shortest_word
    return winner   



def create_letter_freq_dict(letter_bank):
    letter_count = {}
    #store the letters in given list as a dictionary w frequency
    for elem in letter_bank:
        if elem in letter_count.keys():
            letter_count[elem] += 1
        else:
            letter_count[elem] = 1
    return letter_count