import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abdeepak/CodingChallenges/merge_arrays/ros2_ws/install/merge_arrays'
