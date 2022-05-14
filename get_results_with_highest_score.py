import pandas as pd
import matplotlib.pyplot as plt

import logging

import torch
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

# internal libraries
from ressources import target_to_label

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

# set a seed value
torch.manual_seed(555)

top_X = 5

label_to_target = {v: k for k, v in target_to_label.items()}

targets = list(target_to_label.keys())
targets.append("0")

res_df = pd.read_csv("results/zs-nli-19.csv")
# print(res_df.head())

target_df = pd.read_csv("data/afd_targets_odd_12_15_16.csv")

y_true, y_pred = [], []

for i, row in res_df.iterrows():
    results = {}
    top_X_targets = []

    target1 = target_df.iloc[i]["target1"]
    target2 = target_df.iloc[i]["target2"]

    # build target
    for target in targets:
        if target != "0":
            results[target] = row[target]

    print(results)

    target_max = max(results, key=results.get)
    # find X targets with highest score
    for _ in range(top_X):
        target_max_temp = max(results, key=results.get)

        top_X_targets.append(target_max_temp)
        results.pop(target_max_temp)

    y_true.append(target1)
    y_pred.append(target1 if target1 in top_X_targets else target_max)

print(classification_report(y_true, y_pred, labels=targets))

fig, ax = plt.subplots(figsize=(20, 15))
ConfusionMatrixDisplay.from_predictions(y_true, y_pred, labels=targets, ax=ax)
plt.show()
