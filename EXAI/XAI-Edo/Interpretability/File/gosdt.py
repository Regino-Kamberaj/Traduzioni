# Python 3.11
# 
# NOTE: Need to change check_X_y import in _threshold_guessing.py (from sklearn.utils import check_X_y)

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from gosdt import ThresholdGuessBinarizer, GOSDTClassifier

# Parameters
GBDT_N_EST = 40
GBDT_MAX_DEPTH = 1
REGULARIZATION = 0.001
SIMILAR_SUPPORT = False
DEPTH_BUDGET = 6
TIME_LIMIT = 60
VERBOSE = True

# Read the dataset
df = pd.read_csv("fico.csv", sep=",")
X, y = df.iloc[:, :-1], df.iloc[:, -1]
h = df.columns[:-1]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2021)
print("X train shape:{}, X test shape:{}".format(X_train.shape, X_test.shape))

# Step 1: Guess Thresholds
X_train = pd.DataFrame(X_train, columns=h)
X_test = pd.DataFrame(X_test, columns=h)
enc = ThresholdGuessBinarizer(n_estimators=GBDT_N_EST, max_depth=GBDT_MAX_DEPTH, random_state=2021)
enc.set_output(transform="pandas")
X_train_guessed = enc.fit_transform(X_train, y_train)
X_test_guessed = enc.transform(X_test)
print(f"After guessing, X train shape:{X_train_guessed.shape}, X test shape:{X_test_guessed.shape}")
print("train set column names == test set column names: {list(X_train_guessed.columns)==list(X_test_guessed.columns)}")

# Step 2: Guess Lower Bounds
enc = GradientBoostingClassifier(n_estimators=GBDT_N_EST, max_depth=GBDT_MAX_DEPTH, random_state=42)
enc.fit(X_train_guessed, y_train)
warm_labels = enc.predict(X_train_guessed)

# Step 3: Train the GOSDT classifier
clf = GOSDTClassifier(regularization=REGULARIZATION, similar_support=SIMILAR_SUPPORT, time_limit=TIME_LIMIT, depth_budget=DEPTH_BUDGET, verbose=VERBOSE) 
clf.fit(X_train_guessed, y_train, y_ref=warm_labels)
#clf.fit(X_train_guessed, y_train)

# Step 4: Evaluate the model
print("Evaluating the model, extracting tree and scores", flush=True)
clf.predict(X_test_guessed)


print(f"Model training time: {clf.result_.time}")
print(f"Training accuracy: {clf.score(X_train_guessed, y_train)}")
print(f"Test accuracy: {clf.score(X_test_guessed, y_test)}")

print(clf.trees_[0])

