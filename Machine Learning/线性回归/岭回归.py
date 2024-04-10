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


X_test = []
Y_test = []
for _ in range(10000):
    x = np.random.randn(d)
    y = w.dot(x) + np.random.randn()
    X_test.append(x)
    Y_test.append(y)

X_test = np.array(X_test)
Y_test = np.array(Y_test)


def l2_mse(y_true, y_test, l, w):
    return ((y_true - y_test) ** 2) / len(y_true) + l * np.sum(w ** 2)

def l2_gradient(y_true, y_test):
    return 2 * (y_test - y_true) / len(y_true)

def batch_gradient_descent_with_l2(w, alpha, x, y, l):
    
    y_pred = x.dot(w)
    error = l2_mse(y, y_pred, l, w).mean()
    grad = np.dot(x.T, l2_gradient(y, y_pred))
    w = w - alpha * grad - alpha * l * w *2

    return w, error


if __name__ == '__main__':
    train_loss = []
    test_loss = []
    print("Batch Gradient Descent with L2")
    l = 0.0001 # lambda
    for epoch in range(1000):
        w, error = batch_gradient_descent_with_l2(w, 0.01, X, Y, l) # train
        y_pred = X_test.dot(w) 
        error_test = l2_mse(Y_test, y_pred, l, w).mean() # test
        if epoch % 100 == 0:
            print("Epoch: {}, TrainError: {}, TestError: {}".format(epoch, error, error_test))

        train_loss.append(error)
        test_loss.append(error_test)
        
    plt.plot(train_loss, label="Train-L2")
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.show()

    plt.plot(test_loss, label="Test-L2")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()
    
    plt.plot(train_loss, label="Train-L2")
    plt.plot(test_loss, label="Test-L2")
    plt.legend()
    plt.show()