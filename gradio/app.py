# Use a pipeline as a high-level helper
import gradio as gr

from transformers import pipeline

pipe = pipeline("translation", model="ayoubkirouane/Med_English2Spanish")
def predict(text):
  return pipe(text)[0]["translation_text"]

with gr.Blocks() as demo:
    english_inp = gr.Textbox(label="English Sentence")
    spanish_op = gr.Textbox(label="Spanish Translation")
    translate_btn = gr.Button("Translate")
    translate_btn.click(fn=predict, inputs=english_inp, outputs=spanish_op)

demo.launch()