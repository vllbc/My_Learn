import numpy as np
class RegressionTree:
    def __init__(self, max_depth=2, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = {}
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n_features = X.shape[1]
        self.n_samples = X.shape[0]
        self.tree = self._build_tree(X, y)
    def predict(self, X):
        return np.array([self._predict(inputs) for inputs in X])
    def _build_tree(self, X, y, depth=0):
        m = X.shape[0]
        n = X.shape[1]
        # 1. 终止条件
        if m <= self.min_samples_split or depth >= self.max_depth:
            return self._leaf(y)
        # 2. 找到最优分裂特征和特征值
        feature, value = self._best_split(X, y)
        # 3. 构建子树
        left_idx, right_idx = self._split(X, feature, value)
        left = self._build_tree(X[left_idx, :], y[left_idx], depth + 1)
        right = self._build_tree(X[right_idx, :], y[right_idx], depth + 1)
        return {"feature": feature, "value": value, "left": left, "right": right}
    def _leaf(self, y):
        return np.mean(y)
    def _best_split(self, X, y):
        m = X.shape[0]
        n = X.shape[1]
        min_mse = np.inf
        best_feature = None
        best_value = None
        for feature in range(n):
            values = np.unique(X[:, feature])
            for value in values:
                y1 = y[X[:, feature] < value]
                y2 = y[X[:, feature] >= value]
                mse = np.mean(y1) - np.mean(y2)
                if mse < min_mse:
                    min_mse = mse
                    best_feature = feature
                    best_value = value
        return best_feature, best_value
    def _split(self, X, feature, value):
        left_idx = np.argwhere(X[:, feature] < value).flatten()
        right_idx = np.argwhere(X[:, feature] >= value).flatten()
        return left_idx, right_idx
    

class GBDT:
    def __init__(self, n_estimators=10, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []
    def fit(self, X, y):
        y_pred = np.zeros_like(y, dtype=np.float)
        for i in range(self.n_estimators):
            tree = RegressionTree(self.max_depth)
            tree.fit(X, -self.gradient(y, y_pred))
            y_pred += self.learning_rate * tree.predict(X)
            self.trees.append(tree)
    def predict(self, X):
        y_pred = np.zeros((X.shape[0], ), dtype=np.float)
        for tree in self.trees:
            y_pred += self.learning_rate * tree.predict(X)
        return y_pred
    def gradient(self, y_true, y_pred):
        return y_true - y_pred