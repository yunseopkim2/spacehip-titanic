from context.domains import Dataset
import pandas as pd

class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dname ='./data/'
        this.sname = './save/'

    def get_sname(self):
        return self.ds.sname

    def new_model(self, fname)-> object:
        this = self.ds
        return pd.read_csv(f'{this.dfname}{fname}', index_col=0)

    def save_model(self, fname, dframe):
        this = self.ds
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rap='NaN')

    def new_dframe(self, fname) -> object:
        this = self.ds
        return pd.read_csv(f'{this.dname}{fname}')