# Quora Duplicate Question Detection using NLP and Machine Learning

A Natural Language Processing (NLP) and Machine Learning project that predicts whether two Quora questions have the same meaning.

The project combines text preprocessing, handcrafted similarity features, fuzzy string matching, Bag of Words (BoW) representation, and a Random Forest classifier. The trained model is integrated into a Flask web application for real-time predictions.

---

## 🚀 Project Overview

Duplicate questions are questions that are different in wording but essentially have the same meaning.

For example:

**Question 1:**
> What is the capital of India?

**Question 2:**
> Which city is the capital of India?

These questions have different wording but convey the same meaning.

The goal of this project is to automatically identify such duplicate question pairs.

---

## 🎯 Objectives

- Perform exploratory data analysis on the Quora Question Pairs dataset.
- Clean and preprocess textual data.
- Extract meaningful features from pairs of questions.
- Measure lexical and token-level similarity.
- Apply fuzzy string matching techniques.
- Convert questions into numerical representations using Bag of Words.
- Train a Random Forest classifier.
- Save the trained model and vectorizer.
- Build a Flask web application for real-time predictions.

---

## 📊 Dataset

The project uses the **Quora Question Pairs** dataset.

The dataset contains pairs of questions and a binary target variable:

| Column | Description |
|---|---|
| `id` | Unique ID for the question pair |
| `qid1` | Unique ID of the first question |
| `qid2` | Unique ID of the second question |
| `question1` | First question |
| `question2` | Second question |
| `is_duplicate` | Target variable |

### Target Variable

```text
0 → Not Duplicate
1 → Duplicate
````

The dataset contains human-labeled question pairs, where `is_duplicate = 1` indicates that the two questions have essentially the same meaning.

---

# 🧹 Text Preprocessing

The following preprocessing techniques are applied to the questions:

* Lowercasing
* Removing leading and trailing spaces
* Handling special characters
* Converting symbols such as `%`, `$`, `₹`, and `€`
* Handling `[math]`
* Number normalization
* Contraction expansion
* HTML tag removal
* Punctuation removal

### Example

Original:

```text
How's my ₹100 salary? <b>It's good!</b>
```

After preprocessing:

```text
how is my rupee 100 salary it is good
```

---

# 🧠 Feature Engineering

The project uses multiple feature groups to capture different types of similarity between the two questions.

## 1. Basic Features

Features based on the structure of the questions:

* Question length
* Number of words
* Number of common words
* Total unique words
* Word share

These features provide information about how similar the two questions are at a basic lexical level.

---

## 2. Token-Based Features

Token-level similarity features include:

* Common word count ratios
* Common stopword ratios
* Common token ratios
* First word equality
* Last word equality

These features help identify overlap between the two questions.

---

## 3. Length Features

Length-based features include:

* Absolute difference in token count
* Average number of tokens
* Longest common substring ratio

These features capture structural similarity between question pairs.

---

# 🔤 Fuzzy Matching Features

Fuzzy string matching is used to measure similarity even when the exact wording differs.

The project uses:

### Fuzzy Ratio

Measures the overall similarity between two questions.

### Partial Ratio

Measures similarity between parts of the two questions.

### Token Sort Ratio

Sorts the words before comparing the questions, making the comparison less sensitive to word order.

Example:

```text
Python is easy
Easy Python is
```

Token sorting can identify these as highly similar.

### Token Set Ratio

Compares unique words between the two questions and is useful when one question contains additional words.

---

# 📝 Bag of Words

The project uses **CountVectorizer** to convert the preprocessed questions into numerical vectors.

The vectorizer is trained on the question corpus and uses a vocabulary of up to 3,000 features.

The final model input combines:

```text
Handcrafted Features
        +
Question 1 BoW Features
        +
Question 2 BoW Features
```

This allows the model to use both manually engineered similarity features and textual information.

---

# 🤖 Machine Learning Model

The final classifier used in this project is:

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions.

The model learns patterns associated with duplicate and non-duplicate question pairs.

### Prediction

The model produces two possible classes:

```text
0 → Not Duplicate
1 → Duplicate
```

The Flask application also displays the estimated duplicate probability.

---

# 🌐 Flask Web Application

The trained model is integrated into a Flask web application.

The user enters:

```text
Question 1
Question 2
```

The application then:

```text
User Input
     ↓
Text Preprocessing
     ↓
Feature Engineering
     ↓
Fuzzy Features
     ↓
Bag of Words
     ↓
Random Forest Model
     ↓
Prediction
```

The application returns:

```text
Duplicate Questions
```

or

```text
Not Duplicate
```

along with the duplicate probability.

---

# 📁 Project Structure

```text
quora-duplicate-question-detection/
│
├── app.py
├── utils.py
├── model.pkl
├── cv.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### File Description

| File                   | Purpose                               |
| ---------------------- | ------------------------------------- |
| `app.py`               | Flask application                     |
| `utils.py`             | Preprocessing and feature engineering |
| `model.pkl`            | Trained Random Forest model           |
| `cv.pkl`               | Saved CountVectorizer                 |
| `requirements.txt`     | Python dependencies                   |
| `templates/index.html` | Web interface                         |
| `static/style.css`     | Web application styling               |
| `.gitignore`           | Files excluded from Git               |
| `.gitattributes`       | Git LFS configuration                 |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/venky2237/quora-duplicate-question-detection.git
```

Move into the project directory:

```bash
cd quora-duplicate-question-detection
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download NLTK stopwords

```bash
python -c "import nltk; nltk.download('stopwords')"
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open this address in your browser.

---

# 💡 Example

### Input

**Question 1**

```text
What is the capital of India?
```

**Question 2**

```text
Which city is the capital of India?
```

### Output

```text
Duplicate Questions

Duplicate probability: 54%
```

The probability represents the model's estimated probability for the duplicate class.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* BeautifulSoup
* FuzzyWuzzy
* Distance
* Flask
* HTML
* CSS
* Git
* Git LFS

---

# 🔬 Machine Learning Pipeline

```text
Quora Question Pairs Dataset
             ↓
       Exploratory Data Analysis
             ↓
       Missing Value Handling
             ↓
       Text Preprocessing
             ↓
       Feature Engineering
             ↓
 ┌─────────────────────────────┐
 │ Basic Features              │
 │ Token Features              │
 │ Length Features             │
 │ Fuzzy Features              │
 └─────────────────────────────┘
             ↓
       Bag of Words
             ↓
       Feature Combination
             ↓
       Random Forest
             ↓
       Model Evaluation
             ↓
       model.pkl
             ↓
       Flask Web Application
```

---

# 📌 Future Improvements

Possible improvements include:

* TF-IDF representation
* Word embeddings
* Word2Vec
* GloVe
* Sentence Transformers
* BERT-based semantic similarity
* Hyperparameter optimization
* Model calibration
* Improved UI/UX
* Cloud deployment
* REST API implementation

---

# 👨‍💻 Author

**Venky Chukkala**

GitHub:

[https://github.com/venky2237](https://github.com/venky2237)

---

## ⭐ Project Highlights

This project demonstrates practical experience in:

* Natural Language Processing
* Text preprocessing
* Feature engineering
* Similarity measurement
* Fuzzy string matching
* Bag of Words
* Machine Learning
* Random Forest
* Model persistence
* Flask development
* Git & GitHub
* Git LFS

````

### Then save and push it

From your activated terminal:

```powershell
git add README.md
git commit -m "Add professional project README"
git push
````

