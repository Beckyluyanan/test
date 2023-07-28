import numpy as np
import gradio as gr
# 定义一个方法：输入一张图片，将图片不做任何处理就输出
def display(input_img):
    return input_img

# 使用gradio库的Interface方法创建一个用户界面。这个界面包括一个接收用户在canvas中绘制的图片的输入框和一个显示图片的输出框。
# 其中，图片的形状被设定为(100,100)，源被设置为"canvas"，表示输入图片是用户在canvas中绘制的
demo = gr.Interface(fn=display,  inputs=gr.Image(shape=(100, 100),source="canvas"), outputs="image")
demo.launch(share=True)
