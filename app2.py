import gradio as gr
from MMEdu import MMClassification as cls
model = cls(backbone = 'MobileNet')
checkpoint='model/latest.pth'

def predict(img):
    result = model.inference(image=img, show=False, checkpoint=checkpoint)
    return str(result)

image = gr.inputs.Image(type="filepath")
demo = gr.Interface(fn=predict, inputs=image, outputs="text")
demo.launch(share=True)
