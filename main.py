from multiprocessing import Process, Value, Array, Lock, Semaphore, current_process
from pathlib import Path
from random import randint
import sys

class CreateImage(Process):
    def __init__(self, directory, num_process:int, width:int, heigth:int, px_red, px_green, px_blue, lock):
        super().__init__()
        self._directory = directory
        self._num_process = num_process
        self._width = width
        self._heigth = heigth
        self._px_red = px_red
        self._px_green = px_green
        self._px_blue = px_blue
        self._lock = lock


    def run(self):
        print(f"[Hijo {self._num_process}]          Creando imagen {self._width}x{self._heigth}px")
        
        with open(f"p{self._num_process}.ppm","w") as fw:
            fw.write(f"P3\n{self._width} {self._heigth}\n255\n")
            total_pixel = self._heigth*self._width

            for _ in range(total_pixel):
                rand_px_red = randint(0,255)
                rand_px_green = randint(0,255)
                rand_px_blue = randint(0,255)

                while not isPrimo(rand_px_red):
                    rand_px_red = randint(0,255)
                
                while not isPrimo(rand_px_green):
                    rand_px_green = randint(0,255)
                
                while not isPrimo(rand_px_blue):
                    rand_px_blue = randint(0,255)

                fw.write(f"{rand_px_red} {rand_px_green} {rand_px_blue}\n")

                with self._lock:
                    self._px_red.value = int((rand_px_red + self._px_red.value) / 2)
                    self._px_green.value = int((rand_px_green + self._px_green.value) / 2)
                    self._px_blue.value = int((rand_px_blue + self._px_blue.value) / 2)


def isPrimo(num:int):
    counter = 2
    if num <= 2:
        return False
    while num > counter:
        if num % counter == 0:
            return False
        counter += 1
    return True


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: main.py <count> <width> <height>\nParameters:\n- <count>: The total number of images to generate.\n- <width>: The width of each generated image in pixels.\n- <height>: The height of each generated image in pixels.")
        exit(1)

    px_red = Value("i",0)
    px_green = Value("i",0)
    px_blue = Value("i",0)
    lock = Lock()
    dictory = Path("./")

    processes = [CreateImage(dictory, (i + 1), int(sys.argv[2]), int(sys.argv[3]), px_red, px_green, px_blue, lock) for i in range((int(sys.argv[1])))]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"[PADRE] Media pixeles RGB:\n       R = {px_red.value}\n       G = {px_green.value}\n       B = {px_blue.value}")
