import random

def ask_math_riddle():
    riddle = "If A+A+A=39 and B+B-A=25 and 6+C+B=50 then what does A+B+C=?"
    riddle_answer = "57"
    user_answer = input(f"{riddle} ")
    return riddle_answer, user_answer

def generate_math_question():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    print(f"What is {num1} {operator} {num2}?")
    return num1, num2, operator

def ask_math_question():
    num1, num2, operator = generate_math_question()
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return None, None
        answer = num1 / num2  # For simplicity, assuming float division
    else:
        print("Invalid operator!")
        return None, None
    try:
        user_answer = float(input("Your answer: "))  # Allow for float inputs
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None, None
    return user_answer, answer


def game_start():
    print("Welcome to the Detective Game!")
    print("You arrive at the crime scene.")
    print("Investigate the area and find clues to solve the mystery.")
    start = input("ARE YOU READY? ")
    if start.lower() in ['yes', 'y', 'yess', 'yesss', 'yup', 'yuppp', 'yupppp', 'yuppppp','yessss', 'yesssss', 'yessssss', 'yesssssss', 'yessssssss','yessir', 'yessirr','yessirrr', 'yessirrrr', 'yessirrrrr', 'yessirrrrrr']:
        print("Lets get started!")
        print("To Begin the game you need to answer a Maths Riddle")

        while True:
            user_answer, answer = ask_math_riddle()
            if user_answer == answer:
                print("Correct!")
                break
            else:
                print ("Uncorrect, Try Again")

        print("Now that you have correctly answered the Maths Riddle")
        print("You also need to answer a Maths Question")

        while True:
            user_answer, answer = ask_math_question()
            if user_answer == answer:
                print("Correct!")
                break
            else:
                print("Incorrect!")
                print("You have to try again.")

        print("You come home from school to find that your mum is dead.")
        print("You know that this means that she has left you a large sum of money.")
        print("Do you go to the police, or investigate yourself? ")
        choice = input("Type 'p' to go to the police or 'i' to investigate: ")
        if choice.lower() in ['police', 'p']:
            print("You go to the police station and ask for help.")
            print("The police arrive and decide that she had a heart attack.")
            print("Do you question the police or leave?")
            choice = input("Type 'q' or 'l': ")
            if choice == 'l':
              print("You decide to trust the police and leave the scene.")
              print("The police say to stop wasting time and call your dad to pick you up.")
              print("Your dad comes and picks you up from the police station.")
              print("He tells you to stop trying to be a detective and drop it.")
              print("Do you obey him or not?")
              choice = input("Type 'o' to obey or 'd' to disobey: ")
              if choice == 'o':
                print("You decide to obey your dad and leave the investigation to the police.")
                print('You get home to find that the money your mum left you has been stolen.')
                print("Do you go to the police or continue investigating?")
                choice = input("Type 'p' to go to the police or 'i' to investigate: ")
                if choice == 'p':
                  print("You go to the police station and try to tell them that your money was stolen.")
                  print("The police tell you that if you keep wasting police time they will fine you.")
                  print("You decide to investigate yourself.")
                  print("You remember hearing someone say that they were going to number three Chairea street.")
                  print("You had thought you were dreaming at the time, but maybe it was someone talking about where they were taking the money.")
                  print("Do you go to number three Chairea street or continue investigating?")
                  choice = input("Type 'c' to continue investigating or 'g' to go to number three Chairea street: ")
                  if choice == 'g':
                    print("You decide to go to number three Chairea street.")
                    print("Luckily it is just around the corner from your house.")
                    print("You arrive at three Chairea street, but the door is locked.")
                    print("You see a riddle on the side of the door.")
                    print("The code to unlock the door is the answer to the riddle.")
                  if choice == 'c':
                    print("You decide to continue investigating but you can't find anymore leads.")
                    print("You decide to go to number three Chairea street.")
                    print("Luckily it is just around the corner from your house.")
                    print("You arrive at three Chairea street, but the door is locked.")
                    print("You see a riddle on the side of the door.")
                    print("The code to unlock the door is the answer to the riddle.")
                    user_answer, answer = ask_math_riddle()
                    if user_answer == answer:
                        print("Correct!")
                        print("The door unlocks.")
                        print("You carefully open the door and peer inside.")
                        print("You can see the robbers sitting at a table with all of your money.")
                        print("You decide to create a distraction.")
                        print("You can either set off a smoke bomb, set a dog on them, or start a fire.")
                        choice = input("Type 's' to set off a smoke device, 'd' to set a dog on them and 'f' to start a fire: ")
                        if choice == 's':
                            # code to set off a smoke device
                            print("You have to do some maths to work out the physics of where to throw the smoke bomb.")
                            while True:
                                user_answer, answer = ask_math_riddle()
                                if user_answer == answer:
                                    print("Correct!")
                                    print("You throw the smoke device, and the robbers run away thinking that it is the police.")
                                    print("You run and grab the money and get away with it.")
                                    print("You put the money safely in the bank.")
                                    break
                                else:
                                    print ("Uncorrect, Try Again")
                        elif choice == 'd':
                            # code to set a dog on them
                            print("A Dog attacks you!")
                        elif choice == 'f':
                            # code to start a fire
                            print("You tried to start a fire and burned your hand")
                        else:
                            print("Invalid choice")
                        while True:
                            user_answer, answer = ask_math_question()
                            if user_answer == answer:
                                print("Correct!")
                                print("You throw the smoke bomb, and the robbers run away thinking that it is the police.")
                                print("You run and grab the money and get away with it.")
                                print("You put the money safely in the bank.")
                                break
                            else:
                                print("Incorrect!")
                                print("The door remains locked.")
                                print("You have to try again.")
                    else:
                       print("You got the question wrong")
                    if choice == 'd':
                        print("You have to do some maths to work out where to let go of the dog.")
                        while True:
                            user_answer, answer = ask_math_question()
                            if user_answer == answer:
                                print("Correct!")
                                print("You let go of the dog and the robbers run away.")
                                print("You run and grab the money and get away with it.")
                                print("You put the money safely in the bank.")
                                break
                            else:
                                print("Incorrect. The correct answer was:", answer)

                print("You decide to continue investigating the case on your own.")
                print("You look around the room and take in every detail.")
                print("You decide that you can either investigate the body or the surroundings.")
                choice = input("Type 'body' or 'surroundings': ")
                if choice == 'body':
                  print("You look at you mums body, but you can't find anything strange.")
                  print("Then you notice a brown stain around her lips.")
                  print("You lok around and see a chocolate milkshake on the table.")
                  print("You are starting to think that maybe she did just have a heart attack.")
                  print("Do you continue investigating or leave?")
                  choice = input("Type 'c' for continue or 'd' for discontinue: ")
                  if choice == 'c':
                    print("Out of loyalty to your mum you continue the investigation.")
                    print("You look around the room and take in every detail.")
                    print("You see the chocolate milkshake on the table.")
                    print("You know how much your mum loves chocolate milkshakes.")
                    print("You realise that milkshakes can lead to heart attacks.")
                    print("Do you accept that the police were right or continue investigating?")
                    choice = input("Type 'a' for accept or 'd' for don't accept: ")
                    if choice == 'a':
                      print("You accept that the police were right and leave the investigation.")
                      game_start()
                    if choice == 'do':
                      print("You decide to take a closer look at the milkshake.")
                      print("You cannot find anything strange about the milkshake.")
                      print("Thats when you accidently kick a box on the floor.")
                      print("Do you pick up the box or leave it?")
                      choice = input("Type 'p' to pick it up or 'n' to not pick it up: ")
                      if choice == 'p':
                        print("You pick up the box and see that it is rat poison.")
                        print("You find this strange because you don't have rats in your house.")
                        print("You wonder if someone put the rat poison in your mums milkshake.")
                        print("You realise that that would be considered murder.")
                        print("Do you go to the police or keep investigating yourself?")
                        choice = input("Type 'p' to go to the police or 'i' to investigate: ")
                        if choice == 'p':
                          print('You get home to find that the money your mum left you has been stolen.')
                          print("Do you go to the police or continue investigating?")
                          print("Type 'p' to go to the police or 'i' to investigate: ")
                          if choice == 'p':
                            print("You go to the police station and try to tell them that your money was stolen.")
                            print("The police tell you that if you keep wasting police time they will fine you.")
                            print("You decide to investigate yourself.")
                            print("You remember hearing someone say that they were going to number three Chairea street.")
                            print("You had thought you were dreaming at the time, but maybe it was someone talking about where they were taking the money.")
                            print("Do you go to number three Chairea street or continue investigating?")
                            print("Type 'c' to continue investigating or 'g' to go to number three Chairea street: ")
                            if choice == 'c':
                              print("You decide to continue investigating but you can't find anymore leads.")
                              print("You decide to go to number three Chairea street.")
                        if choice == 'surroundings':
                            print("You look around the room and take in every detail.")
                            print("You notice a chocolate milkshake on the table.")
                            print("You decide to take a closer look at the milkshake.")
                            print("You cannot find anything strange about the milkshake.")
                            print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                            print("The police won't let you have the milkshake tested.")
                            print('You get home to find that the money your mum left you has been stolen.')
                            print("Do you go to the police or continue investigating?")
                            print("Type 'p' to go to the police or 'i' to investigate: ")
                            if choice == 'p':
                              print("You go to the police station and try to tell them that your money was stolen.")
                              print("The police tell you that if you keep wasting police time they will fine you.")
                              print("You decide to investigate yourself.")
                              print("You remember hearing someone say that they were going to number three Chairea street.")
                              print("You had thought you were dreaming at the time, but maybe it was someone talking about where they were taking the money.")
                              print("Do you go to number three Chairea street or continue investigating?")
                              print("Type 'c' to continue investigating or 'g' to go to number three Chairea street: ")
                              if choice == 'c':
                                print("You decide to continue investigating but you can't find anymore leads.")
                                print("You decide to go to number three Chairea street.")
                if choice == 'i':
                  print("You choose to investigate yourself.")
                  print("You look around the room and take in every detail.")
                  print("You decide that you can either investigate the body or the surroundings.")
                choice = input("Type 'b' or 's': ")
                if choice == 'b':
                  print("You look at you mums body, but you can't find anything strange.")
                  print("Then you notice a brown stain around her lips.")
                  print("You find this strange until you notice the chocolate milkshake on the table.")
                  print("You are starting to think that maybe she did just have a heart attack.")
                  print("Do you continue investigating or leave?")
                choice = input("Type 'continue' or 'discontinue': ")
                if choice == 'continue':
                  print("Out of loyalty to your mum you continue the investigation.")
                  print("You look around the room and take in every detail.")
                  print("You see the chocolate milkshake on the table.")
                  print("You know how much your mum loves chocolate milkshakes.")
                  print("You realise that milkshakes can lead to heart attacks.")
                  print("Do you accept that the police were right or continue investigating?")
                  choice = input("Type 'accept' or 'dont accept': ")
                  if choice == 'accept':
                    print("You decide to accept that the police were right and stop investigating.")
                    game_start()
                  elif choice == 'dont accept':
                    print("You decide to take a closer look at the milkshake.")
                    print("You cannot find anything strange about the milkshake.")
                    print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                    print("The milkshake doesn't contain any poison, and the police show you an ultra-scan of yor mums heart.")
                    print("You realise that she did have a heart attack and decide that next time you should leave the investagating to the police.")

                  if choice == 's':
                    print("You look around the room and take in every detail.")
                    print("You notice a chocolate milkshakje on the table.")
                    print("You decide to take a closer look at the milkshake.")
                    print("You cannot find anything strange about the milkshake.")
                    print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                    print("The milkshake doesn't contain any poison, and the police show you an ultra-scan of yor mums heart.")
                    print("You realise that she did have a heart attack and decide that next time you should leave the investagating to the police.")

                  if choice == 'q':
                    print("You tell the police that your mum is only 32 and very fit.")
                    print("The police say to stop wasting time and call your dad to pick you up.")
                    print("Your dad comes and picks you up from the police station.")
                    print("He tells you to stop trying to be a detective and drop it.")
                    print("Do you obey him or not?")
                    choice = input("Type 'o' to obey or 'd' to disobey: ")
                    if choice == 'o':
                      print("You decide to obey your dad and leave the investigation to the police.")
                      print('You get home to find that the money your mum left you has been stolen.')
                      print("Do you go to the police or continue investigating?")
                    if choice == 'd':
                      print("You decide to continue investigating the case on your own.")
                    print("You look around the room and take in every detail.")
                    print("You decide that you can either investigate the body or the surroundings.")
                    choice = input("Type 'body' or 'surroundings': ")
                    if choice == 'body':
                      print("You look at you mums body, but you can't find anything strange.")
                      print("Then you notice a brown stain around her lips.")
                      print("You lok around and see a chocolate milkshake on the table.")
                      print("You are starting to think that maybe she did just have a heart attack.")
                      print("Do you continue investigating or leave?")
                      choice = input("Type 'c' for continue or 'd' for discontinue: ")
                      if choice == 'c':
                        print("Out of loyalty to your mum you continue the investigation.")
                        print("You look around the room and take in every detail.")
                        print("You see the chocolate milkshake on the table.")
                        print("You know how much your mum loves chocolate milkshakes.")
                        print("You realise that milkshakes can lead to heart attacks.")
                        print("Do you accept that the police were right or continue investigating?")
                        choice = input("Type 'a' for accept or 'd' for don't accept: ")
                        if choice == 'a':
                          print("You accept that the police were right and leave the investigation.")
                          game_start()
                        if choice == 'do':
                          print("You decide to take a closer look at the milkshake.")
                          print("You cannot find anything strange about the milkshake.")
                          print("Thats when you accidently kick a box on the floor.")
                          print("Do you pick up the box or leave it?")
                          choice = input("Type 'p' to pick it up or 'n' to not pick it up: ")
                          if choice == 'p':
                            print("You pick up the box and see that it is rat poison.")
                            print("You find this strange because you don't have rats in your house.")
                            print("You wonder if someone put the rat poison in your mums milkshake.")
                            print("You realise that that would be considered murder.")
                            print("Do you go to the police or keep investigating yourself?")
                            choice = input("Type 'p' to go to the police or 'i' to investigate: ")
                            if choice == 'p':
                              game_start()
                    if choice == 'surroundings':
                        print("You look around the room and take in every detail.")
                        print("You notice a chocolate milkshake on the table.")
                        print("You decide to take a closer look at the milkshake.")
                        print("You cannot find anything strange about the milkshake.")
                        print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                        print("The milkshake doesn't contain any poison, and the police show you an ultra-scan of yor mums heart.")
                        print("You realise that she did have a heart attack and decide that next time you should leave the investagating to the police.")
                        game_start()

                    if choice.lower() in ['investigate', 'i']:
                        print("You choose to investigate yourself.")
                        print("You look around the room and take in every detail.")
                        print("You decide that you can either investigate the body or the surroundings.")
                        choice = input("Type 'b' or 's': ")
                        if choice == 'b':
                            print("You look at you mums body, but you can't find anything strange.")
                            print("Then you notice a brown stain around her lips.")
                            print("You find this strange until you notice the chocolate milkshake on the table.")
                            print("You know how much your mum loves chocolate milkshakes.")
                            print("You realise that milkshakes can lead to heart attacks.")
                            print("Do you continue investigating?")
                            choice = input("Type 'c' to continue and 'l' to leave: ")
                            if choice == 'l':
                                print("You decide that she must have had a heart attack.")
                                print("Then you notice that the money she left you has gone missing.")
                                print("Do you go to the police or continue investigating?")
                                choice = input("Type 'p' to go to the police or 'i' to investigate: ")
                                if choice == 'p':
                                    print("You decide to go to the police station to find out what happened.")
                                    print("They are busy with another case and make you leave.")
                                    print("You decide to investigate yourself.")
                                    print("You remember hearing someone say that they were going to number three Chairea street.")
                                    print("You had thought you were dreaming at the time, but maybe it was someone talking about where they were taking the money.")
                                    print("Do you go to number three Chairea street or continue investigating?")
                                    choice = input("Type 'c' to continue investigating or 'g' to go to number three Chairea street: ")
                                    if choice == 'g':
                                        print("You decide to go to number three Chairea street.")
                                        print("Luckily it is just around the corner from your house.")
                                        print("You arrive at three Chairea street, but the door is locked.")
                                        print("You see a riddle on the side of the door.")
                                        user_answer, answer = ask_math_riddle()
                                        if user_answer.lower() == answer:
                                            print("Correct!")
                                            print("The door unlocks.")
                                            print("You carefully open the door and peer inside.")
                                            print("You can see the robbers sitting at a table with all of your money.")
                                            print("You decide to create a distraction.")
                                            print("You can either set off a smoke bomb, set a dog on them, or start a fire.")
                                            choice = input("Type 's' to set off a smoke bomb, 'd' to set a dog on them and 'f' to start a fire: ")
                                            if choice == 's':
                                                print("You have to do some maths to work out the physics of where to throw the smoke bomb.")

                                else:
                                    print("Incorrect!")
                                    print("The door remains locked.")
                                    print("You have to try again.")

                        if choice == 'c':
                            print("You decide to continue investigating but you can't find anymore leads.")
                            print("You decide to go to number three Chairea street.")
                            print("Luckily it is just around the corner from your house.")
                            print("You arrive at three Chairea street, but the door is locked.")
                            print("You see a riddle on the side of the door.")
                            print("The code to unlock the door is the answer to the riddle.")
                            user_answer, answer = ask_math_riddle()
                            if user_answer.lower() == answer:
                                print("Correct!")
                                print("The door unlocks.")
                                print("You carefully open the door and peer inside.")
                                print("You can see the robbers sitting at a table with all of your money.")
                                print("You decide to create a distraction.")
                                print("You can either set off a smoke bomb, set a dog on them, or start a fire.")
                                choice = input("Type 's' to set off a smoke bomb, 'd' to set a dog on them and 'f' to start a fire: ")
                                if choice == 'f':
                                    print("You have to do some maths to work out the where to start the fire.")
                                    user_answer, answer = ask_math_question()
                                    if user_answer == answer:
                                        print("Correct!")
                                        print("You start the fire and the robbers run away.")
                                        print("You run and grab the money and get away with it.")
                                        print("You put the money safely in the bank.")
                                    else:
                                        print("Incorrect. The correct answer is:", answer)

                                    if choice == 'd':
                                        print("You have to do some maths to work out where to let go of the dog.")
                                        user_answer = int(input("Your answer: "))
                                        if user_answer == answer:
                                            print("Correct!")
                                            print("You let go of the dog and the robbers run away.")
                                            print("You run and grab the money and get away with it.")
                                            print("You put the money safely in the bank.")
                                        else:
                                            print("Incorrect. The correct answer is:", answer)

                                    if choice == 's':
                                        print("You have to do some maths to work out where to throw the smoke bomb.")
                                        user_answer, answer = ask_math_question()
                                        if user_answer == answer:
                                            print("Correct!")
                                            print("You throw the smoke bomb, and the robbers run away thinking that it is the police.")
                                            print("You run and grab the money and get away with it.")
                                            print("You put the money safely in the bank.")
                                        else:
                                            print("Incorrect. The correct answer is:", answer)
                                            ask_math_question()
                                    ask_math_question()

                                else:
                                    print("Incorrect!")
                                print("The door remains locked.")
                                print("You have to try again.")


                    if choice == 'c':
                        print("You decide to take a closer look at the milkshake.")
                        print("You cannot find anything strange about the milkshake.")
                        print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                        print("The milkshake doesn't contain any poison, and the police show you an ultra-scan of yor mums heart.")
                        print("You realise that she did have a heart attack and decide that next time you should leave the investagating to the police.")

                    if choice == 's':
                        print("You look around the room and take in every detail.")
                        print("You notice a chocolate milkshakje on the table.")
                        print("You decide to take a closer look at the milkshake.")
                        print("You cannot find anything strange about the milkshake.")
                        print("Just to be sure, you take the milkshake to the police station to be tested for poison.")
                        print("They are busy with another case and make you leave.")
                        print("You decide to investigate yourself.")
                        print("You remember hearing someone say that they were going to number three Chairea street.")
                        print("You had thought you were dreaming at the time, but maybe it was someone talking about where they were taking the money.")
                        print("Do you go to number three Chairea street or continue investigating?")
                        choice = input("Type 'c' to continue investigating or 'g' to go to number three Chairea street: ")
                        if choice == 'g':
                            print("You decide to go to number three Chairea street.")
                            print("Luckily it is just around the corner from your house.")
                            print("You arrive at three Chairea street, but the door is locked.")
                            print("You see a riddle on the side of the door.")
                            print("The code to unlock the door is the answer to the riddle.")
                        # user_answer, answer = ask_math_riddle()
                        #     riddle = "If A+A+A=39 and B+B-A=25 and 6+C+B=50 then what does A+B+C=?"
                        #     answer = "57"
                        #     user_answer = input(f"{riddle} ")
                        #     if user_answer.lower() == answer:
                        #         print("Correct!")
                        #         print("The door unlocks.")
                        #         print("You carefully open the door and peer inside.")
                        #         print("You can see the robbers sitting at a table with all of your money.")
                        #         print("You decide to create a distraction.")
                        #         print("You can either set off a smoke bomb, set a dog on them, or start a fire.")
                        #         choice = input("Type 's' to set off a smoke bomb, 'd' to set a dog on them and 'f' to start a fire: ")
                        #         if choice == 's':
                        #             print("You have to do some maths to work out the physics of where to throw the smoke bomb.")
                        #             def generate_math_question():
                        #                 operators = ['+', '-', '*', '/']
                        #                 num1 = random.randint(1, 10)
                        #                 num2 = random.randint(1, 10)
                        #                 operator = random.choice(operators)
                        #                 question = f"What is {num1} {operator} {num2}? "
                        #                 return question


                        #             def ask_math_question():
                        #                 question = generate_math_question()
                        #                 print(question)
                        #                 answer = eval(question)
                        #                 user_answer = int(input("Your answer: "))
                        #                 if user_answer == answer:
                        #                     print("Correct!")
                        #                     print("You throw the smoke bomb, and the robbers run away thinking that it is the police.")
                        #                     print("You run and grab the money and get away with it.")
                        #                     print("You put the money safely in the bank.")
                        #                 else:
                        #                     print("Incorrect. The correct answer is:", answer)
                        #                 ask_math_question()

                        #     else:
                        #         print("Incorrect!")
                        #         print("The door remains locked.")
                        #         print("You have to try again.")
                        #         ask_math_riddle()
                        # ask_math_riddle()
                        # if choice == 'c':
                        #     print("You decide to continue investigating but you can't find anymore leads.")
                        #     print("You decide to go to number three Chairea street.")
                        #     print("Luckily it is just around the corner from your house.")
                        #     print("You arrive at three Chairea street, but the door is locked.")
                        #     print("You see a riddle on the side of the door.")
                        #     print("The code to unlock the door is the answer to the riddle.")
                        # user_answer, answer = ask_math_riddle()
                        #     riddle = "If A+A+A=39 and B+B-A=25 and 6+C+B=50 then what does A+B+C=?"
                        #     answer = "57"
                        #     user_answer = input(f"{riddle} ")
                        #     if user_answer.lower() == answer:
                        #         print("Correct!")
                        #         print("The door unlocks.")
                        #         print("You carefully open the door and peer inside.")
                        #         print("You can see the robbers sitting at a table with all of your money.")
                        #         print("You decide to create a distraction.")
                        #         print("You can either set off a smoke bomb, set a dog on them, or start a fire.")
                        #         choice = input("Type 's' to set off a smoke bomb, 'd' to set a dog on them and 'f' to start a fire: ")
                        #         if choice == 'f':
                        #             print("You have to do some maths to work out the where to start the fire.")
                        #             def generate_math_question():
                        #                 operators = ['+', '-', '*', '/']
                        #                 num1 = random.randint(1, 10)
                        #                 num2 = random.randint(1, 10)
                        #                 operator = random.choice(operators)
                        #                 question = f"What is {num1} {operator} {num2}? "
                        #                 return question
                        #             def ask_math_question():
                        #                 question = generate_math_question()
                        #                 print(question)
                        #                 answer = eval(question)
                        #                 user_answer = int(input("Your answer: "))
                        #                 if user_answer == answer:
                        #                     print("Correct!")
                        #                     print("You start the fire and the robbers run away.")
                        #                     print("You run and grab the money and get away with it.")
                        #                     print("You put the money safely in the bank.")
                        #                 else:
                        #                     print("Incorrect. The correct answer is:", answer)
                        #                 ask_math_question()
                        #             ask_math_question()
                        #         if choice == 'd':
                        #             print("You have to do some maths to work out where to let go of the dog.")
                        #             def generate_math_question():
                        #                 operators = ['+', '-', '*', '/']
                        #                 num1 = random.randint(1, 10)
                        #                 num2 = random.randint(1, 10)
                        #                 operator = random.choice(operators)
                        #                 question = f"What is {num1} {operator} {num2}? "
                        #             def ask_math_question():
                        #                 question = generate_math_question()
                        #                 print(question)
                        #                 answer = eval(question)
                        #                 user_answer = int(input("Your answer: "))
                        #                 if user_answer == answer:
                        #                     print("Correct!")
                        #                     print("You let go of the dog and the robbers run away.")
                        #                     print("You run and grab the money and get away with it.")
                        #                     print("You put the money safely in the bank.")
                        #                 else:
                        #                     print("Incorrect. The correct answer is:", answer)


                        #         if choice == 's':
                        #             print("You have to do some maths to work out where to throw the smoke bomb.")
                        #             def generate_math_question():
                        #                 operators = ['+', '-', '*', '/']
                        #                 num1 = random.randint(1, 10)
                        #                 num2 = random.randint(1, 10)
                        #                 operator = random.choice(operators)
                        #                 question = f"What is {num1} {operator} {num2}? "
                        #                 return question
                        #             def ask_math_question():
                        #                 question = generate_math_question()
                        #                 print(question)
                        #                 answer = eval(question)
                        #                 user_answer = int(input("Your answer: "))
                        #                 if user_answer == answer:
                        #                     print("Correct!")
                        #                     print("You throw the smoke bomb, and the robbers run away thinking that it is the police.")
                        #                     print("You run and grab the money and get away with it.")
                        #                     print("You put the money safely in the bank.")
                        #                 else:
                        #                     print("Incorrect. The correct answer is:", answer)
                        #                 ask_math_question()


                        #     else:
                        #         print("Incorrect!")
                        #         print("The door remains locked.")
                        #         print("You have to try again.")
                        #         ask_math_riddle()

    else:
        print("Okay, come back when you are ready.")

def main():
    game_start()

if __name__ == "__main__":
    main()
