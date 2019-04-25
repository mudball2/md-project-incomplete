label start:
    with fade    

    stop music #Stops main menu music because apparently it can't stop it's own channel.
###################################
#TODO: Reserved for Prologue.
###################################

#Day 1: Going to School. After Prologue_2
    #scene bg
    scene bg_passenger_car with fade

    tc "The six o'clock train is now departing. Please take your seats and stand clear from the doors."

    tc "The six o'clock train is now departing."

    w "[[I started having some strange dreams last night. I can't help but feel like it\'s some sort of omen, especially now that I start classes today.]"

    w "[[This wasn't happening before, and these dreams don't sound like anything good can come from them.]"

    w "[[The commute from the dorms to the Campus' Main Station was about 40 minutes. It involved going through a tunnel that sat under a mountain range separating the dorms from the academy.]"

    w "[[The academy, of course, had its foundation built on a valley inside the range.]"

    w "[[It actually made for some beautiful scenery, but the chilly weather persisted even up into the summer months.]"

    w "[[Since the trains ran 24/7 and also simultaneously accomodate for the commute by providing dining facilities and private seating, most people never complained about the time alloted for the commute.]"

    w "[[I certainly had no problem sitting by myself. I figured it would do me good to avoid any problems immediately. Plus the private seating did provide some amount of peace, but peace is easily interupted.]"

    w "[[The door leading to the hallway outside my seating compartment opened, and a young woman was standing at the doorway with two men accompanying her.]"

    w "[[Trouble?]"
    
    w "[[No, maybe the seating ran out. Unlikely, though.]"
    
    w "[[She was clad in the academy uniform and on her left sleeve was a crest. The crest didn't signify that she was a student at Praesentia though, but that she was a Hackett.]"

    w "[[I suppose a Hackett wouldn't come here to start trouble with me.]"

    w "[[Though...I have been wrong before.]"
    
    #im.Flip(ch_jodie_neutral, vertical=True)
    
    show ch_jodie_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    qm "May I come in?"

    w "Sure."

    w "[[She was a beautiful young woman. I wasn't surprised, but I was definitely a little shocked. Not just by her, but because of the fact that I wasn't expecting any interaction today.]"

    w "[[She was the only one that entered, the two accompanying her waited outside the door.]"
  
    w "[[I felt like a high school kid thinking it, but if all women attending the academy looked like her, I just may yet enjoy what time I'll spend here at Praesentia.]"

    qm "Hello, Wyatt. I'm Jodie Lawson, the Hackett representative for the student council here at Praesentia. It is to my knowledge that Professor Yawakaze was touring you for orientation yesterday. Is that correct?"

    w "[[I was still speechless from the shock of anyone coming to greet me, especially this early in the day.]"

    w "[[My silence persisted just long enough for her to speak again.]"

    w "[[She smiled.]"
    
    hide ch_jodie_neutral
    
    show ch_jodie_happy at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    j "Is there something on my face?"

    w "[[It seems my apparent staring may have lead to a misunderstanding already.]"

menu:
    "No":
        jump a

    "Hello":
        jump p
 
    "It's nothing. Yes, he showed me around.":
        jump h

# codeBlc Aggressive Answer
label a:
    play music "music/JodieTheme.mp3"
    
    w "No, your face is perfect."

    w "[[Crap, I didn't quite mean it to come out like that.]"

    w "[[Jodie's smile remained, and a soft giggle escaped her lips]"
    
    hide ch_jodie_happy
    
    show ch_jodie_laugh at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    j "Thanks, I work hard to maintain my complexion." 

    w "[[Even though my cliche compliment was a bit too obvious, she seemed to take it well. I might be able to push this further.]" 

    w "With looks like yours, it couldn't possibly be all that hard."

    w "[[Yeah, that was probably pushing it too far.]"

    w "[[But still....she didn't seem all that fazed by it. My only assumption was that she got stuck in these conversations all too often.]"
    
    hide ch_jodie_laugh

    show ch_jodie_happy at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)
    
    j "Thanks again, Wyatt. I do have other rounds to make this morning, though. May we begin?"

    w "[[I broke the ice a bit, but her business-as-usual nature seemed to take precedence here.]"

    w "[[At the very least, I was learning that I was more or less treated like an equal here. I guess it wouldn't be possible for everyone to know my background.]"

    w "Of course."

    w "Professor Yawakaze was the one who showed me around yesterday."

    j "Great. So did she tell you about our Student Learning Aid?"

    w "She may have mentioned it."

    w "[[Although I failed to notice it before, she was holding a container similar to the dimensions of an average suitcase. She laid in front of her, on her lap, and proceeded to opening it.]"

    w "[[Afterwards, she turned the case my direction and inside was an electronic device made to equip on one's forearm. An SLA as the Professor yesterday had initially called it.]"

    j "This little device will help you out during your time here at this academy.  It has installed your schedule, a school map, a student planner, games and a lot of other stuff that will probably prove useful."

    j "It is called an Asla by many of the students here."

    j "Professor Yawakaze would've given you this yesterday, but she can be forgetful at times.  Giving it to you now beats wandering aimlessly around campus."

    w "I had actually planned on visiting the Administration building."

    j "Oh, well then you would've ran into me anyways. Doing this now just saves us both time later in the day."

    w "[[She gave a slight nod.  I took this as permission to grab the Asla from the case so I did.]"

    w "It's a little lighter than I had thought."

    j "It's a good thing though, trust me. "
    
    w "[[She closed the case and stood up.]"

    j "Oh, as the Hackett representative for the Student Council you can contact me at any time through the Asla should any problems arise or if you should fail to understand the device."

    j "Any thing you ask will be given to either me or my assistants via email."

    w "So I can contact {i}you{/i} anytime?"

    j "Yes."

    w "How do I use this?"

    j "Play around with it. Thank you for your time, Mr. Armstrong."

    w "[[She went back to formalities at some point.]"

    w "Thank you for making me worth your time."
    
    hide ch_jodie_happy with dissolve

    w "[[She opened the door leaving the seating compartment. The two standing outside the door followed her down the hall on each side of her like bodyguards, I watched as she walked away until the door closed automatically.]"
  
    w "[[This device? An Asla.]"

    w "[[I heard Professor Yawakaze call it a SLA device yesterday. I wonder if that's the faculty's name for it or something. I might've asked Jodie to clarify, but I guess anyone at the school would know.]"

    w "[[I examined the Asla closely. It was made to strap at least two-thirds of an individual's left forearm. It was an electronic device based on a weapon of the elite that was produced a number years back.]"

    w "[[If I recall correctly, it was originally made to transfer magic energy into raw energy. Many in the higher social classes had a great affinity for magic energy, and as a result, a lot of raw energy was made from it.]"

    w "[[I put the device on my left forearm and it adjusted itself automatically. It felt a little tight, but I couldn't really do much about it.]"

    w "[[I thought for a brief moment of seeing if I could perhaps use my magical energy to produce some unique energy, but I had my doubts. Bad blood meant bad affinity.]"

    w "[[I still wanted to give it a shot though.]"

    w "..."

    #TODO: Sound effect of notification.

    #TODO: Custom SLA device textbox graphic?
    d "Energy alteration is not available for use on commuter train. Only classrooms approved for magical use."

    w "[[Oh, well. Whether it is magic or raw energy, I'm not expecting much, but it may be easier to fit in here if I could get some basics in.]"

    w "[[The commuter train would be arriving to the campus sooner than I would like to think, I might as well enjoy this peace.]"

    jump firstClass

# endBlc

