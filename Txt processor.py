# This takes in a file, returns a file that has been formatted correctly
# copy the data onto a line and for every full stop, take a new line

# TODO replace "/n" with a space
# TODO if full stop comes before a MR or MRS it doesnt take a new line


file_to_write = open("textfiles/finalfile.txt", "w", encoding='utf-8')
# file_to_write.write("hello" + "\n")
# file_to_write.write("hello")
# print("printing done")


filename = "textFiles/testText2.txt"
with open(filename, 'r', encoding='utf-8') as f:
    phrase = ""
    for line in f:
        split_line = line.split(".")
        if split_line[0] != "\n" and split_line[0][0:7] != "Page | ":
            print(split_line)
            if len(split_line) > 1:
                for i in range(len(split_line) - 1):
                    # if word == mr or mrs just add to phrase
                    if len(split_line[i]) > 2:
                        mr = split_line[i][-2] + split_line[i][-1]
                        mrs = split_line[i][-3] + split_line[i][-2] + split_line[i][-1]
                        if mr == "Mr" or mrs == "Mrs":
                            phrase += split_line[i]
                        else:
                            phrase += split_line[i]
                            file_to_write.write(phrase.lower() + "\n")
                            phrase = ""
                    elif len(split_line[i]) > 1:
                        mr = split_line[i][-2] + split_line[i][-1]
                        if mr == "Mr":
                            phrase += split_line[i]
                        else:
                            phrase += split_line[i]
                            file_to_write.write(phrase.lower() + "\n")
                            phrase = ""
                    # else:
                        # phrase += split_line[i]
                        # file_to_write.write(phrase + "\n")
                        # phrase = ""
                # temp_phrase = split_line[-1][0:-2]
                temp_phrase = split_line[-1].replace("\n", "")
                phrase += temp_phrase + " "
            else:
                # temp_phrase = split_line[-1][0:-2]
                temp_phrase = split_line[-1].replace("\n", "")
                phrase += temp_phrase + " "


# split = line.split(".")
# print(split)

# split_line = re.split(".",line)
# print(split_line)/
#
# line = "hello mr. gallop"
# splittt = line.split(".")
# print(splittt)
# print(splittt[0][-2] + splittt[0][-1])


line2 = "hello thomas/n"
line3 = line2[0:-2]
print(line3)