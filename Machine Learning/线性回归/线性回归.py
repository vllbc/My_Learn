import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
w = np.array([2, 1, 4, 5, 3])
d = len(w)
X = []
Y = []
for _ in range(1000000):
    x = np.random.randn(d)
    y = w.dot(x) + np.random.randn()
    X.append(x)
    Y.append(y)
    
X = np.array(X)
Y = np.array(Y)

def mse(y_true, y_test):
    return ((y_true - y_test) ** 2) / len(y_true)

def gradient(y_true, y_test):
    return 2 * (y_test - y_true) / len(y_true)

def batch_gradient_descent(w, alpha, x, y):
    
    y_pred = x.dot(w)
    error = mse(y, y_pred).mean()
    grad = np.dot(x.T, gradient(y, y_pred))
    w = w - alpha * grad

    return w, error

def stochastic_gradient_descent(w, alpha, x, y, epoch):
    
    alpha_update = alpha
    for i in range(len(x)):
        y_pred = x[i].dot(w)
        grad = np.dot(x[i].T, (y_pred - y[i])) * 2 / len(x)
        w = w- alpha_update * grad
        alpha_update = alpha_update / (epoch+1)
    error = mse(y, x.dot(w)).mean()

    return w, error


X_test = []
Y_test = []
for _ in range(10000):
    x = np.random.randn(d)
    y = w.dot(x) + np.random.randn()
    X_test.append(x)
    Y_test.append(y)

X_test = np.array(X_test)
Y_test = np.array(Y_test)


if __name__ == "__main__":
    train_loss = []
    test_loss = []
    print("Batch Gradient Descent")
    for epoch in range(1000):
        w, error = batch_gradient_descent(w, 0.01, X, Y) # train
        y_pred = X_test.dot(w) 
        error_test = mse(Y_test, y_pred).mean() # test
        if epoch % 100 == 0:
            print("Epoch: {}, TrainError: {}, TestError: {}".format(epoch, error, error_test))

        train_loss.append(error)
        test_loss.append(error_test)
        
    plt.plot(train_loss, label="Train-No-L2")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()

    plt.plot(test_loss, label="Test-No-L2")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()
    
    plt.plot(train_loss, label="Train-No-L2")
    plt.plot(test_loss, label="Test-No-L2")
    plt.legend()
    plt.show()
    