# codeBlc Passive Answer
label p:
    play music "music/JodieTheme.mp3"
        
    w "[[I chose to dismiss the joking question and continue with the conversation at hand. It was more on instinct than it was reasoning, however.]"

    w "Hello, Jodie. I was going to visit the Administrative Building today, but I'm guessing you're here to save me the trip?"

    j "That was part of the plan, yes. Professor Yawakaze has a knack for being forgetful, and she was supposed to give you something essential yesterday which I'm here to deliver."

    w "[[She tapped a suitcase that I failed to see when she walked in.]"

    j "It will serve you well in figuring out what you're supposed to be doing for the rest of the day, and many days afterward. It's also a tool you'll be using in your core classes."

    w "So...\"essential\"?"

    w "[[We were implicitly making fun of the good-natured professor. At the very least, I was.]"

    j "Very."

    w "[[She picked up the case and placed it on her lap facing me while opening it. Inside was a device that looked like a bracer of some sorts. In fact, it was an electronic device that was mainly accustomed to military use.]"

    j "This is a Student Learning Aid, we call it an Asla here. It's a typical magic alteration device, but this one has been packed with software that will prove useful in your classes."

    j "It will also show you your schedule and a map with your classes."

    w "Well, this saves me time."

    w "[[Suddenly, I didn't feel as bad for making fun of the professor.]"

    w "[[I reached for the Asla inside the case and examined it closely when it was in my hand. Looked simple enough to use. Basically a tablet on a wrist; with some other quirks as well.]"

    w "Thanks."

    w "[[I was hoping she would leave with that, but she apparently had more to say.]"

    j "The magic alteration function won't work outside your core class, although everything else should work fine regardless of your location."

    j "It also doesn't inhibit your magical energy. So you can use whatever magic you specify in without worry."

    w "[[She didn't seem to have any knowledge of my background. What she just said was enough to tell me that. I doubt with my low magical affinity I could do anything to impress this woman, let alone myself.]"

    w "[[I decided to play along though.]"

    w "Oh, good. I wouldn't want to go without that."

    j "Most of us wouldn't."

    j "If you don't my asking; what is your magic?"

    w "[[I wasn't even sure what to call it. I wasn't very fond of it, and it was magic that took me from my quiet life with the Cartwright's. Considering where I was, however, I would just have to accept that.]"

    w "Telekinesis, I guess."

    j "Interesting...I can't recall any Hackett who has that power. It's pretty unique for anyone, actually; is that even really magic?"

    w "Can't say, but it is more or less what got me here."

    j "Maybe it's the rarity of it, then. Oh, well...I thought to acquaint you with someone, but I suppose not." 

    j "Well, I have other rounds to make. If any urgent questions arise, you can contact me via email with your Asla. Me or one of my assistants will get back to you as quickly as possible."

    w "[[She stood and got ready to leave.]"

    j "Should you need help looking for a friend, find me. I'll help you if I can."

    w "Thank you again."

    j "Bye."
    
    hide ch_jodie_happy with dissolve

    w "[[She opened the door exiting the seating compartment. The two that were accompanying her followed suit like bodyguards. I watched them walk away unitl they were out of sight and the door shut automatically.]"

    w "[[After that, my attention turned immediately to the Asla I was given.  Or an SLA device as Professor Yawakaze had called it.  The name of a weapon that turned magic energy into raw energy.]"

    w "[[Regardless of its origins, it didn't look all that threatening.  I placed it on my left forearm and the device adjusted automatically.]"

    w "[[It felt a little tight.]"

    w "[[I proceeded to look at my classes and their locations before returning back to the peacefulness I had started with.]"

    w "[[\"Should you need help looking for a friend.\"  I sort of hoped I could pass my time here without too much interaction with the higher ups.  Coming here wasn't exactly voluntarily.]"

    jump firstClass

# endBlc

# codeBlc Hesitant Answer
label h:
    play music "music/JodieTheme.mp3"
    
    w "It's nothing. Yes, it was Professor Yawakaze that showed me around. "

    j "Alright, good. I'm sure she told you about the Asla that she failed to give to you too."

    w "[[She pointed to a suitcase she had brought in with her. I was assuming that this device she was mentioning was tucked nicely into it. The professor had called it a SLA though, and I was planning on going to the Administration building to pick it up.]"

    j "I'm here to deliver it so that way you wouldn\'t be wandering aimlessly around campus for your first day. Had you been registered the same time as everyone else, it wouldn\'t have been a problem."

    j "It\'s abnormal for a student to be admitted this late in the semester, but I guess you either had good reasoning or a high enough social status for anyone to care. What\'s your story?"

    w "..."

    w "[[I didn\'t really want to answer that. Neither case she mentioned was correct, and I didn\'t even know the reason for my own admission. I do know it involved Hito intervention, though. That\'s it."

    w "[[They were the ones that intercepted me during my quiet life with the Cartwright\'s.]"

    j "Not much of a talker, are you?"

    w "..."

    w "[[I wasn\'t really trying to be rude, but I felt like the conversation so far answered that question. Usually I did like talking, I was just a little out of my element.]"

    w "...Not really."

    j "Alright, then. I guess I should just wrap up here then."

    w "[[She picked up the suitcase she had brought in and opened it on her lap facing toward me. Inside was this device she called an Asla. I wasted no time in grabbing the item from the case and proceeded to examing it.]"

    w "...An Asla?"

    j "A student learning aid."

    j "It has your class schedule and locations. It will also prove useful in your core classes by providing learning software and of course it\'s function to turn magic energy into raw energy."

    j "As you know, military training is part of the curriculum here at Praesentia. The main alteration function won\'t work outside your classes though, but won\'t inhibit your natural magic either."

    w "[[I placed the device on my left forearm. It was basically the tablet version of a bracer. The device even adjusted itself to a certain tightness around my arm.]"

    w "It's tight"

    j "Think of it as being secure."

    w "[[She\'s clearly an optimist. However, I say that with confidence, even knowing that I\'m not the best judge of character.]"

    j "It will serve you well."

    w "Thanks. At least I know where I'm going today."

    j "I'm glad I can help. Plus, I do my best to make sure that every Hackett at Praesentia is well prepared. It\'s my job."

    w "Right..."

    w "[[She closed the case and then put it back on the floor.]"

    j "If you tell me what magic your core class will cover, I can also see about finding you a friend."

    w "[[Maybe if I spoke more, she wouldn\'t of felt the need to say something like that. I couldn\'t help but feel it was something my mother would say and do too.]"

    w "I think I\'ll manage."

    j "If you insist, but the offer stands."

    w "[[She got up and was preparing to leave.]"

    j "Also, seeing as how you\'re a little...timid. I\'d be sure to stay away from the Heidler\'s. They won\'t treat you well here if you\'re like that."

    w "I didn\'t expect them to treat me well regardless."

    w "[[I heard a giggle escape from Jodie\'s mouth.]"

    j "Perhaps you\'re right."
    
    hide ch_jodie_happy with dissolve 

    w "[[With that, she opened up the door exiting the seating compartment and walked away. The two that accompanied her followed suit like bodyguards. They never made a noise while waiting outside.]"

    w "[[Well...that went well.]"

    jump firstClass
# endBlc 

# endBlc

# codeBlc First Class
label firstClass:
    stop music

    scene bg_train_station

    w "[[After examining the Asla on the commuter train, memorizing my schedule and orientating myself further with the map of the school, I was pretty confident I could make my way around single-handedly.]"

    w "[[Jodie had in fact done her job well in making sure I wouldn\'t be walking around aimlessly.]"

    w "[[Since the school is especially large to go traversing every location on foot, the station where the commuter train left off had rail cars to take students to various parts of the school.]"

    w "[[I checked my Asla one more time to make sure I was going to board the right railcar and after assuring myself a few times I boarded it so that it would take me to my first class. ]"

    w "[[It just so happened that this class was scheduled for the same time every day out of the week. ]"

    w "[[It was unusual since Praesentia ran off a block scheduling system, so I will have to ask at some point whether core classes surrounding the use of an individual's magic was usually scheduled that way or not. ]"

    w "[[The rail car began to take off. ]"

    #TODO: SFX of doors closing on a rail car. Hydrolic in nature.

    #TODO: Transition. In a hallway.

    #TODO: Walking SFX.

    w "[[Although the orientation I attended was a little less than informative, it did allow me to see many parts of the school and the types of classes that they had to offer. Even after attending that though, I still didn't remember this building at all. ]"

    w "[[Unless the Asla had lead me astray this is where my class was being held. Trusting the device, I scanned for the room number that it had displayed. ]"

    w "[[I did eventually come across room 404 but it was different from the other classrooms. It was...smaller. ]"

    w "[[It was not a double door like the rest of the classrooms, and there was no other door that was labelled by the same number. Which would have indicated that the room would extend down a hallway. ]"

    w "[[I was a bit perplexed and was beginning to question my own ability to read a map. ]"

    w "[[Regardless of my doubts, I entered. Not totally sure what to expect. ]"

    scene bg_classroom

    w "[[The room was large enough to house twenty or so seats that were lined up neatly and with a large desk that faced all of the student desks. ]"

    w "[[There was a man in the chair behind the desk. Presumably, the instructor. ]"

    qm "Wyatt Armstrong?"

    w "[[He was asking this in a matter-of-factly kind of way. Trying not to miss this cue like I did with Jodie's on the train, I answered. ]"

    w "...Yes."

    qm "Take a seat."

    w "[[His voice was coarse, and it had a considerable amount of authority behind it. So naturally, I found a seat and sat down.]"

    w "... ... ..."

    #TODO: Show passage of time with the BG/CG.

    w "[[He was also considerably quiet for a man that was supposed to teach me. Class started half an hour ago and I still have two and half more to go. ]"

    w "[[I bided my time fiddling with the Asla and learning to use it. From it, I learned that this man's name was Dr. Shimazu. I also learned I was bored. ]"

    w "[[Without thinking, I finally spoke. ]"

    w "Do you plan on teaching today? "

    sh "No."

    w "[[An immediate response!]"

    w "Do you {i}plan{/i} on teaching me? "

    sh "Eventually."

    w "[[It seemed like these one worded answers were all I was going to get from him, but then I decided to inquire why I was the only student in the class.]"

    w "Am I the only one in this school who has telekenetic magic affinity?"

    sh "No...I do too."

    w "[[I felt I had a small victory since he at least gave me an elaborate answer. Well, elaborate for him anyway.]"

    w "[[I decided to take my chances]"

    w "Can I leave?"

    sh "No."

    w "[[I let out an exasperated sigh. Usually I'm more patient, but this whole surprise school thing and leaving the comfort of my old home seems to be testing that patience.]"

    w "[[I was hoping to have at least one class where I was practically doing nothing, but I wasn't hoping for it to be my core class, the one that took the most time out of the day.]"

    w "[[I had to do something to kill the time...]"

    w "[[I looked at Dr. Shimazu to see what he was doing to prevent boredom, but he seemed content sitting on his comfortable chair in the front of the classroom. I unfortunaltely couldn't do that without going crazy.]"

    w "[[What should I do?]"

