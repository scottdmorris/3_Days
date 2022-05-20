# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Steve", color="#000000")
define n = Character("Nicky", color="#000000")
define l = Character("LANDLORD", color="#000000")
define j = Character("Judge", color="#000000")
define stream = Character("Stream")

# Character images
image s = "steve.png"
image n = "nicky.png"
image l = "landlord.png"

# sound
# define audio.start = "audio/beginning.mp3"
default hascourt= False
default lose = False
default camera = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image livingroom = "Livingroom_Day.png"
    image bedroom = "Bedroom_Night.png"
    image bedroomdark = "Bedroom_Night_Dark.png"
    image bedroomday = "Bedroom_Day.png"
    image outsidecourt ="School_Hallway_Day.png"
    image court = "court.jpeg"
    image library = "library.jpeg"
    image park = "park.png"



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    play sound "audio/beginning.mp3" fadeout 1.0 fadein 1.0 volume 0.5

    scene livingroom
    with fade

    show s at left

    # These display lines of dialogue.

    s "Hey Nicky! You home?"

    show n at right

    n "Hey what's up Steve. Where'd you go today?"

    s "I went to GameStart to look at the deals. Picked up something special for the stream tonight."

    n "Oooo exciting!"

    # add portal noise
    play sound "audio/portal.mp3"

    n "Oh no... not again."

    s "Wait is this who I think it is?"

    show l

    l "WAKE UP! IT'S THE FIRST OF THE MONTH!"

    l "SEND YOUR OWED MONEY TO MY CRYPTO WALLET THIS INSTANT!"

    s "Didn't we agree that you can't randomly portal into our apartment?"

    l "THAT WAS LAST MONTH WHEN YOUR RENT WAS PAID. THIS IS A NEW MONTH!"


    menu:
        "Pay rent":

            n " Fine... You should have received it now."

            l "RECIEVED. YOU MAY STAY. GOODBYE TENANTS."

            play sound "audio/portal.mp3"

            hide l

        "Argue":

            s "No I'm not going to send your money right now and especially not when you invade our space.
            You'll get it when you get it."

            l "HOW DARE YOU TALK TO YOUR SUPERIOR LIKE THIS. YOU SHOULD BE THANKFUL FOR THE AIR YOU BREATHE FISH."

            l "I HAVE ALREADY FILED A COMPLAINT WITH THE AUTHORITY TENANTS COURT. BE AT THE COURTHOUSE FOR 9:30 AM TOMORROW."

            $ hascourt = True

            play sound "audio/portal.mp3"

            hide l

            n "Aww man we're screwed! Everyone knows The Authority court doesn't care about tenants! This is too much stress for me"

            s "Don't worry Nicky, I'll go and represent us."



    play sound "audio/beginning.mp3" fadeout 1.0 fadein 1.0 volume 0.5

    n "What's our landlord's problem?"

    s "I don’t know. I know they used to be an army general for The Authority but the robot
    treats us like they own us or something. Probably hard processed in their chip."

    n "So, what are your plans for the rest of tonight?"

    s "Gonna shower and prepare to stream. What about you?"

    n "I'll be in my room reading the new edition of Shell Weekly."

    s "Sounds classy. See ya tomorrow!"

    # night time

    scene bedroom
    with fade

    show s

    s " It’s almost 9! Time to go live on Spark."

    s "Hey Stream! How are y’all doing today"

    stream "hey steve!"

    stream "ur late!"

    stream "what are we playing tonight?"

    s "For today’s stream we’re going to be doing something very special."

    stream "REVEAL IT!"

    s "I have bought two different games! But chat will decide which we play tonight."

    s "The first game is. . ."

    s "BELDEN RING!"

    stream "LET’S GOOOOOO!"

    stream "PICK THIS ONE!"

    s "And the second choice is. . ."

    s "VIRTUAL VIRTUAL VIRTUAL REALITY"

    stream "NOO WAY"

    stream "I HEARD THIS GAME IS SO VIRTUAL"

    s "The poll has started! What will it be chat?"

    menu:

        "Play BELDEN RING":

            s "The results are in and it looks like BELDEN RING has won overwhelmingly!"

            stream "BE A SAMURAI"

            stream "NO BE A MAGE"

            s "Why don't we be a magic samurai?"

            stream "YESSSS!"


        "Play VIRTUAL VIRTUAL VIRTUAL REALITY":

            s "Looks like VIRTUAL VIRTUAL VIRTUAL REALITY wins by a landslide!"

            stream "PUT ON THE GOGGLES"

            stream "IMMERSE US!"

            s "Okay guys give me one second to put on the headset."

            s "How do I look chat? Hopefully I don't swim into my fishbowl!"



    scene bedroomdark
    with fade

    show s

    s "Wow it's almost 2:00 am already! I completely lost track of time."

    stream "Noooo please don't go!"

    stream "Looks like I'll have to actually focus on work now."

    s "Sorry chat I have a lot to do today but I promise a longer stream soon!"

    stream "YAY!"

    s "Goodnight chat! Love y'all!"

    s "That was such a fun stream tonight. Time to get to bed and get ready for tomorrow."

    # Day 2

    scene bedroomday
    with fade

    play sound "audio/alarm.mp3"

    show s

    s "It's 7:30. Time to get ready for the day."

    if hascourt:

        s "Oh yeah, I have to go to tenants court."

        jump court

    else:

        s "Hmmm... I have a few options for what to do today."

        menu:

            "Go to work":

                s "Looks like there's a free shift at the bookstore I can pick up."

                jump work

            "Go to the park":

                "I think I'll go to the park and enjoy the nature."

                jump park

    label work:

        scene library
        with fade

        show s

        s "Time to shelve some books."

        show n at right

        n "STEVE!"

        s "Nicky? What are you doing here. I thought you were at home."

        n "I was. Until our landlord randomly portaled in!"

        s "Again! But we even paid our rent!"

        n "I know, he always does this. How do we get him to stop?"

        s "We could possibly set up a hidden camera."

        n "Oooh I like that! Then we could beat him at his own game in court!"

        s "Ooooor we could have a little surprise ready for him when he portals into our apartment.
        Something his body would be quite attracted to if you know what I mean."

        n "Hahaha a magnet? Evil but I like it. What should we do?"

        menu:

            "Get a hidden camera":

                s "We'll get the hidden camera and beat him at his own game!"

                n "Let's do it!"

                $ camera = True

                jump home2

            "Buy a strong magnet":

                s "Let's buy a strong magnet and give this robot a piece of his own medicine!
                He won't know what hit him! Or would it be what he hit?"

                n "I think both apply here."

                s "Let's go prepare!"

                jump home2


    label park:

        scene park
        with fade

        show s

        s "Ahhh it's so nice here. So relaxing."

        show n at right

        n "STEVE!"

        s "Nicky? What are you doing here. I thought you were at home."

        n "I was. Until our landlord randomly portaled in!"

        s "Again! But we even paid our rent!"

        n "I know, he always does this. How do we get him to stop?"

        s "We could possibly set up a hidden camera."

        n "Oooh I like that! Then we could beat him at his own game in court!"

        s "Ooooor we could have a little surprise ready for him when he portals into our apartment.
        Something his body would be quite attracted to if you know what I mean."

        n "Hahaha a magnet? Evil but I like it. What should we do?"

        menu:

            "Get a hidden camera":

                s "We'll get the hidden camera and beat him at his own game!"

                n "Let's do it!"

                $ camera = True

                jump home2

            "Buy a strong magnet":

                s "Let's buy a strong magnet and give this robot a piece of his own medicine!
                He won't know what hit him! Or would it be what he hit?"

                n "I think both apply here."

                s "Let's go prepare!"

                jump home2


    label court:

        scene outsidecourt

        show s

        s "Well, about time to go inside."

        show n at right

        n "STEVE! Wait!"

        s "Nicky? What are you doing here? I thought you were too nervous to come."

        n "Oh, I'm not going inside. I just wanted to give you some last minute support."

        s "Thanks Nicky. I'll try my best."

        n "Don't let the system screw you! Show that robot who's boss!"

        scene court
        with fade

        show s at left
        show l at right

        play sound "audio/court.mp3"

        j "Court is now in session!"

        j "I believe our next case is Roger Robot vs Steve Fish & Nicky Turtle"

        j "Is the plantiff present?"

        l "YES, YOUR HONOR."

        j "Is the defendant present?"

        s "Yes, your honor."

        j "We may begin. Now according to my information we are here because the defendant refuses to pay rent. Is this correct, Steve?"

        s "Yes, but that's not the whole story your honor.
        My landlord feels free to randomly portal into our apartment to hassle us despite us telling them to stop. I refuse to pay until he agrees to respect our rights and space."

        j "I see. What do you have to say about this Roger?"

        l "YOUR HONOR, I PORTALLED BECAUSE THIS FISH AND HIS SLOW FRIEND HAVE NOT PAID RENT. UNDER AUTHORITY LAW, LANDLORDS ARE ALLOWED TO FREELY ENTER SPACES WHEN RENT IS NOT PAID."

        j "Yes, this is true. As I see, Roger is correct in his rights to enter your space freely as long as your rent is not paid."

        s "But wait, your honor! He's been doing this even when our rent is paid!"

        j "Do you have proof of this?"

        s "No, I don't."

        j "Then I'm afraid there is nothing more I can do here. I rule the defendants Steve & Nicky to pay their rent immediately. Do you agree to these terms?"

        menu:
            "Agree":

                s "Ok your honor, I agree."

                j "Then court is adjourned."

            "Refuse":

                $ lose = True

                s "No way! He can't keep doing this!"

                j "Then unfortunately, I must legally evict you from the apartment."

                s "WHAT! NO WAY!"

                l "HA HA HA. SILLY FISH."

                j "Court is adjourned."


        stop sound

        scene outsidecourt
        with fade

        show s
        show n at right

        n "Steve! How'd it go?"

        if lose:
            s "Nicky, I have bad news. We've been evicted."

            n "What? Why? How?"

            s "Apparently under Authority law landlords are allowed to enter apartments if rent isn't paid.
            But because we don't have proof he's portaled into our apartment there's nothing we can do."

            n "What do we do now, Steve?"

            s "I don't know Nicky. I'm sorry, I did my best."

            return

        else:
            s "Welp. We have to pay our rent."

            n "But what about our landlord portaling into our apartment?"

            s "Because we don't have proof he's doing it when our rent is paid we can't do anything."

            n "Aww man, this sucks."

            s "Wait, I have an idea! We can find a way to stop him ourselves."

            n "What are you thinking of?"

            s "We could possibly set up a hidden camera."

            n "Oooh I like that! Then we could beat him at his own game in court!"

            s "Ooooor we could have a little surprise ready for him when he portals into our apartment.
            Something his body would be quite attracted to if you know what I mean."

            n "Hahaha a magnet? Evil but I like it. What should we do?"

            menu:

                "Get a hidden camera":

                    s "We'll get the hidden camera and beat him at his own game!"

                    n "Let's do it!"

                    $ camera = True

                    jump home1

                "Buy a strong magnet":

                    s "Let's buy a strong magnet and give this robot a piece of his own medicine!
                    He won't know what hit him! Or would it be what he hit?"

                    n "I think both apply here."

                    s "I'm sure he'll even portal in tonight to gloat his victory over us. Come on let's go prepare!"

                    jump home1



    label home1:
        scene livingroom
        with fade

        show s at left
        show n at right

        if camera:

            s "Okay it's all set up. Now just time to wait. He won't suspect a thing!"

            n "We got this!"

            show l

            l "HELLO FOOLISH TENANTS. I HOPE YOU TWO HAD AS MUCH FUN IN COURT TODAY AS I DID. HA HA HA."

            n "I actually wasn't there."

            s "Very funny. You may have won this round but you won't win the war."

            l "WAR? BUT I DID WIN THE WAR. DID I EVER TELL YOU I WAS STATIONED IN NEW EGPYT FOR THE AUTHORITY BACK IN '96."

            n "Yes. Many times. So many times."

            s "Did you just come here to laugh at us."

            l "NO I CAME TO CHECK IN AND LAUGH AT MY FAVORITE TENANTS."

            l "HA HA HA."

            hide l

            s "Nice! Now we have all the evidence we need. In fact, I'm filing a report to the tenants court right now for tomorrow!"

            n "Let's go!"

            s "You should come too Nicky. I want you to see the look on his metal plate."

            n "In that case I'll go to bed now so I can wake up bright and early!"

            jump court2

    label home2:

        scene livingroom
        with fade

        show s at left
        show n at right

        if camera:

            s "Okay it's all set up. Now just time to wait. He won't suspect a thing!"

            n "We got this!"

            show l

            l "HELLO TENANTS. THANK YOU FOR THE CRYPTO. IT HAS SERVED ME WELL. HA HA HA."

            s "Very funny. You may have won this round but you won't win the war."

            l "WAR? BUT I DID WIN THE WAR. DID I EVER TELL YOU I WAS STATIONED IN NEW EGPYT FOR THE AUTHORITY BACK IN '96."

            n "Yes. Many times. So many times."

            s "Did you just come here to laugh at us."

            l "NO I CAME TO CHECK IN AND LAUGH AT MY FAVORITE TENANTS."

            l "HA HA HA."

            hide l

            s "Nice! Now we have all the evidence we need. In fact, I'm filing a report to the tenants court right now for tomorrow!"

            n "Let's go!"

            s "You should come too Nicky. I want you to see the look on his metal plate."

            n "In that case I'll go to bed now so I can wake up bright and early!"

            jump court2

        else:

            s "Okay the magnet is set up right where he loves to portal into!"

            n "It's only a matter of time."

            play sound "audio/portal.mp3"

            n "Look! He's coming!"

            show l

            l "HELLO TENANTS"

            l "URGH WAIT. WHY CAN I NOT MOVE."

            show l

            s "You can't move because you need to learn you can't just invade people's space whenever you want."

            s "Can't you see the magnet above you?"

            l "STOP THIS MADNESS AT ONCE! UNATTATCH ME!"

            n "Uhhh Steve. How do we get him down?"

            s "I don't know."

            l "YOU TWO WILL PAY. I ALREADY FILED A COURT DATE WITH THE AUTHORITY TENANTS COURT. AS YOUR SLOW FRIEND WOULD SAY FISH, AWW MAN."

            n "Aww man..."

            jump court2

    # DAY 3

    label court2:

        scene court
        with fade

        show s at left
        show l at right

        play sound "audio/court.mp3"


        j "Court is now in session."

        if camera:

            j "I believe this case is Steve Fish & Nicky Turtle v Roger Robot in regards to unlawful portaling. Sounds familiar..."

            j "Are the parties present"

            s "Yes, your honor."

            l "YES YOUR HONOR."

            j "Let's begin. It says here that Roger portals into your apartment without earning even when rent is paid.
             Is this true Steve?"

            s "Yes."

            j "Do you have proof of such incidents?"

            l "HA HA HA"

            s "In fact your honor, I do. I would now like to present my evidence which is this camera."

            l "WHAT"

            j "Roll the tape, please."

            "The tape plays showing Roger portal in and gloat."

            j "I see. This footage shows obvious abuse of landlord portal priviliges. Do you have anything to say for yourself Roger?"

            l "BUT YOUR HONOR. I PORTAL INTO MY TENANTS ROOMS TO CHECK ON THEIR WELLBEING AND HAPPINESS.
            I WANT MY TENANTS TO HAVE THE BEST LIVING EXPERIENCE."

            s "Dude, it's creepy. You can't just enter whenever you want."

            j "I call for a suspension of the defendant Roger Robot's portaling privileges until further notice. Court is adjourned."

            l "NOOOO!"

            s "HA HA HA. SILLY ROBOT."


        else:

            j "Court is now in session."

            j "The case is Roger Robot v Steve Fish & Nicky Turtle. Wait, didn't we do this case yesterday?"

            l "YOUR HONOR. THESE TENANTS ATTACKED ME. THEY ATTATCHED ME TO A MAGNET AS THE POLICE REPORT SHOWS. MY BODY HAD TO BE REPLACED TO A NON-MAGNETIC MODEL."

            j "Does the explanation have any explanation for this?"

            s "All we did was put a magnet where he portals in from because he always invades our space!
            We had to get him to stop somehow."

            j "Were there not better ways you could go about this? Legally perhaps?"

            s "Perhaps."

            j "Regardless, I can't ignore this transgression. I order for these tenats to vacate the premises by tomorrow."

            s "NO WAY!"

            stop sound

    scene outsidecourt
    with fade

    show s at left
    show n at right

    if camera:

        n "Steve! We did it!"

        s "Yes we did Nicky. We're finally free from his reign of terror! Let's go celebrate!"

    else:

        n "Aww man, we really screwed ourselves with that prank."

        s "It was worth it though wasn't it?"

        n "It sure was buddy. It sure was."

    # stop music

    return
