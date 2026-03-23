This code is created to play around with the **fizzbuzz logic** with multithreading added into the mix.  

---

The code consists of two main files currently, one containing the Fizzbuzz class and the other is the main, where the logic is implemented, as well as the threading.  

## Fizzbuzz class file 

I chose to separate the logic from the fizzbuzz class to grant greater freedom with the provided numbers, this way the methods' only purpose is to add their own item to the fizzbuzz list, without ever interacting with the ordinal number, they are associated with. I wished to achieve as much separation as possible.  

To ensure the threads follow each other in order, I created one event for each method and another one for the main file's fizzbuzz logic.
- This was made, so while one method is working, others are in *wait*, not filling up the list, when it is not their turn.
- Additionally, the main fizzbuzz_logic event was added (which I will refer to as the main event from now on), so while one method is working, the main file's for loop is not acting ahead, but rather patiently waits for the method to finish, before it moves on.  

## Main file  

In the main file, I created a separate function which encompasses the fizzbuzz logic, where the for loop checks, which method should be called on the list. Then in the main function, separate threads are created for each method and started, so when I call the *fizzbuzz_logic* function, the threads are already in *wait*.

## Events and threading  

As I have mentioned, when you run the program, first the threads start and are blocked by the *wait*. This is when the fizzbuzz logic comes in and calls *set* on the method that comes next in the list. In the method, the *wait* is not blocking anymore, so if the list is not filled up to the maximum, the rigth item is appended, then the method *clears* it's own method event and after that signals *set* to the main event, so when the method's while loop continues, it gets stuck again in it's own wait, and the main *fizzbuzz_logic* can go on.

After the list is filled up and the for loop is finished in the main file, some of the methods are still in wait mode, where they got to before the list reached it's maximum size. Therefore, the next *set* call is there, so the methods can finish their last loop, where they are not appending the list, just exit the loop.

Lastly, when all of the above is done, all of the threads can join, terminating the program.

