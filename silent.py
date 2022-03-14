import pytchat
import sys

print("введи ID канала:")
stream = input()

param = ['тихо', 'тиш']
chat = pytchat.create(video_id=stream)
while chat.is_alive():
    for c in chat.get().sync_items():
        d = c.datetime
        a = c.author.name
        m = c.message
        if filter == "n":
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
        else:
            for element in param:
                if element in m:
                    print(d,[a],m)
