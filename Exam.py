# 3 - masala

import threading
import time

def print_numbers():
    for i in range(1,14):
        time.sleep(1)
        print(f'Son: {i}')

def print_letters():
    letters = "ABCDEFGHIJKLMNO"
    for i in letters:
        time.sleep(1)
        print(f'Harf: {i}')

def main():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()