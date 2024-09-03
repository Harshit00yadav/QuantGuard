from time import sleep


def render_frame(frame):
    for row in frame.split("\n"):
        for col in row:
            if col == "B":
                # █
                print("\u2588", end="")
            elif col == "1":
                # 
                print("\ue0ba", end="")
            elif col == "2":
                # 
                print("\ue0b8", end="")
            elif col == "3":
                # 
                print("\ue0bc", end="")
            elif col == "4":
                # 
                print("\ue0be", end="")
            elif col == " ":
                print(" ", end="")
            else:
                try:
                    if col.islower():
                        print(col.upper(), end="")
                except:
                    pass
        print()

def animate():
    frames = "" 
    with open("assets/loadinglogo.txt", "r") as f:
        frames = "".join(f.readlines()).split("@frame")
    metadata = frames[0].split(";")
    print("\033[?25l", end="")
    i = 1
    while i <= int(metadata[0]):
        render_frame(frames[i])
        sleep(0.3)
        i += 1
        print(f"\033[{int(metadata[1])+2}A", end="")
    print("\033[?25h", end="")

