# --- 1. SETUP & CHARACTERS ---
define s = Character("siena")
define q = Character("angela")
define r = Character("mrs. Copper")
define g = Character("maya")
define p = Character("principal")
define l = Character("leya")
# Backgrounds
image bg_gate = "images/landscape1.jpg"
image bg_classroom = "images/classroom.jpg"
image bg_hallway = "images/hallway.jpg"
image bg_hostel = "images/hostel.jpg"
image bg_room = "images/room.jpg"
image bg_office = "images/office.jpg"
image bg_bedroom = "images/bedroom.jpg"
# Sprites
image siena = "images/siena_scared.png"
image siena_thinking = "images/siena_thinking.png"
image siena_confused = "images/siena_confused.png"
image siena_happy = "images/siena_happy.png"
image angela_angry= "images/angela_angry.png"
image angela_laugh = "images/angela_laugh.png"
image maya_happy = "images/maya_happy.png"
image mrs_copper_angry = "images/mrs.copper_angry.png"
image mrs_copper_happy = "images/mrs.copper_happy.png"
image principal_happy = "images/principal_happy.png"
image principal_confused = "images/principal_confused.png"
image leya_shocked = "images/leya_shocked.png"  
# AUDIO    
define audio.theme = "audio/background_track.ogg"
define audio.battle = "audio/action_music.mp3" 


