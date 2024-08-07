
class ComfyUIWebAnnotator:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "标注节点接入": ("*"),
                "序号": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "参数名称": (
                    "STRING",
                    {"multiline": False, "default": "参数名称"},
                ),
                "类型":  (["image", "selection", "text","image_editer",], ),
                "数值约束/依赖项":  (
                    "STRING",
                    {"multiline": False, "default": ".png,.jpg,.jpeg,.webp"},),
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


NODE_CLASS_MAPPINGS = {"ComfyUI-Shangxiaobao": ComfyUIWebAnnotator}
NODE_DISPLAY_NAME_MAPPINGS = {"Shangxiaobao": "ComfyUI-Shangxiaobao"}