import smartpy as sp

@sp.module
def main():    
    class SpekunContract(sp.Contract):
        def __init__(self):
            self.data.sepeda = {}
            self.data.peminjam = sp.set()

        @sp.entrypoint
        def add_sepeda(self, params):
            assert not self.data.sepeda.contains(params.id_sepeda), 'id spekun telah terdaftar'
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some(params.node), self.data.sepeda)

        @sp.entrypoint
        def borrow_sepeda(self, params):
            assert sp.slice(0,4,self.data.sepeda[params.id_sepeda])  == sp.Some('node'), 'spekun telah dipinjam'
            assert not self.data.peminjam.contains(params.peminjam), 'peminjam telah meminjam spekun lain'
            self.data.peminjam.add(params.peminjam)
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some(params.peminjam), self.data.sepeda)

        @sp.entrypoint
        def return_sepeda(self, params):
            node = sp.slice(0,4,self.data.sepeda[params.id_sepeda])
            assert self.data.sepeda[params.id_sepeda] == params.peminjam, 'bukan peminjam'
            assert node != sp.Some('node'), 'spekun telah dikembalikan'
            self.data.peminjam.remove(params.peminjam)
            self.data.sepeda = sp.update_map(params.id_sepeda, sp.Some(params.node), self.data.sepeda)

@sp.add_test(name = "Spekun")
def test():
    scenario = sp.test_scenario(main)
    scenario.h1("Spekun")
    c1 = main.SpekunContract()
    scenario += c1
    c1.add_sepeda(id_sepeda='x123', node='node1')
    c1.add_sepeda(id_sepeda='x125', node='node2')
    c1.borrow_sepeda(id_sepeda='x123', peminjam='1906350824')
    c1.return_sepeda(id_sepeda='x123', peminjam='1906350824', node='node2')