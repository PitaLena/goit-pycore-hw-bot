import pickle

with open("addressbook.pkl", "rb") as f:
    book = pickle.load(f)

for name, record in book.data.items():
    print(record)