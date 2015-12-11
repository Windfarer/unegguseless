d = open('lst.txt').read()
d = d.split()
print("["+",".join(['"{}"'.format(i.strip()) for i in d])+"]")
