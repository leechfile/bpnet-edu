import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1, epochs=10000):
        # 初始化网络结构和超参数
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs

        # 初始化权重
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def sigmoid(self, z):
        # Sigmoid激活函数
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        # Sigmoid函数的导数
        return z * (1 - z)

    def mse(self,y,y_hat):

    def forward(self, X):
        # 前向传播过程
        self.z2 = np.dot(X, self.W1)  # 隐藏层输入
        self.a2 = self.sigmoid(self.z2)  # 隐藏层激活输出
        self.z3 = np.dot(self.a2, self.W2)  # 输出层输入
        y_hat = self.sigmoid(self.z3)  # 输出层激活输出
        return y_hat

    def backward(self, X, y, y_hat):
        # 反向传播和权重更新
        # 计算输出层误差
        self.error = y - y_hat
        # 应用激活函数的导数计算输出层梯度
        self.delta3 = self.error * self.sigmoid_derivative(y_hat)
        # 计算隐藏层的误差
        self.z2_error = self.delta3.dot(self.W2.T)
        # 应用激活函数的导数计算隐藏层梯度
        self.delta2 = self.z2_error * self.sigmoid_derivative(self.a2)

        # 更新权重
        self.W1 += X.T.dot(self.delta2) * self.learning_rate
        self.W2 += self.a2.T.dot(self.delta3) * self.learning_rate

    def train(self, X, y):
        loss = []
        for _ in range(self.epochs):
            y_hat = self.forward(X)
            loss.append(y-y_hat)
            self.backward(X, y, y_hat)

    def predict(self, X):
        # 预测新数据的函数
        return self.forward(X)

    def get_weights(self):
        # 返回各层的权重
        return self.W1, self.W2