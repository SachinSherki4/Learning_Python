
import time
print("1. Delay Execution of code using sleep()")
print("Execution started!")
time.sleep(2)
print("This printed after 2 Seconds of time")
time.sleep(1.5)
print("This printed after 1.5 Seconds of time\n")

print("2. Calculating Program Execution time")
start_time=time.time()
a,b=12,34
print(a+b)
time.sleep(0.1)
end_time=time.time()
execution_time=end_time-start_time
print(f"Total Program execution time {execution_time-0.1} Seconds. \n")
