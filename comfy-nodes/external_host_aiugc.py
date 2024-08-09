import folder_paths
from PIL import Image, ImageOps
import numpy as np
import torch

class ComfyUIWebHost:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ComfyUI 主机地址":  (
                    "STRING",
                    {"multiline": False, "default": "shangxiaobao.com:7190"},),                
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()

    FUNCTION = "run"

    CATEGORY = "AIUGC"

    def run(self, input_id, default_value=None):
        return


NODE_CLASS_MAPPINGS = {"ComfyUIWebHost": ComfyUIWebHost}
NODE_DISPLAY_NAME_MAPPINGS = {"ComfyUIWebHost": "Comfyui AIUGC Host (ComfyUI-aiugc)"}