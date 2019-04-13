from time import time

class Stop_Watch:

    def __init__(self):
        self.__start_time = time()
        self.__end_time = end_time

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time

    def start(self):
        self.__start_time = time()

    def stop(self):
        self.__end_time = time()

    def get_elapsed_time(self, start, stop):
        return round(stop - start * 1000)


def main():
    watch = Stop_Watch()
    start = watch.start()
    sum = 0
    for i in range(1, 1000001):
        sum = sum + i
    stop = watch.stop()
    elapsed = get_elapsed_time(start, stop)
    print("Time in milliseconds:", elapsed)

main()
