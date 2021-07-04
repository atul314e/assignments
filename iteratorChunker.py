def chunker(n, iterable):
    chunks=[]
    while(1):
        tmp=[]
        try:
            for ite in range(n):
                tmp.append(next(iterable))
            chunks.append(tmp)
        except StopIteration:
            chunks.append(tmp)
            break
    return chunks
data = map(str, list(range(1200)))
chunks = chunker(500, data)
assert len(chunks)==3
assert len(chunks[0])==500
assert type(chunks[0])==list
assert type(chunks[0][0])==str
assert len(chunks[-1])==200