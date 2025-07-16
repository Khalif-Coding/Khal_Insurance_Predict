def replaceBMI(X):
    X = X.copy()
    height_m = X['Height'] / 100
    X['BMI'] = X['Weight'] / (height_m ** 2)
            
    return X.drop(columns=['Height', 'Weight'])