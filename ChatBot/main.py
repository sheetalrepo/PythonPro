import re


def get_message_probability(human_message_list, bot_words_list, is_single_response=False, imp_words=[]):
    message_certainty = 0
    has_imp_words = True

    # Counts how many words are present in each predefined message
    for word in human_message_list:  # hello how are you
        if word in bot_words_list:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(bot_words_list))

    # Checks that the important words are in the string
    for word in imp_words:
        if word not in human_message_list:
            has_imp_words = False
            break

    # Must either have the required words, or be a single response
    if has_imp_words or is_single_response:
        return int(percentage * 100)
    else:
        return 0


def process_human_message(human_message_list): # ['how','are','you']
    highest_prob_list = {}         #Empty Dictionary


    def bot_response(bot_response, bot_words_list, is_single_response=False, imp_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = get_message_probability(human_message_list, bot_words_list, is_single_response, imp_words)
        #print (highest_prob_list)


    bot_response('Hello Dear', ['hello', 'hi', 'hey', 'hola'], is_single_response=True)
    bot_response('I am doing fine, Thanks', ['how', 'are', 'you', 'doing'], imp_words=['how'])
    bot_response('Please tell me how may i help you', ['i', 'need', 'some', 'help'], imp_words=['help'])
    bot_response('Its fine, no problem', ['not', 'now', 'may', 'be', 'later'], imp_words=['later'])
    bot_response('You Are Welcome', ['thank', 'thanks'], is_single_response=True)
    bot_response('See you soon', ['bye', 'goodbye', 'adios'], is_single_response=True)


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print("Compelete Dictionary Values with Probability:")
    #print(highest_prob_list)
    #print("Best Match Response:")
    #print(best_match)

    return best_match



def get_response_from_bot(user_input):
    split_words = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = process_human_message(split_words)
    return response


while True:
    print('OceanBlue: ' + get_response_from_bot(input('Human: ')) + '\n')
