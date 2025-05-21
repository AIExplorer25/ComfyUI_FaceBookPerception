from huggingface_hub.hf_api import HfFolder
# get your token here https://huggingface.co/settings/tokens


import os
import torch
from PIL import Image
import time
from IPython.display import HTML
from base64 import b64encode
import textwrap
import requests
import urllib.request
from comfy.k_diffusion.utils import FolderOfImages
from core.args import dataclass_from_dict
from core.transforms.image_transform import get_image_transform
from core.transforms.video_transform import get_video_transform
from apps.plm.generate import PackedCausalTransformerGeneratorArgs, PackedCausalTransformerGenerator, load_consolidated_model_and_tokenizer



class ImagePerception:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_name": ("STRING", {"multiline": True, "default": "facebook/Perception-LM-8B"}),
                "media_path": ("STRING", {"multiline": True, "default": ""}),
                "image": ("STRING", {"placeholder": "X://insert/path/here.png", "vhs_path_extensions": list(FolderOfImages.IMG_EXTENSIONS)}),
                "question": ("STRING", {"multiline": True, "default": "Describe the image in details."}),
                "media_type": ("STRING", {"multiline": True, "default": ""}),
                "number_of_frames": ("INT", { "default": 4, "min": 0, "max": 100}),
                "number_of_tiles": ("INT", { "default": 1, "min": 0, "max": 100}),
                "temperature": ("FLOAT", { "default": 0.0, "min": 0, "max": 100}),
                "top_p": ("INT", { "default": None, "min": 0, "max": 100}),
                "top_k": ("INT", { "default": None, "min": 0, "max": 100}),
          
            }
        }

    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_caption",)
    FUNCTION = "generate_captions"
    OUTPUT_NODE = True
    CATEGORY = "utils"


    
    def generate_captions(self,model_name,media_path, image, question, media_type, number_of_frames, number_of_tiles, temperature, top_p, top_k):
        # Handle case where inputs are not lists
        print("inside generate_captions function...")
        
        
        return ", ".join("output"),



NODE_CLASS_MAPPINGS = {
    "ImagePerception": ImagePerception,

    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImagePerception": "Image Perception FB",


}