menu:
    "Might as well try teaching myself.":
      jump a2

    "Wait...could this be a test?":
      jump p2

    "Going to sleep is the best option.":
      jump h2

label a2:
    w "[[As a child I always knew that I had a magical affinity, but like most others in my family it wasn\'t really practiced or known of because there wasn\'t much point.]"

    w "[[Like trying to make Helium atom with a single Hydroden atom, we didn\'t really have enough to get the desired outcome. Or that\'s what we always assumed.]"

    w "[[Practicing magic only seemed to prove the fact. The divinity of each family can ablaze whole forests, conjure whole armies, even crush mountains into sand. I could flip a page with enough concentration.]"

    w "[[I looked at Dr. Shimazu one more time, he had pulled out a book at some point and was dedicating a good amount of focus into it.]"

    w "[[So in response, I pulled out a pen from my jacket pocket and placed it on my desk.]"

    w "[[Paper is simple enough, I was going to try conjuring enough of my magic to at least get this pen to move.  From my preconception: my magic is rare, but it also seems more like a mind trick than a magic trick.]"

    w "[[Perhaps if I treat it like exercise it'll get stronger. The concept seemed to work for the individuals of higher social standing.]"

    w "[[I hovered both my hands over the pen and used all my strength to get some kind of reaction out of it. It's hard to explain, but somehow magic is simultaneously physically and mentally straining on the body.]"

    w "[[I'm not sure what it feels like for everyone else like me, but nausea and light-headedness are my symptoms for using too much magic.]"

    #NOTE: I'm going to say that emphasis on the pen would be very important here. If animation could be implemented it would be very kool. If not, a tremor of the screen will do.

    w "[[My limbs were tingling strangely as if my blood was boiling within them, but I was noticing the slight vibration of the pen in front of me.]"

    w "[[A response! This was a good sign.]"

    w "[[Even though the pen was appearing to lift slightly I felt like the very life was draining from my body as I was trying to lift it from the desk.]"

    w "[[With a loud gasp I did one last hurrah on the pen and it flipped.]"

    w "[[I put my weight on the desk and I was panting a sweating. Being out of breath made me question if I was even breathing during that endeavour.]"

    sh "BAHAhahaha!"

    w "[[My eyes shot up to see Dr. Shimazu genuinely laughing.]"

    sh "It would be easier to write by picking up the pen don't you think?"

    w "[[Suddenly his face went serious again.]"

    w "[[I'm not sure why, but this time his face sort of startled me and authority returned to his voice.]"

    sh "Here!"

    w "[[The book on his desk flew off and flew towards mine at lightning speed slamming onto the surface. It opened flipping throught the pages to around the center of the book.]"

    sh "Use that for exercise!"

    w "[[It's almost as if he read my mind, asking me to flip pages for exercise. I felt somewhat insulted at first, but knew it would probably be easier like this.]"

    w "[[So I caught my breath wiped my forehead with the back of my hand and started reading, flipping the pages handlessly as I progressed.]"

    w "[[It was a storybook, and I briefly wondered why he would be reading this of all things. As a result I looked up to catch a quick glimpse of him writing in a pocket sized notebook.]"

    w "[[After what happened earlier today, I learned it was better not to ask]"

    #NOTE:I may include prologue 1.5 here, but it would also mean limiting this information to assertive players. The storybook would of course be in the fashion of the Human perspective rather than the Angels. It would of course be teaching kids the importance of treating those with a higher social status with respect and obediance.

    w "[[I kept flipping the pages as I read.]"

    w "[[With this, I was at least hoping that this class would not be as boring as I had initially thought.]"

    jump Lunch

label p2:
    w "[[It\'s possible it might be, but I don\'t know. I looked back to Dr. Shimazu and he was just staring off to the distance and stroking his unkept beard with his left hand.]"

    w "[[The only test that would involve that is some sort of meditation. It sounds relevant to the Telekinetic magic affinity that I was supposed to be taught how to use in this class, but it why would he say he wasn't going to teach me and attempt to teach me.]"

    w "[[...Unless that was part of the test]"

    w "[[Now it just sounds foolish]"

    w "[[I placed my elbows on the desk and rested my head on my hands. After that I tried to meditate.]"

    w "... ... ..."

    w "[[How does one actually meditate?]"

    #NOTE: Unless I find more ideas for this direction, for now this arc will be continued in with the assertive continuation. I feel like a passive person may end up coming to the conclusion of trying somethin especially in an attempt to fit.

    w "[[Do I even really need this guy?]"

    w "[[I wouldn't think so. I may have lucked out with this class, but as I meet people fitting in may work out better for me.]"

    w "[[This is sort of a fresh start, no one actually knows my origins as of now, even if they did learn it, it would be hard for the whole school to find out considering the size.]"

    #NOTE: Here we are contemplating either to do a contuination of the aggressive arc or continue the passive arc. For now aggressive will be implemented.

    #Note: I got rid of AJ's rendition after the last note. and noticed that the conclusion jumped to lunch rather than jumping to the assertive arc like I requested. So I added an approriate continuation here. 

    w "[[I looked at Dr. Shimazu one more time, he had pulled out a book at some point and was dedicating a good amount of focus into it.]"

    w "[[So in response, I pulled out a pen from my jacket pocket and placed it on my desk.]"

    w "[[Paper is simple enough, I was going to try conjuring enough of my magic to at least get this pen to move.  From my preconception: my magic is rare, but it also seems more like a mind trick than a magic trick.]"

    w "[[Perhaps if I treat it like exercise it'll get stronger. The concept seemed to work for the individuals of higher social standing.]"

    w "[[I hovered both my hands over the pen and used all my strength to get some kind of reaction out of it. It's hard to explain, but somehow magic is simultaneously physically and mentally straining on the body.]"

    w "[[I'm not sure what it feels like for everyone else like me, but nausea and light-headedness are my symptoms for using too much magic.]"

    #NOTE: I'm going to say that emphasis on the pen would be very important here. If animation could be implemented it would be very kool. If not, a tremor of the screen will do.

    w "[[My limbs were tingling strangely as if my blood was boiling within them, but I was noticing the slight vibration of the pen in front of me.]"

    w "[[A response! This was a good sign.]"

    w "[[Even though the pen was appearing to lift slightly I felt like the very life was draining from my body as I was trying to lift it from the desk.]"

    w "[[With a loud gasp I did one last hurrah on the pen and it flipped.]"

    w "[[I put my weight on the desk and I was panting a sweating. Being out of breath made me question if I was even breathing during that endeavour.]"

    sh "BAHAhahaha!"

    w "[[My eyes shot up to see Dr. Shimazu genuinely laughing.]"

    sh "It would be easier to write by picking up the pen don't you think?"

    w "[[Suddenly his face went serious again.]"

    w "[[I'm not sure why, but this time his face sort of startled me and authority returned to his voice.]"

    sh "Here!"

    w "[[The book on his desk flew off and flew towards mine at lightning speed slamming onto the surface. It opened flipping throught the pages to around the center of the book.]"

    sh "Use that for exercise!"

    w "[[I caught my breath, wiped my forehead with the back of my hand and started reading, flipping the pages handlessly as I progressed.]"

    w "[[It was a storybook, and I briefly wondered why he would be reading this of all things. As a result I looked up to catch a quick glimpse of him writing in a pocket sized notebook.]"

    w "[[After what happened earlier today, I learned it was better not to ask]"

    w "[[I kept flipping the pages as I read.]"

    w "[[With this, I was at least hoping that this class would not be as boring as I had initially thought.]"

    jump Lunch

label h2:
    w "[[Actually...I was a little hesitant to do anything to kill time. It may end up bringing about more circular conversation with this man.]"

    w "[[The only option that didn't really bring about to much attention to myself was to sleep, and I found it to be a pretty good idea.]"

    w "[[I crossed my arms over the desk I was sitting at and laid down my head.]"

    w "[[Closing my eyes I began to wonder whether or not I would wake up in time for my next classes, but if I recalled correctly it was lunch for me right after this period.]"

    w "[[That being said I guess it was no problem, unless I ended up sleeping the whole day. Which I think is extremely unlikely. Surprisingly I slept well last night.]"

    w "[[Eventually I began thinking very little about anything, this whole extra schooling was strange already. If I just let all the strange things happen maybe they would stop eventually.]"

    w "[[My last thought was thinking that wouldn't be so bad before losing consciousness.]"

    w "[[Wasn't long though before I started hearing voices again.]"

    qm "Sleeping Wyatt?"

    qm "Action is not always the best way to proceed, but no action is never the right way to."

    w "[[That doesn't even mean anything.]"

    jump Lunch
# endBlc

# codeBlc Lunch

