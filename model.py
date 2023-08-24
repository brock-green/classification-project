from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

def get_tree(X_train, X_validate, y_train, y_validate):
    '''Takes in 4 positional arguments for X_train, X_validate, y_train, y_validate. Creates (max_depth=5, random_state=666) and fits DT model on train data. Returns print statement of the accuracy score for the model on train and validate.
    '''

    # create classifier object
    clf = DecisionTreeClassifier(max_depth=5, random_state=666)

    #fit model on training data
    clf = clf.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Decision Tree on train data is {clf.score(X_train, y_train): .2%}")
    print(f"Accuracy of Decision Tree on validate data is {clf.score(X_validate, y_validate): .2%}")
    
def get_knn(X_train, X_validate, y_train, y_validate):
    '''Takes in 4 positional arguments for X_train, X_validate, y_train, y_validate. Creates (n_neighbors=5, weights='uniform') and fits KNN model on train data. Returns print statement of the accuracy score for the model on train and validate.'''

    # create model object and fit it to the training data
    knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    knn.fit(X_train, y_train)

    # print results
    print(f"Accuracy of KNN on train is {knn.score(X_train, y_train): .2%}")
    print(f"Accuracy of KNN on validate is {knn.score(X_validate, y_validate): .2%}")
    
def get_reg(X_train, X_validate, y_train, y_validate):
    '''Takes in 4 positional arguments for X_train, X_validate, y_train, y_validate. Creates (solver='liblinear') and fits Logistic Regression model on train data. Returns print statement of the accuracy score for the model on train and validate.'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logit.score(X_train, y_train): .2%}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(X_validate, y_validate): .2%}")
    
def get_reg_test(X_train, X_test, y_train, y_test):
    '''Takes in 4 positional arguments for X_train, X_test, y_train, y_test. Creates (solver='liblinear') and fits Logistic Regression model on train data. Returns print statement of the accuracy score for the model on test data.'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Logistic Regression on test is {logit.score(X_test, y_test): .2%}")