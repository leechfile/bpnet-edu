import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem,QMessageBox
from data_windows import Ui_Form
from main_windows import Ui_MainWindow
from models import SimpleNeuralNetwork
import pdb



class Data_windows(Ui_Form,QMainWindow):
    """数据窗口的展示"""
    def __init__(self):
        super(Data_windows, self).__init__()
        self.setupUi(self)
        self.Load_btn.clicked.connect(self.openFileDialog)
        self.Edu_btn.clicked.connect(self.loadEduFile)
        self.Pre_btn.clicked.connect(self.preData)
        self.df = None


    def openFileDialog(self):
        # 打开文件选择对话框
        options = QFileDialog.Options()
        init_path = os.getcwd()
        filePath, _ = QFileDialog.getOpenFileName(self, '选择文件', init_path, 'All Files (*);;Text Files (*.txt);;Excel Files (*.xlsx)', options=options)

        # 如果选择了文件，则更新表格
        if filePath:
            try:
                self.fillTable(filePath)

            except Exception as e:
                # 弹出警告窗口
                msg = QMessageBox()
                msg.setText('wrong!!')#'upload excel file!'
                print(e)
                msg.show()
                msg.exec_()

    def loadEduFile(self):
        filepath = '9.2 演示功能模块数据.xlsx'
        if os.path.exists(filepath):
            self.fillTable(filepath)
        else:
            msg = QMessageBox()
            msg.setText(f'{filepath} file not exist!!')
            msg.show()
            msg.exec_()

    def fillTable(self,filepath=None):
        if filepath:
            self.df = pd.read_excel(filepath)
        n, m = self.df.shape
        self.Data.setRowCount(n)
        self.Data.setColumnCount(m)
        pdb.set_trace()
        self.Data.setHorizontalHeaderLabels(self.df.columns)
        # 填充表格的数据
        for i in range(n):
            for j in range(m):
                # 设置表格
                self.Data.setItem(i, j, QTableWidgetItem(self.df.iloc[i, j]))

    def preData(self):
        self.df = preprocess_data(self.df)
        self.fillTable()
        visualize_data(self.df)


class Main_windows(Ui_MainWindow,QMainWindow):
    def init(self):
        super(Main_windows, self).init()
        self.setupUi(self)
        # 设置按钮的映射关系
        self.edu_btn.clicked.connect(self.dataw)
        self.exit_btn.clicked.connect(self.close)
        self.test_nerual.clicked.connect(self.dataw)
    def dataw(self):
        datawindows = Data_windows()
        datawindows.show()



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
    # 创建一个包含多个子图的图形
    fig, axes = plt.subplots(1, 2, figsize=(15, 12))

    # 绘制直方图
    data.hist(bins=15, ax=axes[0, 0])
    axes[0, 0].set_title("Histograms of the features")
    # 绘制箱线图
    data.plot(kind='box', ax=axes[0, 1], subplots=True)
    axes[0, 1].set_title("Boxplots of the features")
    plt.tight_layout()     # 调整子图之间的间距
    plt.show()

    # 绘制相关性热图
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def train_nerual(data):
    """根据data的维度确定输入输出层的大小"""
    #TODO 可能需要确定分类 或者是 回归

    # 确定数据维度
    n,m = data.shape

    # 创建神经网络模型 , 训练和可视化

def waste():
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





if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Data_windows()
    windows.show()
    sys.exit(app.exec_())

