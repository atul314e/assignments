data = list(range(1200))

totalNums=len(data)
Iter=int(totalNums/500)+1 if int(totalNums/500)!=totalNums/500 else totalNums/500
start=0
end=500
chunks = [data[start+500*ite:end+500*ite] if end+500*ite<=totalNums else data[start+500*ite:totalNums] for ite in range(Iter)]

assert len(chunks)==3
assert len(chunks[0])==500
assert len(chunks[-1])==200