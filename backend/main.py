import joblib 
import sys

model_nb = joblib.load("../backend/models/spamdet_nb.pk1")

model_lr = joblib.load("../backend/models/spamdet_lr.pk1")

model_dt = joblib.load("../backend/models/spamdet_dt.pk1")

if sys.argv[2] == "nb":
    print(model_nb.predict([sys.argv[1]])[0])
if sys.argv[2] == "dt":
    print(model_dt.predict([sys.argv[1]])[0])
if sys.argv[2] == "lr":
    print(model_lr.predict([sys.argv[1]])[0])


