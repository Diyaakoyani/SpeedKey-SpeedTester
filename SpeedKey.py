from time import time 
def accuracy(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors+=1
        else:
            if inwords[i]==words[i]:
                if(inwords[i+1] == words[i+1]) and (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors+=1
            else:
                errors+=1
    return errors

def speed(inprompt,stime,etime):
    global time_
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = (twords/time_)*60

    return speed

def elapsedtime(stime,etime):
    time_ = etime - stime 
    return time_

if __name__ == "__main__":
    prompt = "Computer science (CS) is the study of computers and algorithmic processes."
    print("type the below paragraph:")
    print(prompt)

    input("Press Enter when you are ready to check your speed!!!!!")

    stime = time()
    inprompt = input()
    etime = time()
    time_ = round(elapsedtime(stime,etime),2)
    speed_ = speed(inprompt,stime,etime)
    errors = accuracy(prompt)
    print("Total time elapsed = ", time_, "seconds")
    print("Average Typing Speed = ", speed_, "wpm")
    print("errors = ", errors)