
from IPython.display            import display
import matplotlib.pyplot        as plt
import numpy                    as np
import pandas                   as pd
import seaborn                  as sns
from imblearn.over_sampling     import RandomOverSampler
from imblearn.over_sampling     import BorderlineSMOTE
from imblearn.over_sampling     import SMOTE
from imblearn.over_sampling     import SMOTENC
from imblearn.under_sampling    import RandomUnderSampler
from sklearn.metrics            import ConfusionMatrixDisplay
from sklearn.metrics            import confusion_matrix
from sklearn.model_selection    import train_test_split
from sklearn.neighbors          import KNeighborsClassifier

class Fraud:
    def __init__(self):
        self._file = 'data/2_fraud_ex.csv'
        self._df_origin = pd.read_csv(self._file)
        self._df_origin.rename(columns={'oldbalanceOrg':'oldbalanceOrig'}, inplace=True)
        self._types = {'CASH_IN': 0, 'CASH_OUT': 1, 'PAYMENT': 2, 'DEBIT': 3}
        self._df_origin = self._df_origin[['type', 'amount', 'oldbalanceOrig',
            'oldbalanceDest', 'newbalanceDest', 'isFraud']]
        self._df_origin['type'] = self._df_origin['type'].apply(lambda x: self._types.get(x, 4))
        self.reset_df()
        self.RAND_SEED = 0
        self._clf = None
    
    @property
    def types(self):
        return self._types
    
    def reset_df(self):
        self._df = self._df_origin.copy()
        
    @property
    def df(self):
        return self._df
        
    def head(self):
        display(self._df.head())
        
    def make_small(self, ratio=0.1):
        _, self._df_small_origin, _, _ = train_test_split(self._df, self._df['isFraud'],
            test_size=ratio, random_state=self.RAND_SEED, stratify=self._df['isFraud'])
        self.reset_df_small()
        
    def reset_df_small(self):
        self._df_small = self._df_small_origin.copy()
        
    @property
    def df_small(self):
        return self._df_small
    
    def prepare_set(self):
        self._df_X = self._df_small.drop(columns='isFraud')
        self._df_y = self._df_small.isFraud

        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(
            self._df_X, self._df_y, random_state=self.RAND_SEED, stratify=self._df_y)
        self._sm = SMOTENC(categorical_features=[0], random_state=self.RAND_SEED, k_neighbors=7)
        self._X_sm_train, self._y_sm_train = self._sm.fit_resample(self._X_train, self._y_train)
        
    def show_shapes(self):
        print(f'X_train {self._X_train.shape} became {self._X_sm_train.shape}')
        print(f'y_train {self._y_train.shape} became {self._y_sm_train.shape}')
        
    def train_data(self):
        return self._X_sm_train, self._y_sm_train
    
    def test_data(self):
        return self._X_test, self._y_test
    
    @property
    def df_X(self):
        return self._df_X
    
    @property
    def df_y(self):
        return self._df_y
    
    @property
    def clf(self):
        return self._clf

    @clf.setter
    def clf(self, clf):
        self._clf = clf
    
    def show_score(self, clf=None):
        if clf == None:
            print(f"Train score: {self._clf.score(self._X_sm_train, self._y_sm_train):.3f}")
            print(f"Test score: {self._clf.score(self._X_test, self._y_test):.3f}")
        else:
            print(f"Train score: {clf.score(self._X_sm_train, self._y_sm_train):.3f}")
            print(f"Test score: {clf.score(self._X_test, self._y_test):.3f}")
    
        if clf == None:
            ConfusionMatrixDisplay.from_estimator(self._clf, self._X_test, self._y_test, display_labels=['Non-Fraud', 'Fraud'])
        else:
            ConfusionMatrixDisplay.from_estimator(clf, self._X_test, self._y_test, display_labels=['Non-Fraud', 'Fraud'])
        plt.show()

    def describe_matrix(self, clf=None):
        if clf == None:
            tn, fp, fn, tp = confusion_matrix(
                self._y_test, self._clf.predict(self._X_test), labels=self._clf.classes_).ravel()
        else:
            tn, fp, fn, tp = confusion_matrix(
                self._y_test, clf.predict(self._X_test), labels=clf.classes_).ravel()

        precision, recall = tp / (tp+fp), tp / (tp+fn)
        pd.options.display.float_format = '{:.3%}'.format
        display(pd.DataFrame({
            'name': ['Accuracy', 'Precision', 'Recall(TPR)', 'F-Score', 'FPR(Type I Error)', 'Type II Error'],
            'value': [(tp+tn) / (tp+tn+fp+fn), precision, recall, 2 * (precision*recall) / (precision+recall),
                fp / (fp+tn), fn / (tp+fn)]
        }))
    

class Crowdfunding:
    def __init__(self):
        self._df = pd.read_excel('data/crowdfunding_ex.xlsx')
        self._x_df = self._df[["Backers", "CountryCode", "VideoCount", "ImageCount", "TagCode", "Goal", "Period", "SNS", 
               "Fiends" , "#ofCreation", "보상수"]]
        self._x_df.rename(columns={'보상수': '#ofRewards'}, inplace=True)
        self._y = self._df['Funded'] > self._df['Goal'] # Success

    @property
    def x_df(self):
        return self._x_df

    @property
    def y(self):
        return self._y

if __name__ == "__main__":
    try:
        pass
    except:
        print('An error has occured.')