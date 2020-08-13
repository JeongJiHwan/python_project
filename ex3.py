import sys
import os

src = sys.argv[1]
dst = sys.argv[2]

if not os.path.exists(src):
    print('%s does not exist' %src)
else:
    fr = open(src, 'r')
    fw = open(dst, 'w')
    
    for line in fr:
        fw.write(line)
        
    fr.close()
    fw.close()
