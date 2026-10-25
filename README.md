# iris-classifier
just a simple ai :>

# 🎬 Movie Review Sentiment Analyzer

## 📌 Description
This project is a simple machine learning application that analyzes movie reviews and classifies them as either positive or negative.

## 🤖 Technologies Used
- Python
- Scikit-learn
- Natural Language Processing (NLP)
- Machine Learning

## ⚙️ How It Works
1. The model learns from example movie reviews labeled as positive or negative.
2. `CountVectorizer` converts text into numerical features.
3. The `MultinomialNB` algorithm learns to classify the reviews.
4. The user enters a movie review, and the model predicts its sentiment.

## 📂 Project Structure
```text
sentiment-analyzer/
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Installation and Usage

### 1. Install the dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the program
```bash
python main.py
```

### 3. Enter a movie review
Example:
```text
I loved this movie
```

Expected output:
```text
Sentiment: positive
```

## 🧠 Machine Learning Algorithm
This project uses **Multinomial Naive Bayes**, a probabilistic classification algorithm commonly used for text classification.

## 📊 Dataset
The model is trained on a small collection of example movie reviews included in `main.py`.

## 🎯 Project Goal
The goal is to demonstrate basic machine learning, text preprocessing, sentiment classification, and Python programming.

## ⚠️ Limitations
This is a beginner-level demonstration trained on only six examples. Its predictions are limited and may not be accurate for unfamiliar reviews.

## 👨‍💻 Author
Created as a beginner machine learning project.
