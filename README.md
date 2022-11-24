正在研究一個快速替換掉正片OP/ED為nc版本的方案
可以省下對OP/ED mask credit的時間 (x

based on AviSynth's ReplaceFramesSimple (http://avisynth.nl/index.php/RemapFrames)

usage

import lolifunc as lolic
clip = lolic.ReplaceNC(clip,ncop,mappings=[0 2157])
clip = lolic.ReplaceNC(clip,nced,mappings=[32608 34765])

