import pytchat
import sys

data = []

with open("filter.txt", encoding='utf-8') as f:
    for line in f:
        data.append(line.split())
data = sum(data, [])


print(data)