label Lunch:
    
    # Show the lunchroom scene beginning
    scene bg_lunch_day with fade
    
    w "[[The bell rang signalling the end of the class, I got up from my seat and walked promptly to the door.  My core class wasn't really that eventful so I wasn't exactly in a hurry to stick around.]"

    w "[[Dr Shimazu, who had stayed quiet for the majority of the class still remained silent as I dismissed myself. I wasn't going to instigate a conversation either. Three hours with that man was more than enough for one day.]"

    w "[[Perhaps I wasn't giving him enough credit though, for all I knew everyone on campus teached this way. Which would really suck, so I doubt it's the case.]"

    w "[[I left the room and worked my way to a railcar that was to transport me to a building near the center of campus that housed a large food court. As far as Praesentia was concerned it was nothing more than a cafeteria.]"

    w "[[I was hungry.]"

    w "[[The Cafeteria was definitely larger than most food courts, and had a wide variety of cuisines to choose from. I got something that was reminiscent of the Western continent from which most Hackett's hailed.]"

    w "[[It seemed like a pretty crude dish compared to the Eastern continent of the Hito's and the Central of the Heidler's, but as history would have it, the Hackett's didn't care for spending too much time to prepare a dish.]"

    w "[[A slab of beef with some other tender sides was more than enough for dining on, especially since traditionally life was rougher the further west you went. It's a pride of the Hackett's rather than being seen as a downfall.]"

    w "[[What good actually came from being picky about food?]"

    w "[[I guess I was no different in that front, but the other cuisines did look a lot more delicious.]"

    w "[[The only problem was...I didn't want to sit next to anyone.]"

    w "[[This seemed almost impossible though from looking around the dining facility. I went to look at the seating outside...it was also packed.]"

    w "[[I continued to walk further from my meal's origin until the number of people eating in random locations started dwindling to zero. Somehow though I still found myself entering a random building and sitting inside one of the classrooms to eat.]"

    w "[[This classroom was slightly larger than my last, and looked like a lab for some scientific studies. Praesentia acted as a school that taught both career and magic education. Working almost like any other university but with more emphasis on the magical arts.]"

    w "[[That being a difference, and also who gets to attend it. The highest in the ladder, or the best of the best from around the world. Everyone here will take part in running the world eventually.]"

    w "[[I can't see myself as one of those people though.]"

    w "[[I began to eat my lunch in the silence of this vacant room.]"

    qm "I'm sorry, but what are you doing here?"

    w "[[I stopped chewing immediately.]"

    w "[[Crap! Was I not allowed to be in here or something?]"

    w "[[I turned around to confront the person asking the question but was rather surprised by what I was greeted with. It was a young woman that was neither clad in the school uniform nor in the usual garbs of an instructor.]"
    
    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0) with dissolve

    w "[[Judging by what she was wearing she was here to clean...and no doubt, a plebeian.]"

    w "[[I could definitely just ask her to go away, but that would only work depending on who told her to come here. Was it another plebe, or was it of someone with higher social standing than me?]"

    w "[[Of course I could also just tell her why I'm here. She can't tell me to go away. Although I'm not too much higher up the ladder than she is, I'm still of better standing than her.]"

    w "[[What I did didn't matter, but I had to say something.]"
    

menu:
    "Why are {i}you{/i} here?":
        jump a3

    "(Tell her the truth) I'm just eating. (You like eating)":
        jump p3
 
    "Um...hello?":
        jump h3

# codeBlc Aggressive Answer
label a3:
    
    play music "music/KaoriTheme.wav"

    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    w "[[Might as well exercise some power.]"

    w "[[With that being said I suddenly lost sight of this person as she shot down.]"

    w "[[I looked down to try and meet her gaze again and I found her kneeling behind the seat I was in. Her eyes were shut tight and she appeared very nervous.]"
    
    hide ch_kaori_netural
    
    show ch_kaori_scared at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    qm "I-I\'m v-very sorry your holiness!! I was just told no one would be here! I was sent to clean! I\'m sorry!"

    w "[[Holiness? I was hardly at that rank, but I guess to a plebeian it didn\'t matter much. She was being a little loud too.]"

    w "[[I took a quick look around the room.]"

    w "They sent you to clean this whole place by yourself?"

    w "[[She laughed nervously and looked embarrassed]"
    
    hide ch_kaori_scared
    
    show ch_kaori_laughblush at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    qm "I guess I\'m sort of being punished your holiness."

    w "Punished for what?"

    qm "I\'m too embarrassed to say, but it did involve a fusebox or something like that."

    w "[[I was curious, but decided not to ask.]"

    w "Must have been pretty bad."

    w "[[She laughed nervously again.]"

    w "[[She looked a little afraid of me, probably because of my faked irritated response initially.  I may have carried this misunderstanding on too long...?]"
   
menu:
    "POWER!":
       jump a4
    
    "It's better to be polite for a favorable first impression.":
       jump ph
       
label a4:
    #>>Random note: I'm writing this without completing the continuation: I already hate it. We'll try to see what we can do differently. I may omit entire section and just continue with P/H continuation.

    w "[[I couldn't help but grin at the thought. Back home I was always the one that was bullied and forced to do things I didn't want to do, but now I was in Praesentia. I have a chance to rise through the ranks, I should learn to live with it.]"

    w "[[The schools were segregated when growing up, and no plebeians ever went to a school where divine blood was present, they didn't even receive the same amount of schooling. As a result I never had a chance to see what it was like to be above someone.]"

    w "[[Right now I was above her, more importantly she was likely told to clean this place by another plebeian and whose order I can easily overcome. The Cartwright's whom I lived with were usually the ones ordering plebeians and myself around.]"

    w "[[Adding some authority to my voice I decided to play around a little bit.]"

    w "What\'s your name?"
    
    hide ch_kaori_laughblush
    
    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    k "Kaori, your holiness."

    w "[[She seemed concerned.]"

    w "Sit down over here."

    w "[[I motioned to a chair that was a seat away from me. As I expected she unquestioningly complied.]"

    w "You can clean after I'm done eating."

    w "[[She looked offset by the remark. I can imagine it was because cleaning this whole room by herself would already take up quite a bit of time.]"

    w "[[It wasn't my problem if she had a deadline though.]"

    w "[[I began to eat again, and it was peaceful. I had remembered then that she had ruined my initial peace, so I guess this could serve as bit of a punishment. In fact she did resemble a child placed in timeout like that.]"

    w "[[Perhaps that's how she saw it too.]"

    w "[[Looking at her carefully now I could see she was about my age, it was just that her antics made her seem childish.]"

    w "[[I think there's a word for it...was it...spastic. I don't know. She was a nervous wreck from my perspective.]"

    w "[[She was looking down, frowning and trying not to stare.]"

    k "Um..."

    w "[[I finished chewing before I answered.]"

    w "Go ahead."

    k "If you don't mind my asking again, why are you here your holiness? Eating here I mean."

    w "I\'m trying to avoid people, and you can call me Wyatt. "

    w "[[I bit another fork-full of food.]"

    k "Very well, Master Wyatt. Avoid Heidler\'s you mean?"

    w "I meant what I said, and I mean people."

    w "[[Her frown seemed to deepen at that.]"

    k "Of course Master Wyatt, I'm sorry. Are you shy?"

    w "[[Without thinking I answered immediately]"

    w "Intimidated."

    w "[[She seemed surprised and I regretted not taking another bite to avoid answering.]"

    k "Really?"

    w "[[I cleared my throat.]"

    k "Forgive me Master Wyatt, with confidence like yours I thought you would have many friends."

    w "[[Confidence, is that what she calls it?]"

#NOTE:>>Out of time. Continue to write bringing up these:
#	-Possible explanation of intimidation
#	-Kaori reassuring Wyatt
#	-Wyatt softening up
#	-Going to next class

    w "If what you call confidence persists then maybe in due time, but it is my first day here and I haven\'t exactly had any real oppurtunities to make any."

    k "They let you start mid-semester?  You must be very important master Wyatt."

    w "[[More misunderstandings.]"

    w "[[She seemed to forget that I had said intimidated at the very least.]"

    w "Yeah, sure.  I'll make some friends."

    k "With all due respect Master Wyatt- here is not the place to do such a thing."

    w "[[Wait a minute.  Was she trying to make me leave?  She's more clever than I thought.  At least if what I'm thinking is true.]"

    w "[[Of course she would want me to leave though, she's being punished and forced to clean a room that I'm preventing her from doing.]"

    w "[[\'Well\' I thought, \'I\'m punishing her for being a nuisance.\']"

    w "Well said Kaori, but I will be eating my lunch in here today.  Any meagre business you have can wait."

    w "[[She seemed to frown slightly and she nodded silently.  I was unsure if it's because my assumption had been correct.]"

    w "[[So I did as I said I would and took my time to finish eating.]"

    w "... ... ..."

    w "[[...And let me say- it was a very good meal.]"

    w "[[I stood up and Kaori looked up from the noise I created.  It seemed she was waiting for me to tell her to go about her business.  So I gave her what she was expecting.]"

    w "Alright Kaori, you can start cleaning then."

    w "[[She got up and I looked down to see my dirtied plates on the tray that had carried my meal.]"

    w "Also, would you clean up for me? I have to go to class."

    w "Of course Master Wyatt!  Thank you!"

    w "[[Thank you she said, for punishing her and making her life harder.]"

    w "[[It made think of moments in the past when I was being pushed around by my higher ups, it didn't matter how, whether emotionally or physically.  The things they would say.  The things they would do.]"

    w "[[And all I had to say for it was, \'thank you.\']"

    w "[[I smiled those times too before cursing under my breath, but I knew very well and I\'m sure Kaori did too, it could always be much worse.]"

    w "[[I walked out of that classroom with my head down, thinking about bad times of the past.  I just wanted to get to class, and get my time at Praesentia over with.]"
    
    jump laterClasses


