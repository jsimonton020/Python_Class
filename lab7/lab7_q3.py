from time import time


class Stop_Watch:

    # contructor initializes start time
    def __init__(self):
        self.__start_time = time()

    # method for returning start time
    def get_start_time(self):
        return self.__start_time

    # method for returning end time
    def get_end_time(self):
        return self.__end_time

    # method to reset start time
    def start(self):
        self.__start_time = time()

    # method to set the end time, also creates attribute here
    def stop(self):
        self.__end_time = time()

    # method to return elapsed time in milliseconds
    def get_elapsed_time(self):
        return (self.__end_time - self.__start_time) * 1000


def main():
    # instatiate the watch object
    watch = Stop_Watch()
    # set sum to zero and start the timer
    sum = 0
    watch.start()
    # calulate 1 to 1000000
    for i in range(1, 1000001):
        sum += i
    # stop the timer
    watch.stop()
    # print the time
    print(watch.get_elapsed_time(), "miliseconds passed adding 1 to 1000000")


main()

'''
44.6009635925293 miliseconds passed adding 1 to 1000000
'''
