from time import sleep
from random import choice

class Logo:
    def __init__(self, path):
        self.logo_data = ""
        self.meta_data = ""
        with open(path, "r") as f:
            data = "".join(f.readlines()).split("@frame\n")
            self.logo_data = data[1].replace("\n","")
            self.meta_data = list(map(int, data[0].split(";")))
        self.canvas = [" " for _ in range(self.meta_data[0]*self.meta_data[1])]
        self.indexies_ = [i for i in range(self.meta_data[0]*self.meta_data[1])]

    def render_canvas(self):
        for i in range(self.meta_data[0]*self.meta_data[1]):
            # print(self.canvas[i], end="")
            if self.canvas[i] == "B":
                # █
                print("\u2588", end="")
            elif self.canvas[i] == "1":
                # 
                print("\ue0ba", end="")
            elif self.canvas[i] == "2":
                # 
                print("\ue0b8", end="")
            elif self.canvas[i] == "3":
                # 
                print("\ue0bc", end="")
            elif self.canvas[i] == "4":
                # 
                print("\ue0be", end="")
            elif not self.canvas[i].isalnum():
                print(self.canvas[i], end="")
            else:
                try:
                    if self.canvas[i].islower():
                        print(self.canvas[i].upper(), end="")
                except:
                    pass
            if (1+i) % (self.meta_data[0]) == 0:
                print()

    def blit_on_canvas(self, n):
        for _ in range(n):
            if self.indexies_ == []:
                break
            c = choice(self.indexies_)
            self.canvas[c] = self.logo_data[c]
            self.indexies_.remove(c)

    def clear_logo_downup(self):
        for _ in range(self.meta_data[0]):
            print("\r\033[2K\033[A", end="")

    def display(self):
        print("\033[?25l", end="")
        frames = 12
        for _ in range(frames):
            self.blit_on_canvas(self.meta_data[0]*self.meta_data[1]//frames)
            self.render_canvas()
            print(f"\r\033[{self.meta_data[0]}A", end="")
            sleep(0.1)
        self.blit_on_canvas(self.meta_data[0]*self.meta_data[1])
        self.render_canvas()
        sleep(1.5)
        print("\033[?25h", end="")
        self.clear_logo_downup()
