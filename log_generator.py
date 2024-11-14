import datetime
import random

def reformat_time(number):
    if number < 60:
        return (0, number)
    else:
        minutes = 1
        seconds = number - 60
        while seconds > 60:
            minutes += 1
            seconds = seconds - 60
        return (minutes, seconds)


messages = [
    "paris olympics tickets prices",
    "www.google.com",
    "parks",
    "lets meet at the park",
    "it snowed so much this month",
    "hello world",
    "meet you at the catskills mountains",
    "my plants are dying",
    "how to water my plants",
    "snowproof boots",
    "nigerian solar cells",
    "loans for small business"
]
ip_adds = [
    "103.40.01",
    "109.100.70",
    "109.100.70",
    "109.100.70",
    "107.90.10",
    "109.70.10",
    "107.90.10",
    "121.70.10",
    "121.70.10",
    "107.90.40",
    "105.60.60",
    "105.60.60",
]

# group by ip
timestamp = 0
message_dictionaries = dict()
for i, m in enumerate(messages):
    print(i, m)
    m_i_ip = ip_adds[i]
    if m_i_ip not in message_dictionaries:
        message_dictionaries[m_i_ip] = [m]
    else:
        message_dictionaries[m_i_ip].append(m)

# generate lines in logs
lines = []
for key in message_dictionaries.keys():
    subset = message_dictionaries[key]
    time = random.randint(0, 20)  # randomize start time a bit
    for val in subset:
        for char in list(val):
            time += 1
            line = [key, char, time]
            lines.append(line)
        time += 30

# sort by time and reformat
sorted_lines = sorted(lines, key=lambda x: x[2])
formatted_lines = []
for l in sorted_lines:
    min, sec = reformat_time(l[2])
    formatted_line = str(f"{l[0]} {l[1]} 00:{min}:{sec}:{random.randint(10,60)}")
    formatted_lines.append(formatted_line)

with open("logs/logs_randomized.txt", "w") as f:
    for line in formatted_lines:
        print(line, file=f)



