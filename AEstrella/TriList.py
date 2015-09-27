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


class PentaList:
    def __init__(self):
        self.main = dict()

    def add(self, nodo):
        """
        :type nodo: AEstrella.Nodo.Nodo
        """

        keys = self.keyMaker(nodo.Modelo.matrix)
        if keys[0] not in self.main.keys():
            self.main[keys[0]]={keys[1]:{keys[2]:{keys[3]:{keys[4]:nodo}}}}
        elif keys[1] not in self.main[keys[0]].keys():
            self.main[keys[0]][keys[1]]={keys[2]:{keys[3]:{keys[4]:nodo}}}
        elif keys[2] not in self.main[keys[0]][keys[1]].keys():
            self.main[keys[0]][keys[1]][keys[2]]={keys[3]:{keys[4]:nodo}}
        elif keys[3] not in self.main[keys[0]][keys[1]][keys[2]].keys():
            self.main[keys[0]][keys[1]][keys[2]][keys[3]]= {keys[4]:nodo}
        else:
            self.main[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]=nodo

    def keyMaker(self,matrix):
        keys = list(map(lambda x: "".join(x),matrix))
        return keys

    def remove(self, nodo):
        """
        :type nodo: AEstrella.Nodo.Nodo
        """

        keys = self.keyMaker(nodo.Modelo.matrix)
        del self.main[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]
        if len(self.main[keys[0]][keys[1]][keys[2]][keys[3]])==0:
            del self.main[keys[0]][keys[1]][keys[2]][keys[3]]
        if len(self.main[keys[0]][keys[1]][keys[2]])==0:
            del self.main[keys[0]][keys[1]][keys[2]]
        if len(self.main[keys[0]][keys[1]]) == 0:
            del self.main[keys[0]][keys[1]]
        if len(self.main[keys[0]]) == 0:
            del self.main[keys[0]]

    def find(self, nodo):
        """
        :type nodo: AEstrella.Nodo.Nodo
        """
        keys = self.keyMaker(nodo.Modelo.matrix)
        if keys[0] not in self.main.keys():
            return False
        elif keys[1] not in self.main[keys[0]].keys():
            return False
        elif keys[2] not in self.main[keys[0]][keys[1]].keys():
            return False
        elif keys[3] not in self.main[keys[0]][keys[1]][keys[2]].keys():
            return False
        elif keys[4] not in self.main[keys[0]][keys[1]][keys[2]][keys[3]].keys():
            return False
        else:
            return self.main[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]




