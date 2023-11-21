import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class SimpleNeuralNetworkModified:
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
        for _ in range(self.epochs):
            y_hat = self.forward(X)
            self.backward(X, y, y_hat)

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

    # 创建一个修改后的网络实例
    nn_modified = SimpleNeuralNetworkModified(input_size=3, hidden_size=4, output_size=1, learning_rate=0.01,
                                              epochs=1000)

    # 使用同样的测试数据
    nn_modified.train(X_train, y_train)

    # 测试网络的预测功能
    predictions_modified = nn_modified.predict(X_train)
    weights_modified = nn_modified.get_weights()

    print(predictions_modified, weights_modified ) # 返回预测结果和网络的权重