label ph:
        
    w "[[To be honest, I felt very bad after she shot to the ground bowing and kneeling before me.  It was like she was just waiting to receive a final judgement from me who she readily and respectfully acknowledged as a superior.]"

    w "What\'s your name?"
    
    hide ch_kaori_laughblush
    
    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    k "I am Kaori, your holiness."

    w "Very well Kaori, you can call me Wyatt. And you can get up, I\'m not going to punish you."

    w "[[She raised herself slowly and I think I heard a sigh of relief as she was doing so.  I was glad that she no longer felt nervous at least.]"

    k "Thank you for you kindness master Wyatt.  I didn\'t mean to disturb your meal."

    w "[[I guess she answered her own question from earlier.]"

    w "I know Kaori, you made that known.  Please, have a seat."

    w "[[She seemed to hesitate at first and I wasn\'t really sure why, but she did end up sitting a seat away from me in the classroom. Perhaps she was worried about sitting too close to me, but it made the atmosphere a little awkward.]"

    w "[[I decided to try breaking the ice again.]"

    w "A fusebox?"

    w "[[Her childish antics erupted to life again.]"

    k "Please don\'t make me tell, Master Wyatt!"

    w "[[I couldn't help but smile.]"

    w "Alright alright.  Do you mind if I eat?"

    k "No, not at all.  I do ask that I be allowed to clean too though Master Wyatt, I\'m on a schedule. Of course I mean no disrespect by asking this of you."

    w "[[That might explain her hesitation.]"

    w "Sorry I didn't know.  Go ahead."

    w "[[So I ate, and she cleaned.]"

    w "[[I ended up finishing my meal in quite a hurry because I was still feeling a little awkward myself.  I should've just kept up the power act.  It was foolish of me to think that since she didn't seem to mind, she just kept cleaning merrily.]"

    w "[[It was if she had forgotten I was there.]"

    w "[[As I got up from my seat and began to clean up after myself I was stopped by her voice.]"

    k "I\'ll take care of those for you Master Wyatt."

    w "[[I looked towards Kaori who was carrying a mop around and cleaning the tiled floors of the classroom.  I was about to object saying it was alright, but I remembered that I had to get to my next class eventually.]"

    w "[[I had a lot of time before my next class though, so it could have been that I was just too lazy.]"

    w "Alright, sorry for the extra work."

    k "It\'s no problem at all, Master Wyatt.  I do hope your friends are present tomorrow so you won\'t eat alone again."

    w "Oh, it\'s not that Kaori.  This is my first day, I haven't exactly had the opportunity to make a friend yet."

    k "Your first day?"

    w "[[She suddenly got a very nervous look again.]"

    k "I\'m sorry again for disturbing your meal, Master Wyatt.  I had no idea you were important enough to be admitted mid-semester."

    w "It\'s fine, and I\'m hardly important.  Just lucky I guess."

    w "[[I would call myself anything but lucky, and more importantly I was nothing near important.]"

    w "[[Saying that seemed to calm her down though.  She appeared to be very much a nervous wreck.]"

    k "Sorry Master Wyatt, I didn't mean to assume."

    w "[[More importantly it sounded like she didn\'t know whether to be formal or informal.  That could just be her strange personality though.]"

    k "You\'re of the Hackett divinity right?"

    w "Yes."

    k "I know it might be hard attending Praesentia with Heidler\'s always being around, but a friend may help make it easier."

    w "[[Funny, she seemed genuinely concerned. Then again, plebeians worshipped the three families, why would they ever wish us harm.]"

    w "[[As an added bonus: when the Heidler's and the Hackett\'s were at peace, there were no plebeians dying. I suddenly felt very bad for them.]"

    w "I\'m leaving now."

    k "I hope to meet you again, Master Wyatt."

    w "[[I was thinking of the last war that was fought between the two feuding families, and the loss of my dad.  I wonder how many plebeians have experienced the same from the bloodshed of our families\' wars?]"

    #NOTE: I'm writing this after completing this last section and all I have to say is, I'm sorry.  I'm not sure why I can't conjure up any good ideas to continue this assertive arc, but heavy editing/revising may make me happy. 
    
    jump laterClasses
    

# endBlc

# codeBlc Passive Answer
label p3:

    play music "music/KaoriTheme.wav"
    
    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    w "[[I already walked my meal all the way out here, and I definitely didn't want to get up now and walk it somewhere else on the account of a simple question from this girl.]"

    w "[[I can state my business and keep along with it.]"

    w "I\'m eating my lunch. I wanted to eat somewhere quiet."

    qm "Sorry...I didn\'t mean to ruin your quiet place. I certainly hope I\'m not intruding..."

    w "[[She seemed genuinely concerned about intruding so I helped ease the tension.]"

    w "No, you\'re not."

    k "Kaori at your service. "

    w "[[I wanted to confirm my suspicions too.]"

    w "Are going to clean this place all by yourself?"

    w "[[In between each response I made sure to take quick bites of my food, talking to someone was not making me any less hungry and she didn't seem to mind either.  She feigned a laugh and responded to my question.]"

    k "I guess you can say I'm being punished for some mistakes that I've made recently, but I wasn't expecting your Holiness to here. "

    w "[[Now I wanted to laugh]"

    k "Would your Holiness mind if I cleaned while you eat?  I'm racing against a deadline.  I'll clean as quietly as I can, or if I'm too much trouble for your Holiness I'll leave. "

    w "It\'s no problem; as long as I get to eat.  "

    w "[[With that she smiled and began to clean starting at the front of the room.  Since she was going to be here I decided to take advantage of the company and ask her some stuff.]"

    w "Must have been pretty bad whatever you did to make you clean this whole room by yourself. "

    w "[[Even though she had just started cleaning, she paused her duties to look at me with an embarassed expression.]"

#Didn't mention it, but some carefree music may play well with this arc.  Let's make the player feel safe/happy. 

    k "That\'s hardly the case at all your Holiness, it was the number of people it affected that was the problem. As it turned out the problem I caused was easily fixed. "

    k "My boss did this so I can learn my lesson and not repeat my mistake.  He's such a good man."

    w "[[Her gestures were somewhat reminiscent of a child and it felt like I was speaking to one as well.  At least she was doing her best to make the most from her circumstance.  I certainly wouldn't compliment the people punishing me.]"

    w "[[I mean...If they're not around why pretend to respect them? Haha!]"

    w "The number of people it affected? "

    k "...Yeah...does your Holiness remember the blackout last week...?"

    w "I wouldn\'t know anything about it.  Today is my first day. "

    w "[[She stopped abruptly and looked at me surprised.]"

    k "You were accepted into Praesentia mid-semester?"

    w "[[I nodded]"

    k "I had no idea you were in such a high station your holiness. "

    w "[[Praesentia, and mid-semester of all things.  I was not in any station or skilled in magic, my first day so far was more than enough to express that.]"

    w "That\'s not it at all Kaori.  In fact it's quite the opposite."

    w "[[My voice was filled with disdain now, while prevously I was speaking in a somewhat cheerful mood and I was suddenly no longer hungry.]"

    w "[[My change of mood was no obstacle for Kaori though, and was quick to speak again.]"

    k "Your holiness is still a carrier of divine blood, and should not be so hard on yourself."

    w "Maybe..."

    w "[[She smiled. Probably happy that she was able to cheer me up just a little.]"

    w "and Kaori...." 

    k "Yes?"

    w "My name is Wyatt."

    w "[[She smiled brightly and complied.]"

    k "Very well master Wyatt."

    k "Have you made any friends on your first day, master Wyatt?"

    w "[[I thought a little bit about her question, in all honesty I've been a little afraid to, but at the same time no oppurtunities have really arisen.]"

    w "[[My last class was completely empty if not for Dr. Shimazu, and I didn't exactly think Jodie from the train really counted, yet.]"

    w "Actually...I sort of felt like I was in the progress of making one. "

#I don't know if a blushing Kaori would do good at all here.  Let me know what yout think?

    k "I-I'm flattered master Wyatt, but I'm not worthy of any friendship from you.  It would serve you best to make friends with your classmates?"

    w "I don't know Kaori, you seem pretty friendly to me, but there is some truth to what you're saying.  Finding friends with affiliation to  the Hacketts would serve me very well."

    w "I don't think they would accept me being at my level, and as a result I have been pretty isolated from the rest of the Hacketts."

    k "But it's you're first day master Wyatt.  No one knows you, and you wouldn't know if anyone will accept you if you don't try.  "

    w "[[Her usual gestures and antics were childish for the most part, but she had this underlying wisdom when she spoke.  At least I hope it was wisdom.]"

    w "[[If nothing else, her intentions were well-meaning.]"

    w "I'll see what I can do for the remainder of the day and tomorrow, but it's qualities like that prove your worthy of being anyone's friend.  "

    #Maybe some more of that blushing cliche bullcrap that most animes seem to pull. "I like you Sakura-chan"  "And I like pizza, what's your point? Oh, do you mean love me? okay that's kool"

    k "Thank you again Master Wyatt."

    w "I should be thanking you actually.  Before you came around my day had been pretty crappy. "

    w "Regretably though I need to go.  My next class will begin soon. "

    w "[[I began to take my tray and leave.]"

    k "Don't worry about the tray, I'll take that for you."

    w "You sure?"

    k "Of course, I'll be happy to Master Wyatt. "

    w "[[I nodded my head as a sign of thanks and worked my way to one of the exits.]"

    w "[[And with that I made my way to the nearest Railcar stop, and towards my next class.  Somewhere along my way to class I realized that Kaori didn't really get much cleaning done thanks to our conversation.]"

    w "[[I hope she doesn't get into more trouble.]"
    
    jump laterClasses
                  
