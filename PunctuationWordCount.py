# Authour: Jaimin Kirankumar Kerai, v1.0
# A program which counts the nummber of specified punctuation and words
# It will normalise this data by dividing each count by the number of sentences
# With the counts (and normalising) the program is able to 'compare' to texts by determining
# the distance between each
# The program accepts up to three parameters, in four different situations, the last arguement is assumed to be False unless stated
# The first being: (filename of the first text, 'listing'), this will list the counts of the punctuation or words 
# The second being: (filename of first text, filename of second text), this will determine the 'distance' between the texts
# The third being: (filename of the first text, 'listing', True), this will list the normalised counts of the punctuation or words
# The fourth being: (filename of first text, filename of second text, True), this will determine the normalised 'distance' between the texts

import math

# This main function will complete all major concluding computations and outputs
def main(textfile1, arg2, normalize=False):
    # The determining the route according to the inputs
    if arg2 == 'listing':
        # Non-normalised path
        if normalize == False:
            # Calling the function to count the words and punctuation as well as the paragraph, sentence and word count
            profile1, words_per_sent, sent_per_para,_= word_punctuation_count(textfile1)
            profile1['words_per_sentence'] = words_per_sent
            profile1['sentences_per_par'] = sent_per_para
            # The print output of the dictionaries
            print("The pure count of the punctuation and words of the chosen file:")
            for key, value in sorted(profile1.items()):
                print('{}: {}'.format(key,format(value,'.4f')))
        # Normalised path
        elif normalize == True:
            profile1,_,_,_= word_punctuation_count(textfile1)
            profile1 = normalize_data(textfile1)
            # The print output of the dictionaries
            print("The normalized count of the punctuation and words of the chosen file:")
            for key, value in sorted(profile1.items()):
                print('{}: {}'.format(key,format(value,'.4f')))
        # The program will exit if an invalid third arguement is entered    
        else:
            exit()
    # if the input is a file, or not 'listing', the following will compute        
    else:
        # Non-normalised pathway
        if normalize == False:
            # Calling the functions to count the words and punctuation as well as the paragraph, sentence and word count
            profile1, words_per_sent1, sent_per_para1,_= word_punctuation_count(textfile1)
            profile2, words_per_sent2, sent_per_para2,_= word_punctuation_count(arg2)
            profile1['words_per_sentence'] = words_per_sent1
            profile1['sentences_per_par'] = sent_per_para1
            profile2['words_per_sentence'] = words_per_sent2
            profile2['sentences_per_par'] = sent_per_para2
            # Calling functions to determine the distance between two calculated profiles
            difference_sum = distance(profile1, profile2)
            # The print output of the difference sum
            print("The distance between the two texts is:", difference_sum)
        # Normalised pathway
        elif normalize  == True:
            # The two profiles will be calculated as normalised
            profile1 = normalize_data(textfile1)
            profile2 = normalize_data(arg2)
            # The difference of sum will be computed
            difference_sum = distance(profile1, profile2)
            # The print output of the difference sum
            print("The normalized distance between the two texts is:", difference_sum)
        # The program will exit if an invalid second arguement is entered 
        else:
            exit()
            
# A function designed to take one input, the file, and calculate the count of the paragraphs, sentences and words.
# It will also count the number of specific punctuation and words, then add these into a dictionary labelled as the profile
def word_punctuation_count(file):
    # A list of the punctuation required to count
    punctuation_list = [',',';',"'",'-']
    # A list of the words required to count
    words_list = ["also", "although", "and", "as", "because", "before", "but", "for", "if", "nor", "of", "or", "since", "that","though", "until", "when", "whenever", "whereas", "which", "while", "yet"]
    # Initialisation of dictionaries and variables
    profile = {}
    words_in_text = 0
    # Opening the file and turning the text into a list seperated by each word and punctuation
    input_file = open(file,'r')
    # Removal of unnessary characters and addition of seperator characters
    count_file = input_file.read().replace('.',' ').replace('?',' ').replace('!',' ').replace('\n\n\n',' ').replace('--\n\n',' ').replace('\n\n',' ').replace('--',' ').replace('\n',' ').replace('-',' - ').replace(',',' ,').replace('; ',' ; ').replace('"','').replace(" '",' ').replace("' ",' ').replace("'"," ' ").replace(","," , ").lower().split(' ')
    # A loop to count each of the punctuation and add it to the profile
    for punctuation in punctuation_list:
        punct_count = count_file.count(punctuation)
        profile[punctuation] = punct_count
    # A loop to count each of the specific words and add it to the profile
    for words in words_list:
       word_count = count_file.count(words)
       profile[words] = word_count
    input_file.close()
    # Opening the file and turning the text into a list seperated by paragraphs
    input_file = open(file,'r')
    # Removal of unnessary characters and addition of seperator characters
    words_file = input_file.read().replace(';','').replace(',','').replace(':','').replace("'",'').replace('"','').replace('?','.').replace('!','.').replace('\n\n\n','<>').replace('--\n\n','<>').replace('\n\n','<>').replace('\n',' ').replace('--',' ').replace('-','').replace('@',' ').replace('$','').replace('%','').split('<>')
    # Counting of paragraphs and words
    for paragraph in words_file:
        paragraph_in_text = len(words_file)
        paragraph = paragraph.split('. ')
        for sentence in paragraph:
            sentence = sentence.split(' ')
            words_in_sentence = len(sentence)
            words_in_text += words_in_sentence
    input_file.close()
    # Opening the file and turning the text into a list seperated by sentences
    input_file = open(file,'r')
    # Removal of unnessary characters and addition of seperator characters
    sentence = input_file.read().replace(';','').replace(',','').replace(':','').replace("'",'').replace('"','').replace('?','.').replace('!','.').replace('\n\n\n',' ').replace('--\n\n',' ').replace('\n',' ').replace('--',' ').replace('-','')
    sentences_in_text = len(sentence.strip().split('. '))
    input_file.close()
    # Calculating final values and returning required the profile and variables
    words_per_sent = words_in_text/sentences_in_text
    sent_per_para = sentences_in_text/paragraph_in_text
    return profile, words_per_sent, sent_per_para, sentences_in_text

# A function designed to take a file as an input and run the above function.
# The profile and other returned values are used to normalise each data point of the dictionary
def normalize_data(file):
    # Aquiring the profile from running the word_punctuation_count function
    profile, words_per_sent, sent_per_para, sentences_in_text  = word_punctuation_count(file)
    # Updating each normalised data point in the profile
    for key, value in profile.items():
        profile[key] = value/sentences_in_text
    # Adding the non-normalised values into the profile
    profile['words_per_sentence'] = words_per_sent
    profile['sentences_per_par'] = sent_per_para
    # Returning completely filled/normalised profile
    return profile
        
# A function designed to take two profiles of two texts as the input
# Then determining the distance between these two profiles
def distance(profile1, profile2):
    # Initialising the variable for the sum
    difference_sum = 0
    # Looping through the values of the profiles and using such to determine the difference sum of each 
    for key,_ in profile1.items():
        d = profile1[key] - profile2[key]
        difference_sum += d**2
    # Doing the final calculation and formating the float to 4 decimal places
    difference_sum = format(math.sqrt(difference_sum),'.4f')
    # Returning the difference sum
    return difference_sum




    
    


    