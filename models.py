<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1, epochs=10000):
        # 初始化网络结构和超参数
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.epochs = epochs
=======
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import seaborn as sns
from PyQt5.QtWidgets import QWidget,QMainWindow,QVBoxLayout
>>>>>>> af


class BoxPlotWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle("箱线图")

        # 创建主窗口容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

<<<<<<< HEAD
    def mse(self,y,y_hat):
        pass

    def forward(self, X):
        # 前向传播过程
        self.z2 = np.dot(X, self.W1)  # 隐藏层输入
        self.a2 = self.sigmoid(self.z2)  # 隐藏层激活输出
        self.z3 = np.dot(self.a2, self.W2)  # 输出层输入
        y_hat = self.z3  # 输出层激活输出
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
        history={}
        history['loss'] = []
        for i in range(self.epochs):
            loss = []
            for j in range(X.shape[0]):
                y_hat = self.forward(X[j,:])
                self.backward(X[j,:], y[j,:], y_hat)
                loss.append(y-y_hat)
            print(f'----------epoch{i}: loss:{np.mean(np.power(loss,2))} ---------------')
            history['loss'].append(np.mean(np.power(loss,2)))
        return history

    def predict(self, X):
        # 预测新数据的函数
        res = np.array([[]])
        for i in range(X.shape[0]):
            res = np.concatenate((res,self.forward(X[i,:])),axis=0)
        return res

    def get_weights(self):
        # 返回各层的权重
        return self.W1, self.W2

if __name__ == '__main__':
    # 创建一个修改后的网络实例
    X_train = np.random.randn(100,3)
    y_train = np.mean(X_train,axis=1)+.001*np.random.randn(100)

    nn_modified = SimpleNeuralNetwork(input_size=3, hidden_size=4, output_size=1, learning_rate=0.01,
                                              epochs=100)

    # 使用同样的测试数据
    history = nn_modified.train(X_train, y_train.reshape(-1,1))
    # 测试网络的预测功能
    plt.plot(history)
    predictions_modified = nn_modified.predict(X_train)
    weights_modified = nn_modified.get_weights()

    print(predictions_modified, weights_modified ) # 返回预测结果和网络的权重
=======
        # 创建Matplotlib图形容器
        self.figure = Figure(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot_boxplot()

    def plot_boxplot(self):
        # 绘制箱线图
        self.data.plot(kind='box', ax=self.figure.gca(),subplots=True)
        self.figure.suptitle("特征的箱线图")

        self.figure.tight_layout()


class CorrelationHeatmapWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle("相关性热力图")

        # 创建主窗口容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建Matplotlib图形容器
        self.figure = Figure(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot_correlation_heatmap()

    def plot_correlation_heatmap(self):
        corr_matrix = self.data.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=self.figure.gca())
        self.figure.suptitle("相关性热力图")

class HistogramWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle("直方图")

        # 创建主窗口容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建Matplotlib图形容器
        self.figure = Figure(figsize=(10, 8))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.plot_histogram()

    def plot_histogram(self):
        # 绘制直方图
        self.data.hist(bins=15,ax=self.figure.gca())
        self.figure.suptitle("特征的直方图")
        self.figure.tight_layout()

>>>>>>> af
