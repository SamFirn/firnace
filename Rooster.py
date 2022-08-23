import time

def tick():

    ticking = 0
    tocking = 0
    roost = 0

    while True:
        ticking += 1
        print(f"{roost}:{tocking}:{ticking}")
        time.sleep(1)
        if ticking == 59:
            ticking = 0
            tocking += 1
            if tocking == 59:
                tocking = 0
                roost += 1
                if roost == 1:
                    break
                    

tick()