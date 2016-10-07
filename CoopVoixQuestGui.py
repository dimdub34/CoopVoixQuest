# -*- coding: utf-8 -*-
"""
This module contains the GUI
"""

import logging
from PyQt4 import QtGui, QtCore
from util.utili18n import le2mtrans
from datetime import datetime
import CoopVoixQuestParams as pms
from CoopVoixQuestTexts import trans_CVQ
import CoopVoixQuestTexts as texts_CVQ
from client.cltgui.cltguidialogs import GuiHistorique
from client.cltgui.cltguiwidgets import WPeriod, WExplication, WSpinbox


logger = logging.getLogger("le2m")


class GuiDecision(QtGui.QDialog):
    # def __init__(self, defered, automatique, parent, period, historique):
    def __init__(self, defered, automatique, parent):

        super(GuiDecision, self).__init__(parent)

        # variables
        self._defered = defered
        self._automatique = automatique
        # self._historique = GuiHistorique(self, historique)

        layout = QtGui.QVBoxLayout(self)

        # should be removed if one-shot game
        # wperiod = WPeriod(
        #     period=period, ecran_historique=self._historique)
        # layout.addWidget(wperiod)

        wexplanation = WExplication(
            text=texts_CVQ.get_text_explanation(),
            size=(450, 80), parent=self)
        layout.addWidget(wexplanation)

        gridlayout = QtGui.QGridLayout()
        layout.addLayout(gridlayout)

        # naissance ============================================================
        gridlayout.addWidget(QtGui.QLabel(u"Votre mois de naissance"), 0, 0)
        self._combo_naissance_mois = QtGui.QComboBox()
        self._combo_naissance_mois.addItems(
            [u"Choisir", u"janvier", u"février", u"mars", u"avril", u"mai",
             u"juin", u"juillet", u"août", u"septembre", u"octobre",
             u"novembre", u"décembre"])
        gridlayout.addWidget(self._combo_naissance_mois, 0, 1)
        gridlayout.addWidget(QtGui.QLabel(u"Votre année de naissance"), 0, 2)
        today_year = datetime.now().year
        self._spin_naissance_annee = QtGui.QSpinBox()
        self._spin_naissance_annee.setMinimum(today_year - 100)
        self._spin_naissance_annee.setMaximum(today_year)
        self._spin_naissance_annee.setSingleStep(1)
        self._spin_naissance_annee.setValue(today_year)
        self._spin_naissance_annee.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_naissance_annee, 0, 3)

        # parents ==============================================================
        gridlayout.addWidget(QtGui.QLabel(u"Année de naissance de votre père"), 1, 0)
        self._spin_naissance_annee_pere = QtGui.QSpinBox()
        self._spin_naissance_annee_pere.setMinimum(today_year - 100)
        self._spin_naissance_annee_pere.setMaximum(today_year)
        self._spin_naissance_annee_pere.setSingleStep(1)
        self._spin_naissance_annee_pere.setValue(today_year)
        self._spin_naissance_annee_pere.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_naissance_annee_pere, 1, 1)

        gridlayout.addWidget(QtGui.QLabel(u"Année de naissance de votre mère"), 1, 2)
        self._spin_naissance_annee_mere = QtGui.QSpinBox()
        self._spin_naissance_annee_mere.setMinimum(today_year - 100)
        self._spin_naissance_annee_mere.setMaximum(today_year)
        self._spin_naissance_annee_mere.setSingleStep(1)
        self._spin_naissance_annee_mere.setValue(today_year)
        self._spin_naissance_annee_mere.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_naissance_annee_mere, 1, 3)

        # situation maritale ===================================================
        gridlayout.addWidget(QtGui.QLabel(u"Etes-vous en couple?"), 2, 0)
        self._radio_couple_oui = QtGui.QRadioButton(u"oui")
        self._radio_couple_non = QtGui.QRadioButton(u"non")
        self._radio_couple_group = QtGui.QButtonGroup()
        self._radio_couple_group.addButton(self._radio_couple_oui)
        self._radio_couple_group.addButton(self._radio_couple_non)
        self._layout_couple = QtGui.QHBoxLayout()
        self._layout_couple.addWidget(self._radio_couple_oui)
        self._layout_couple.addWidget(self._radio_couple_non)
        gridlayout.addLayout(self._layout_couple, 2, 1)

        gridlayout.addWidget(QtGui.QLabel(u"Depuis combien de temps?"), 2, 2)
        self._combo_couple = QtGui.QComboBox()
        self._combo_couple.addItems(pms.COUPLE_LISTE)
        gridlayout.addWidget(self._combo_couple, 2, 3)

        gridlayout.addWidget(QtGui.QLabel(u"Année de naissance de votre partenaire"), 2, 4)
        self._spin_couple_partenaire_naissance = QtGui.QSpinBox()
        self._spin_couple_partenaire_naissance.setMinimum(today_year - 100)
        self._spin_couple_partenaire_naissance.setMaximum(today_year)
        self._spin_couple_partenaire_naissance.setSingleStep(1)
        self._spin_couple_partenaire_naissance.setValue(today_year)
        self._spin_couple_partenaire_naissance.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_couple_partenaire_naissance, 2, 5)

        self._combo_couple.setEnabled(False)
        self._spin_couple_partenaire_naissance.setEnabled(False)
        self._radio_couple_group.buttonClicked.connect(self._enable_couple)

        gridlayout.addWidget(QtGui.QLabel(
            u"Combien de partenaires sexuels du sexe opposé avez-vous eu au "
            u"cours de toute votre vie?"), 3, 0, 1, 3)
        self._spin_couple_partenaire_hetero = QtGui.QSpinBox()
        self._spin_couple_partenaire_hetero.setMinimum(0)
        self._spin_couple_partenaire_hetero.setMaximum(100)
        self._spin_couple_partenaire_hetero.setSingleStep(1)
        self._spin_couple_partenaire_hetero.setValue(0)
        self._spin_couple_partenaire_hetero.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_couple_partenaire_hetero, 3, 3)

        gridlayout.addWidget(QtGui.QLabel(
            u"Combien de partenaires sexuels du même sexe avez-vous eu au "
            u"cours de toute votre vie?"), 4, 0, 1, 3)
        self._spin_couple_partenaire_homo = QtGui.QSpinBox()
        self._spin_couple_partenaire_homo.setMinimum(0)
        self._spin_couple_partenaire_homo.setMaximum(100)
        self._spin_couple_partenaire_homo.setSingleStep(1)
        self._spin_couple_partenaire_homo.setValue(0)
        self._spin_couple_partenaire_homo.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        gridlayout.addWidget(self._spin_couple_partenaire_homo, 4, 3)

        # self._wdecision = WSpinbox(
        #     label=trans_CVQ(u"label decision"),
        #     minimum=pms.DECISION_MIN, maximum=pms.DECISION_MAX,
        #     interval=pms.DECISION_STEP, automatique=self._automatique,
        #     parent=self)
        # layout.addWidget(self._wdecision)

        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        buttons.accepted.connect(self._accept)
        layout.addWidget(buttons)

        self.setWindowTitle(trans_CVQ(u"Questionnaire"))
        self.adjustSize()
        self.setFixedSize(self.size())

        if self._automatique:
            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(
                buttons.button(QtGui.QDialogButtonBox.Ok).click)
            self._timer_automatique.start(7000)

    def _enable_couple(self):
        if self._radio_couple_oui.isChecked():
            self._combo_couple.setEnabled(True)
            self._spin_couple_partenaire_naissance.setEnabled(True)
        else:
            self._combo_couple.setEnabled(False)
            self._spin_couple_partenaire_naissance.setEnabled(False)

                
    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        # decision = self._wdecision.get_value()
        answers = {}
        if not self._automatique:
            confirmation = QtGui.QMessageBox.question(
                self, le2mtrans(u"Confirmation"),
                le2mtrans(u"Do you confirm your choice?"),
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            if confirmation != QtGui.QMessageBox.Yes: 
                return
        logger.info(u"Send back {}".format(answers))
        self.accept()
        self._defered.callback(answers)
