import sys

xmfa = open(sys.argv[1]).read().split(">")

Sequence = []
name = []

for i in xmfa:
    if len(i) != 0:
        name.append(i[i.index("+") + 2:i.index("\n")])
        Sequence.append(i[i.index("\n"):].replace("=","").replace("-","").replace("\n",""))

fasta = open(sys.argv[2],"w")


i = 0
for seq in Sequence:
    if len(seq) > 10 and (seq.upper().count("A") + seq.upper().count("T")+ seq.upper().count("C")+ seq.upper().count("G")) != len(seq):
        fasta.write(">" + name[i] + "\n" + seq + "\n")
    i = i + 1
fasta.close()
