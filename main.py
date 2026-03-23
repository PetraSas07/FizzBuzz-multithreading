from fizzbuzz import FizzBuzz
import threading

def fizzbuzz_logic(fizzbuzz_list, first_number, second_number):
    multiplied = first_number * second_number
    for i in range(fizzbuzz_list.size):
        print("number:", i)
        if ((i + 1) % multiplied) == 0:
            fizzbuzz_list.event_fb.set()
            while fizzbuzz_list.event_fb.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        elif ((i + 1) % first_number) == 0:
            fizzbuzz_list.event_f.set()
            while fizzbuzz_list.event_f.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        elif ((i + 1) % second_number) == 0:
            fizzbuzz_list.event_b.set()
            while fizzbuzz_list.event_b.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
        else:
            fizzbuzz_list.event_n.set()
            while fizzbuzz_list.event_n.is_set():
                print("waiting for main")
                fizzbuzz_list.event_main.wait()
    print("out from for loop")

def main():
    fizzbuzz_list = FizzBuzz(30)
    first_number = 3
    second_number = 5

    threads = []
    thread_A = threading.Thread(target= fizzbuzz_list.number)
    threads.append(thread_A)
    thread_B = threading.Thread(target= fizzbuzz_list.fizzbuzz)
    threads.append(thread_B)
    thread_C = threading.Thread(target= fizzbuzz_list.fizz)
    threads.append(thread_C)
    thread_D = threading.Thread(target= fizzbuzz_list.buzz)
    threads.append(thread_D)
    
    for thread in threads:
        thread.start()

    # Fizzbuzz logic with thread events
    print("Threads started")
    fizzbuzz_logic(fizzbuzz_list, first_number, second_number)

    # Clearing the fizzbuzz method while loop waits
    for event in fizzbuzz_list.event_list:
        event.set()
    print("after main clears")

    for thread in threads:
        thread.join()
    print("after the main joins")
    print(fizzbuzz_list.string_list)


if __name__ == "__main__":
    main()
