from fizzbuzz import FizzBuzz
import threading

def main():
    # Create original instance to work on
    fizzbuzz_list = FizzBuzz(16)
    # Create threads
    thread_A = threading.Thread(target= fizzbuzz_list.number)
    thread_B = threading.Thread(target= fizzbuzz_list.fizzbuzz, args= (3, 5))
    thread_C = threading.Thread(target= fizzbuzz_list.fizz, args= (3,))
    thread_D = threading.Thread(target= fizzbuzz_list.buzz, args= (5,))
    

    # Start the threads
    
    thread_A.start()
    thread_B.start()
    thread_C.start()
    thread_D.start()

    # Join the threads
    thread_A.join()
    thread_B.join()
    thread_C.join()
    thread_D.join()

    print(fizzbuzz_list.string_list)


if __name__ == "__main__":
    main()
