import json
import os
import random


# TODO Save the JSONS so only need to train if JSON file doesn't exist - loop 1:8
# TODO make it so if the file exists it uses that data other than training

# TODO make starting sentences better/ not chosing word if it has no following words
# TODO make it so you have to input words for it to work
# TODO grammer AI implementation
# TODO look at how questions get answered and try implement


# TRAIN FUNCTION
# will take in file as an argument
# create blank "unique words" array at the start
# start with one level analysis - then gp two - then three - set variable at start and increament when loop finished
# For each word in file
# if word not in unique_words - save to unique words
# if it is - skip over it
# save word as variable - Word
# use Find function - finds each instance of the word in the file, returns array of the following words
# use Analyse function - takes in array of words, returns array of words in correct JSON format
# loop

# Train should get the list of unique words
# Then using unique words go through line by line and get the next words for each unique word
# then outside of that loop get all the Next_words and build the final

name = "Harry_Potter_1_Level_"
# If the file exists in JSONS folder then get the data from that
# if it doesn't then train and save the data

def Train(file, level):
    present = False
    JSONS = []
    lineindex = 0
    unique_words = GetUniqueWords(file, level)
    print(unique_words)

    file.seek(0)
    for line in file:
        lineindex += 1
        loading = "Training line {}".format(lineindex)
        print(loading)
        words = line.split()
        indexes = getUniqueIndexes(line, unique_words, level)
        for index in indexes:
            Next_words = get_Next_Words(words, unique_words[index], level)
            temp_JSON = build_final_JSON(Next_words, unique_words[index])
            for i in range(len(JSONS)):
                if JSONS[i]["word"] == temp_JSON["word"]:
                    new_JSON = Combine_JSONS(JSONS[i], temp_JSON)
                    JSONS[i] = new_JSON
                    present = True

            if not present:
                JSONS.append(temp_JSON)
                present = False

    return JSONS


# remake each possible unique word
# search through unique words and add it to the index
def getUniqueIndexes(line, unique_words, level):
    unique_words_indexes = []
    temp_unique_words = []
    words = line.split()
    temp_phrase = ""

    # build the new word and add it to the list of temp words
    for word_index in range(len(words)):

        # temp_word = words[word_index].lower()
        if word_index < level:
            for index in range(word_index):
                temp_phrase += words[index] + " "
            temp_phrase += words[word_index]
            temp_phrase = temp_phrase.lower()
            temp_unique_words.append(temp_phrase)

        elif word_index > level:
            for index3 in range(level - 1):
                temp_phrase += words[(word_index - level + index3)] + " "
            temp_phrase += words[word_index - 1]
            temp_phrase = temp_phrase.lower()
            temp_unique_words.append(temp_phrase)
        temp_phrase = ""

        for word in temp_unique_words:
            for unique_word_index in range(len(unique_words)):
                if word == unique_words[unique_word_index]:
                    unique_words_indexes.append(unique_word_index)

    return unique_words_indexes


def Combine_JSONS(JSON1, JSON2):
    final_following_words = []
    for following_word in JSON1["following_words"]:
        for count in range(following_word["count"]):
            final_following_words.append(following_word["word"])

    for following_word in JSON2["following_words"]:
        for count in range(following_word["count"]):
            final_following_words.append(following_word["word"])

    final_JSON = build_final_JSON(final_following_words,JSON1["word"])

    return final_JSON


def GetUniqueWords(file, level):
    unique_words = []
    list_of_words_2 = []
    temp_phrase = ""
    for line in file:
        words = line.split()
        word_index = 0
        for word in words:
            temp_word = word.lower()
            list_of_words_2.append(temp_word)

            if word_index < level:
                for index3 in range(word_index):
                    temp_phrase += words[index3] + " "
                temp_phrase += words[word_index]
                temp_phrase = temp_phrase.lower()
                if temp_phrase not in unique_words:
                    unique_words.append(temp_phrase)
            elif word_index > level:
                for index3 in range(level - 1):
                    temp_phrase += words[(word_index - level + index3)] + " "
                temp_phrase += words[word_index - 1]
                temp_phrase = temp_phrase.lower()
                if temp_phrase not in unique_words:
                    unique_words.append(temp_phrase)
                temp_phrase = ""
                for index3 in range(level - 1):
                    temp_phrase += words[(word_index - level + index3 + 1)] + " "
                temp_phrase += words[word_index]
                temp_phrase = temp_phrase.lower()
                if temp_phrase not in unique_words:
                    unique_words.append(temp_phrase)
            temp_phrase = ""
            word_index += 1
    return unique_words


def array_count(array_or_following_words, word):
    count = 0
    for array_word in array_or_following_words:
        if array_word == word:
            count += 1

    return count


