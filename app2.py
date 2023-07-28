import gradio as gr
import BaseDeploy as bd

model_path = 'model/cats_dogs.onnx'

def predict(img):
    model = bd(model_path)
    result = model.inference(img)
    result = model.print_result(result)
    return result

image = gr.inputs.Image(type="filepath",source="webcam")
demo = gr.Interface(fn=predict, inputs=image, outputs="text")
demo.launch(share=True)
