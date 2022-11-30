def getFrameRange(chapterFile, mode):
    try:
        with open(chapterFile, 'r') as f:
            chapters = f.readlines()
            chapters = chapters[0::2]
            chapters = [x.strip() for x in chapters]
            chapters = [x.split("=") for x in chapters]
            chapters = {x[0]:x[1] for x in chapters}
    except:
        raise ValueError('ReplaceNC: chapter file is not correct!')

    try:
        for chapter in chapters:
            chapters[chapter] = timeToFrame(chapters[chapter])
    except:
        raise ValueError('ReplaceNC: chapter file\'s format is not correct!')

    cf = list(chapters.values())
    opt = []

    for i in range(len(cf)):
        try:
            if cf[i+1] - cf[i] < 2160:
                if cf[i+1] - cf[i] > 2154:
                    opt.append('['+str(cf[i])+' '+str(cf[i+1])+']')
        except:
            opt.append('['+str(cf[i])+' '+str(cf[i]+2157)+']')
    
    if mode == 'op':
        return opt[0]
    elif mode == 'ed':
        try:
            return opt[1]
        except:
            raise TypeError('ReplaceNC: This clip must not have op or ed!')
    elif mode == 'all':
        return opt[0] + ' ' + opt[1]
    else:
        raise ValueError('ReplaceNC: mode is wrong!')


def timeToFrame(time):
    time = time.split(":")
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2].split(".")[0])
    milliseconds = int(time[2].split(".")[1])
    frame = (hours * 60 * 60 * 23.976) + (minutes * 60 * 23.976) + (seconds * 23.976) + (milliseconds * 23.976 / 1000)
    #frames count from 0
    return int(frame)


#load chapter file
chapterFile = input('Input chapter file path(.txt) : ') 

print(getFrameRange(chapterFile, 'all'))
