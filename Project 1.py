score = 0

answer = input("Who is the current captain of the India cricket team? ")
if answer.lower() == "rohit sharma":
    print("Correct!")
    score += 1
else:
    print(f"The correct answer is 'Rohit Sharma', not {answer!r}")

answer = input("Which Indian player is known as the 'King Kohli'? ")
if answer.lower() == "virat kohli":
    print("Correct!")
    score += 1
else:
    print(f"The correct answer is 'Virat Kohli', not {answer!r}")

answer = input("Which stadium is also called the 'Home of Indian Cricket'? ")
if answer.lower() == "wankhede stadium" or answer.lower() == "wankhede":
    print("Correct!")
    score += 1
else:
    print(f"The correct answer is 'Wankhede Stadium', not {answer!r}")

answer = input("Who is the highest run scorer in ODI cricket for India? ")
if answer.lower() == "sachin tendulkar":
    print("Correct!")
    score += 1
else:
    print(f"The correct answer is 'Sachin Tendulkar', not {answer!r}")

answer = input("Which Indian bowler is known for his yorkers and death overs? ")
if answer.lower() == "jasprit bumrah":
    print("Correct!")
    score += 1
else:
    print(f"The correct answer is 'Jasprit Bumrah', not {answer!r}")

print(f"\nYour final score is {score}/5")