import numpy as np


class LogisticRegression:
    def __init__(self):
        pass
    def sigmoid(self,a):
        res = []
        for x in a:
            if x >= 0:
                res.append(1/(1+np.exp(-x)))
            else:
                res.append(np.exp(x) / (np.exp(x) + 1))
        return np.array(res)
    def train(self, X, y_true, n_iters=100, learning_rate=1):
        """
        根据给定的训练集X和y来训练逻辑回归
        """
        # 第零步：初始化参数
        n_samples, n_features = X.shape
        #👆样本数m和特征量数n分别赋值为X的行数和列数
        self.weights = np.zeros((n_features,1))
        self.bias = 0
        costs = []

        for i in range(n_iters):
            # 第一步和第二步：计算输入的特征量和权值的线性组合，使用sigmoid函数
            y_predict = self.sigmoid(np.dot(X,self.weights)+self.bias)
            # 第三步：计算代价值，用于之后计算代价函数值
            cost = (-1/n_samples)*np.sum(y_true*np.log(y_predict+1e-5)+(1-y_true)*(np.log(1-y_predict+1e-5)))
            # 第四步：计算梯度
            dw = (1/n_samples)*np.dot(X.T,(y_predict - y_true))
            db = (1/n_samples)*np.sum(y_predict-y_true)
            # 第五步；更新参数
            self.weights = self.weights - learning_rate * dw
            self.bias = self.bias - learning_rate * db

            costs.append(cost)
            if i%10 == 0:
                print(f"Cost after iteration {i}:{cost}")

        # return self.weights,self.bias,costs

    def predict(self,X):
        """
        对于测试集X，预测二元分类标签
        """
        y_predict = self.sigmoid(np.dot(X,self.weights)+self.bias)
        return np.array(y_predict)