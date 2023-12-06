### style sheet

当使用Qt的StyleSheet来设置背景时，你可以使用一些属性和值来控制背景的外观和行为。以下是一些有关背景样式的常见属性和值：

1. `background-color`: 设置背景颜色。
   
   ```
   background-color: #RRGGBB;
   ```

2. `background-image`: 设置背景图像。
   
   ```
   background-image: url("image.jpg");
   ```

3. `background-repeat`: 设置背景图像的重复方式。
   
   - `no-repeat`: 图像不重复，只显示一次。
   - `repeat`: 图像在水平和垂直方向上重复。
   - `repeat-x`: 图像在水平方向上重复。
   - `repeat-y`: 图像在垂直方向上重复。

4. `background-position`: 设置背景图像的位置。
   
   ```
   background-position: center;
   ```

5. `background-size`: 设置背景图像的大小。
   
   ```
   background-size: cover;  /* 图像保持纵横比，尽量填充整个区域 */
   ```

6. `background-origin`: 设置背景图像的起始位置。
   
   - `padding-box`: 从内边距区域开始绘制。
   - `border-box`: 从边框区域开始绘制。
   - `content-box`: 从内容区域开始绘制。

7. `background-attachment`: 设置背景图像的滚动行为。
   
   - `scroll`: 背景图像会跟随内容滚动。
   - `fixed`: 背景图像固定在视口中，不随内容滚动。

这些属性和值可以结合使用，以实现不同的背景效果。例如，你可以将背景颜色和背景图像一起使用，或者设置背景图像的位置和大小来控制其显示方式。通过调整这些属性和值，你可以创建各种不同的背景效果，以满足你的界面设计需求。

Qt的StyleSheet支持许多其他常见的参数，用于控制部件的外观和行为。以下是一些常见的StyleSheet参数和示例：

1. `color`: 设置文本颜色。
   
   ```
   color: red;
   ```

2. `font-family`: 设置字体家族。
   
   ```
   font-family: Arial, sans-serif;
   ```

3. `font-size`: 设置字体大小。
   
   ```
   font-size: 16px;
   ```

4. `font-weight`: 设置字体粗细。
   
   ```
   font-weight: bold;
   ```

5. `text-align`: 设置文本对齐方式。
   
   ```
   text-align: center;
   ```

6. `border`: 设置边框样式。
   
   ```
   border: 1px solid #000;
   ```

7. `border-radius`: 设置边框圆角半径。
   
   ```
   border-radius: 5px;
   ```

8. `padding`: 设置内边距。
   
   ```
   padding: 10px;
   ```

9. `margin`: 设置外边距。
   
   ```
   margin: 20px;
   ```

10. `width` 和 `height`: 设置部件的宽度和高度。
    
    ```
    width: 100px;
    height: 50px;
    ```

11. `min-width` 和 `min-height`: 设置部件的最小宽度和最小高度。
    
    ```
    min-width: 50px;
    min-height: 30px;
    ```

12. `max-width` 和 `max-height`: 设置部件的最大宽度和最大高度。
    
    ```
    max-width: 200px;
    max-height: 100px;
    ```

13. `opacity`: 设置部件的不透明度。
    
    ```
    opacity: 0.5; /* 取值范围从0（完全透明）到1（完全不透明） */
    ```

14. `background-color`: 设置背景颜色。
    
    ```
    background-color: #F0F0F0;
    ```

15. `border-color`: 设置边框颜色。
    
    ```
    border-color: #333;
    ```

16. `border-width`: 设置边框宽度。
    
    ```
    border-width: 2px;
    ```

17. `border-style`: 设置边框样式。
    
    ```
    border-style: dashed;
    ```

这些是一些常见的StyleSheet参数，你可以使用它们来自定义部件的样式，以满足你的界面设计需求。通过组合和调整这些参数，你可以创建各种不同的外观效果。注意，不同的部件类型可能支持不同的参数，你可以查阅Qt的文档以获取更多信息。

### pyqt与matplotlib结合

---

# 在 PyQt 中集成 Matplotlib：打造动态数据可视化应用

## 引言

