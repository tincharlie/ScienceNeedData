class model_creation:
    def __init__(self,df):
        self.df = df

    def model_builder(self, df, Ycol, cols_to_drop, model_obj):
        """
                         Data Science Library
         method name: model Builder
        desc: Here we are created the whole model on the basis of previous library;
        In terms of preprocessing, cvtune, datavisualization, anova etc we are come up to
        this conclusion and this code is used to create the model directly from the calling
        the library only.
        author name: TinCharlie

        :param df: Passing DataFrame
        :param Ycol: Target COlumns
        :param cols_to_drop: Columns whichever we want to delete
        :param model_obj: Applying the algorithms for finishing the model.
        :return: Return the accuracy of your model.
        """
        import pandas as pd
        df = df.drop(labels=cols_to_drop, axis=1)
        from replacer.mean_mode_replacer import replace
        replace.Mean_mode_replacer(df)
        Y = df[Ycol]
        X = df.drop(labels=Ycol, axis=1)
        from PreprocessData.preprocessing import preprocess
        X_new = preprocess.preprocess_data(X)
        from sklearn.model_selection import train_test_split
        xtrain, xtest, ytrain, ytest = train_test_split(X_new, Y, test_size=0.2, random_state=31)
        from metrics.check_overfit import overfit_or_not
        if ytrain[Ycol[0]].dtypes == "object":
            overfit_or_not.find_overfit_cat(model_obj, xtrain, xtest, ytrain, ytest)
        else:
            overfit_or_not.find_overfit_con(model_obj, xtrain, xtest, ytrain, ytest)