__author__ = 'ia'


class TriList:
    def __init__(self):
        self.main_d = dict()

    def add(self, nodo):
        """
        :type nodo: AEstrella.Nodo.Nodo
        """
        nodo_f = nodo.f()
        nodo_h = nodo.H
        if nodo_f not in self.main_d.keys():
            self.main_d[nodo_f] = {nodo_h:{nodo}}
        elif nodo_h not in self.main_d[nodo_f].keys():
            self.main_d[nodo_f][nodo_h] = {nodo}
        else:
            self.main_d[nodo_f][nodo_h].add(nodo)

    def remove(self, nodo):
        """

        :type nodo: AEstrella.Nodo.Nodo
        """
        nodo_f = nodo.f()
        nodo_h = nodo.H
        self.main_d[nodo_f][nodo_h].remove(nodo)
        self.clean_up(nodo_f, nodo_h)

    def clean_up(self, nodo_f, nodo_h):
        if len(self.main_d[nodo_f][nodo_h]) == 0:
            del self.main_d[nodo_f][nodo_h]
        if len(self.main_d[nodo_f]) == 0:
            del self.main_d[nodo_f]

    def pop_min(self):
        u_f = min(self.main_d)
        u_h = min(self.main_d[u_f])
        ret = self.main_d[u_f][u_h].pop()
        self.clean_up(u_f,u_h)
        return ret

        return ret

    def find(self, nodo):
        """
        :type nodo: AEstrella.Nodo.Nodo
        """
        nodo_f = nodo.f()
        nodo_h = nodo.H
        for key in self.main_d:
            if nodo_h not in self.main_d[key].keys():
                continue
            for elem in self.main_d[key][nodo_h]:
                if elem.Modelo.matrix == nodo.Modelo.matrix:
                    return elem
        return False

    def __len__(self):
        acc = 0
        for key in self.main_d:
            for inner in self.main_d[key]:
                acc += len(self.main_d[key][inner])
        return acc