在现代软件开发中，数据可视化是一个重要的组成部分，尤其是在需要实时展示数据的场景中。PyQt 作为一个强大的跨平台 GUI 库，配合 Matplotlib 这个数据可视化的重要工具，可以创建功能丰富的桌面应用。然而，要将这两个工具结合起来，需要了解它们之间的一些兼容性细节。

## 为什么选择 PyQt 和 Matplotlib







### 使用 Matplotlib 的 FigureCanvas

1. **FigureCanvas 的引入**：Matplotlib 提供了一个特殊的 Qt 控件，名为 `FigureCanvasQTAgg`，这是一个将 Matplotlib 图表渲染为 Qt 控件的桥梁。
2. **创建绘图区域**：首先在 PyQt 中创建一个窗口或面板，用于承载 Matplotlib 图表。
3. **集成图表**：将 Matplotlib 的图表作为一个 `FigureCanvasQTAgg` 实例添加到 PyQt 的布局中。
   
   布局**QMainWindows -> central_widget-> Layout ->  Figure**
   
   ```python
     # 创建主窗口容器
     central_widget = QWidget()
     self.setCentralWidget(central_widget)
     layout = QVBoxLayout(central_widget)
   
     # 创建Matplotlib图形容器
     self.figure = Figure(figsize=(10, 8))
     self.canvas = FigureCanvas(self.figure)
     layout.addWidget(self.canvas)
   ```
   1. **创建主窗口容器 (`central_widget`)**:
      
      - `central_widget = QWidget()`：这行代码创建了一个 QWidget 实例，这个实例是所有其他界面元素的容器。
      - `self.setCentralWidget(central_widget)`：这行代码将刚创建的 `central_widget` 设置为主窗口的中心部件。在 PyQt 的 `QMainWindow` 结构中，中心部件可以占据大部分的窗口空间。
   
   2. **设置布局 (`layout`)**:
      
      - `layout = QVBoxLayout(central_widget)`：这里创建了一个垂直布局（`QVBoxLayout`），并将它设置在 `central_widget` 上。这个布局将决定如何垂直排列添加到 `central_widget` 的子部件。
   
   3. **创建 Matplotlib 图形容器**:
      
      - `self.figure = Figure(figsize=(10, 8))`：创建一个 Matplotlib 图形实例 `Figure`，这个实例是绘图的基础，相当于绘图的画布。
      - `self.canvas = FigureCanvas(self.figure)`：这行代码将前面创建的 Matplotlib 图形（即 `self.figure`）包装到一个 `FigureCanvas` 中，`FigureCanvas` 是一个 PyQt 部件，它使 Matplotlib 的图形能够被嵌入到 PyQt 的窗口部件中。
   
   4. **将 Matplotlib 图形添加到布局**:
      
      - `layout.addWidget(self.canvas)`：最后，这行代码将 Matplotlib 的画布（封装在 `FigureCanvas` 中）添加到之前创建的垂直布局中。这意味着 Matplotlib 的图形会被放置在 `central_widget` 中，并遵循垂直布局的规则。
   
   



接下来，通过一个具体的例子来展示整个过程。这个例子会创建一个简单的 PyQt 应用，其中包含一个动态更新的 Matplotlib 图表。

### 步骤一：设置 PyQt 环境

```python
# PyQt 相关导入
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# Matplotlib 相关导入
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei'

# 其他必要导入
import sys
```

### 步骤二：集成 Matplotlib

```python
]


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

# 应用启动
app = QApplication(sys.argv)
main = MainApp()
main.show()
sys.exit(app.exec_())
```

我们直接在画布上，就正常的使用就行了

`Qtable`的运用

### 创造Qtable

Qtable 也是一种控件 **QtWidget** Qt的控件。

你需要分清楚**Widget - Layout**,Layout是布局，所有的都在上面

```python
        self.Data = QTableWidget(self.layoutWidget)
        self.Data.setRowCount(n)
        self.Data.setColumnCount(m)


        # 现在 df.columns 已经是字符串类型了
        self.Data.setHorizontalHeaderLabels(self.columns)
        # 填充表格的数据
        for i in range(n):
            for j in range(m):
                # 设置表格
                self.Data.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))
```

### 在程序中创造小窗口

`self.msg = QmessageBox ` 保存这个的变量

使用`msg.setText()设置为你`

项目文件 我们如何进行包的导入 然后让他分模块能够分的更加细致。
