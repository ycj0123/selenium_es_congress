import pickle

with open('saved_links.pickle', 'rb') as f:
    saved_links = pickle.load(f)

print(len(saved_links))