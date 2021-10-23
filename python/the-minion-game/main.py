
if __name__ == "__main__":
    word = input()
    #word = "BANANA"
    vowels = "AEIOU"
    count = {"Stuart":0, "Kevin":0}
    for i in range(len(word)):
        if word[i] in vowels:
            count["Kevin"] += len(word)-i
        else:
            count["Stuart"] += len(word)-i
    
    if count["Stuart"] > count["Kevin"]:
        print(f"Stuart {count['Stuart']}")
    elif count["Kevin"] > count["Stuart"]:
        print(f"Kevin {count['Kevin']}")
    else:
        print("Draw")


