
def timeToFrame(time):
    time = time.split(":")
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2].split(".")[0])
    milliseconds = int(time[2].split(".")[1])
    frame = (hours * 60 * 60 * 23.976) + (minutes * 60 * 23.976) + (seconds * 23.976) + (milliseconds * 23.976 / 1000)
    #無條件捨去小數點後的數字(從0開始計算)。
    return int(frame)

def main():
    time = input("input time: ")
    end  = input("input end time: ")
    during = timeToFrame(end) - timeToFrame(time)
    print('"['+str(timeToFrame(time))+' '+str(timeToFrame(end))+ ']"'+ 'during : ' + str(during))
    exit()

main()

'''
00:00:00.000                             : en:Chapter 01
00:01:30.007                             : en:Chapter 02
00:08:41.980                             : en:Chapter 03
00:17:06.984                             : en:Chapter 04
00:22:29.974                             : en:Chapter 05
clip = fvf.ReplaceNC(clip, ncop, mappings="[0 2157]")
clip = fvf.ReplaceNC(clip, nced, mappings="[32366 34523]")
'''