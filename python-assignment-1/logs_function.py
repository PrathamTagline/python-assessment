import datetime
def log_function_execution_time(fun):

    def wrapper():
        print("log function started")
        start_time = datetime.datetime.now()
        print(f"{start_time}")
        fun()
        end_time = datetime.datetime.now()
        print(f"{end_time}")
        print(f"total time = {end_time - start_time}")
        print("log fucntin end close")
    return wrapper

@log_function_execution_time
def logs():
    numberList = [number for number in range(100)]
    print(numberList)


logs()