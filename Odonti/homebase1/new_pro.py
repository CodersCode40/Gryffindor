from time import sleep

def traffic_light():
    for i in range(10):
        print("stop")
        print("Red")
        sleep(5)
        
        print("Get Ready")
        print("Yellow")
        sleep(5)

        print("Go")
        print("Green")
        sleep(7)

traffic_light()