import time
import os

def verify_time(isHour):
    while True:
        
        try:
            time_input = int(input())
        except ValueError:
            print("Please enter a number")
            continue

        if time_input < 0:
            print("Time cannot be negative")
            continue

        if isHour:
            return time_input
        else:
            if time_input < 60:
                return time_input
            print("Value must be between 0 and 59")



def main():
    print("WELCOME TO COUNTDOWN CLOCK")
    print("Enter hours (unlimited): ", end="")
    hour = verify_time(True)
    print("Enter minutes (0-59): ",  end="")
    minute = verify_time(False)
    print("Enter seconds (0-59): ", end="")
    second = verify_time(False)

    for h in reversed(range (hour+1)):
        for m in reversed(range (minute+1)):
            for s in reversed(range (second+1)):
                print(f"Remaining time: {h:02}:{m:02}:{s:02}")
                time.sleep(1)
                os.system("clear")
            second = 59 
        minute = 59
    print("BEEPPPPPPPPPP")


if __name__ == "__main__":
    main()