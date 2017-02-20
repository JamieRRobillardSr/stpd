question = ""

me = { "height" : "5'10"
            , "color" : "purple"
            ,  "author" : "Robert A. Heinlin"
            ,  "name" : "Jamie R. Robillard" }

while question != "bye":
    question = input("Ask questions about me (help for assitance) : ")
    if question in me:
        print(question + " = " + me[question])
    elif question == "help":
        print("\nAvailable options:\n")
        print("name    -- prints my name.")
        print("author  -- prints my favorite author.")
        print("height  -- prints my height")
        print("color   -- prints my favorite color.")
        print("help    -- prints this help screen.")
        print("bye     -- Exits the program.")
    elif question != "bye":
        print("I do not know that answer")
    else:
        print("Bye!")
