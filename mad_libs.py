# Yes, I realize this recursive implementation is VERY questionable
# No, I definitely don't intend to fix the problem by booting them to the start if they
# call ask_for_input too many times ;)

# Stack overflow is just a figure of speech, right? ...Right?

import random

aan_mode: bool = False # Toggle aan_identifier generation //EXPERIMENTAL//
rand_words: bool = False 

    
# Pls no modify below # 



class SlotOfSpeech:
    
    # aan_identifier should be the string 'a' or 'an' to match the type itself for user display, 
    #     e.g. 'enter adjective' ---> 'enter an adjective'
    # aan_place_flag defines whether the user input should be placed with a generated aan_identifier,
    #     e.g. '{killer} rabit' ---> '{a killer} rabbit'  
    # display_name can be the same between several slot types, they will act as one input group,
    # summing their respective slot request counts for the user, while keeping their properties intact
    
    def __init__(self, display_name, slot_id, request_count, aan_identifier, aan_place_flag):
        self.display_name = display_name
        self.slot_id = slot_id
        self.request_count = request_count
        self.aan_identifier = aan_identifier
        self.aan_place_flag = aan_place_flag
        self.user_input_list = []
        
        

class MadlibFile:
    
    # "Self documenting"
    def __init__(self, story_text, slot_list):
        
        self.story_text = story_text
        self.slot_list = slot_list
        
    

madlib_file_global = MadlibFile('', [])

def help_and_welcome():
    print("\n\n")
    print("Welcome to the MadLibs test program. Handle with care.")
    print("Press enter to continue")
    
    user_input = ask_for_input(True)
    
    if user_input == "analytics":
        dev_menu()
    else:
        menu()
        

def dev_menu():
    return
    

def menu():
    
    print("\n\n")
    print('Welcome to the menu. No meat.')
    print('p = play, o = options, q = quit')
    
    user_input = ask_for_input(False)
    
    if user_input == 'o':
        options_selector()
    elif user_input == 'p':
        play_menu()
    elif user_input == 'q':
        print('Goodbye.')
        return
    else:
        print('Something went wrong, please try again.')
        menu()
    
    

def play_menu():
    print('\n\n')
    
    story_input_loops()
    
    return

def options_selector():
    
    global rand_words
    
    print('\n')
    print('r to toggle shuffle, m to return to menu.')
    
    if rand_words:
        
        print('Shuffle is currently on.')
        
    else:
        
        print('Shuffle is currently off.')   
    
    user_input = ask_for_input(False)
    
    if user_input == 'r':
        
        rand_words = not rand_words
        options_selector()
    
    elif user_input == 'm':
        
        menu()
    
    else:
        print('\n')
        print('Something went wrong, please try again.')
        options_selector()
    
    return

def ask_for_input(allow_empty):
    
    if allow_empty == None:
        allow_empty = False
    
    user_input: str = input()
    user_input = user_input.strip()
    user_input = user_input.lower()
    
    if '#' in user_input:
        print ("Please do not try to break the madlibs generator.")
        return ask_for_input(allow_empty)
        
    elif user_input == "" and not allow_empty:
        'Please enter something before continuing.'
        return ask_for_input(False)
    
    else:
        return user_input
    

def story_input_loops():
    
    mad_file = test_story_init()
    
    fresh_slot_flag: bool = False
    slot_name_holder = ''
    
    for slot_desc in mad_file.slot_list:
        
        i = 0
        while i < slot_desc.request_count:                

            print('\n')

            if slot_name_holder != slot_desc.display_name:
                
                print ('Please enter ' + slot_desc.aan_identifier + ' ' + slot_desc.display_name)
                slot_name_holder = slot_desc.display_name
                
            else:
                print ('Please enter another ' + slot_desc.display_name)
            
            user_input = ask_for_input(False)
            
            if slot_desc.aan_place_flag:
                
                if aan_mode:
                    # run aan-generator and add in front of user_input
                    return
                    
                else:
                    user_input = 'a(n) ' + user_input 
                    
            slot_desc.user_input_list.append(user_input)
            i += 1
            
    for slot_desc in mad_file.slot_list:
        
        random.shuffle(slot_desc.user_input_list)
    story_processor(mad_file)
    

def story_processor(mad_file):
    
    print('\n')
    print('Are you satisfied with your input? (y/n)')
    user_input = ask_for_input(False)
    
    if user_input == 'y':
        
        word_eater(mad_file)
            
    elif user_input == 'n':
        
        story_input_loops()
        
    else:
        
        print('Please enter either "y" or "n"')
        story_processor(mad_file)
        
        
        
    

def word_eater(mad_file):
    
    for slot_desc in mad_file.slot_list:
        
        for word in slot_desc.user_input_list:
        
            mad_file.story_text = mad_file.story_text.replace(slot_desc.slot_id, word, 1)
            
    print('\n\n')
    print("Here is your story!")
    print('\n')
    print(mad_file.story_text)
            

def test_story_init():
    
    slot_list_test = []



    slot_list_test.append(SlotOfSpeech("adverb ending in -ly", "#adverb_1", 1, 'an', False))
    slot_list_test.append(SlotOfSpeech("verb", "#verb_1", 1, 'a', False))
    slot_list_test.append(SlotOfSpeech("adjective", "#adjective_1", 1, 'an', False))
    slot_list_test.append(SlotOfSpeech("name of a place", "#place_name_1", 2, 'the', False))
    slot_list_test.append(SlotOfSpeech("noun", "#noun_1", 3, 'a', False))
    slot_list_test.append(SlotOfSpeech("name of a person", "#person_name_1", 2, 'the', False))
    slot_list_test.append(SlotOfSpeech("verb ending in -ing", "#verb_2", 1, 'a', False))
    slot_list_test.append(SlotOfSpeech("past tense verb", "#verb_3", 2, 'a', False))
    slot_list_test.append(SlotOfSpeech("plural noun", "#noun_2", 1, 'a', False))

    test_story = "There once was tall, #adjective_1 man, by the name of #person_name_1. One day, while #verb_2 near #place_name_1, he saw a massive #noun_1! It was nearly the size of ten #noun_2. \"I have to tell #person_name_1 about this\" he thought, as he #verb_3 there. He #adverb_1 took out his #noun_1 and #verb_3! Having done that, he ran home -to #place_name_1- where he could finnaly #verb_1."
    #verb_2 in #place_name_1, when he spotted #animal_1"
    
    return MadlibFile(test_story, slot_list_test)

help_and_welcome()