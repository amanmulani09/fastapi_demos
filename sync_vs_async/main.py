import time
import asyncio

# def fetch_data():
#     time.sleep(2)  # pretend API call
#     return "Data fetched"

# print("Start") # Print Start
# result = fetch_data() # waits for 2 second 
# print(result) # print result 
# print("End") # print End 


# synchnous (line by line, waits until the current function execution ends(wait,db,i/o))



async def fetch_data():
    await asyncio.sleep(2)  # non-blocking sleep
    return "Data fetched"

async def main():
    print("Start")
    result = await fetch_data()
    print(result)
    print("End")

asyncio.run(main())
