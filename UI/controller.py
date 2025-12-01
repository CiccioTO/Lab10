import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info:
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        soglia_str = float(self._view.guadagno_medio_minimo.value)


        if not soglia_str:
            self._view.show_alert("Inserire un valore per il guadagno minimo!")
            return



        self._model.costruisci_grafo(soglia_str)

        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()
        elenco_archi = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()


        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hub: {num_nodi}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte valide: {num_archi}")
        )
        self._view.lista_visualizzazione.controls.append(
            ft.Divider()
        )

        if not elenco_archi:
            self._view.lista_visualizzazione.controls.append(
                ft.Text("Nessuna tratta trovata con questa soglia.")
            )
        else:
            for u, v, peso in elenco_archi:

                row_text = f"{u} -> {v}  |  {peso:.2f} €"
                self._view.lista_visualizzazione.controls.append(ft.Text(row_text))

        self._view.update()