# Return an array of all the following words
# take in a list of words and a searched word
# find every instance of the word in the array
# get the following word and add it to the array
def get_Next_Words(words, searched_word, level):
    follow_up_words = []
    next_indexes = []
    temp_phrase = ""
    temp_index = 0

    # to find every instance you must iterate through array and recreate the word level based on whether it was
    for word_index in range(len(words)):
        if (word_index + 1) < len(words):
            if word_index < level:
                if word_index == 0:
                    temp_phrase += words[0]
                    if temp_phrase == searched_word:
                        next_indexes.append(word_index + 1)
                else:
                    for i in range(word_index):
                        temp_phrase += words[i] + " "
                        # temp_phrase += words[word_index - level + i] + " "
                    temp_phrase += words[word_index]

                    if temp_phrase == searched_word:
                        next_indexes.append(word_index + 1)
            elif word_index == level:
                for i in range(level - 1):
                    temp_phrase += words[word_index - level + i + 1] + " "
                temp_phrase += words[word_index]
                if temp_phrase == searched_word:
                    next_indexes.append(word_index + 1)
            elif word_index > level:
                for i in range(level - 1):
                    temp_phrase += words[word_index - level + i + 1] + " "
                temp_phrase += words[word_index]
                if temp_phrase == searched_word:
                    next_indexes.append(word_index + 1)
        temp_phrase = ""

    for i in range(level - 1):
        if level < len(words):
            temp_phrase += words[-level + i] + " "
    temp_phrase += words[-1]
    if temp_phrase == searched_word:
        next_indexes.append(word_index + 1)

    for index in next_indexes:
        if index < len(words):
            Next_word = words[index]
            follow_up_words.append(Next_word)

    next_indexes = []

    return follow_up_words


def build_final_JSON(list_of_next_words, word):
    # For each word in the array
    # Get Count of each word
    # add word to array of repeated words
    # create JSON using count and word
    # before end, create final JSON using list of JSONS
    JSONs = []
    repeated_words = []
    for listWord in list_of_next_words:
        if listWord not in repeated_words:
            count = array_count(list_of_next_words, listWord)
            repeated_words.append(listWord)
            first_JSON = {"word": listWord, "count": count}
            JSONs.append(first_JSON)
    final_JSON = {"word": word, "following_words": JSONs}
    return final_JSON


def print_data(trained_data, level):
    final_phrase = ""
    changing_phrase = ""

    first_words = getFirstWords(trained_data)
    first_JSON = random.choice(first_words)
    first_word = first_JSON["word"]
    final_phrase += first_word
    changing_phrase += first_word
    possible = True
    if not HasNextWords(changing_phrase, trained_data):
        possible = False

    while possible:
        next_words = createProbablitiyArray(changing_phrase, trained_data)
        next_temp_word = random.choice(next_words)
        final_phrase += " " + next_temp_word
        changing_phrase += " " + next_temp_word
        temp_phrase_array = changing_phrase.split()
        if len(temp_phrase_array) > level:
            del temp_phrase_array[0]
            changing_phrase = reconcatenate(temp_phrase_array)
        possible = HasNextWords(changing_phrase, trained_data)
        if not HasNextWords(changing_phrase, trained_data):
            possible = False

    return final_phrase


def HasNextWords(changing_phrase, trained_data):
    Boolean = False
    for i in range(len(trained_data)):
        if trained_data[i]["word"] == changing_phrase:
            if len(trained_data[i]["following_words"]) > 0:
                Boolean = True

    return Boolean


def reconcatenate(phrase_array):
    temp_phrase = ""
    for i in range(len(phrase_array) - 1):
        temp_phrase += phrase_array[i] + " "
    temp_phrase += phrase_array[-1]
    return temp_phrase


def FindNextWords(temp_phrase, dataset):
    JSON_array = []
    for i in range(len(dataset)):
        if dataset[i]["word"] == temp_phrase:
            JSON_array.append(dataset[i]["following_words"])
    return JSON_array


def getFirstWords(JsonArray):
    final_array = []
    for JSON in JsonArray:
        phrase = JSON["word"]
        words_split = phrase.split()
        if len(words_split) == 1:
            final_array.append(JSON)
    return final_array


def createProbablitiyArray(phrase, trained_data):
    temp_array = []
    final_array = []
    index = 0
    for i in range(len(trained_data)):
        if trained_data[i]["word"] == phrase:
            temp_array = trained_data[i]["following_words"]
    for i in temp_array:
        for j in range(i["count"]):
            final_array.append(i["word"])

    # take in array of following words
    # fill array with the individual words count times
    # random.choice
    # return word
    return final_array


with open("finalfile2.txt", 'r', encoding='utf-8') as f:
    for level in range(8):
        file_name = "JSONS\Harry_Potter_1_Level_{}.JSON".format((level + 1))
        if not os.path.isfile(file_name):
            jsonFile = open(file_name, "w")
            trained_data = Train(f, level)
            for data in trained_data:
                print(data)
                saved_json = json.dumps(data)
                jsonFile.write(saved_json)
            trained_data = ""