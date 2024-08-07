import folder_paths
from PIL import Image, ImageOps
import numpy as np
import torch

class ComfyUIWebAnnotator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "序号": (
                    "STRING",
                    {"multiline": False, "default": "1"},
                ),
                "名称": (
                    "STRING",
                    {"multiline": False, "default": "image"},
                ),
                "类型": (
                    "STRING",
                    {"multiline": False, "default": "image"},
                ),
                "依赖项": (
                    "STRING",
                    {"multiline": False, "default": "image"},
                ),
                "替换项": (
                    "STRING",
                    {"multiline": False, "default": "amount"},
                ),
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()

    FUNCTION = "run"

    CATEGORY = "image"

    def run(self, input_id, default_value=None):
        return


NODE_CLASS_MAPPINGS = {"ComfyUIWebAnnotator": ComfyUIWebAnnotator}
NODE_DISPLAY_NAME_MAPPINGS = {"ComfyUIWebAnnotator": "Comfyui Annotator (ComfyUI Web)"}