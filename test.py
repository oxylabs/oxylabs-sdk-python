from multiprocessing import Process
import time


def your_function():
    time.sleep(10)
    pass


if __name__ == "__main__":
    # Create a Process object
    p = Process(target=your_function)
    # Start the process
    p.start()
    # Wait for 5 seconds or until process finishes
    p.join(5)

    # If thread is still active
    if p.is_alive():
        print("Function is running... let's kill it...")
        # Terminate the process
        p.terminate()
        p.join()
