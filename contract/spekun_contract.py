import smartpy as sp

@sp.module
def main():
    class SpekunContract(sp.Contract):
        def __init__(self):
            self.data.sepeda = {}

        @sp.entrypoint
        def add_sepeda(self, params):
            assert not self.data.sepeda.contains(params.id_sepeda), 'id spekun telah terdaftar'
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some('idle'), self.data.sepeda)

        @sp.entrypoint
        def borrow_sepeda(self, params):
            assert self.data.sepeda[params.id_sepeda] == 'idle', 'spekun telah dipinjam'
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some(params.peminjam), self.data.sepeda)

        @sp.entrypoint
        def return_sepeda(self, params):
            assert self.data.sepeda[params.id_sepeda] != 'idle', 'spekun telah dikembalikan'
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some('idle'), self.data.sepeda)

@sp.add_test(name = "Spekun")
def test():
    scenario = sp.test_scenario(main)
    scenario.h1("Spekun")
    c1 = main.SpekunContract()
    scenario += c1
    c1.add_sepeda(id_sepeda='x123')
    c1.add_sepeda(id_sepeda='x125')
    c1.borrow_sepeda(id_sepeda='x123', peminjam='rafi')
    c1.borrow_sepeda(id_sepeda='x125', peminjam='rafi')
    c1.return_sepeda(id_sepeda='x123')
    c1.return_sepeda(id_sepeda='x125')