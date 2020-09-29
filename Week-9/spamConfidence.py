# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
floatValue = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    floatValue = float(line[line.find('0'): ]) + floatValue
    count = count + 1
print('Average spam confidence:', floatValue / count)
