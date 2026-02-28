answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

clear_answer = answer.strip().lower()

if clear_answer == "42" or clear_answer == "forty two" or clear_answer == "forty-two":
    print("Yes")
else:
    print("No")