# SCENE 1: THE ARRIVAL
label start:
    play music theme fadein 1.0
    scene bg_hallway with fade
    "8 O'CLOCK"
    "STANDING INFRONT OF THE GATE OF MARDIN HIGH."
    "THIS STORY OF SIENA WHO SWICHTED FROM A PUBLIC HIGH SCHOOL AND HER STRUGGLE TO FIT IN."
    
    scene bg_hallway with fade
    show siena at truecenter
    s "Okie... okie.... i can do this."
    s "Changing highschool wasn't a great idea, but it is what it is."
    s "there goes notingg..."
    pause 1.0

    # SCENE 2: THE CLASSROOM CLASH
    scene bg_classroom 
    show siena_scared at truecenter
    s "woah!!..Its so quiet here... my public school would be exploding with noise right now."
    s "mabe that corner would be fine for today."
    hide siena_scared
    show angela_angry at center with moveinright
    q "hey new girl,where do u think ur doing."
    
    # --- THE OPTIONS START HERE ---
    menu:
        "Talk back to her":
            hide angela_angry
            show siena_angry at truecenter
            s "are you blind? I am taking a seat."
            hide siena_angry
            show angela_angry at center 
            q "Excuse me?! You have no idea who you're talking to!"
            hide angela_angry
            show leya_shocked at center
            l "Oh my god, did she really just say that?"
            $ beef_level = "high"
            hide leya_shocked

        "Just leave it and find other seat":
            hide angela_angry
            show siena_thinking at truecenter
            s "Sorry, I'll just find another seat."
            hide siena_thinking
            show angela_angry at center
            q "That's right, run away. It's the only thing you're worth of."
            hide angela_angry
            show leya_shocked at right
            l "Haha, she's so naive, she can be the new chicken."
            hide leya_shocked
            $ beef_level = "low"

    show mrs_copper_happy at right with moveinright
    r "Girls, everything fine here? huh angela."
    hide mrs_copper_happy
    show angela_laugh at center
    q "Yes, Mrs. Copper. Everything is fine."
    hide angela_laugh
    
    show mrs_copper_happy at left
    r "Class meet our new student, Siena. I hope you all make her feel welcome."
    r "siena, meet at 5, in the hostel,okie?"
    hide mrs_copper_happy
    show siena_happy at right
    s "Sure, Mrs. Copper."
    pause 0.5

    # SCENE 3: THE HOSTEL 
    scene bg_hostel with fade
    show siena_happy at left
    s "Hope this place is better than the classroom..."
    s "I wish my roommate is a bit more friendly"
    
    show maya_happy at right with moveinright
    g "we have separate rooms there, but we can be friends if you want."
    g "I'm Maya, by the way."
    s "Oh, nice to meet you, Maya. I'm Siena."
    g "They're so mean, aren't they? she's the queenbee there."
    s "Well yah, they are a bit... intimidating. But I guess I'll get used to it."
    g "They've always been like that. Even back when I... when I was 'there'."
    s "Oo youre a senior? That's cool."
    g "No silly, we used have ap calcus together, but I dropped it."
    s "Oh that's okay, and call me sie if you want. I don't like formal stuff."
    g "Sure, Sie. So, do you want to hang out later?"
    
    hide maya_happy 
    show siena_happy at center
    s "Yeah, that sounds great! I could use a friend here."
    pause 0.5

    # SCENE 4: KARMA COMES BACK
    scene bg_hostel with fade
    "Maya and Siena quickly become friends, and Maya helps Siena navigate the social scene at school."
    "Next day..."
    scene bg_hallway with fade
    show siena_happy at left
    show maya_happy at right with moveinright
    g "So, how was your day? Again did she mess again?"
    s "Angela was absent today, I heard she was sick and her minions were normal today."
    g "Oh, that's good. I hope she gets better soon. But don't worry about her, she's not worth your time."
    s "Thats karma yk."
    
    hide maya_happy 
    hide siena_happy
    show leya_shocked at center
    l "Youre gosiping about Angela."
    l "But who are you talking to? werido. Anyway youre dead tmrw."
    hide leya_shocked
    show siena_thinking at center
    s "Are they are blind? or wot."
    hide siena_thinking
    show maya_happy at right with moveinright
    g "Just ignore her, I'll take care of it."
    hide maya_happy
    show siena_scared at center
    s "Huh, I don't want to cause any trouble. Maybe it's better if I just stay away from her."
    hide siena_scared
    pause 0.5

    # SCENE 5: THE CONFRONTATION
    "The next day..."
    scene bg_classroom with fade
    show leya_shocked at center
    l "Angela, yesterday she was talking about you, and she was saying some really bad things about you."
    l "She was saying that you're a freak and that you had karma here."
    hide leya_shocked
    show angela_angry at center
    q "whatttttt???? who the hell does think she think she is?" 
    hide angela_angry
    show siena_angry at center
    s " Why are you lying leya? I am not like u guys i have better things to do."
    hide siena_angry
    show mrs_copper_angry at truecenter

    r "whats going on here?"
    hide mrs_copper_angry  
    show siena_thinking at center
    
    # --- THE CRITICAL CHOICE ---
    menu:
        "Tell Mrs. Copper everything.":
            $ told_warden = True
            s "Mrs. Copper, She's bullying me since the first day."
            hide siena_thinking
            show angela_angry at center 
            q "How dare you accuse me of bullying! You're just a pathetic loser !"
            hide angela_angry
            show mrs_copper_angry at truecenter
            r "Angela, this is a serious accusation. We will have to investigate this matter further."
            hide mrs_copper_angry
            show leya_shocked at center
            l "Oh my god, I can't believe she said that! Angela is going to be so mad!"
            hide leya_shocked
        "Stay silent and look at the floor":
            $ told_warden = False
            s "I... No, Mrs. Copper. Everything is fine. I'm just tired from the move."
            hide siena_thinking
            show angela_laugh at center 
            q "yes mrs.copper, everything is fine. I was just helping her around."
            hide angela_laugh
    
    show mrs_copper_happy at right 
    r "Well, I hope you can work things out. But if you ever need anything, don't hesitate to come to me."
    hide mrs_copper_happy
    pause 0.5

    # SCENE 6: THE AFTERMATH
    scene bg_room with fade
    "Back in her room, Siena is alone and confused."
    show siena_thinking at center
    s "I don't know if I made the right choice."
    "Knock knock"
    s "Who's there?"
    g "It's me, Maya. Can I come in?"
    menu:
        "Tell to go away":
            show siena_angry at center
            s "Sorry, Maya. I just need some time alone right now."
            hide siena_angry
            g "Oh, I understand. I'll give you some space. But if you ever want to talk, I'm here for you."
        "Let her in":
            s "Sure, Maya. Come in."
            show maya_happy at right with moveinright
            g "Thanks, I just wanted to check on you. I know things have been tough with Angela and everything."
            hide maya_happy
            show siena_thinking at center
            s "Yeah, it's been really hard. I just don't know how to deal with her"
            hide siena_thinking

    hide siena_thinking
    pause 0.5

    # SCENE 7: THE TRUTH
    "The next day..."
    scene bg_hallway with fade
    show siena_happy at left
    show maya_happy at right with moveinright
    s "AP calculus was so fun today, you should join again."
    g "I wish I could, but I dropped it. I just couldn't handle the stress of it all."
    s "Oh, that's okay. I understand. But if you ever want to try it again, I'm here to help you."
    hide maya_happy 
    hide siena_happy
    show leya_shocked at center
    l "look at the creep!!, she is talking to the locker."
    hide leya_shocked 
    show angela_laugh at center 
    q "Haha, werido talking to herself, what a loser!"
    hide angela_laugh
    show siena_angry at truecenter
    s "Are you blind fr?"
    s " CUZ I CAN SEE A WHOLE PERSON HERE."
    hide siena_angry
    show angela_angry at center
    q "How dare you talk to me like that! You're just a pathetic loser!"
    q "Maybe pschyo too, you should be in a mental hospital, not in school!"
    hide angela_angry
    show leya_shocked at center
    l "yes, youre right Angela, she is a psycho,"
    l "I heard she talks to herself in the bathroom and eats her own hair."
    hide leya_shocked
    show siena_angry at center
    s "What the hell? That's not true at all! Why are they saying these things about me?"
    s "Whats your problem? Why are you so obsessed with me? I just want to be left alone!"
    s "lets go maya, we dont need to deal with this."
    hide siena_angry
    scene bg_hallway 
    pause 0.5
    show siena_thinking at right
    s "Maya, where are you."
    hide siena_thinking
    show leya_shocked at center
    l "Hate on one side but wear the omen bracelet thing are not great here."
    hide leya_shocked
    show angela_angry at center 
    q "SHUT UP LEYA, dont tell her about the bracelet."
    hide angela_angry
    pause 0.5

    # SCENE 8: THE REALIZATION
    scene bg_room with fade
    show siena_thinking at center
    s "Maya totally embrassed me."
    s "Maybe shes not the friend I thought she was."
    s "But what was the point of her telling me about the bracelet? Was she trying to warn me or something?"
    hide siena_thinking
    show maya_happy at right
    g "Hey,everything fine."
    show siena_angry at left
    s " You embarrassed me in front of everyone, and you didn't even try to defend me. I thought you were my friend, but I guess I was wrong."
    g "Sie, i just saw the principal and I got scared."

    menu:
        "Ask her about the barcelet":
           s " what the thing about the bracelets"
           g "They are just some good luck charms that some people wear. I thought it might help you feel better, but I guess it didn't work."
        "Leave it":
            s " i want space right now, Maya."
            g "Oh, I understand."
    pause 0.5

    # SCENE 9: THE REALITY
    scene bg_classroom with fade         
    show siena_happy at center
    s "good morning ,mrs.copper"
    hide siena_happy
    show mrs_copper_happy at right
    r "Good morning, Siena. How are you doing today?"
    hide mrs_copper_happy
    show siena_happy at center
    s "I'm doing well, thank you for asking. I just wanted to say that I really appreciate everything you've done for me since I arrived here."
    hide siena_happy
    show mrs_copper_happy at right 
    r "You're very welcome, Siena. I'm glad to hear that you're settling in well. Remember, if you ever need anything, don't hesitate to come to me."
    r "But sweetie where is your bracelet? I thought you were wearing it."
    hide mrs_copper_happy
    show siena_thinking at center
    s " what bracelet? I don't have any bracelet."
    hide siena_thinking
    show mrs_copper_angry at trucenter
    r " Angela was incharge . She didnt give you one?"
    hide mrs_copper_angry
    show siena_thinking at center
    s "No,I havent"
    s "Anything special about it?"
    hide siena_thinking
    show mrs_copper_happy at right 
    r "It's just a simple bracelet, but it has some significance to the students here. It's a symbol of protection and good luck, and it's usually given to new students by the senior students."
    r "Angela was supposed to give you one, but I guess she forgot or something."
    r "You can collect one from the principal's office."
    r "Class is starting in 5 min, you have time."
    hide mrs_copper_happy
    show siena_thinking at center
    s "Oh, I see. I didn't know about that. Thanks for letting me know, Mrs. Copper."
    hide siena_thinking
    pause 0.5
    
    scene bg_office with fade
    show siena_happy at left
    show principal_happy at right with moveinright
    s "Good morning, Principal. I heard from Mrs. Copper that I need to get a bracelet from you."
    p "Ah, yes. The bracelet. It's a tradition here for new students to receive one as a symbol of welcome and protection."
    p "Here you go, Siena. I hope it brings you good luck and helps you feel more at home here."
    p "How is AP calculus going? I heard you got the highest score on the last test."
    s "Thank you, sir. AP calculus is going well,"
    hide principal_happy 
    hide siena_happy
    show principal_happy at center
    p "That's great to hear. Keep up the good work, and if you ever need any help or support, don't hesitate to come to me."
    p " And remember, you're not alone here. We're all here to support you and help you succeed."
    p "Our highschool is know for well maths yk."
    p "Noone has ever dropped AP calculus."
    pause 2.0
    p "Maybe because its compulsory for everyone."
    p "HAHAHHHAHAAHHHHAHHAAAAAA."
    hide principal_happy
    show siena_thinking at center
    s "Compulsory??? I thought it was an elective."
    pause 2.0
    s "My frn maya dropped out and she said it was optiona!!!!!."
    hide siena_thinking
    show principal_confused at right 
    p "Who's Maya? let me check the records."
    p "There is a maya brookes who was there and she dropped AP calculus in 1989."
    pause 3.0
    p "She was a senior back . She was a very bright student, but she had some personal issues that made it difficult for her to keep up with the coursework."
    p "She probably in her 60s now, how can she be your friend?"
    hide principal_confused
    show siena_scared at center
    s "Wait, what? That doesn't make any sense. How could Maya be a here if she dropped out in 1989?"
    hide siena_scared
    show principal_happy at right with moveinright
    p "Sweetie, nice try, but im funnier and now go to your class."
    hide principal_happy
    
    scene bg_classroom with fade
    show siena_thinking at center
    s "This is so weird. I don't understand what's going on. Why would the principal lie about something like that?"
    s "And why would Maya lie about dropping AP calculus? I thought she was my friend."
    hide siena_thinking
    pause 0.2
    show mrs_copper_happy at right 
    r " limit was actually the ...."
    r "Siena, is everything okay? You look a bit confused."
    hide mrs_copper_happy
    show siena_thinking at center
    s "Yes mrs.copper, is it true that AP calculus is compulsory for everyone? I thought it was an elective."
    hide siena_thinking
    show angela_laugh at center 
    q "HAHAHAHAA, you really thought you could just drop AP calculus? That's hilarious!"
    hide angela_laugh
    show mrs_copper_angry at right 
    r "Angela, that's enough. Siena, AP calculus is indeed compulsory for all students here. I'm not sure why there was a misunderstanding, but it's important that you attend all your classes and keep up with the coursework."
    hide mrs_copper_angry
    show siena_thinking at center
    s " did you have a maya named brookes who dropped AP calculus?"
    hide siena_thinking
    show mrs_copper_angry at center
    r "Maya Brookes? I don't know anyone by that name. Are you sure you're not making things up?"
    hide mrs_copper_angry
    show angela_laugh at center 
    q "HAHAHAHAA, you really thought there was a maya brookes? That's hilarious!"
    hide angela_laugh
    show mrs_copper_happy at right 
    r "Angela, that's enough. Siena, I understand that you're confused, but I assure you that there is no Maya Brookes who dropped AP calculus. It's important that you focus on your studies and not get distracted by rumors or false information."
    hide mrs_copper_happy
    show siena_thinking at center
    s "maya."
    s "maya brookes."
    hide siena_thinking
    pause 0.5
    
    #--- THE CALL-----
    scene bg_bedroom with fade
    show siena_thinking at center
    s "I.. MAYA."
    hide siena_thinking
    pause 0.5

    "SIE!!!!??"
    "YOU CALLED ME ?"
    "TO BE CONTINUED..."
    stop music fadeout 1.0
    return