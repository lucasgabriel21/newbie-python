def conversao(m):
    """converte um valor em m para dm,cm e mm em uma tupla"""
    dm = 10*m
    cm = 100*m
    mm = 1000*m
    return (dm,cm,mm)
