from sklearn.base import BaseEstimator, TransformerMixin
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        data = X.copy()
        return data.drop(labels=self.columns, axis='columns')

    rm_columns = DropColumns(
        columns=["NOME", "MATRICULA","INGLES"]
    )
    rm_columns.fit(X=df_data_1)
    
    df_data_2 = pd.DataFrame.from_records(
        data=rm_columns.transform(
            X=df_data_1
        ),
    )
