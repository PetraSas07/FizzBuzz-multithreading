from fizzbuzz import Fizzbuzz as F
import threading

def main():
    # Create original instance to work on
    line = F(16)
    # Create threads
    thread_A = threading.Thread(target= line.fizzbuzz, args= (4, 6))
    thread_B = threading.Thread(target= line.fizz, args= (4,))
    thread_C = threading.Thread(target= line.buzz, args= (6,))

    # Start the threads
    thread_A.start()
    thread_B.start()
    thread_C.start()

    # Join the threads
    thread_A.join()
    thread_B.join()
    thread_C.join()


if __name__ == "__main__":
    main()