# endBlc

# codeBlc Hesitant Answer
label h3:

    play music "music/KaoriTheme.wav"
    
    show ch_kaori_neutral at Position(xpos=200, ypos=-20, xanchor=0, yanchor=0)

    w "Um...Hello, who're you?"

    #Quick surprised look

    k "Forgive me your holiness, Kaori at your service."

    #Back to neutral

    k "I was inquiring about your presence, but I can see you're eating a meal."

    w "Don't be so formal, it makes me nervous...And call me Wyatt."

    k "O-of course Master Wyatt...sorry."

    k "Um...I've been sent here to clean the room, but I wasn't expecting a student to be eating here.  Would you like me to wait until you're done eating."

    w "[[I looked at my plate and found it was about half finished, but I wasn't really up for eating in front of someone who was just gonna sit there and watch me.]"

    w "[[Although she could\'ve meant that she was going to wait outside and I was just jumping to quick conculsions.]"

    w "No, it's alright I was just about full anyways."

    w "[[In truth I had lost my appetite with the start she had initially given me.  So I just stood up leaving the tray that held fine ceramic plates on the desk and faced this Kaori girl.]"

    w "[[She wasn't bad...I quickly shook that though from my head though.]"

    w "[[It seemed the attraction towards plebians will always be stuck in my blood. My only hope was to fight it.  I gave a quick inspection of the room, noting its size.]"

    w "You\'re going to clean this whole classroom by yourself?"

    k "Hehe...I guess you can say I\'m sort of being punished for a clumsy mistake I made a little while back."

    w "[[She had a somewhat childish and carefree aura about her, and didn't seem too phased by the fact that this was supposed to be a punishment.  At least she wasn't talking to me like some sort of royalty anymore.  I was far below that.]"

    w "[[Failing to hold any title because of my forefathers and because of my family serving as vassals under the Cartwright family I could recall dozens of times I had a similar punishment to hers.]"

    w "[[She was already taking cleaning utensils out from a cart she had brought into the class, it made me wonder how she came in this class without me realizing. I must've been pretty hungry.]"

    w "Do you need help?"

    w "[[I don't know what I was saying, force of habit it seemed.]"

    #...I don't know...a surprised Kaori?  

    k "...no, master Wyatt.  I couldn\'t possible ask for your help."
 
    w "You\'re not, I'm offering it."

    w "[[There was a brief silence.  I wasn't sure if she was shocked or considering my offer.]"

    k "It wouldn't be much of a lesson if I had help with my punishment though, right?"

    w "[[Seems she was insistent on doing it on her own. Regardless of what I was saying, I didn't really want to help either.  I guess I was just feeling sorry for her.]"

    w "[[I knew well enough that this was a pretty mild punishment though, she probably upset another plebeian rather than upset someone with divine attributes. I've seen plebeians get hit really bad from doing something as miniscule as forgetting to turn an A/C on.]"

    w "Yeah...I guess you\'re right."

    k "Wouldn\'t you rather be with your friends during your freetime master Wyatt?"

    w "Possibly, but I haven\'t had the oppurtunity to make any yet.  It is my first day."

    k "...but isn't there a policy preventing mid-semester applicants or transfers?"

    w "There is."

    k "Then...?"

    w "..."

    k "You must be very powerful!?"

    w "[[She said this with utter confidence and the look on her face made it seem like she was convinced there was no way she could be wrong.]"

    w "...I guess so."

    w "[[I didn't want to kill her vibe, so I just smiled and let it be known that there was a possibility she was right but without confirming it.]"

    k "You should make friends very soon then."

    k "And forgive me again for interrupting your meal."

    w "You\'re forgiven."

    w "You sure you don\'t need help?"

    k "No sir, I'll manage."

    w "Alright."

    w "[[I turned around and picked up the tray that held my incomplete meal.]"

    k "I can take that for you master Wyatt. "

    w "No, at least let me help you with this. "

    k "Very well, have a good day master Wyatt. "

    w "You\'re being too formal again. "

    w "[[With that I exited the room and ridded myself of the food tray.  I still had classes for the remainder of the day, and I didn't want to be late to any of them.]"

    w "[[Plus I was guaranteed that these next classes wouldn't be as void as my first one.]"
    
    jump laterClasses

# endBlc
    #Some more random thoughts.  A new day can begin in numerous ways, 
    #I think that it's important to not let it begin the same way everytime as it may bring about a more pridictable story than the one 
    #I'm already composing. I think if I just let it flow straight to the more important parts of the daily activities of our 
    #MC it would be alright, but what do I know?  I'm no professional writer or nothing.  
    #Maybe it would've helped to take some creative writing courses or something.  
    #All the nonsense I write just falls out of my brain as a gooey substance that I try to make solid.  
    #Hopefully by the end of this I'll make something seemingly credible for avid visual novel readers.  
    #Here I am ranting and stuffs, time to get to the story.

    w "[[I had gotten up a little ealier than planned this morning, but that was to be expected after yesterday somehow proved so tiring to me. I only wondered about how long it would take to become accustomed to this new and unexpected lifestyle.]"

