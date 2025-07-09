# detector.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Load the dataset
df = pd.read_csv("news.csv")
df = df[['title', 'text', 'label']]
df['content'] = df['title'] + " " + df['text']

# Split the data
x_train, x_test, y_train, y_test = train_test_split(df['content'], df['label'], test_size=0.2)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_tf = vectorizer.fit_transform(x_train)
x_test_tf = vectorizer.transform(x_test)

# Train the model
classifier = PassiveAggressiveClassifier(max_iter=50)
classifier.fit(x_train_tf, y_train)

# Prediction function
def predict_news(news_text):
    transformed = vectorizer.transform([news_text])
    return classifier.predict(transformed)[0]
