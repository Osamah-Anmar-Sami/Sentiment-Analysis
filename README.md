# Sentiment-Analysis
This repository contains a Sentiment Analysis project that classifies the sentiment of text data as positive, or negative. The goal of this project is to build a model that can accurately determine the sentiment expressed in a given piece of text, which can be applied to various applications such as social media monitoring, customer feedback analysis, and more.

# DataSet
Arabic DataSet: https://github.com/elnagara/HARD-Arabic-Dataset/tree/master

English DataSet: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

# Pre Trained Word Embedding
* Aravec : https://github.com/bakrianoo/aravec
* Glove : https://nlp.stanford.edu/projects/glove/


# Other Pre Trained Word Embedding
* Google : https://www.kaggle.com/datasets/adarshsng/googlenewsvectors
* Fasttext : https://fasttext.cc/docs/en/crawl-vectors.html



# Utils Folder
* confusion_matrix.py
* text_preprocessing.py
* deeplearning.py
* generate_poitive_negative.py
* machinelearning.py
* most_frequent_word_plot.py
* performance_metrics.py
* plot_model_changes.py
* sentimentinformation.py
* textnormalization.py
* word_vector.py
* wordcloud.py
* contraction_expand.py
* transformer.py
* model_inference.py

# Library For Text Preprocessing
* emoji 
* NLTK
* Spacy
* Fasttext
* ruqia
* camel_tools
* pyarabic
* and many other 


# Model
The model used in this project is a machine learning classifier trained on the preprocessed text data. Several models have been experimented with, including:

* Logistic Regression
* Support Vector Machine (SVM)
* Naive Bayes
* Decision Tree
* Random Forest
* SGD
* LSTM (Long Short-Term Memory) Neural Network
* GRU (Gated Recurrent Unit)
* Bidirectional LSTM
* Transformers

#  Installation
```bash
git clone https://github.com/Osama-Anmar-Sami/Sentiment-Analysis.git
cd Sentiment-Analysis
pip install -r requirements.txt
```
#  Usage
Just insert your text in **text** of model inference

#  Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
