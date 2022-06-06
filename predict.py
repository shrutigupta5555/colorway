import joblib
import pickle
from methods import get_colors

def predict_colors():
    model = joblib.load('static/model.pkl')
    print('lol')
    return model('static/flag.jpg')
    # print(f'lmao {a}')
    
print(predict_colors())