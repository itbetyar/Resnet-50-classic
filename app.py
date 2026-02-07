######################################
#######################
### IT Betyár  2024.03

## Egyszeru, oktatasi celu, AI modell deployement minta, kepfelismerese
## https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/

## Frissítve 2026.02

import gradio as gr
import torch
from timm import create_model
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import requests

IMAGENET_1k_URL = "https://storage.googleapis.com/bit_models/ilsvrc2012_wordnet_lemmas.txt"
LABELS = requests.get(IMAGENET_1k_URL).text.strip().split('\n')

model = create_model('resnet50', pretrained=True)
transform = create_transform(**resolve_data_config({}, model=model))
model.eval()

def predict_fn(img):
    img = img.convert('RGB')
    img = transform(img).unsqueeze(0)
    with torch.no_grad():
        out = model(img)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)
    values, indices = torch.topk(probabilities, k=5)

    # Get the top labels and select only the first part of the label
    top_labels = [LABELS[i].split(',')[0] for i in indices]

    # Return only the label and its probability
    return {top_labels[i]: values[i].item() for i in range(5)}


# HTML for the header
header_html = """
<div style="text-align: center; max-width: 650px; margin: 0 auto;">
    <img src="https://huggingface.co/spaces/itbetyar/gradio-demo/resolve/main/imgclass.webp" alt="Header Image" style="max-width: 100%; height: auto; margin: 20px 0;">
    <h1 style="color: #67768c; font-size: 2.5em;">IT Betyár | Resnet 50 Image Classifier</h1>
    <p style="color: #FFFFFF; font-size: 1.2em;">
        Üdvözlünk képosztályozónkban! Ez egy oktatási minta app, ami a <b>ResNet50</b> A.I. modellt használja
        a képek osztályozására. Tölts fel egy képet, és megmutatjuk a három legjobb predikciót.
    </p>
        <p style="color: #92F8FD; font-size: 1.2em;">
        Figyelem! Egyszerűségre és érthetőségre törekvő, oktatási kód, nem a csúcsmodern rendszereket használja!
    </p>
</div>
"""

with gr.Blocks() as demo:
    gr.HTML(header_html)
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type='pil', label="Tölts fel egy képet...", width=500, height=400, sources=["upload","webcam"])
            
            with gr.Row():
                clear_btn = gr.Button("Reset")
                classify_btn = gr.Button("Mehet")
            
            
        with gr.Column():
            gr.HTML("""<div style="background: #27272A; padding:15px; font-size:16px;">
                    Alább láthatod a kép osztályozás eredményét</div>""")
            output = gr.Label(num_top_classes=3, label="A kép osztálya:")
    
    classify_btn.click(predict_fn, inputs=input_image, outputs=output)
    clear_btn.click(lambda: [None, None], inputs=None, outputs=[input_image, output])

# Add examples section properly
    with gr.Row():
        gr.Examples(
                examples=[
                    "imgs/lion.jpg",
                    "imgs/car.jpg", 
                    "imgs/cheetah.jpg",
                    "imgs/banana.jpg",
                    "imgs/bus.jpg",
                    "imgs/parfum.jpg",
                    "imgs/alligator.jpg",
                    "imgs/arc.jpg"
                ],
                inputs=input_image, label="Betölthető minták"
            )
        
    with gr.Row():    
        gr.HTML("""<div style="margin:100px;"></div>""")

demo.launch()

### IT Betyár  2024.03

## Egyszeru, oktatasi celu, AI modell deployement minta, kepfelismerese
## https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/

## Frissítve 2026.02
#######################
######################################