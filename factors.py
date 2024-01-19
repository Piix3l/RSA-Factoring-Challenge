#!/usr/bin/python3

import time
start_time = time.time()
# -----------------------------------------------------------------------------
import sys

if len(sys.argv) != 2:
    print('expected 1 argument got 0')
else:
    # Open the file in read mode
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Process each line as needed
            a = line.strip()
            number = int(a)
            for i in range(2, int(line)):
                if number % i == 0:
                    ans = i
                    print(f"{number}={int(number/i)}*{i}")
                    break
# -----------------------------------------------------------------------------
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.4f} seconds")
