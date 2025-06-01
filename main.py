score = int(input("Enter them score: "))

with open("file.txt") as f:
    highscore = f.read()

    if highscore == "": 
        highscore = 0
    else: 
        highscore = int(highscore)
    
# only file opening and closing related kaam with mai karna hoga

if highscore < score: 
    highscore = score
    with open("file.txt","w") as f:
        f.write(str(score))
     
    # so the score would be written 

else: 
    print("No highscore")

print(f"The score is {score}")
print(f"The highscore is {highscore}")
