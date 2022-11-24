## ReplaceNC

以 AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames) 為基礎改寫

一個快速替換電視動畫的OP/ED為NC版本的腳本

## 使用方法

你可以使用 getframe.py 輸入章節文件，查看它輸出的幀範圍是否符合預期。

目前的版本很笨，不會判斷該集是否有常規的OP/ED，使用此腳本記得預覽被替換的位置，看看是否符合預期。

```py
#自動定位幀範圍
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
clip = rnc.ReplaceNC(clip, ncop, mode='op', chapter=r"C:\...\chapter.txt")
clip = rnc.ReplaceNC(clip, nced, mode='ed', chapter=r"C:\...\chapter.txt")
```

```py
#手動定位幀範圍
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
#mappings=[OP/ED起始幀 OP/ED結束幀]
clip = rnc.ReplaceNC_manual(clip, ncop, mappings=[0 2157])
clip = rnc.ReplaceNC_manual(clip, nced, mappings=[32608 34765])
```
