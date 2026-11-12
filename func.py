
def player():
    health = 100
    print("bro this is player\n")
    for i in range(10):
        health -= 10
        print(health)
        print("OUCH\n")
    if health  < 10 :
        print("Player died")

def enemy():
    print("HAHAHA I DESTROY EVERYONE !!!!")
player()