label laterClasses:

    stop music
    
    #The Last scene should have some sort of representation showing that time has passed or is passing up until this point. No locational awareness is set yet but the MC would either be walking to the campus' Main Station or already be there. The Sky should have an orange hue to signify late afternoon or something. Whatever everyone can agree on. 

    w "[[The last three classes went on without a hitch, one of them was a military training class as well as a couple science courses.]"

    w "[[Praesentia academy  has a block schedule so the only class I'll have tomorrow that was the same as today is the one with Dr. Shimazu, and spending everyday with him wasn't exactly a comforting thought.]"

    w "[[I also managed to talk to a few people from these other classes, as it turns out they are rather large as opposed to my core class. None of the people I talked to though seemed like they would be a potential friend.]"

    w "[[It seems this natural barrier I put around myself and my past doesn't exactly attract people, but I knew that would be the case.]"

    w "[[Another oddity I found is that the classes are generally segregated based on what family people are affiliated with. The Hacketts were in classes with Hacketts, and Heidlers with Heidlers.]"

    w "[[Hitos were found everywhere though, this was their continent afterall. Plus they weren't involved in any feuding.]"

    w "... ... ..."

    w "[[Anyways, I'm tired. Although this was any other day on the calender, it was still a long day for me.]"

    w "[[I just want to get to the Main Station as soon as I can.]"

    #Now a note here: I'm intergretating some of the stuff that AJ came up with regarding the encounter with Chistopher Hackett and Evelyn Logan, since he did basically create the personality for both characters. Shy Evelyn will be introduced first and stay shy until her purpose is revealed by Act II. That's the plan anyways. This will also be taking place for the fact that I don't want Chris and Evelyn to be complete strangers by the time they become more important characters to the MC later in the story. 

    w "[[I may have been walking a little too quick though...as I approached a corner leading to the Main Station my shoulder crashed into someone.]"

    w "[[It was not long afterwards when I was shoved hard against a wall by someone accompanying the person I bumped with his fist tightly grasping my collar. The impact hurt my back.]"

    ha "Watch yourself! That was His Holiness and Heir to the Divine Throne you just shoved! "

    w "[[What? These people are Hacketts that's for sure, but that would mean that the person I ran into was Christopher Hackett!]"

    w "[[I looked at the student who was pratically crushing me against the wall with a single fist and then behind him.]"

    w "[[Sure enough it was Christopher Hackett as I recognized him from pictures on the Net and certain stations on television. Behind him was the shadow of a girl who looked somewhat displeased with me, probably for the same reason as this guy holding me fast.]"

    w "[[A smile formed on the face of Christopher, and he approached me and this other guy while placing a hand on the man's shoulder.]"

    ch "Calm down, it was accident. This isn't how we treat our friends.  "

    w "[[The student glanced at the girl that stood quietly behind Chris and she gave a slight nod of approval, it was then when he released me. I groaned softly from the release of pressure on my body.]"

    ch "What's your name? I don't think I've seen you around before. "

    w "[[He definietly had the accent of divinity that dwelled on an island to the East of the Western Continent, the sovreign land of the Hacketts. I could only hope He really wasn't offended at all.]"

    w "[[It would be a bad way to start my time at Praesentia.]"

    w "[[Normally a man in my position would kneel before him as I spoke, but I feigned royalty at the hopes of not making a scene and placed a fist over my heart with my head bowed as I spoke.]"

    w "Wyatt Armstrong your Holiness.  "

    ch "Haha. Well don't feel too bad Mr. Armstrong, people are always trying to run into me.  Though you were more brash than many others. "

    w "[[I dropped my salute due to his conversational nature.]"

    w "I apologize, I was in a hurry to get some sleep. It's been a long day. "

    w "[[I'll stick with being as formal as I can. Unlike Kaori, I am speaking to true divinity, if not for me playing royalty like most others are in this school, I would be in deep shit...I think.]"

    ch "Must be, I remember my first day of classes. The size of Praesentia alone can be overwhelming. Luckily I had some friends coming in though. "

    w "...Yes, it's my first day. How did you guess that one?"

    ch "Just instinct I presume. Though you're not making hard to see. "

    w "Most people find my random acception strange though."

    ch "It is, but the more Hacketts being accepted here the better."

    ha "...Um Chris..."

    ch "Time already Evelyn?  "

    w "[[She nodded]"

    ch "Very well. Sorry to keep you from your sleep Mr Armstrong. "

    w "I'm sorry to keep you from your class. "

    w "[[I watched as the two males departed, finding it hard to remember the girl's presence. She had only said one word during our encounter. Who was she?]"

    w "[[Silently she followed the two giants like shadow; their footsteps like falling stone, hers, like falling snow.]"

    w "[[I suppose it wasn't important who she was. Afterall Chris is the only heir to the Divine throne of the Hacketts. I guess that doesn't stop him from getting a class or two this late in the day though.]"

    w "[[I went to my dorm room immediately afterwards. With my luck I'll run into an important Heidler figure next, and that has no good outcome.]"
    
    #Transition to next scene 
    
    #Nighttime looking, SFX: crickets

    narrate "... ... ..."

    ch "He must've been the one Jodie was talking about Evelyn. Strange for a student to be admitted during the semester."

    ch "It was telekenisis right? "

    e "..."

    ch "He'll be fine here.  "

    e "...Chris?"

    ch "Yes Evelyn?"

    e "Was it alright for him to treat you as he did?"

    ch "Why not? As far as everyone is concerned besides us he is royalty. I suspect if he's successful here he may one day rise in social standing. "

    e "...and if he's not successful?"

    ch "It'll be fine Evelyn. "

    ch "Hm...What do you think about about Jodie, Evelyn? "

    #It 's been sometime since writing this little skit, but it should prove fine. I was originally writing it with Evelyn proving to more angry than anything else. I realize now though that it would possibly be better to show her as shy during this conversation by adding a blush everytime Chris talks to her. 

    e "... "
    
    #Transition to next scene
    
    #This section will be pretty heavily experimental. Remember: MC is asleep so is 80-95% of students and faculty, but campus never closes.  The POV is switching to third person and for the sake of avoiding further???, I'll just include full names and shit. 

    #Also I'm writing this intoxicated. We'll see if my drunk self is a better writer than my sober self. 

    play music "music/NarrateTheme.wav"

    narrate "[[Loyalty, duty, respect, honor; these are the words that saturated the air, so many have lost so much, so much has been sacrificed, so much has been forgotten. In a world where ranks and title meant everything, rivals cannot be equals.]"

    narrate "[[A time was approaching, a time was agreed upon, who could come was also agreed upon.]"

    narrate "[[A man stood still waiting for the arrival of his mistress, the arrival of all that he has ever put faith in; a princess of the Holy throne. By her order he would stand there a lifetime and call it an acheivement.]"

    narrate "[[And so he stood, quiet and vigilant.]"

    #a noise

    narrate "[[There she was. He would pretend not to notice, it always made her feel good when he pretended she was better than him at sneaking; that she was better at anything.]"

    narrate "[[She approached silently behind him until she was close, very close.]"

    narrate "[[She whispered to gain his attention.]"

    a "...Luke."

    narrate "[[He whispered too. He didn't turn to face her.]"

    l "Yes my queen?"

    narrate "[[She got closer and wrapped her arms around his chest and pressed her breasts on his back.  While doing so she feigned sorrow.]"

    a "...queen?"

    l "...Yes my goddess? "

    narrate "[[He could almost feel her smile form against his neck and she gave him a light kiss.]"

    a "And don't you forget it {i}Sir{/i} Luke. It is my blessing that allows you to breathe, and my love that allows you to live. "

    l "..."

    a "They're coming my knight. Would you be so kind as to tell my fiance? "

    l "It would be my pleasure, your holiness. "

    a "Pleasure is all seek to give you Luke. Let's go then. "

    narrate "[[Lukas extended his elbow offering to escort Anya to Mathematics West, a peculiar structure that was more often than not generally ignored by all the students of the academy. No one likes math, right?]"

    narrate "[[Save for one individual that was quite fond of it, whom just so happened to be the heir to the Heidler Holy throne, Niklas Heidler.]"

    narrate "[[Together the couple walked into the building and to the elevator which brought them about two-thirds the way to the top. Room 615 was the commonplace for Niklas, usually caught looking out the extravagant window pointing west.]"

    narrate "[[The sunset was usually his reason for doing so, but everytime he said that the sun was nowhere near setting, just like today. The sun set some hours ago.]"

    narrate "[[The couple knocked on the door and without waiting for an answer they walked in. As expected, there sat Niklas, his hands crossed beneath his chin and staring out the window at a starlit sky.]"

    narrate "[[Lukas being a gentleman showed Anya to a seat and approached Niklas, his best friend, who was no doubt in very deep thought. It was under his recommendation that such precautions were taken to begin with.]"

    narrate "[[Lukas whispered in his ear to ensure he didn't startle his friend.]"
 
    l "The Hacketts have been sighted approaching the agreed venue. It seems they want to go through with the negotiations. "

    a "... ... ..."

    l "Your holiness? "

    n "...Alright. We will answer in kind."

    n "Was Christopher Hackett with them? "

    l "Of course."

    n "And the girl?"

    l "And the girl. "

    n "Alright everyone gather up! "

    narrate "[[The room which had many people at its perimeter came to life, eager to listen to the news.]"

    n "The Hacketts have responded to...our demands, and are currently heading torwards the rendevous. "

    n "Those who were trusted to come along meet us outside. The rest of you go to the lobby and stay on standby. That is all. "

    narrate "[[Like a hive under distress everyone in the room moved with a purpose with only three bodies remaining completely still the entire time.]"

    narrate "[[When the room was empty of all but the three Niklas spoke again.]"

    n "Your coming too, right Lukas?"

    l "Of course. "

    n "Thanks, I'll need you for this. "

    narrate "[[Niklas walked up to Anya's seat and offered his elbow as a means to escort.]"

    narrate "[[She refused.]"

    a "I can find my own way. "

    n "Of course. Lukas?"

    l "Yes? "

    n "Let's go. "

    narrate "[[The last three members left in the room walked out separately.]  "

    narrate "... ... ... "

    narrate "... ..."

    narrate "..."

    ch "They're a little late aren't they? "

    ha "No, we're just a little bit early your holiness. "

    ch "Hmmm..."

    ch "If you say so. What do you think Evelyn?"

    #Again, I think the blush stuff should only happen when Chris speaks to her while she stays pretty serious with everything else. 

    e "...I haven't thought about it. "

    narrate "[[A group of about ten Hacketts stood silently in the darkeness for a while, until Evelyn spoke again.]"

    e "They're here! "

    narrate "[[What seemed like silence began fading into the clattering of soft footsteps that increaded in volume until distinctive silhouettes formed in from the shadow before them.]"

    narrate "[[The meeting place was an old clearing that sat behind a building called the Koshiba building, it was dark and the railcar track that sat beside didn't run this late in the night.]"

    narrate "[[Eleven Heidlers arrived at the clearing and Evelyn leaned towards Chris to whisper in his ear.]"

    e "...They brought the knight. This wasn't part of the agreement, we should leave...now!"

    ch "shh... We came here to talk, I plan on doing as much before I leave. Okay?"

    #She submits

    e "..."

    narrate "[[She nodded, but only after putting some thought into Chris' orders.]"

    ch "Mr Heidler! How long has it been? A couple months?  "

    n "Just about. I see you brought your crew. "

    ch "Of course, just like you."

    ch "...Plus that knight as well. "

    n "Straight to business then. I want the East Courtyard. It's been in your hands for years, but as you can imagine space has been quite limited. "

    ha "The East Courtyard!?!?"

    ha "You're crazy!"

    ch "shh!"

    ch "The East Courtyard? I expected something just as ambitious if you were willing to meet with us tonight. "

    narrate "[[Chris paced a little bit seemingly in thought before he turned back to the Heidler party to continue the conversation.]"

    ch "...Why?"

    n "Like I said, space is limited. "

    ch "You own half the academy and about one-third of the population.  Why do you need the courtyard?"

    narrate "[[Niklas shot a quick glance to Anya, then his attention shot back to Chris.]"

    n "...Details, they can be such a pain can't they?"

    ch "Sometimes. "

    ha "You can't be serious your holiness! The East Courtyard is more than just a small piece of land!"

    ch "And what of me {i}Herr{/i} Heidler? You're making my space somewhat limited as well."

    narrate "[[Chris held his hands together behind his back keeping one hand close to his ASLA as he paced back and forth in front of his group of Hacketts.]"

    a "Your kin seems to be quite questioning of you Hackett, perhaps we should let {i}him{/i} do the negotiations. "

    narrate "[[Looking only at Anya Chris replied.]"

    ch "Your kin seems quite untame Niklas, perhaps we should let your bitch do the talking."

    #Anya should look...aggravated.

    narrate "[[Fear was no way to control a man, and the Hacketts who follow Chris have every right to speak their mind without a Heidlers opinion.]"

    narrate "[[Nonetheless it was a stupid move. Chris continued to pace in front of his fellow Hacketts as a means to slow the coming storm that brewed between both parties. There was no stopping the inevitable though; he shot a glance to Evelyn. A reassuring look at each other was enough.]"

    narrate "[[Chris descreetly fiddled with his ASLA and the message was sent, but in that short time not all the Heidlers were alright with the insult he had used to refute Anya.]"

    #Anya is mad

    a "W-what!?"

    l "Enough! Let's settle this!"

    #Anya grins

    narrate "[[A burst of energy is shot from the Heidler party towards the Hackett party, which causes some of the Hacketts to lose their balance.]"

    narrate "[[A brawl breaks out between the groups, as the leaders observe the fighting amongst the followers.]"

    #Some fighting noises maybe? 

    narrate "[[A loud gunshot echoes above the fighting and the participants of the brawl are brought to a halt.]"

    narrate "[[A third faction appears from the shadows entering the moons eerie glow revealing Jodie Lawson at the head of the discplinary committee. The loud shot was the discharge of a weapon carried by Jodie pointed towards the sky.] (with smoke leaving the barrels end.)"

    narrate "[[The groups stunned with shock retreated behind their respected leaders.] "

    j "Infighting between students is strictly prohibited on school grounds. You are all in violation of this edict."

    narrate "[[Chris approaches her, and the discplinary committee takes aim at him with their weapons to assure he didn't get too close.] "

    ch "Miss Lawson. I was wondering when you planned on showing up. "

    j "Christopher; I'm disappointed in your lack of control in the sitaution. You know as well as anyone else that the rules are to be strictly followed and adhered to."

    e "I'm disappointed in you Miss Lawson, Authority should not be mistaken for true power."

    ch "Evelyn."

    #Evelyn (Looks towards chris)

    ch "Jodie is right. "

    n "... And our Heidler representation?"

    t "Is here, your holiness."

    n "Ah, Thank you."

    t "I believe Jodie and I can agree a compromise needs to be met."

    j "I concur, this problem needs to be resolved. Tonight. "

    narrate "[[Silent side conversations filled the Hackett and Heidler parties, they looked towards their leaders for a response to the recent developments. A lively Hackett was the one who broke the small chatter.]"

    ch "Alright, have the east courtyard."

    narrate "[[A sense of victory washes over the faces of the Heidlers as the Hackett and his group of allies begin to walk away, until chris makes one final demand.]"

    ch "But we get the main library."

    n "That's not allowed!"

    ch "I know, It's a compromise and it's a fair one at that. The courtyard, for the library. "

    narrate "[[The last Hackett fades into the shadows of the night, leaving the student council and Jodie to go about their business with the Heidlers.]"

    j "A fair trade Torsten?"

    t "That's hardly the case and you know it!"

    narrate "[[Niklas stood silently motioning his arm for is group to leave, of course Anya and Lukas stayed put as Niklas approached the student coucil members.]"

    j "How so? Either both parties gained something or both parties gained nothing, this was a win-win. "

    narrate "[[Before Torsten could refute Niklas spoke.]"

    n "Enough Torsten. We got what we came for. "

    t "Your Holiness...?"

    n "We'll leave it be for now. "

    t "As you wish."

    narrate "[[Torsten shot Jodie an angry glance but pushed no further. With that the student council dispersed and the remaining Heidlers went about their business.]"

    narrate "... ... ..."

