import time
# i.sleep () this are seconds

my_time = int(input('write the time in seconds: '))
my_time += 1

for x in reversed(range(0 ,my_time)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print('Time is up')
print('\n')





# count numbers straight
for x in range(0, my_time):
    print(x)
    time.sleep(1)
print('Time is up')
print('\n')

#count numbers backgrounds, method 1
for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)
print('Time is up')
print('\n')

#count numbers backgrounds, method 2
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)
print('Time is up')
print('\n')



