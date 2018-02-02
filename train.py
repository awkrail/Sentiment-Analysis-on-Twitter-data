import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split

import xgboost
from sklearn.naive_bayes import GaussianNB

def main():
    with open("dataset/amazon_cells_labelled.txt", "r") as f:
        array = [row.split("\t") for row in f.readlines()]
    
    texts = [row[0] for row in array]
    labels = [int(row[1].replace("\n", "")) for row in array]
    labels = np.array(labels, dtype=np.int32)

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(texts)

    X = vectors.toarray()
    y = labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)
    accuracy = np.sum(y_pred == y_test) / X_test.shape[0]
    print(accuracy)

if __name__ == "__main__":
    main()