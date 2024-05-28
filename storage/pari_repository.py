from storage.pari import Pari

paris = []


def add_pari(name, challenger_name):
    paris.append(Pari(name, challenger_name))


def set_pari_taker(challenger_name, taker_name):
    for pari in paris:
        if pari.challenger_name == challenger_name and not hasattr(pari, taker_name):
            pari.set_taker(taker_name)
            return pari
