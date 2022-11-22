import re
import vapoursynth as vs

def ReplaceNC(clipa, clipb, mappings=None, filename=None):
    #B替代A , A是片 , B是NC , mapping是A的op or ed範圍

    if not isinstance(clipa, vs.VideoNode):
        raise TypeError('ReplaceFrames: "clipa" must be a clip!')
    if not isinstance(clipb, vs.VideoNode):
        raise TypeError('ReplaceFrames: "clipb" must be a clip!')
    if clipa.format.id != clipb.format.id:
        raise TypeError('ReplaceFrames: "clipa" and "clipb" must have the same format!')
    if filename is not None and not isinstance(filename, str):
        raise TypeError('ReplaceFrames: "filename" must be a string!')
    if mappings is not None and not isinstance(mappings, str):
        raise TypeError('ReplaceFrames: "mappings" must be a string!')
    if mappings is None:
        mappings = ''

    if filename:
        with open(filename, 'r') as mf:
            mappings += '\n{}'.format(mf.read())
    # Some people used this as separators and wondered why it wasn't working
    mappings = mappings.replace(',', ' ').replace(':', ' ')

    frames = re.findall('\d+(?!\d*\s*\d*\s*\d*\])', mappings)
    ranges = re.findall('\[\s*\d+\s+\d+\s*\]', mappings)
    maps = []
    for range_ in ranges:
        maps.append([int(x) for x in range_.strip('[ ]').split()])
    for frame in frames:
        maps.append([int(frame), int(frame)])

    for start, end in maps:
        if start > end:
            raise ValueError('ReplaceFrames: Start frame is bigger than end frame: [{} {}]'.format(start, end))
        if end >= clipa.num_frames or end >= clipb.num_frames+start:
            raise ValueError('ReplaceFrames: End frame too big, one of the clips has less frames: {}'.format(end)) 

    out = clipa
    for start, end in maps:
        temp = clipb[0:end+1-start] 
        if start != 0:
            temp = out[:start] + temp
        if end < out.num_frames - 1:
            temp = temp + out[end+1:]
        out = temp
    return out
