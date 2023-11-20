import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # 初始化网络结构
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # 初始化权重
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        return z * (1 - z)

    def forward(self, X):
        # 前向传播
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        y_hat = self.sigmoid(self.z3)
        return y_hat

    def backward(self, X, y, y_hat, learning_rate):
        # 反向传播和权重更新
        self.error = y - y_hat
        self.delta3 = self.error * self.sigmoid_derivative(y_hat)
        self.z2_error = self.delta3.dot(self.W2.T)
        self.delta2 = self.z2_error * self.sigmoid_derivative(self.a2)

        # 更新权重
        self.W1 += X.T.dot(self.delta2) * learning_rate
        self.W2 += self.a2.T.dot(self.delta3) * learning_rate

    def train(self, X, y, learning_rate=0.1, epochs=10000):
        for _ in range(epochs):
            y_hat = self.forward(X)
            self.backward(X, y, y_hat, learning_rate)

    def predict(self, X):
        # 预测新数据的函数
        return self.forward(X)

    def get_weights(self):
        # 返回各层的权重
        return self.W1, self.W2


def preprocess_data(data):
    """
    对数据进行预处理：标准化和删除缺失值。

    :param data: pandas DataFrame，包含待处理的数据
    :return: 预处理后的DataFrame
    """
    # 删除缺失值
    data_cleaned = data.dropna()

    # 数据标准化
    # 计算均值和标准差
    mean = data_cleaned.mean()
    std = data_cleaned.std()
    # 应用标准化
    data_standardized = (data_cleaned - mean) / std

    return data_standardized


def visualize_data(data):
    """
    对数据进行基本的可视化，包括直方图和箱线图。

    :param data: pandas DataFrame，包含待可视化的数据
    """
    # 绘制直方图
    data.hist(bins=15, figsize=(15, 6), layout=(2, 4))
    plt.suptitle("Histograms of the features")
    plt.show()

    # 绘制箱线图
    data.plot(kind='box', figsize=(15, 6), layout=(2, 4), subplots=True)
    plt.suptitle("Boxplots of the features")
    plt.show()

    # 绘制相关性热图
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

if __name__ == '__main__':
    # 示例数据
    data_example = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100) * 10,
        'C': np.random.rand(100) * 100,
        'D': np.random.randn(100)  # 正态分布
    })

    # 添加一些缺失值
    data_example.loc[5:10, ['B', 'C']] = np.nan

    # 预处理数据
    preprocessed_data = preprocess_data(data_example)

    # 可视化预处理后的数据
    visualize_data(preprocessed_data)


    # 创建一个网络实例
    nn = SimpleNeuralNetwork(input_size=3, hidden_size=4, output_size=1)

    # 测试数据
    X_train = np.array([[0, 0, 1],
                        [0, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]])
    y_train = np.array([[0],
                        [1],
                        [1],
                        [0]])

    # 训练网络
    nn.train(X_train, y_train)

    # 测试网络的预测功能
    predictions = nn.predict(X_train)
    weights = nn.get_weights()
    print(predictions, weights)  # 返回预测结果和网络的权重
