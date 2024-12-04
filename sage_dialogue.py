# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:09:01 2024

@author: Xin Yi
"""
import json

with open("assets/skills.json", 'r') as f:
    skills = json.load(f)

skill_type = "power"

sage_dialogue = {
    
    "first_encounter": 
        {
            "welcome": ("You have encounted a sage! \n"
                        "sages are masters of their craft, ready to share their wisdom with those deemed worthy. \n"
                        "Learn from them to unlock new skills and enhance your abilities! \n")
        },
        
    "1":
        {
            "welcome": ("Hello there, traveller! \n" 
                        "I’m here to help you power up. Isn’t this exciting? \n"
                        "Alright, shall we begin? \n"),
        
                
            "quiz_time" :("Wonderful! Now, let’s see how well you’ve grasped it.\n"),
            
            "wrong" : ("Oh no, close but not quite! \n" 
                       "Don’t worry, you’re learning.\n" 
                       "Just remember: Solve it from left to right. \n" 
                       "Practice makes perfect! \n"),
            
            "correct" : ("Brilliant! I knew you had it in you—great work!\n"
                         f"You have learned Skill 2: {list(skills[skill_type]['2'].keys())[0]} \n"
                         "That’s all from me for now. Safe travels, brave one! \n"
                         "Something tells me you’re destined for greatness. I’ll be rooting for you!\n")
        },
        
    "2": 
        {
            "welcome": ("You have encounted a sage! \n"
                        "Hmph. Another feeble adventurer. \n"
                        "Your skills are weak—barely worth my time. \n" 
                        "But... I suppose I can teach you BOBMAS rule. \n" 
                        "Pay attention! \n"),
            
            "quiz_time" : ("Enough spoon-feeding. \n"
                           "Let’s see if you were listening. \n"),
            
            "wrong": ("Ugh… wrong. \n"
                      "It’s like I said: Use the BODMAS rule and solve from left to right. \n"
                      "Fs this time, will you?\n"),
            
            "correct": ("Hmph. I’ll admit, that was better than I expected. \n"
                        f"You have learned Skill 3: {list(skills[skill_type]['3'].keys())[0]} \n"
                        "That’s all the help you’ll get from me. \n"
                        "Now go! The world won’t save itself, and I’ve no time for slackers.\n")
        },
        
    "3":
        {
            "welcome": ("You have encounted a sage! \n"
                        "Greetings, young one. \n"
                        "Your journey has been long, and the road ahead will test your very soul. \n"
                        "But first, it is time to learn the final lesson on how to analysis problem statement.\n"),
            
            "quiz_time" : ("Now, let us see if you have the wisdom to wield such power. \n"
                           "Your understanding will be tested. \n"),
            
            "wrong" : ("Not quite, but do not despair. \n"
                       "Patience is the mark of the wise. \n"
                       "Reflect on this: [give hint]. Then, try again."),
            
            "correct" : ("Yes, that is correct. Your insight serves you well."
                         "Congratulations! \n" 
                         f"You have learned the ultimate skill: {list(skills[skill_type]['4'].keys())[0]} \n" 
                         "Go forth, hero, and fulfil your destiny. \n" 
                         "The world’s hope rests with you, and you have proven yourself worthy of that burden. \n"
                         "Remember, even in darkness, the light of wisdom shall guide you. \n")
        }
    
    }