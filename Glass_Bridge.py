import random

def glass_bridge():
    print(""" \n***WELCOME TO THE SECOND GAME. THE OBJECTIVE OF THE GAME IS TO CROSS THE BRIDGE BY PICKING THE CORRECT TILE TO STEP ON.***
                
        ***CHOOSE WHICH GLASS TILE TO JUMP TO OR USE OTHER METHODS TO GET ACROSS ***\n""")
    
    app_running = True
    square_counter = 0
    push_choice = True
    
    
    while app_running == True:
        squares = ["right", "left"]
        square_choice = (input("Choose which square to jump to: [r]ight or [l]eft: "))                          
        invisible_hand = random.choice(squares)
        
        if square_counter >= 3:
            print("You survived the glass bridge! \n")
            print("""
            
             \n***YOU NOW HAVE 45 BILLION WON BUT YOU ARE ALSO CONSTANTLY HAUNTED BY THE PAST AND DECIDE TO GIVE ALL YOUR MONEY AWAY!! CONGRATS!***


mmmmmmmmmmmmmmmddddysooooooooooooo+++++++++++++++++++++++++++++++++++++++oooyhddddNNmmmmmmmmmmNNNMMMMMNmyssso++++++++++++++++++++++++++++++++++++++oooooooooooooooossssssoooooooosss
mmmmmmmmmmmmdddddddysoooooooooo++++++++++++++++++++++++++++++++++++++++++syhdddmmmmmmmmmNNNNMMMMMMMMMMMNmdddhhyysso++++++++++++++++++++++++++++++++++++oooooooooooooossssoooooooosss
mmmmmmmmmmmddddddddhooooooooooo+++++++++++++++++++++++++++++++++++++++oshmmmmNNNNmmmmmNNNNNNNMMMMMMMMMMMMNNNNNmmmmhyo++++++++++++++++++++++++++++++++++++ooooooooooooossooooooooosss
mmmmmmmmdmmddddddddhsoooooooooo++++++++++++++++++++++++++++++++++++ooshdmmNNNNMMNmmmmmNNNNNMNMMMMMMMMMMMMMMMNNNNNNNmmyo+++++++++++++++++++++++++++++++++++ooooooooooooooooooooooooss
mmmmmmmmdddddddddddhsooooooo++++++++++++++++++++++++++++++++++++oooshmmmNNNNNMMMNNNmmNNNNNNNNNNNNNmmNNNMMMMMMMMMNNNNNmds++++++++++++++++++++++++++++++++++ooooooooooooooo++ooooooooo
mmmmmmmmmmmddddddddhsooooooo+++++++++++++++++++++++++++++++oooosyhdmmNNNNNMMMMMNNNNNNNNNmmmmmmddhyssosyhmNMMMMMMMMNNMNNmyo+++++++++++++++++++++++++++++++++ooooooooooooso++ooooooooo
mmmmmmmmmmmddddddddhyoooo+++++++++++++++++++++++++++++++++++oshdmmmNNNMMMMMMMMMNNNMMNNNNmddhhhys+///:/++shmMMMMMMMMNNMNNmyo+++++++++++++++++++++++++++++++++ooooooooooooo+++oooooooo
mmmmmmmmmmmmdhhddddhyooo+++++++++++++++++++++++++++++++++++ooymNNNNNNNNNNNMMMMMNNMMNNNNNmhhysso+//:::///+osdNMMMMMMNMNMNNmyo+++++++++++++++++++++++++++++++++ooooooooooo++++oooooooo
mmmmddmmmmNNmhhNmdddyooo++++++++++++++++++++++++++++++++++ooydNNmNMNNNNNNNNNMMMMMMMNNNNNmhysoo+/+///////+++sdNMMMMNNNNMMNNmyo++++++++++++++++++++++++++++++++ooooooooooo+++++ooooooo
mmmdddmmmmmdddNMNmddhoo+++++++++++++++++++++++++++++++++++oohmmNNNNMMNMMMMMMMMMMMMMNmNNNdysooo+++///++/++++oydNMMMNNNMNNNNNdys+++++++++++++++++++++++++++++++ooooooooooo++++++oooooo
mmddddddmNNNNMMMNmddhoo+++++++++++++++++++++++++++++++++++oymNNNmmNNNNNNNMMMNMMMNMNmNNNdyso++++//////+++++++shmNMMMMMMNNNNNhhso+++++++++++++++++++++++++++++++oooooooooo++++++oooooo
mmddddddmNNMMMMMNNddho+++++++++++++++++++++++++++++++++++oymNNMNNNNNNNNNNNMMMMNNNNNNmdhsoo++////::::////++++osdNMMMMMMNNNNNddhso++++++++++++++++++++++++++++++ooooooooo++++++++ooooo
mdddddddddmNMMNNNmddho++++++++++++++++++++++++++++++++++++hNMMMMNMMMNNNNNNMNNNMNNmmdhysooo+++////:::::///+++oshNMMMMMMNNNNNdhhso+++++++++++++++++++++++++++++++oooooooo++++++++ooooo
dddddddddddmmmmmddddds+++++++++++++++++++++++++++++++++++odNMMMNNMMMMMNmmNNNNNNNNNNmmddhysssoooosso++//////+osymMMMMMMMMMNNmys+++++++++++++++++++++++++++++++++oooooooo++++++++ooooo
ddddddddddddhddhhyyyyo+o+++++++++++++++++++++++++++++++++omNMMMNNMMMMNdhhdmdddhhdmmmmmmdhyyyssyhddmmmmdhyysoosymMMMMMMMMMMNms++++++++++++++++++++++++++++++++++++oooooo++++++++ooooo
dddddddddhhhhhhhyyyyys+++++++++++++++++++++++++++++++++++ohMMMMNNMMMMmhhddhyssyyyhhdmmdddhyyyhhddmmmmdmdddhhysydNMMMMMMMMMNho++++++++++++++++++++++++++++++++++++oo+ooo+++++++oooooo
ddddddddhhhhhhhhyyyyyso+++++++++++++++++++++++++++++++++++odMMMMMMMMNhyhyyyhddmmmmmmmdddhhyyyddmmdhhyyssyyhddhyhNMMMMMMMMMmso+++++++++++++++++++++++++++++++++++++o+ooo+++++++oooooo
ddddmmmdhhhhhhhhyyyyyso++++++++++++++++++++++++++++++++++++omMMMMMMMhyyyyhmmmdmmmmmNNmmdysooshmmdmmmmdhhysyydhyyNMMMMMMMMNNs++++++++++++++++++++++++++++++++++++++ooooo+++++++oooooo
ddddmmmddhhhhhhhhyyyys+++++++++++++++++++++++++++++++++///++yNMMMMMmyssssyyyhhhhhhhdddhys+//+yddmmmmmNNNNmdyyyyydMMMMMMMMNms++++/++++++++++++++++++++++++++++++++++++o++++++++oooooo
dddddmmmddhhdddhhhhhhy++++/++//////////////////////////////+ymNMMMMhoooo+++osshddddhyssso/:/+syydddhhhhhhdmdhyysyNMMMMMMNho+//////////////////////////////++++++++++++++++++++oooooo
dddddmmmmdddddmdhhdddho+++++++++++++++++++++++++++++++++++++smNNMMNso++++++++++oo+++oooo+:::+osoosyyyyyyssooossssNMMMMMNhoo++++++++++++++++++++++++++++++++++++++ooooo++++++++oooooo
ddddddmmmddhhdddhhdddho+++++++++++++++++++++++++++++++++++++odNNMMdso++++++++++//+++++++/::/++o++++++++/////+++osmMMMMNNdso+o++++++++++++++++ooooooooooooooooooooooooo++++++++oooooo
ddddddmmmddhhhhhhhhhhyoo+++syyyyyyyyyyyyyyyyyyyyyyyyyysssssyyhmMMMdso+++++oooo+oosyysoo+/:://+oso+///+++/////++osmMMMMNNmhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysoooo+++++++ooooooo
ddddddmmmmddhhhhhhdddhs+o++oysooooooooooooooooooooooooooooooohmNMMdsoooosssyyyhhddy+/+++++++oooshhyoo++++++//++oyNMMMMNNmhyssooooooooooooooooooooooooooooossssssyooooo+++++++ooooooo
ddddddmmmdddddddhhhhddy++++osoooooooooooooooooooooooooo++++++osydmdsyyyyhhhhddmmdysoooooosssso++sdmdhysoooo+++oshMMMMNNNmdyoooooooooooooooooooooooooooooooooooossooooo+++++++ooooooo
dddddmmmmmdddmmmddddddy++++oso+++oooooooooooooooooooo++++++++oooohhyhhhhhdmmmmmdhddmmmdhhhddddhhhddmmdhyyysssssydMMMNNdhysooooooooooooooooooooooooooooooooooooossooooo++++++oooooooo
ddddmmmdmNNNNNNNNNmmmmho+++oso+++oooooooooooooooooooo++++++++shhdmhyhhhddmmmmmdhhhhddmmmmmmmmNmddhhmmmmddhhhhhyymmNmmhysooooooooooooooooooooooooooooooooooooooossooooo+++++ooooooooo
hddddmddddmmNNNNNmmmddyo+++ooo++o+oooo+++++ooooooooo+++++++++sdmNNNhhhhddmNmmddhhyyhhdddmmmmmddhhdddmmmmddddhhhhddhysssoooooooooooooooooooooooooooooooooooooooossooooo+++++ooooooooo
hdmmmmddddddddddddhhhhyo+++ooo+oo+oooo++++++oooooooo+++++++oosydmNNdyddddmNNmmddhhhhhhhhdddhhhyyyhhdmmNNdmddhhhhdmdhyysoooooooooooooooooooooooooooooooooooooooosoooooo+++++ooooooooo
ddmNNNmmddddddmmdddhhhyo+++ooo+oo+oooo++++++oooooooo+++++++oooydmNNmyhhhdddNNmMNmdddddddmddmdddddmmmNNNmdmdddhhmmdhysoooooooooooooooooooooooooooooooooooooooooosoooooo+++++ooooooooo
ddmNMNNmdddddmmmmddhhhyo+o++ooo++oooooooooooooooooooooooo+ooooymNNNNdhhhhhdmmdmNNhhyyysyhyyhydhdmNMNNNmddddddhmMNmhysoooooooooooooooooooooooooooooooooooooooooossoooooo++oooooooooss
dddmmmmmdddddmmmmdhhhhhs+o++ooo++ooooooooooooooooooooooooooooooshmNNNdhhhhhdddhhdmNmddhhdhhhhmmNNmmmmdddddddhmMMNNdhsoooooooooooooooooooooooooooooooooooooooooossoooooo+ooooooooosss
ddhddhdddddddmmmdddhhhhs+++oosoooooooooooooooooooooo+++oooooooooosyhhdhhhhhhdhyyyhhhhddddddhhddddhddhhhdddddmNNNmyoooooooooooooooooooooooooooooooooooooooooooossoooooo+oooooooooooss
ddhhhhdmmdddmmmmmdddddhyo++oosoooooooooooooooooooooo+++ooooooooooosssymmhhhhhhhyyyyysyyyhyyyyyyhhhhhhhddddmNNhhyssoooooooooooooooooooooooooooooooooooooooooooossooooooooooooooooosss
ddhhhddmmmmmmmmmmmdddddyo++oosooooooooooooooooooooooo+ooooooooooooooohNMmhhyyyyyyyyhhhhhhhhhhhhyhhhhhhdddmMMMmysoooooooooooooooooooooooooooooooooooooooooooooossoooooooooooooooossss
dddhdddmmmmmmmmmNNmddddyo+o+osooooooooooooooooooooooooooooooooooooossmMMMdhhyyyssyyhhddddddddhyyyyyhhhddhNMMMNdyyssooooooooooooooooooooooooooooooooooooooooooossoooooooooooooooossss
dddhddddmmmmmmmNNmmddddyooooosooooooooooooooooooooooooooooooo++////ohNMMMmdhhyssosssyyyyyyyyyyyssyyhhddddMMMMNmdy///+ooossoooooooooooooooooooooooooooooooooooossoooooooooooooooossss
ddddddhddmmmmmmNmddddddhooo+osooo+oooooooooooo++oo+ooooo++/:-----:/ydNMMMmhhdyssoooosssssssssssssyhddddddMMMMMNmdy::---::/+oooooooooooooooooooooooooooooooooosssoosooooooooooossssss
ddddddddmmmmmmNmddhhdddhooo+osooo+ooooooooooooo+o++//:---------:::sdmNNMMNddddysssssssssooooossyyhmmddddmMMMMMNNdds:------.-----:::/++ooooooooooooooooooooooosssoossoooooooossssssss
ddddddddmNmmmmNmdhhhhdmdooooossoooooooo+ooo+++::--...-.------::::/ddmNNMMMNmddmddhhhhyysyyyhhhhddmdddddmmMMMMNNNmdd+::--------.........-:/+oooooooooooooooooosssoossoooooooossssssss
ddddddddmmmmmNNmdhhhhhddsoooossooooooooooo/:-..------------:-://+sdmNNNMMMMNmmmmdddddddddmmmmmmmmmddddmmNMMMMNNNNmdh/:------------------...-/oooooooooooooooosssoosooooooossssssssss
ddddddddmmmmmNNmdhddhhdmyoooossooooooooo+:..-----------::+osyhdddddmNNNNMMMMNmmmmddmmmmmmmmmmmmmmmdddmmmNMMMNNNNNNmddhyo+/:-----------------.-+oooooooooooooossssssssosssssssyyyyyyy
mmmmmmmmmmmmmmNNmmmmmmmmyoooossoooooooo:-.----:---:/+oyhdddddddddddmNNNNMMMMNNmmmmddddddddmmmmmmmmdmmmmNNMMMNNNNmmNddddddddhys+/::------------./ooooooooosoossssssssyyyhhhhhhhhhdddd
NNNNNNNmmmmmmmmmmmNNNNmmyoooossoooooo/-.----::/osyhdddmmddddddddddmNNNNNNMMMMMNmmmmmmmmmmmmmmmmmmddmmmmNNMMMNNNNmmmmdddddddmmmmddhyso+/:-------./ooooooosssosssssssyyhhhhhhhhhdddddd
NNNNNNNNNNmmmmmmmNNNNNmmyoooossooooo/---:/oshdddmmddddddddddddddddmmNNNNNNMMMMNNmmmmmmmmmmmmmmmmddmmmmmNMMMMNNNmNNmmmddddddmmddddmmmmdhys+/:-----/ooooossssssyyssssyhhhhhhhhhhdddddd
NNNNNNNNNNmmddmmNNNNNNmmhsooossoooo+--:oyddmmmddddddddddddmdddddhdddmmmNNNNMMMMMNmmmmmmmmmmmmmmmmmmmmmNMMMMNNNNmNNNmmmddddmmmddddddddddmmmdhs/:::-:sooosossssyyssssyhhhhhhhhhhdddddd
NNNNNNNNNNmmmmmNNNNNNNNNdssoossooo+:/shddmmmmmdddmmmmddddmmmddmmdddmmmmNNNNMMMMMMNNNmNNNNNNNNNmmmmmNNMMMMMNNNNmmmNNmmdmdddmmmdddddddddddmmmmmds//:-/oooooosssyyssssyhhhhhhhhhhdddddd
NNNNNNNNNNNNNNMMNNNNNNNNdsooosso+o/odNmdmmmmmmmmmmmmmddmmmmddmmdmmNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNmmmmmmmdddddddmmddddmddmmmmmmmmdh+/::/++++oooosssssyyhhhhhhhhhddddddd
NNNNNNmNNNMMMMMMNNmmmmNNmssoooooooommNmdmmmmmmmmmmmmmmmmmmddmmdmNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMNNmmmNNNNNmmmmmdmmmmmmdddmmmmdddmdmmmmmmmmdmmy+::ososssssssssyyyhhhhhhhddddddddd
NNNNmmmNNNMMMMNNNmmmmmNNmysssoooo/ymmNmmmmmmmmmmmmmmmmmmmmdmmdmmNNNmNNNNNNNNNNNmmmmNNNNNNNNNNNNNmmdhyyyhmNNNmmmmmmmmmmNNNmmdmmmmmdddmmmmmmmmmmdmNmd/:/ssssssyssyyyyyhhhhhhdddddddddd
NNNmmmmNNMMMNNNNmmmmmNNNNhyyyyyyo/hmNNmmmNmmmmmmmmmmmmmmmmmmddmmNNNmNNNNNNNNNNNmyyyyhhhhhhhyyyysssssssyhmNNNmmmmmmmNNNNmmdmmdmmmmmddmmmmmmmmmmmmmNh//:yhhhhhhhhhhhhhhhhhdddddddddddd
NNNmmmmmNNNNNNmmmmmmmmmmmhyyyyys//dmNNmmmNmmmmmmmmmmdmmmmmmmddmmNNNmNNNNNNNNNNNNmhysssssoooooooooo+ooshmNNNNNNmNNNNNNmmmmddmmmmmmdmddmmmmmmmmmmmNNd///+yyyyyyyyhhhhhhhhhdddddddddddd



             """)
            exit() 
        elif square_choice == 'r' and invisible_hand == 'right' or square_choice == 'l' and invisible_hand == 'left':
            print("You Died!")
            glass_bridge()
        elif square_choice == 'r' and invisible_hand == 'left' or square_choice == 'l' and invisible_hand == 'right':          # if player choice is different from the "invisible_hand", move on
            square_counter += 2
            square_choice2 = input("\nYou survived, [m]ove again or [p]ush the player in front of you: ")
            
            if square_choice2 == 'm':
                print("Move Again\n")
            elif square_choice2 == 'p':
                if push_choice == True:
                    square_counter += 1
                    print("You pushed the player in front of you and moved one square forward, no pushes remaining\n")
                    push_choice = False                                                                                 # player should only have the option to press push once
                else:
                    print("Push already used, please move again\n")

