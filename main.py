## Simple Lossless String Compression ##

import compression

phrase = "to be or not to be, that is the question"
compressed, key = compression.compress(phrase)

def utf8len(s):
  return len(s.encode('utf-8'))

def dictStringBytes(dictString):
  sum = 0 
  for v in dictString:
    sum += utf8len(v)
  return sum

print("Uncompressed: " + phrase)
print("Compressed: " + compressed)
print("Bytes before compression: %s, Bytes after compression: %s"%(utf8len(phrase), utf8len(compressed)+dictStringBytes(key)))
