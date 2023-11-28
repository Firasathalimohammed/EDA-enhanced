import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


class CarClassificationVisualization:
    def __init__(self, data):
        self.data = data

    def plot_stacked_bar_chart(self):
        grouped_data = self.data.groupby(['maint', 'safety', 'class']).size().unstack().fillna(0)
        grouped_data.plot(kind='bar', stacked=True, figsize=(12, 6))
        plt.title('Car Classification by Maintenance Cost and Safety Rating')
        plt.xlabel('Maintenance Cost and Safety Rating')
        plt.ylabel('Count')
        plt.show()

    def plot_heatmap(self):
        pivot_table = self.data.pivot_table(index='maint', columns='safety', values='class', aggfunc='count', fill_value=0)
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_table, annot=True, cmap='viridis')
        plt.title('Heatmap of Car Classification by Maintenance Cost and Safety Rating')
        plt.xlabel('Safety Rating')
        plt.ylabel('Maintenance Cost')
        plt.show()


class CarClassificationAnalysis:
    def __init__(self, data):
        self.data = data

    def perform_chi_square_test(self):
        contingency_table = pd.crosstab(self.data['maint'], self.data['class'])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        return chi2, p

    def perform_logistic_regression(self):
        # Encoding categorical variables
        le = LabelEncoder()
        X = self.data[['maint', 'safety']].apply(le.fit_transform)
        y = le.fit_transform(self.data['class'])

        # Splitting the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Logistic Regression Model
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Predictions and Classification Report
        predictions = model.predict(X_test)
        report = classification_report(y_test, predictions, target_names=le.classes_)
        return report
