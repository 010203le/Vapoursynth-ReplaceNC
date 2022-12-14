[中文說明](https://github.com/010203le/Vapoursynth-ReplaceNC/blob/main/README_cht.md "中文說明")

## ReplaceNC

based on AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames)

A quickly replace the OP/ED of the TV anime with the NC (non-credit) version's script.

## Usage

You can use getframe.py to input a chapter file first to see if the frame range is as expected.

Current version is stupid. It will not judge whether there is a OP/ED in one episode, and it may replace NC to the wrong place. Be sure to check whether the output results meet expectations.

```py
#automatic positioning frame range
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
clip = rnc.ReplaceNC(clip, ncop, mode='op', chapter=r"C:\...\chapter.txt")
clip = rnc.ReplaceNC(clip, nced, mode='ed', chapter=r"C:\...\chapter.txt")
```

```py
#manual positioning frame range
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
#mappings=[OP/EDstartFrame OP/EDendFrame]
clip = rnc.ReplaceNC_manual(clip, ncop, mappings="[0 2157]")
clip = rnc.ReplaceNC_manual(clip, nced, mappings="[32608 34765]")
```
