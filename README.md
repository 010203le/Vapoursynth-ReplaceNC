## ReplaceNC

based on AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames)

A quickly replace the OP/ED of the TV anime with the NC (non-credit) version's script.

## Usage

You can use getframe.py to input a chapter file first to see if the frame range is as expected.

Current version is stupid. It will not judge whether there is a OP/ED in one episode, and it may replace NC to the wrong place. Be sure to check whether the output results meet expectations.

```py
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
clip = rnc.ReplaceNC(clip, ncop, mode='op', chapter='C:\...\chapter.txt')
clip = rnc.ReplaceNC(clip, nced, mode='ed', chapter='C:\...\chapter.txt')
```

