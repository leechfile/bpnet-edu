import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem,QMessageBox
from PyQt5.QtGui import QPainter,QPixmap
from data_windows import Ui_Form
from main_windows import Ui_MainWindow
from remind_windows import Ui_remind_windows
from models import SimpleNeuralNetwork
from nerual_main import nerual_start





class Data_windows(Ui_Form,QMainWindow):
    """数据窗口的展示"""
    def __init__(self):
        super(Data_windows, self).__init__()
        self.setupUi(self)
        self.Load_btn.clicked.connect(self.openFileDialog)
        self.Edu_btn.clicked.connect(self.loadEduFile)
        self.Pre_btn.clicked.connect(self.preData)
        self.Pre_btn.setText('预处理数据')
        self.Train_btn.clicked.connect(lambda :nerual_start(self.df))
        self.df = None
        self.msg = QMessageBox()


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
                self.msg.setText('wrong!!')#'upload excel file!'
                print(e)
                self.msg.show()
                # self.msg.exec_()

    def loadEduFile(self):
        filepath = 'iris.xlsx'
        if os.path.exists(filepath):
            self.fillTable(filepath)
        else:
            self.msg.setText(f'{filepath} file not exist!!')
            self.msg.show()


    def fillTable(self,filepath=None):
        if filepath:
            self.df = pd.read_excel(filepath)
        n, m = self.df.shape
        self.Data.setRowCount(n)
        self.Data.setColumnCount(m)
        # pdb.set_trace()
        if not isinstance(self.df.columns[0], str):  # 或者使用 type(df.columns) != pd.Index
            # 如果不是 pd.Index 类型，则转换为字符串类型
            self.df.columns = self.df.columns.astype(str)

        # 现在 df.columns 已经是字符串类型了
        self.Data.setHorizontalHeaderLabels(self.df.columns)
        # 填充表格的数据
        for i in range(n):
            for j in range(m):
                # 设置表格
                self.Data.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

    def preData(self):
        """我们需要传进去df,之后使用df进行训练,同时砍掉神经网络部分的功能 ()"""
        # os.chdir('nerual_gui')
        self.msg.setText('注意! 该神经网络平台只能演示分类问题,回归预测正在开发中!')
        self.msg.show()
        self.msg.exec_()
        self.df = preprocess_data(self.df)
        self.fillTable()
        # visualize_data(self.df)
        # 导入模块 进行







class Main_windows(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Main_windows, self).__init__()
        self.setupUi(self)
        # 设置按钮的映射关系
        self.datawindows = Data_windows()
        self.edu_btn.clicked.connect(self.edu_clicked)
        self.exit_btn.clicked.connect(self.close)
        self.test_nerual.clicked.connect(lambda :self.datawindows.show())
        self.Remind_windows = Remind_windows()
        self.Remind_windows.show()
    def edu_clicked(self):
        self.datawindows.show()
        self.datawindows.loadEduFile()

    def paintEvent(self,event,bg_img='image/bg1.jpg'):
        painter = QPainter(self)
        pixmap = QPixmap(bg_img)
        painter.drawPixmap(self.rect(),pixmap)



class Remind_windows(Ui_remind_windows,QMainWindow):
    def __init__(self):
        super(Remind_windows, self).__init__()
        self.setupUi(self)
        self.Close_btn.clicked.connect(self.close)



def preprocess_data(data:pd.DataFrame):
    """
    对数据进行预处理：标准化和删除缺失值。

    :param data: pandas DataFrame，包含待处理的数据
    :return: 预处理后的DataFrame
    """
    # 分离target
    data = data.dropna()

    data_cleaned = data.iloc[:,:-1]
    label = data.iloc[:,-1]

    # 数据标准化

    # 应用标准化
    data_standardized = (data_cleaned - data_cleaned.min()) / (data_cleaned.max() - data_cleaned.min())

    return pd.concat([data_standardized,label])

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

if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    windows = Main_windows()
    windows.show()
    sys.exit(app.exec_())


