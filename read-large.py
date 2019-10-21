import resource
import os

file_name = "./convertcsv.csv"

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name)

count = 0

for line in txt_file:
    count += 1

txt_file.close()

print(f'Number of Lines in the file is {count - 1}')

print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)
