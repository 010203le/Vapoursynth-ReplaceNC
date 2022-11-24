## ReplaceNC

based on AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames)

正在研究一個快速替換掉電視動畫的OP/ED為nc版本的方案

有rescale的話，可以省下對OP/ED mask credit的時間 (x


## usage

可以先使用getframe.py輸入一個章節檔案，查看結果是否符合預期。

目前版本很笨，不會判斷該集是否有OP/ED，需要自行確認，也有可能換錯地方，務必自行檢查輸出內容是否符合預期。

```
import replacenc as rnc

ncop = core.lsmas.LWLibavSource(r"C:\...\NCOP.mkv", threads=1)
nced = core.lsmas.LWLibavSource(r"C:\...\NCED.mkv", threads=1)
clip = rnc.ReplaceNC(clip, ncop, mode='op', chapter='C:\...\chapter.txt')
clip = rnc.ReplaceNC(clip, nced, mode='ed', chapter='C:\...\chapter.txt')
```

