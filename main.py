import pytchat
import sys

# if __name__ == "__main__":
#     # for param in sys.argv:
#         # chat = pytchat.create(video_id=param)



print("введи ID канала:")
stream = input()
print("включить фильтр? [y/N] ")
filt = input()

# param = ['Бердянск', 'Николаев', 'Мариуполь', 'Киев', 'Запорож', 'Токмак', 'Мелитополь', 'Харьков', 'Днепр', 'тихо', 'тиш', 'бах', 'гром', 'сирен', 'тревога', 'взрыв', 'Львов', 'границ', 'самол', 'вертол', 'авиа','помо']
param = []
with open("filter.txt", encoding='utf-8') as filter:
    for line in filter:
        param.append(line.split())
param = sum(param, [])

chat = pytchat.create(video_id=stream)
while chat.is_alive():
    for c in chat.get().sync_items():
        d = c.datetime
        a = c.author.name
        m = c.message

        if filt == "n":
            log = open('log.txt', 'a', encoding='utf-8')
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            log.write(d + " [" + a + "] " + "\'" + m + "\'" + '\n')
            log.close()
        else:
            for element in param:
                if element in m:
                    log = open('log.txt', 'a', encoding='utf-8')
                    print(d,[a],m)
                    log.write(d + " [" + a + "] " + "\'" + m + "\'" + '\n')
                    log.close()
