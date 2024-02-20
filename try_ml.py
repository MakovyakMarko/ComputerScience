# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:08:26 2023

@author: Marko
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm

# Завантажуємо набір даних (у цьому випадку, набір даних про іриси)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Розділяємо дані на навчальний і тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Створюємо модель SVM та навчаємо її на навчальних даних
clf = svm.SVC()
clf.fit(X_train, y_train)

# Робимо передбачення на тестових даних
y_pred = clf.predict(X_test)

# Виводимо точність моделі
accuracy = np.mean(y_pred == y_test)
print("Точність моделі:", accuracy)