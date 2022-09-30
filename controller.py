from listFile import listFile
from listRef import listRef
import sys
import json


argList=[*sys.argv]
argList.pop(0)
argList.pop(0)
res=eval(sys.argv[1])(*argList)
json_files = json.dumps(res,indent=4)
print(json_files)
sys.stdout.flush()