#Note: Groups discuss the turnout of the events that had just occured and what the future plans will be for our Heidlers and Hacketts. Also show more discussion between the groups and their leaders.

    #Transition to last scene 
    
    #Optional story to include.  Should be included in fact, but only after thorough revision, I'm not sure where I'm going with this due to the fact that it's just some extra ideas I wanted to include for the act. 

    #Still 3rd-person POV.  We'll start with Hacketts then...

    narrate "[[Chris sat idly at one of the many study tables housed by the main library and opened a can of pop.  He had dismissed the other members of his crew sometime ago, but as usual he still had a small shadow at his side.]"

    e "The Main Library was an even bolder move than the Eastern coutyard that the Heidlers demanded.  "

    ch "It wasn't a bold move at all for their part, it was an unnecessary one. I still wonder what they wished to obtain from it.  "

    ch "It's that Anya girl I bet.  She's a very beautiful woman, but it's too bad her arrogance ruins her looks. "

    e "..."

    ch "She has to be the catalyst to the whole thing.  Who else could it be? "

    e "That knight. "

    ch "...Possibly.  My dad would normally say to suspect the woman first. "

    e "It all started with the arrival of that knight though. "

    ch "True enough, but I don't believe he could ever be the one pulling the strings."

    j "Perhaps it's all deception, just like our tactics and methods? "

    narrate "[[Jodie approached the two sitting individuals, as usual her professionalism seemed to excrete from every pore as she took a seat across from them.]"

    ch "I'm not so sure you could call it deception Jodie.  It seemed to me like you were enjoying putting me in my place.  "

    j "Forgive me your Holiness, I could hardly help myself.  "

    ch "But you're also wrong Jodie, infighting between the Heidlers is hardly a new development.  This implicit fighting we're picking up with our guts must be happening, otherwise His Holiness Niklas would not have been struck dumb from my final demand. "

    ch "In fact, I feel he would've just refused to compromise and let go of the notion of obtaining the East Courtyard all together. The question is why didn't he? "

    j "The Main Library!  That's quite the acheivement your Holiness.  It's been neutral territory since the opening of the Academy. "

    ch "It would also seem that we Hacketts were the only ones that walked out with an actual deal.  We lost nothing. "

    e "Except the East courtyard. "

    ch "I may enjoy my lunch here more anyways. It's quiet, I like it. This place has implicitly been off limits, and we got it. "

    j "Is there anything else you need me for your Holiness? "

    ch "Send out a mass email to the Hackett population, let them know to avoid the East courtyard whenever possible.  "

    j "Anything else?"

    ch "How about some alone time?  Just me and you. "

    j "You flatter me your Holiness. "

    narrate "[[Jodie stood from her seat and began to leave, a clear sign of rejection for Christopher.]"

    narrate "[[Christopher was laughing to himself silently and turned to face Evelyn.]"

    ch "If my father could see me now Evelyn; he would hate me. "

    e "His holiness only wishes what's best for you. "

    ch "Yeah? hmm... I'm not so sure. "

    ch "I'm getting tired Evelyn.  Let's head back to the dorms for the night. "

    narrate "[[Chistopher got up and Evelyn silently followed him.]"

    narrate "... ... ... "

    narrate "... ..."

    narrate "..."

    #Here begins the Heidler aftermath.

    #Since the last scene was on the campus grounds I going to go ahead and try this one out on the commuter train that the students take to get from the school to the dorms. 

    narrate "[[Niklas was not very happy.  He sat as comfortably as he could on the commuter train trying to enjoy a cup of coffee sweetened generously with pure sugar.  ]"

    narrate "[[Technically he had lost nothing, he was telling himself that as often as he could, but he could not change the atmosphere that this cabin of the train held.  With him were his best friend Lukas and his cousin Anya.]"

    narrate "[[As he suspected, Anya was the first to break the silence.]"

    a "Some Heir you're going to be if the best you can do is stand dumbly after that Hackett's demand. "

    a "Your lack of action lost us the Main Library."

    n "Technically it was never ours.  "

    narrate "[[He took a sip of his coffee as he repeated his thoughts into words.]"

    a "It wasn't theirs either.  "

    n "You got your courtyard, can't you be happy with that? "

    a "I can't be happy losing something vital! "

    a "..."

    narrate "[[Niklas thought momentarily for a solution to Anya's unhappiness.]"

    n "The Science department has its own library, I'm sure we can arrange to use most of the building for Heidler use.  Especially since the head is Heidler himself.  I'll get to it first thing tomorrow."

    a "We shouldn't have to amend our wants to the demands of a Hackett, Niklas!!  We should have never lost the library.  "

    n "You got what you wanted Anya, I'll do what I can to compensate for any losses you felt we've taken.  "

    a "...!"

    n "It's a beautiful scenery that courtyard, we'll use it well. "

    a "I can't believe you."

    narrate "[[With that Anya walked out of the cabin to seek solitude from Niklas, surprisingly she did not ask Lukas to join her.]"

    narrate "[[Lukas was silent for the whole confrontation, his word held no weight anyways between the two he was with.]"

    n "...We were so close as children Lukas. Now it seems I can't talk to her witout making her angry."

    l "Knowledge seems to have changed her relationship with you.  "

    n "Knowledge I wished neither of us ever obtained.  At least for some good amount of years.  "

    n "I knew it was a long shot anyways, and I'm not entirely displeased with our loss of the library. "

    l "Anya seems to think you should be.  "

    n "..."

    l "Sorry. "

    n "Don't be.  "

    narrate "[[A silence fell over the cabin. Niklas liked it this way; he preferred it this way. He looked mesmerizingly out the window and sipped on his coffee from time to time. Then he turned to Lukas to speak again.]"

    n "Go to her Lukas.  See if you can plant a seed of my rationality within her. "

    l "As you wish. "

    narrate "[[Lukas left the cabin and a quick thought ran pass Niklas' mind saying that Lukas was a good friend, and an even better knight.]"

    narrate "[[Then his thoughts swayed back to his emotionless calculating attitude.]"

    stop music
    
    jump firstClassDayTwo
    
    

# endBlc