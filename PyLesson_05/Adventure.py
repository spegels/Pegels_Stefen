choice1 = input("You are exporing the wilderness when you come upon a crashed plane. Do you investigate?")
if choice1 == "yes":
    choice2 = input("Where do you enter the airplane: front, back, or side?")
    if choice2 == "front":
        choice3 = input("You notice a smashed cockpit, and no sign of anyone. Do you search, or leave?")
        if choice3 == "search":
            print("You search for hours, but are unable to find any evidence of what happened. You stumble home to call the police.")
        if choice3 == "leave":
            print("You abandon the airplane, and alert the authorities.")
    if choice2 == "side":
        choice3 = input("You climb up to the plane's emergency exit, which is smashed shut. Do you pry it open, or decide to leave?")
        if choice3 == "pry it open":
            print("You manage to smash the door, and glimpse a shaking flight attendant. You tend to her wounds and help her off.")
        if choice3 == "leave":
            print("Not confident in your physical abilities, you walk home in shame.")
    if choice2 == "back":
        choice3 = input("At the plane's tail, a group of survivors are trapped together in the wreckage. Do you help, or leave?")
        if choice3 == "help":
            print("Choosing to help, you approach the group, only to be crushed by an unstable plane engine.")
        if choice3 == "leave":
            print("Despite their pleading cries, you walk away, trusting your gut.")
if choice1 == "no":
    print("You walk past, refusing to get involved.")
