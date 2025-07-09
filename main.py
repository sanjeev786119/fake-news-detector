# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Load Dataset
df = pd.read_csv("news.csv")  # Make sure news.csv is in same folder
df = df[['title', 'text', 'label']]  # Keep only important columns
df['content'] = df['title'] + " " + df['text']  # Combine title + text

# Step 2: Train/Test Split
x_train, x_test, y_train, y_test = train_test_split(df['content'], df['label'], test_size=0.2)

# Step 3: Convert text into numbers (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_tf = vectorizer.fit_transform(x_train)
x_test_tf = vectorizer.transform(x_test)

# Step 4: Train the Classifier
classifier = PassiveAggressiveClassifier(max_iter=50)
classifier.fit(x_train_tf, y_train)

# Step 5: Evaluate Accuracy
y_pred = classifier.predict(x_test_tf)
print(f"\n✅ Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\n🧾 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 6: Prediction Function
def predict_news(news_text):
    transformed = vectorizer.transform([news_text])
    prediction = classifier.predict(transformed)
    return prediction[0]

# Test it
sample_news = input("Paste your news here:\n")
result = predict_news(sample_news)
print("\nThis news is:", result)
