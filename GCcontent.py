DNA = input("Enter DNA sequence:")
DNA_cap = DNA.upper() #all letters uppercase
seqlen = len(DNA)
Gcontent = DNA_cap.count("G")
Ccontent = DNA_cap.count("C")
GC = Gcontent + Ccontent
GCperc = GC / seqlen * 100
print("GC Percent:" + str("%.2f" % round(GCperc,2)) + "%") #Float limited to 2 decimals
