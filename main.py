from ago import human
from datetime import datetime
from datetime import timedelta

n = input("n = ")
t = input("t = ")
z = input("z = ")

start_time = datetime.now()

for i in range(t):
    if i == 0:
        w = 2
    if i % 30000 == 0:
        time_passed = datetime.now() - start_time
        if time_passed.seconds > 0:
            speed = i / time_passed.seconds
            time_remains = timedelta(seconds=(t - i)/speed)
            percent = "{:.5f}".format((i/t)*100)
            print(f"Progress: {percent}%", end='\t')
            print(f"(block {i} of {t})", end='\t')
            print(f"({int(speed)} blocks/s)", end='\t')
            print(f"({human(time_passed, precision=1, past_tense='{} passed')})", end='\t')
            print(f"({human(time_remains, precision=1, past_tense ='{} remains')})", end='\n')
    w = w**2 % n
print(f"w = {w} (decimal)")
print(f"w = {hex(w)} (hex)")

print(f"z = {z} (decimal)")
print(f"z = {hex(z)} (hex)")

x = w ^ z
print(f"x = {x} (decimal)")
print(f"x = {hex(x)} (hex)")

x = x.to_bytes((x.bit_length()+7)//8, 'big')
print(f"x = {x} (string)")
