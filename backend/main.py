import joblib 
import sys

model = joblib.load("C:\\Users\\DEV\\Documents\\projects\\SpamDetection\\spam_detector\\backend\\spamdet.pk1")

print(model.predict([sys.argv[1]])[0])
