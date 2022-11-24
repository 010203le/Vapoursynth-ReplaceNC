def timeToFrame(time):
    time = time.split(":")
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2].split(".")[0])
    milliseconds = int(time[2].split(".")[1])
    frame = (hours * 60 * 60 * 23.976) + (minutes * 60 * 23.976) + (seconds * 23.976) + (milliseconds * 23.976 / 1000)
    #無條件捨去小數點後的數字(從0開始計算)。
    return int(frame)

#load chapter file
with open("chapters.txt", "r") as f:
    chapters = f.readlines()
    chapters = chapters[0::2]
    chapters = [x.strip() for x in chapters]
    chapters = [x.split("=") for x in chapters]
    chapters = {x[0]:x[1] for x in chapters}

#計算影格數
for chapter in chapters:
    chapters[chapter] = timeToFrame(chapters[chapter])

cf = list(chapters.values())
opt = []
#保留間格符合條件項目
for i in range(len(cf)):
    try:
        if cf[i+1] - cf[i] < 2160:
            if cf[i+1] - cf[i] > 2154:
                opt.append(str('"['+str(cf[i])+' '+str(cf[i+1])+']"'))
    except:
        opt.append(str('"['+str(cf[i])+' '+str(cf[i]+2157)+']"'))


try:
    print(opt[0])
except:
    print('本集沒有OP/ED')

try:
    print(opt[1])
except:
    print('本集沒有OP or ED')


