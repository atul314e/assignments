data = list(range(1200))

Iter=int(1200/500)+1 if int(1200/500)!=(1200/500) else int(1200/500)
start=0
end=500
chunks = [data[start+500*ite:end+500*ite] if end+500*ite<=1200 else data[start+500*ite:1200] for ite in range(Iter)]

assert len(chunks)==3
assert len(chunks[0])==500
assert len(chunks[-1])==200