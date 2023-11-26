import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import seaborn as sns
from PyQt5.QtWidgets import QWidget,QMainWindow,QVBoxLayout


class BoxPlotWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle("箱线图")

        # 创建主窗口容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

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

