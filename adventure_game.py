def pathway():
    print """
    You are knocked over the head with a heavy object and lose consciousness.
    When you come around you find yourself at the beginning of what looks to be a maze.
    \nDo you follow the paths to try and get out?
    """
    get_out = raw_input()
    if get_out == "yes":
        print """
        You follow the path and encounter dead ends
        and circles. Eventually you find what looks
        to be an exit.
        You walk through and
        """
    elif get_out == "no":
        print """
        You sit tight, hoping someone will find you.
        \nThey will. won't they?
        """
#----------------------------------------
print "Would you like to play a game? (yes/no)"

answer = raw_input()

if answer.lower().strip() == "yes" or answer == "y":
    print "A strange man offers you 3 adventure keys, which one do you take? \n 1 2 or 3?"

    keys = raw_input()

    if keys == "1":
        print """You chose key number %s.
        You are stranded on a desert island, or so you thought.
        After a hard day of relaxing on the beach you spot what
        looks to be another human in the trees.
        \nDo you go and investigate? (yes/no)""" % keys

        investigate = raw_input()

        if investigate == "yes":
            print """
            Your curiosity got the better of you and you decide
            to become investigator for the day! It seems your fellow
            human has left the remains of a dead animal on the ground.
            \nDo you go looking for the other half? (yes/no)"""

            curiosity = raw_input()

            if curiosity == "yes":
                print """You do not find the dead animal, however you
                stumble across your fellow human eating something that smells strange.
                \nDo you tap them on the shoulder to find out if you can have some? (yes/no)"""

                tap = raw_input()

                if tap == "yes":
                    print """As you reach out you arm and open your mouth to say 'Hi', they catch a whiff
                    of your scent and turn around before you could utter speech.
                    Blood is dripping from their mouth as they bear their blackened teeth.
                    This is no human! It some sort of zombie!
                    Suddenly your brain decides that you could have a chance of survival is
                    you imitate their actions so they think that you are one of them.
                    \nDo you imitate Mr Zombie? (yes/no)"""

                    imitate = raw_input()
                    if imitate == "yes":
                        print """
                        Imitating the zombie was a stroke of genius! He totally believed
                        you and kindly offered you some of his dead animal. You politely refuse of course.
                        Over the following days, you develop a good friendship with the zombie and you often
                        go exploring together. However, one day you both explore a cave on the other
                        side of the island, it is dark but you eventually reach a point where the
                        ceiling reveals a beam of light, illuminating part of the cave. As you step forward
                        your big size 8's squash a bug on the floor. You begin to lift up your foot and
                        realise that it was a rather hairy spider. You look at your zombie friend, and
                        his gaze is locked on something behind you.
                        \nDo you turn around to look?"""

                        look = raw_input()
                        if look == "yes":
                            print """
                            Momma spider was NOT happy that you squashed her baby!
                            You and the zombie are both spider food tonight!"""

                        elif look == "no":
                            print """
                            You grab your zombie friend and do not turn around,
                            instead opting to make a run for it. You can hear what seems
                            to be hundreds of footsteps behind you crashing on the cave floor,
                            whatever it was behind you either had more than two legs or they
                            were not alone! As you near the exit of the cave the ceiling
                            starts to fall in! Luckily you both make it out in the nick of time
                            and whatever was chasing you is trapped.
                            \n\t\tYou and the zombie walk out unscathed and carry on
                            \t\tdesert island life in peace, for now!"""

                    elif imitate == "no":
                        print """
                        You don't imitate the zombie and instead decide
                        to use your flight reaction...you were never much of a fighter.
                        You run away as fast as you can, until your leg gets stuck in
                        some quick sand, there aren't any branches close enough for you
                        to reach and pull yourself out.
                        \nLooks like it's the end of the road....*titanic music plays*"""

                    elif tap == "no":
                        print"""
                        You decide it's best not to disturb them and begin the trek
                        back to your shelter. Along the way you encounter a beautiful flower
                        and become encapsulated by its beauty. As you edge towards it the flower
                        appears to invite you further. It's a trap! The flower was the tongue
                        of a massive carnivorous plant, a Droseraceae to be precise.
                        \nIt clamps its jaws shut on you, if only you had some tools
                        you could have cut your way out..."""


            elif curiosity == "no":
                print """
                You realise that the dead animal is not actually cooked and
                deduce that this creature you saw was in fact not of human origin.
                You stay well away. On your way back through the trees you discover a cave,
                will you go exploring? (yes/ no)"""

                exploring = raw_input()
                if exploring == "yes":
                    print """
                    It's a little dark so you decide to create a torch using some sticks
                    and some material from your clothes before you enter.
                    As you walk deeper into the cave, you see some drawings on the cave walls.
                    They appear to show lots of tiny people running from something which
                    has been scratched out, so you're not 100% sure what it is.
                    \nDo you venture further into the abyss? (yes/no)"""

                    abyss = raw_input()
                    if abyss == "yes":
                        print"""
                        As you soldier on, the light from your torch bounces of a shiny object.
                        \nDo you go for a closer look (yes/no)?
                        """

                        closer = raw_input()
                        if closer == "yes":
                            print """
                            As you go further, more shiny objects appear.
                            Gold, Silver, Diamonds!!! You've found treasure, lucky you!
                            Now, how to get out of here and carry all this back at the same time......
                            """

                        if closer == "no":
                            print """
                            You take no notice of the shiny object, you've had enough
                            surprises for one day and prefer to exercise caution where
                            your life is at stake! After some time of walking you begin
                            to feel tired and find a nice space to shut your eyes...*yawn*
                            """

                    elif abyss == "no":
                        print"""
                        You think it's best to turn back, that's enough fun for one day!
                        As you reach near to the cave entrance, you discover a flower
                        with a wonderful scent, you wander over to smell it.
                        \nMmm such a lovely smell, reminds me of my favourite perfume....
                        Press any key
                        """

                        any = raw_input()
                        if any == (""):
                            print get_out

                elif exploring == "no":
                    print """
                    You turn around and head back to the beach,
                    that's enough for one day! Maybe tomorrow..."""

            else:
                print "This wasn't an option!"

        elif investigate.lower().strip() == "no":
            print """
            You look, but you do not observe any closer.
            Today is not the day to be nosey, pehaps tomorrow.
            \nBack to zennnn...."""

        else:
            print "Wait, was this a choice?"




    elif keys == "2":
        print """You chose key number %s.
        The game is afoot! You are thirsty and stranded in
        a forest in rural Asia, but come across an old bag.
        \nDo you have a rummage around the bag to see what you can find?
        """ % keys

        rummage = raw_input()
        if rummage == "yes":
            print """
            You discover two tools inside the bag: a knife and some rope.
            A wild beast is running in your direction with a taste for blood in its eyes.
            Which tool do you use to save your life? (knife or rope)"""

            tool = raw_input()
            if tool == "knife":
                print """
                Oh dear, your swipe misses the beast and he scampers away
                with one of the fingers on your left hand. Yikes! Well at
                least you've got 4 left! You bandage yourself up and begin
                to walk through the forest, the knife comes in handy for
                chopping down branches and and swatting mosquitoes.
                You encounter a large web.
                \nDo you go through it or around it? (through/ around)"""

                web = raw_input()
                if web == "through":
                    print """
                    You use your handy knife to cut down the web, however the vibrations
                    alert a rather angry looking blue spider. It starts to chase you as
                    you run through the forest trying to escape it. You see a rock on your left.
                    \nDo you hide behind the rock? (yes/no)
                    """
                    rock = raw_input()
                    if rock == "yes":
                        print """
                        You quickly jump behind the rock and the spider scurries past you.
                        Phew! As you get up, it turns out that this rock was in fact a giant tortoise.
                        Oops! well at least he can't chase you!
                        """
                    elif rock == "no":
                        print """
                        You run past the rock further into the depths of the trees.
                        You see a hanging branch and see it is a good opportunity
                        to grab hold and pull yourself up.
                        \nDo you grab hold of the branch?"""

                        branch = raw_input()
                        if branch == "yes":
                            print """
                            You grab hold of the branch, pulling yourself up.
                            The spider tries for over an hour to get to you and
                            eventually gives up to go and rebuild its web.
                            You cut yourself down and continue on your journey."""
                        elif branch == "no":
                            print """
                            You keep on running, and running, and running, and running....."""

                elif web == "around":
                    print """
                    You go around the web and discover a stream.
                    You're dying for a drink.
                    \nDo you drink the water?(yes/no)
                    """
                    water = raw_input()
                    if water == "yes":
                        print """
                        You drink the water, but begin to feel a little queasy.
                        \nYou decide to take a rest on the forest
                        floor near some large trees..."""

                    elif water == "no":
                        print """
                        You carry on, not wanting to take the risk.
                        Surely there must be some people around here, right?"""


            if tool == "rope":
                print """
                Your quick thinking allows you to lasso the beast and tie it to a tree.
                Yeehaw! as you continue on your journey, the forest begins to fork
                so that you are left with 2 paths.
                Do you go left or right?"""

                choice = raw_input
                if choice == "right":
                    print """
                    You turn right and begin heading deeper into the forest.
                    You come across a large patch of dried up leaves.
                    The urge to jump on them is so strong!
                    \nDo you resist temptation?"""

                    temptation = raw_input()
                    if temptation == "no":
                        print """
                        You have the time of your life jumping on all those leaves!
                        *crunch crunch*
                        That is until you jump straight into the whole that was underneath!
                        Aaaaaaaaaaaaaaaaaaahhhh"""
                    elif temptation == "yes":
                        print """
                        Your willpower is strong. You go around the leaves instead.
                        You're not falling for any traps today!
                        As you stumble across the forest floor, you see some smoke in the distance.
                        Surely this is a sign of life!
                        \nDo you go and see what the cause of this smoke is? (yes/no)"""

                        smoke = raw_input()
                        if smoke == "yes":
                            print"""
                            As you walk towards the smoke, the trees
                            clear and you see houses in the distance.
                            You are saved!"""
                        elif smoke == "no":
                            print "You venture on, and on, and on, and on, and on....."

                elif choice == "left":
                    print"""
                    You turn left and begin heading deeper into the forest.
                    You encounter a narrow stream and suddenly remember
                    that you're thirsty.
                    \nDo you drink the water? (yes/no)
                    """
                    thirst = raw_input()
                    if thirst == "yes":
                        print """
                        You drink the water, but begin to feel a little
                        queasy. You decide to take a rest on the forest
                        floor near some large trees..."""

                    elif thirst == "no":
                        print """
                        You carry on, not wanting to take the risk.
                        Surely there must be some people around here, right?"""
                else:
                    print "Are you lost already?"


            else:
                print "This wasn't an option..."

        elif rummage == "no":
            print """
            You make your way through the forest and step on a vine which
            swings you up in the air, leaving you dangling by your feet.
            You try and cry for help but no one is around. It's a shame you
            didn't look in the bag, perhaps there might have been a knife in
            there that could have cut you down! Oh well, better carry on
            screaming for help! Hopefully the villagers will reach you
            before the tigers ey?"""

    elif keys == "3":
        print "You chose key number %s." % keys
    else:
        print "Hey, that's not a key!"








elif answer.lower().strip() == "no" or answer == "n":
    print "Okay, enjoy the rest of the website!"

else:
    print "Invalid answer!"
