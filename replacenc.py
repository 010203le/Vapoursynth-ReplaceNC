import re
import vapoursynth as vs

def ReplaceNC(clipa, clipb, mode=None, chapter=''):
    #based on AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames)
    #clipb replace clipa, clipb is ncop or nced, modes:op,ed, chapter:chapter file(.txt)

    if not isinstance(clipa, vs.VideoNode):
        raise TypeError('ReplaceNC: "clipa" must be a clip!')
    if not isinstance(clipb, vs.VideoNode):
        raise TypeError('ReplaceNC: "clipb" must be a clip!')
    if clipa.format.id != clipb.format.id:
        raise TypeError('ReplaceNC: "clipa" and "clipb" must have the same format!')

    mappings = getFrameRange(chapter, mode)

    frames = re.findall('\d+(?!\d*\s*\d*\s*\d*\])', mappings)
    ranges = re.findall('\[\s*\d+\s+\d+\s*\]', mappings)
    maps = []
    for range_ in ranges:
        maps.append([int(x) for x in range_.strip('[ ]').split()])
    for frame in frames:
        maps.append([int(frame), int(frame)])

    for start, end in maps:
        if start > end:
            raise ValueError('ReplaceNC: Start frame is bigger than end frame: [{} {}]'.format(start, end))
        if end >= clipa.num_frames or end >= clipb.num_frames+start:
            raise ValueError('ReplaceNC: End frame too big, one of the clips has less frames: {}'.format(end)) 

    out = clipa
    for start, end in maps:
        temp = clipb[0:end+1-start] 
        if start != 0:
            temp = out[:start] + temp
        if end < out.num_frames - 1:
            temp = temp + out[end+1:]
        out = temp
    return out

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
                    opt.append(str('['+str(cf[i])+' '+str(cf[i+1])+']'))
        except:
            opt.append(str('['+str(cf[i])+' '+str(cf[i]+2157)+']'))
    
    if mode == 'op':
        return opt[0]
    elif mode == 'ed':
        try:
            return opt[1]
        except:
            raise TypeError('ReplaceNC: This clip must not have op or ed!')
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
