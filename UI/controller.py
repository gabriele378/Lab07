import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()

        self._view.dropdown_musei.option.clear()
        self._view.dropdown_epoche.option.clear()

        self._view.dropdown_musei.options.append(ft.dropdown.Option("Nessun filtro"))
        for m in musei:
            self._view.dropdown_musei.options.append(ft.dropdown.Option(m))

        self._view.dropdown_epoche.options.append(ft.dropdown.Option("Nessun filtro"))
        for m in epoche:
            self._view.dropdown_epoche.options.append(ft.dropdown.Option(m))

        self.view.update()

    # CALLBACKS DROPDOWN
    # TODO

    def on_museo_change(self, e):
        self.museo_selezionato = e.control.value

    def on_epoche_change(self, e):
        self.epoca_selezionata = e.control.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO

    def mostra_artefatti(self, e):
        museo = None if self.museo_selezionato == "Nessun filtro" else self.museo_selezionato
        epoca = None if self.epoca_selezionata == "Nessun filtro" else self.epoca_selezionata


        artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato")
            return

        self._view.list_view.controls.clear()
        for a in artefatti:
            self._view.list_view.controls.append(ft.Text(f"{a.nome} ({a.epoca}) - ({a.museo})"))

        self._view.update()