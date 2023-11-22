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
