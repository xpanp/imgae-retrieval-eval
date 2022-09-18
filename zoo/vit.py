import timm
import torch

from .model import Model
from .registry import register_model

class ViT(Model):
    def __init__(self, model, ckp):
        super().__init__(model, ckp)
        print("torch version:", torch.__version__)
        print("timm version:", timm.__version__)
        self.model = self.get_model(model, ckp)
        print(model)
        print(self.transform)

    def get_model(self, model, ckp):
        return timm.create_model(model_name=model, pretrained=True)   

    def postprocessing(self, feature):
        if timm.__version__ >= '0.6.5':
            # cls [batch, 197, 768] -> [batch, 768]
            feature = feature[:, 0]
        return feature

@register_model
def vit(model, ckp):
    return ViT(model, ckp)