"""convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py
"""
original = "annotation_investigator/song_instr.pkl"
destination = "annotation_investigator/song_instr_unix.pkl"

outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content) - outsize))
