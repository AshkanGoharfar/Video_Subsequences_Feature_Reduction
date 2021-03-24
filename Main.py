import sys

from Operators import *

output = reduce_feature('skeleton', 'video', 'auto')
# output = reduce_feature('skeleton', 'video', 'non-automatic')
# output = reduce_feature('skeleton', 'camera', 'auto')
# output = reduce_feature('skeleton', 'camera', 'non-automatic')
# output = reduce_feature('hls', 'video', 'non-automatic')
# output = reduce_feature('hls', 'video', 'auto')
# output = reduce_feature('hls', 'camera', 'auto')
# output = reduce_feature('hls', 'camera', 'non-automatic')

# Store hls value of all pixels for all frames in a text file
with open('Output/Video_Sequences.txt', 'w') as filehandle:
    counter = 0
    for listitem in output:
        filehandle.write('Frame %s\n' % str(counter))
        filehandle.write('%s\n' % str(listitem))
        counter += 1

sys_argv = sys.argv
reduce_feature(sys_argv[1], sys_argv[2], sys_argv[3])
