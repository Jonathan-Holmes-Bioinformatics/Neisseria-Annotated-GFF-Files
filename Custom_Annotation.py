import sys


Default = open(sys.argv[1]).read().split("\n")
Annot = open(sys.argv[2]).read().split("\n")

annotation_terms = []
for i in Annot:
    if "NEIS" in i:
        I = i.split("\t")
        start = i.index("fasta:")
        end = i.index(";locus")
        NEIS = (i[start + len("fasta:"):end])
        annotation_terms.append([I[3],I[4],NEIS])


data_frame = []
for i in Default:
    if "product" in i:
        site = i.index(";product")
        I = i.split("\t")
        coord1 = I[3]
        coord2 = I[4]
        l = 0
        for A in annotation_terms:
            if coord1 == A[0] and coord2 == A[1]:
                new_line = i[:site] + ";note=Equivalent NEIS number is = " + A[2] + i[site:]
                data_frame.append(new_line)
                l = l + 1
        if l == 0:
            data_frame.append(i)
    else:
        data_frame.append(i)



new_file = open(sys.argv[3],"w")
for i in data_frame:
    new_file.write(i + "\n")
new_file.close()





