def secret_code():
    print """
   There are some words which come from sanny & calm love story
   ****************************************************************************************
   wuhan             motorcycle        stage_show         new_life            amazing_lake
   
   firstkiss         beautiful_water   plane_delay        new_car             ancienttown

   4506              monkey            phuket             eiffel_tower        lost_camera

   waterfall         ice_show          cliff_hotel        shipwreck           great_wall

   graduation_trip   snorkeling        snow_house         panda               new_home  
   *****************************************************************************************
   I will give you some prompt about years, you need pick out all the word related to that year.
   If you pick out all the right words, you will pass this round.
   And you have three times to make mistake, if you fail in the forth time, you will fail this game.
   Do you understand the rule?
"""
    understand = raw_input("yes or no: ")
    words_2009 = "wuhan  firstkiss  waterfall  lost_camera"
    words_2015 = "graduation_trip  phuket  motorcycle  snorkeling  ancienttown  4506  great_wall"
    words_2016 = "monkey  beautiful_water  panda  stage_show"
    words_2017 = "ice_show  snow_house  plane_delay  amazing_lake  eiffel_tower  shipwreck  cliff_hotel  "
    words_2018 = "new_life  new_home  new_car"
    if understand == "yes" or understand == "":
        print "Round 1 : 2009"
        playgame_year(words_2009)
        print "Round 2 : 2016"
        playgame_year(words_2016)
        print "Round 3 : 2015"
        playgame_year(words_2015)
        print "Round 4 : 2017"
        playgame_year(words_2017)
        print "Congratulations! you win this game!"
    elif understand == "no":
        print "Please read the rule again!"
    else:
        print "Please input 'yes or no' "


def playgame_year(words_year):
    checkwords = check_words(words_year)
    db_checkwords = []
    length = len(checkwords)
    print "This round will have %d words, good luck! " % length
    i = 0
    j = 3
    while i < length:
        print "Please input the %d word" % int(i+1)
        checkword = raw_input("> ")
        if checkword in checkwords:
            print "Great, you get the %d word, come on !" % int(i+1)
            i = i + 1
            checkwords.remove(checkword)
            db_checkwords.append(checkword)
        elif checkword in db_checkwords:
            print "The word have been input, please choose another word!"
        else:
            j = j - 1
            print "You choose a wrong word, please try again and have %d times" %j
            if j == 0:
                game_over()
                break
        if i == length:
            print "Congratulations! you win this round! "

def check_words(words_year):
    words = words_year.split("  ")
    return words

def game_over():
    print "You fail this game, please go to hell !!!!!!"
    exit(0)
   
def start():
    print """
    Hi calm, 
    Yesterday you said I would ask you the question like: do you love me?
  
    NO!
    NO!
    NO!
    NO!

    This isn't a question, because you just have one answer for it.

    "Yes!"
  
    Must "Yes!"
 
    only "Yes!"
  
    So let's start it! welcome to sanny'game center!
 
    Are you ready?
   """
 
    ready = raw_input("y or n: ")
    if ready == "yes" or ready == "":
        print """
        So let's start it ! welcome to sanny'game center !
        Today the name of game is "Secret code".
        Do you remember it ?
        """
        remember = raw_input("yes or no: ")
        if remember == "y" or remember == "" :
            print "so clever boy,Let's try it!"
            secret_code()
        elif remember == "no":
            print "emmmm..baby..do you want to get some prompt?"
            prompt = raw_input("yes or no: ")
            if prompt == "yes" or prompt == "":
                print "The board game, you brought that, remember ?"
                prompt_remember =  raw_input("yes or no: ")
                if prompt_remember == "yes" or prompt_remember == "":
                    print "OK, finally we can start it."
                    secret_code()
                elif prompt_remember == "no":
                    game_over()
                else:
                    print "Please input 'yes or no' "
            elif prompt == "no":
                print game_over()
        else:
            print "Please input 'yes or no' "
    elif ready == "no":
        print "Why are you coming here?"
        game_over()
    else:
        print "Please input 'yes or no' "

start()