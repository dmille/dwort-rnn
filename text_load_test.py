from utils import TextLoader

data_dir = 'data/test'
batch_size = 10
seq_length = 4  # will not need

loader = TextLoader(data_dir, batch_size, seq_length)

x,y = loader.next_batch()
