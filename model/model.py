from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.G = nx.Graph()
        self._idMap = {}

    def costruisci_grafo(self, valore_minimo):
        self.G.clear()


        self._nodes = DAO.read_hubs()
        self.G.add_nodes_from(self._nodes)
        for nodo in self._nodes:
            self._idMap[nodo.id] = nodo


        tratte_direzionali = DAO.get_spedizioni()


        temp_edges = {}


        for spedizione in tratte_direzionali:
            u = spedizione.id_hub_origine
            v = spedizione.id_hub_destinazione
            tot_valore = spedizione.guadagno
            count = spedizione.conteggio

            if u < v:
                key = (u, v)
            else:
                key = (v, u)

            if key not in temp_edges:
                temp_edges[key] = {'tot_valore': 0, 'count': 0}

            temp_edges[key]['tot_valore'] += tot_valore
            temp_edges[key]['count'] += count

        for (u_id, v_id), stats in temp_edges.items():
            media = stats['tot_valore'] / stats['count']

            if media >= valore_minimo:
                if u_id in self._idMap and v_id in self._idMap:
                    nodo_u = self._idMap[u_id]
                    nodo_v = self._idMap[v_id]
                    self.G.add_edge(nodo_u, nodo_v, weight=media)

    def get_num_edges(self):
        return self.G.number_of_edges()

    def get_num_nodes(self):
        return self.G.number_of_nodes()

    def get_all_edges(self):
        edges_data = []
        for u, v, data in self.G.edges(data=True):
            edges_data.append((u, v, data['weight']))
        edges_data.sort(key=lambda x: x[2], reverse=True)
        return edges_data