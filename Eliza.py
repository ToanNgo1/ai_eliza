#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""Eliza chat bot""" 
__author__="Toan Ngo"
# start file
import re
import random
#respond=
name=False
name_log=[]
name_check=["(?<=i am).*", "(?<=can call me).*","(?<=i'm).*","(?<=name is).*"]
pastense_check_L=["hated","used","loved",'hoped']
respond={
    '(hello)':['Hello, nice to meet you!','hi, how are you?'],
    '(hi)':['Hello, nice to meet you!','hi, how are you?'],
    "(how are you)":["oh,i'm doing fine thank you","me doing fine thank"],
    'i feel (.*)':['why do you feel {} ?','how long has it being ?'],
    'i feel (.*) about':["why do you feel that way about them ? ","why do you feel that ?"],
    "i'm feeling (.*) today":['oh no, why are you feeling {}','oh!, what cause you feel that way ?'],
    "i'm (.*)":['oh really, why are you {} ?',' how long has it being that you feeling {}'],
    "i (.*) you": ['what cause you to {} me ?','oh so that how you feel about me.'],
    "i (.*) myself":['why do you {} yourself ?', 'remember to keep everything in morderation even if you {} yourself'],
    "i (.*) family":['why are you feel that about your family ?','what cause you feel {} for your famly ?'],
    "i (.*)":["really?","interesting ?"],
    "(.*) end":["when did it end ?","how did it end ?"],
    "(.*) start":["when did it start ?","how did it start ?"],
    "she (.*) person":['pretty sure they have their own problem to deal with so please just give them some space', 'she must be dealing with her own issue please forgive her'],
    "she (.*)":['why do you think that about her ?', 'why do you think she a {} ?'],
    "he (.*)":['why do you think that about him ?', "why do you think that he a {} ?"],
    "he (.*) person":['pretty sure they have their own reason.'],
    "they (.*) to me":['really?','oh that interesting'],
    "(.*) them":['why do you feel that about them ?','is that how you really feel that about them ?'],
    "(.*) mom":['oh, why are saying that about your mom ?','why are you feel {} for your mom'],
    "(.*) mother":['why are you saying that that about your mother ?', "is that how you feel about your mother ?"],
    "(.*) brother":['oh! tell me more about your brother ?'],
    "(.*) dad":["oh! tell me more about your dad ?", "is that how you feel about your dad?"],
    "(.*) father":["is that really how you feel about your father ?"],
    "(.*) sister":["oh really ?", "how you really feel about your sister ?","tell me more about your sister"],
    "(.*) sorry (.*)":['oh no you dont need to apologize.',"oh please don't apologize"],
    "(.*) friend (.*)":['oho tell me more about those friends of your', 'how does your friend make you feel ?'],
    "(.*) family (.*)":["oh, can you tell me more about your family ? "],
    "(yes)":['you seem quite sure.','ok, but can you elaborate further ?'],
    "(no)":["why not?","ok, but can you elaborate further ?"],
    " (.*) ":["oh please tell me more ?", "tell me about your family.", "can you elaporate on that?"],
    "(.*)":["can you elaporate on that more please ?", "can you go more in dept with that please ?", "im sorry but i dont understand what {} yet"],
    '':['ummm, please tell me something.',"hmmm, can you type something ?","tell me something about yourself.","oh please take your time, i will be waiting >:D","lets talk about your friends."],

}

def bot_respond(input_text):
    for patten,respond_list in respond.items():
        matches=re.match(patten, input_text.lower())
        if matches:
            if matches.group(1):
                #print(matches)
                chose_respond=random.choice(respond_list)
                #print(chose_respond)
                #print(matches.group(1))
                return chose_respond.format(matches.group(1))
            '''else:
                #print("second")
                chose_respond=random.choice(respond_list)
                #print(chose_respond)
                #print(matches.group(0))
                return chose_respond.format(matches.group(0))'''
    #this is when matches fail =no mathes
    return "I'm sorry but i cant understand that yet."

def pastense_check(input_text):
    #global pastense_check
    match=re.search(r'\w*ed\b',input_text.lower())
    if match:
        track=match.group()
        #print(type(track))
        #print(track)
        cath=match.group()[:-2]
            #print(cath)
        if track in pastense_check_L: 
            #print("go in")
            mod=input_text.replace(match.group(),cath+"e")
            return mod
        else: 
            mod=input_text.replace(match.group(), cath)
            return mod
    else:
        return input_text

def name_setter():
    global name_log,name
    print("what are your name users ?")
    while True:
        name=input("your: ")
        for i in name_check:
            mathes=re.search(i, name.lower())
            #print(mathes)
            if mathes !=None:
                #print(mathes)
                value=mathes.group().strip()
                name=True
                break           #for break
        if name==True:
            break           #while break
        else:
            print("can you try that again please")
    name_log.append(value)
    print(f'Hello {name_log[0]}!')
    
#main method
if __name__=="__main__":
    print("welcome to ELIZA chatbot lite")
    name_setter()
    '''while name==False: #Name setter 
        print("what are your name users ?")
        while True:
            name=input("your: ")
            for i in name_check:
                mathes=re.search(i, name.lower())
                print(mathes)
                if mathes !=None:
                    print(mathes)
                    value=mathes.group().strip()
                    break  
        name=True
        name_log.append(value)
        print(f"hello {name_log[0]}")'''
        
    while True:
        user_input = input("your: ")
        if user_input.lower() =='bye':
            print(f"goodbye {name_log[0]}")
            break
        else:
            pastense_checker=pastense_check(user_input)
            print("Eliza: "+ bot_respond(pastense_checker))
