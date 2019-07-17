import torch.nn as nn


class BaseLoss(nn.Module):
    def __init__(self, output_key, target_key):
        super().__init__()
        self.output_key = output_key
        self.target_key = target_key
        self.loss_fn = None

    def _preprocess(self, logits, target):
        return logits, target

    def forward(self, data, output):
        logits = output[self.output_key]
        target = data[self.target_key]
        logits, target = self._preprocess(logits, target)

        return self.loss_fn(logits, target)


class CrossEntropyLoss(nn.Module):
    def __init__(self, output_key, target_key):
        super(CrossEntropyLoss, self).__init__()
        self.loss_fn = nn.CrossEntropyLoss()


class MSELoss(BaseLoss):
    def __init__(self, output_key, target_key):
        super().__init__(output_key, target_key)
        self.loss_fn = nn.MSELoss()
