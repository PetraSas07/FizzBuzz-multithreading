from fizzbuzz import FizzBuzz
import threading
import time as t

def main():
    # Create original instance to work on
    fizzbuzz_list = FizzBuzz(16)

    # Create fizzbuzz numbers
    first_number = 3
    second_number = 5
    multiplied = first_number * second_number

    # Create threads and add them to a list
    thread_A = threading.Thread(target= fizzbuzz_list.number)
    thread_B = threading.Thread(target= fizzbuzz_list.fizzbuzz)
    thread_C = threading.Thread(target= fizzbuzz_list.fizz)
    thread_D = threading.Thread(target= fizzbuzz_list.buzz)
    

    # Start the threads
    thread_A.start()
    thread_B.start()
    thread_C.start()
    thread_D.start()

    print("Threads started")
    for i in range(fizzbuzz_list.size):
        print("number:", i)
        # t.sleep(1)
        if ((fizzbuzz_list.index + 1) % multiplied) == 0:
            fizzbuzz_list.event_fb.set()
            while fizzbuzz_list.event_fb.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        elif ((fizzbuzz_list.index + 1) % first_number) == 0:
            fizzbuzz_list.event_f.set()
            while fizzbuzz_list.event_f.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        elif ((fizzbuzz_list.index + 1) % second_number) == 0:
            fizzbuzz_list.event_b.set()
            while fizzbuzz_list.event_b.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        else:
            fizzbuzz_list.event_n.set()
            while fizzbuzz_list.event_n.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
    print("out from fro loop")

    fizzbuzz_list.event_b.set()
    fizzbuzz_list.event_f.set()
    fizzbuzz_list.event_fb.set()
    fizzbuzz_list.event_n.set()

    print("after main clears")

    # Join the threads
    thread_A.join()
    thread_B.join()
    thread_C.join()
    thread_D.join()

    print("after the main joins")
    print(fizzbuzz_list.string_list)


if __name__ == "__main__":
    main()
