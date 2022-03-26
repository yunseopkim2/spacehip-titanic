from context.domains import Dataset
from context.models import Model


class SpaceshipTemplate(object):
    model = Model()
    dateset = Dataset()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
