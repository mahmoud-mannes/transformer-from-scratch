def prepare_data(path):
    data = open(path).read()
    vocab = sorted(list(set(data)))    
    vocab_size = len(vocab)
    itos = {i:vocab[i] for i in range(vocab_size)}
    stoi = {v:k for k,v in itos.items()}
    encode = lambda inp: [stoi[i] for i in inp]
    decode = lambda inp: "".join([itos[i] for i in inp])
    return {"encoded_data": encode(data),"vocab": vocab,"encode": encode, "decode": decode}