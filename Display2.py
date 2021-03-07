import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# classify a review as negative (0) or positive (1)
def predict_sentiment(word):
 cv = pickle.load(open("/Users/mahdijalil/.atom/Displays2/CV.sav",'rb'))
 x = cv.fit_transform(word).toarray()
 return x


def result():
    print(1)
    x = entry1.get()
    print(x)
    arr2 = np.fromstring('get fucking real dude', sep = ' ')
    #print(arr)

    arr3 = x.split(" ")
    #Sentence = predict_sentiment(x)
    print(arr3)
    #print(Sentence)

    cv = pickle.load(open("/Users/mahdijalil/.atom/Displays2/CV.sav",'rb'))


    t = cv.transform(arr3).toarray()
    print("t:")
    print(t)
    estimate = model.predict(t)
    print(estimate)
    Figure1 = Figure(figsize=(6,5), dpi=100)
    df = pd.DataFrame(data = estimate)
    df = df.rename(columns={0: 'A'})
    df =  df['A'].value_counts()
    fig1, ax1 = plt.subplots()
    labels = df.index

    ax1.pie(df, autopct='%1.1f%%', shadow=False, labels = labels)
    ax1.set_title('Your sentence is percieved to following the following:\n 0: Aggresive , 1: Sarcastic, 2: Genuine')
    bar1 = FigureCanvasTkAgg(Figure1, root)

    plt.show()
    return estimate


model  = pickle.load(open("/Users/mahdijalil/.atom/Displays2/finalized_model2.sav",'rb'))
print(2)
root = tk.Tk()
#creates screen
Screen = tk.Canvas(root, width = 800, height = 300)
Screen.pack()

#Creates Title
label1 = tk.Label(root, text='The Tone Indicator Mark II')
label1.config(font=('Arial', 20))
Screen.create_window(400, 50, window=label1)


#Creates Entry for data
entry1 = tk.Entry(root)
Screen.create_window(400, 100, window=entry1)


#Creates Button
button1 = tk.Button(text='Find the tone!', command = result )
Screen.create_window(400, 180, window=button1)






root.mainloop()
