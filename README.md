# mach_eight_test

You can run this code by opening a terminal or command prompt located where you cloned the repo
and executing:
- **python main.py** if you are on Windows
- **python3 main.py** if you are on Linux or Mac.
You can run the unit test by execution **pytest -v** in the same directory. If you don't have Pytest
installed, you can run "pip install pytest".

You can add/modify the input array and target in the **input.txt** file. Just be sure to validate that the
target parameter is separated by two spaces ("  ") from the array.

The complexity I could achieve is **O(n)** as the most complex task in the "sums" function is to execute
the addition of every element in the input array, **O(1)**, int the dictionary **n** times. After that looking
for any posible solution will be just **O(1)**.