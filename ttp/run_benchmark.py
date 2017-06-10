from sklearn_models import MultNB, BernNB, SVM
from benchmarks import benchmark


TRAIN_SET_PATH = '../data/r8-all-terms.txt'

models = [MultNB(), BernNB(), SVM()]

for model in models:
    print str(model), benchmark(model, TRAIN_SET_PATH)
