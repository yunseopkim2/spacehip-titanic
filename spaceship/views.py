from context.models import Model
from context.domains import Dataset

class SpaceshipView:
    model = Model()
    dataset = Dataset()

    def preprocess(self, train, test) -> object:
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)

        print(f'트레인 컬럼 {this.train.colums}')
        print(f'트레인 헤드 {this.train.head()}')