# -*- coding: utf-8 -*-
"""
This module contains the GUI
"""

import logging
from PyQt4 import QtGui, QtCore
from util.utili18n import le2mtrans
from datetime import datetime, time
from random import randint
import CoopVoixQuestParams as pms
from CoopVoixQuestTexts import trans_CVQ
import CoopVoixQuestTexts as texts_CVQ
from client.cltgui.cltguiwidgets import WExplication
from configuration.configvar import COUNTRIES


logger = logging.getLogger("le2m")


class MyHline(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)


class MyLabel(QtGui.QLabel):
    def __init__(self, text):
        QtGui.QLabel.__init__(self, text)
        self.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)


class MyHBoxLayout(QtGui.QHBoxLayout):
    def __init__(self, widgets_to_add):
        QtGui.QHBoxLayout.__init__(self)
        for e in widgets_to_add:
            self.addWidget(e)
        self.addSpacerItem(
            QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Expanding,
                              QtGui.QSizePolicy.Minimum))


class GuiDemo(QtGui.QDialog):
    def __init__(self, defered, automatique, parent):

        super(GuiDemo, self).__init__(parent)

        self._defered = defered
        self._automatique = automatique

        layout = QtGui.QVBoxLayout(self)

        wexplanation = WExplication(
            text=texts_CVQ.get_text_explanation_demo(),
            size=(450, 80), parent=self)
        layout.addWidget(wexplanation)

        gridlayout = QtGui.QGridLayout()
        gridlayout.setHorizontalSpacing(20)
        layout.addLayout(gridlayout)

        CURRENT_LINE = 0
        self._current_year = datetime.now().year

        # naissance ============================================================
        gridlayout.addWidget(MyLabel(u"Votre mois de naissance"), CURRENT_LINE, 0)
        self._combo_naissance_mois = QtGui.QComboBox()
        self._combo_naissance_mois.addItems(
            [u"Choisir", u"janvier", u"février", u"mars", u"avril", u"mai",
             u"juin", u"juillet", u"août", u"septembre", u"octobre",
             u"novembre", u"décembre"])
        self._combo_naissance_mois.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_naissance_mois, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Votre année de naissance"), CURRENT_LINE, 2)
        self._spin_naissance_annee = QtGui.QSpinBox()
        self._spin_naissance_annee.setMinimum(self._current_year - 100)
        self._spin_naissance_annee.setMaximum(self._current_year)
        self._spin_naissance_annee.setSingleStep(1)
        self._spin_naissance_annee.setValue(self._current_year)
        self._spin_naissance_annee.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_naissance_annee.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_naissance_annee, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Pays de naissance"), CURRENT_LINE, 4)
        pays = [u"Choisir"]
        pays.extend(sorted(COUNTRIES.viewvalues()))
        self._combo_naissance_pays = QtGui.QComboBox()
        self._combo_naissance_pays.addItems(pays)
        self._combo_naissance_pays.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_naissance_pays, CURRENT_LINE, 5)

        CURRENT_LINE += 1

        # parents ==============================================================
        gridlayout.addWidget(MyLabel(u"Année de naissance de votre père"), CURRENT_LINE, 0)
        self._spin_naissance_annee_pere = QtGui.QSpinBox()
        self._spin_naissance_annee_pere.setMinimum(self._current_year - 100)
        self._spin_naissance_annee_pere.setMaximum(self._current_year)
        self._spin_naissance_annee_pere.setSingleStep(1)
        self._spin_naissance_annee_pere.setValue(self._current_year)
        self._spin_naissance_annee_pere.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_naissance_annee_pere.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_naissance_annee_pere, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Année de naissance de votre mère"), CURRENT_LINE, 2)
        self._spin_naissance_annee_mere = QtGui.QSpinBox()
        self._spin_naissance_annee_mere.setMinimum(self._current_year - 100)
        self._spin_naissance_annee_mere.setMaximum(self._current_year)
        self._spin_naissance_annee_mere.setSingleStep(1)
        self._spin_naissance_annee_mere.setValue(self._current_year)
        self._spin_naissance_annee_mere.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_naissance_annee_mere.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_naissance_annee_mere, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        # situation maritale ===================================================
        gridlayout.addWidget(MyLabel(u"Etes-vous en couple?"), CURRENT_LINE, 0)
        self._radio_couple_oui = QtGui.QRadioButton(u"oui")
        self._radio_couple_non = QtGui.QRadioButton(u"non")
        self._radio_couple_group = QtGui.QButtonGroup()
        self._radio_couple_group.addButton(self._radio_couple_oui, 1)
        self._radio_couple_group.addButton(self._radio_couple_non, 0)
        self._layout_couple = MyHBoxLayout(
            [self._radio_couple_oui, self._radio_couple_non])
        gridlayout.addLayout(self._layout_couple, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Depuis combien de temps?"), CURRENT_LINE, 2)
        self._combo_couple = QtGui.QComboBox()
        self._combo_couple.addItems(pms.COUPLE_LISTE)
        self._combo_couple.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_couple, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Année de naissance de votre partenaire"), CURRENT_LINE, 4)
        self._spin_couple_partenaire_naissance = QtGui.QSpinBox()
        self._spin_couple_partenaire_naissance.setMinimum(self._current_year - 100)
        self._spin_couple_partenaire_naissance.setMaximum(self._current_year)
        self._spin_couple_partenaire_naissance.setSingleStep(1)
        self._spin_couple_partenaire_naissance.setValue(self._current_year)
        self._spin_couple_partenaire_naissance.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_couple_partenaire_naissance.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_couple_partenaire_naissance, CURRENT_LINE, 5)

        self._combo_couple.setEnabled(False)
        self._spin_couple_partenaire_naissance.setEnabled(False)
        self._radio_couple_group.buttonClicked.connect(self._enable_couple)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(
            u"Combien de partenaires sexuels du sexe opposé<br />avez-vous eu au "
            u"cours de toute votre vie?"), CURRENT_LINE, 0)
        self._spin_couple_partenaire_hetero = QtGui.QSpinBox()
        self._spin_couple_partenaire_hetero.setMinimum(0)
        self._spin_couple_partenaire_hetero.setMaximum(100)
        self._spin_couple_partenaire_hetero.setSingleStep(1)
        self._spin_couple_partenaire_hetero.setValue(0)
        self._spin_couple_partenaire_hetero.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_couple_partenaire_hetero.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_couple_partenaire_hetero, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(
            u"Combien de partenaires sexuels du même sexe<br />avez-vous eu au "
            u"cours de toute votre vie?"), CURRENT_LINE, 2)
        self._spin_couple_partenaire_homo = QtGui.QSpinBox()
        self._spin_couple_partenaire_homo.setMinimum(0)
        self._spin_couple_partenaire_homo.setMaximum(100)
        self._spin_couple_partenaire_homo.setSingleStep(1)
        self._spin_couple_partenaire_homo.setValue(0)
        self._spin_couple_partenaire_homo.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_couple_partenaire_homo.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_couple_partenaire_homo, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        # Statut socio-économique ==============================================
        gridlayout.addWidget(MyLabel(u"Niveau d'études"), CURRENT_LINE, 0)
        self._combo_etudes = QtGui.QComboBox()
        self._combo_etudes.addItems(pms.ANNEES_ETUDES)
        self._combo_etudes.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_etudes, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Etes-vous propriétaire de votre logement?"), CURRENT_LINE, 2)
        self._radio_logement_oui = QtGui.QRadioButton(u"oui")
        self._radio_logement_non = QtGui.QRadioButton(u"non")
        self._radio_logement_group = QtGui.QButtonGroup()
        self._radio_logement_group.addButton(self._radio_logement_oui, 1)
        self._radio_logement_group.addButton(self._radio_logement_non, 0)
        self._layout_logement = MyHBoxLayout(
            [self._radio_logement_oui, self._radio_logement_non])
        gridlayout.addLayout(self._layout_logement, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Revenus personnels mensuels nets"), CURRENT_LINE, 4)
        self._combo_revenu = QtGui.QComboBox()
        self._combo_revenu.addItems(pms.REVENUS)
        self._combo_revenu.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_revenu, CURRENT_LINE, 5)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Catégorie socio-professionnelle"), CURRENT_LINE, 0)
        self._combo_csp = QtGui.QComboBox()
        self._combo_csp.addItems(pms.CSP)
        self._combo_csp.setMaximumWidth(100)
        gridlayout.addWidget(self._combo_csp, CURRENT_LINE, 1, 1, 2)

        CURRENT_LINE += 1

        # habitudes et sommeil =================================================
        gridlayout.addWidget(MyLabel(u"Etes-vous fumeur?"), CURRENT_LINE, 0)
        self._radio_fumeur_oui = QtGui.QRadioButton(u"oui")
        self._radio_fumeur_non = QtGui.QRadioButton(u"non")
        self._radio_fumeur_group = QtGui.QButtonGroup()
        self._radio_fumeur_group.addButton(self._radio_fumeur_oui, 1)
        self._radio_fumeur_group.addButton(self._radio_fumeur_non, 0)
        self._layout_fumeur = MyHBoxLayout(
            [self._radio_fumeur_oui, self._radio_fumeur_non])
        gridlayout.addLayout(self._layout_fumeur, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Heure du lever"), CURRENT_LINE, 2)
        self._timeedit_lever = QtGui.QTimeEdit()
        self._timeedit_lever.setDisplayFormat("HH:mm")
        self._timeedit_lever.setMaximumWidth(60)
        gridlayout.addWidget(self._timeedit_lever, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Nombre d'heures de sommeil"), CURRENT_LINE, 4)
        self._timeedit_sommeil = QtGui.QTimeEdit()
        self._timeedit_sommeil.setDisplayFormat("HH:mm")
        self._timeedit_sommeil.setMaximumWidth(60)
        gridlayout.addWidget(self._timeedit_sommeil, CURRENT_LINE, 5)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Prenez-vous des médicaments"), CURRENT_LINE, 0)
        self._radio_medicaments_oui = QtGui.QRadioButton(u"oui")
        self._radio_medicaments_non = QtGui.QRadioButton(u"non")
        self._radio_medicaments_group = QtGui.QButtonGroup()
        self._radio_medicaments_group.addButton(self._radio_medicaments_oui, 1)
        self._radio_medicaments_group.addButton(self._radio_medicaments_non, 0)
        self._layout_medicaments = MyHBoxLayout(
            [self._radio_medicaments_oui, self._radio_medicaments_non])
        gridlayout.addLayout(self._layout_medicaments, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Lesquels"), CURRENT_LINE, 2)
        self._lineedit_medicaments = QtGui.QLineEdit()
        gridlayout.addWidget(self._lineedit_medicaments, CURRENT_LINE, 3)

        self._lineedit_medicaments.setEnabled(False)
        self._radio_medicaments_group.buttonClicked.connect(
            lambda _: self._lineedit_medicaments.setEnabled(
                self._radio_medicaments_oui.isChecked()))

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Pratiquez-vous le chant (chorale, cours ...)?"), CURRENT_LINE, 0)
        self._radio_chant_oui = QtGui.QRadioButton(u"oui")
        self._radio_chant_non = QtGui.QRadioButton(u"non")
        self._radio_chant_group = QtGui.QButtonGroup()
        self._radio_chant_group.addButton(self._radio_chant_oui, 1)
        self._radio_chant_group.addButton(self._radio_chant_non, 0)
        self._layout_chant = MyHBoxLayout(
            [self._radio_chant_oui, self._radio_chant_non])
        gridlayout.addLayout(self._layout_chant, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Faites-vous du théatre?"), CURRENT_LINE, 2)
        self._radio_theatre_oui = QtGui.QRadioButton(u"oui")
        self._radio_theatre_non = QtGui.QRadioButton(u"non")
        self._radio_theatre_group = QtGui.QButtonGroup()
        self._radio_theatre_group.addButton(self._radio_theatre_oui, 1)
        self._radio_theatre_group.addButton(self._radio_theatre_non, 0)
        self._layout_theatre = MyHBoxLayout(
            [self._radio_theatre_oui, self._radio_theatre_non])
        gridlayout.addLayout(self._layout_theatre, CURRENT_LINE, 3)

        # buttons
        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        buttons.accepted.connect(self._accept)
        layout.addWidget(buttons)

        self.setWindowTitle(trans_CVQ(u"Questionnaire"))
        self.adjustSize()
        self.setFixedSize(self.size())

        if self._automatique:
            for k, v in self.__dict__.viewitems():
                if "combo" in k:
                    v.setCurrentIndex(randint(1, v.count()-1))
                elif "spin" in k:
                    v.setValue(randint(v.minimum(), v.maximum()))
                elif "group" in k:
                    v.button(randint(0, 1)).click()
                elif "lineedit" in k:
                    v.setText(u"Texte automatique")
                elif "timeedit" in k:
                    v.setTime(QtCore.QTime(randint(0, 23), randint(0, 59)))

            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(
                buttons.button(QtGui.QDialogButtonBox.Ok).click)
            self._timer_automatique.start(7000)

    def _enable_couple(self):
        id_checked = self._radio_couple_group.checkedId()
        self._combo_couple.setEnabled(id_checked)
        self._spin_couple_partenaire_naissance.setEnabled(id_checked)

    def reject(self):
        pass
    
    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        answers = {}
        try:
            
            if self._combo_naissance_mois.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser votre mois de naissance")
            answers["CVQ_naissance_mois"] = self._combo_naissance_mois.currentIndex()
            if self._spin_naissance_annee.value() == self._current_year:
                raise ValueError(u"Vous devez préciser votre année de naissance")
            answers["CVQ_naissance_annee"] = self._spin_naissance_annee.value()
            if self._combo_naissance_pays.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser votre pays de naissance")
            answers["CVQ_naissance_pays"] = self._combo_naissance_pays.currentIndex()
            if self._spin_naissance_annee_pere.value() == self._current_year:
                raise ValueError(u"Vous devez préciser l'année de naissance de "
                                 u"votre père")
            answers["CVQ_naissance_pere"] = self._spin_naissance_annee_pere.value()
            if self._spin_naissance_annee_mere.value() == self._current_year:
                raise ValueError(u"Vous devez préciser l'année de naissance de "
                                 u"votre mère")
            answers["CVQ_naissance_mere"] = self._spin_naissance_annee_mere.value()

            # situation maritale -----------------------------------------------
            if self._radio_couple_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous êtes en couple")
            answers["CVQ_couple"] = self._radio_couple_group.checkedId()
            if answers["CVQ_couple"] == 1:
                if self._combo_couple.currentIndex() == 0:
                    raise ValueError(u"Vous devez préciser depuis combien de "
                                     u"temps vous êtes en couple")
                answers["CVQ_couple_temps"] = self._combo_couple.currentIndex()
                if self._spin_couple_partenaire_naissance.value() == self._current_year:
                    raise ValueError(u"Vous devez préciser l'année de naissance "
                                     u"de votre partenaire")
                answers["CVQ_couple_partenaire_naissance"] = \
                    self._spin_couple_partenaire_naissance.value()
            answers["CVQ_partenaires_heteros"] = self._spin_couple_partenaire_hetero.value()
            answers["CVQ_partenaires_homos"] = self._spin_couple_partenaire_homo.value()

            # statut socio-éco -------------------------------------------------
            if self._combo_etudes.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser votre niveau d'études")
            answers["CVQ_etudes"] = self._combo_etudes.currentIndex()
            if self._radio_logement_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous êtes propriétaire")
            answers["CVQ_proprietaire"] = self._radio_logement_group.checkedId()
            if self._combo_revenu.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser votre revenu")
            answers["CVQ_revenu"] = self._combo_revenu.currentIndex()
            if self._combo_csp.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser votre CSP")
            answers["CVQ_csp"] = self._combo_csp.currentIndex()
            if self._radio_fumeur_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous fumez")
            answers["CVQ_fumeur"] = self._radio_fumeur_group.checkedId()
            heure_lever = self._timeedit_lever.time().toString("hh:mm")
            if heure_lever == "00:00":
                raise ValueError(u"Vous devez préciser votre heure de lever")
            answers["CVQ_lever"] = heure_lever
            sommeil = self._timeedit_sommeil.time().toString("hh:mm")
            if sommeil == "00:00":
                raise ValueError(u"Vous devez préciser votre nombre d'heures "
                                 u"de sommeil")
            answers["CVQ_sommeil"] = sommeil
            if self._radio_medicaments_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous prenez des "
                                 u"médicaments")
            answers["CVQ_medicaments"] = self._radio_medicaments_group.checkedId()
            if answers["CVQ_medicaments"] == 1:
                medocs = unicode(self._lineedit_medicaments.text().toUtf8(), "utf8")
                if not medocs:
                    raise ValueError(u"Vous devez préciser les noms de vos "
                                     u"médicaments")
                answers["CVQ_medicaments_noms"] = medocs
            if self._radio_chant_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous pratiquez "
                                 u"le chant")
            answers["CVQ_chant"] = self._radio_chant_group.checkedId()
            if self._radio_theatre_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous faites du "
                                 u"théâtre")
            answers["CVQ_theatre"] = self._radio_theatre_group.checkedId()


        except ValueError as e:
            QtGui.QMessageBox.warning(
                self, u"Attention", e.message)
            return
        
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


class GuiCoop(QtGui.QDialog):
    def __init__(self, defered, automatique, parent):

        super(GuiCoop, self).__init__(parent)

        self._defered = defered
        self._automatique = automatique

        layout = QtGui.QVBoxLayout(self)

        gridlayout = QtGui.QGridLayout()
        gridlayout.setHorizontalSpacing(20)
        layout.addLayout(gridlayout)

        CURRENT_LINE = 0

        gridlayout.addWidget(MyLabel(u"De manière générale, diriez-vous que "
                                     u"vous faites confiance à la plupart des "
                                     u"gens,<br />ou que vous êtes très prudent "
                                     u"quand vous avez affaire à eux?"),
                             CURRENT_LINE, 0)
        self._radio_confiance_oui = QtGui.QRadioButton(u"Je fais confiance à "
                                                       u"la plupart des gens")
        self._radio_confiance_non = QtGui.QRadioButton(u"Je suis très prudent "
                                                       u"vis à vis d'eux")
        self._radio_confiance_group = QtGui.QButtonGroup()
        self._radio_confiance_group.addButton(self._radio_confiance_oui, 1)
        self._radio_confiance_group.addButton(self._radio_confiance_non, 0)
        self._layout_confiance = MyHBoxLayout([self._radio_confiance_oui,
                                               self._radio_confiance_non])
        gridlayout.addLayout(self._layout_confiance, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Pensez-vous qu'en général les gens "
                                     u"essaient de profiter de vous lorsqu'ils "
                                     u"en ont l'occasion,<br />ou essaient-ils d' "
                                     u"être justes?<br /><em>(1 signifie que "
                                     u"les gens essaient de "
                                     u"profiter de vous et<br />8 que les gens "
                                     u"essaient d'être justes).</em>"),
                             CURRENT_LINE, 0)
        self._combo_profite = QtGui.QComboBox()
        self._combo_profite.addItems(pms.PROFITE)
        self._combo_profite.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_profite, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Vous considérez comme quelqu'un "
                                     u"d'altruiste/généreux?"), CURRENT_LINE, 0)
        self._combo_altruiste = QtGui.QComboBox()
        self._combo_altruiste.addItems(pms.DEGRES)
        self._combo_altruiste.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_altruiste, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Si vous perdiez votre portefeuille "
                                     u"ou votre sac à main qui contient 200€<br />"
                                     u"et que le portefeuille ou sac à main "
                                     u"est retrouvé <strong>par un "
                                     u"inconnu</strong>.<br />Allez-vous "
                                     u"le récupérer avec l'argent?"),
                             CURRENT_LINE, 0)
        self._combo_portefeuille_inconnu = QtGui.QComboBox()
        self._combo_portefeuille_inconnu.addItems(pms.PROBABLE)
        self._combo_portefeuille_inconnu.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_portefeuille_inconnu, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Si vous perdiez votre portefeuille "
                                     u"ou votre sac à main qui contient 200€<br />"
                                     u"et que le portefeuille ou sac à main "
                                     u"est retrouvé <strong>par un de vos"
                                     u"voisins</strong>.<br />Allez-vous "
                                     u"le récupérer avec l'argent?"),
                             CURRENT_LINE, 0)
        self._combo_portefeuille_voisin = QtGui.QComboBox()
        self._combo_portefeuille_voisin.addItems(pms.PROBABLE)
        self._combo_portefeuille_voisin.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_portefeuille_voisin, CURRENT_LINE, 1)

        # buttons
        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        buttons.accepted.connect(self._accept)
        layout.addWidget(buttons)

        self.setWindowTitle(trans_CVQ(u"Questionnaire"))
        self.adjustSize()
        self.setFixedSize(self.size())

        if self._automatique:
            for k, v in self.__dict__.viewitems():
                if "combo" in k:
                    v.setCurrentIndex(randint(1, v.count() - 1))
                elif "group" in k:
                    v.button(randint(0, 1)).click()

            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(
                buttons.button(QtGui.QDialogButtonBox.Ok).click)
            self._timer_automatique.start(7000)

    def reject(self):
        pass

    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        answers = {}
        try:

            if self._radio_confiance_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous faites confiance "
                                 u"aux gens")
            answers["COOP_confiance"] = self._radio_confiance_group.checkedId()
            if self._combo_profite.currentIndex() == 0:
                raise ValueError(u"Vous devez précisez si vous pensez que les "
                                 u"gens essaient de profiter de vous")
            answers["COOP_profite"] = self._combo_profite.currentIndex()
            if self._combo_altruiste.currentIndex() == 0:
                raise ValueError(u"Vous devez précisez si vous vous considérez "
                                 u"altruiste")
            answers["COOP_altruiste"] = self._combo_altruiste.currentIndex()
            if self._combo_portefeuille_inconnu.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser si vous pensez que "
                                 u"vous allez récupérer votre portefeuille ou "
                                 u"sac avec l'argent s'il est retrouvé par un "
                                 u"inconnu")
            answers["COOP_portefeuille_inconnu"] = \
                self._combo_portefeuille_inconnu.currentIndex()
            if self._combo_portefeuille_voisin.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser si vous pensez que "
                                 u"vous allez récupérer votre portefeuille ou "
                                 u"sac avec l'argent s'il est retrouvé par un "
                                 u"de vos voisins")
            answers["COOP_portefeuille_voisin"] = \
                self._combo_portefeuille_voisin.currentIndex()

        except ValueError as e:
            QtGui.QMessageBox.warning(
                self, u"Attention", e.message)
            return

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


class GuiBigFiveTen(QtGui.QDialog):
    def __init__(self, defered, automatique, parent):

        super(GuiBigFiveTen, self).__init__(parent)

        self._defered = defered
        self._automatique = automatique

        layout = QtGui.QVBoxLayout(self)

        explanation = WExplication(
            parent=self,
            text=u"Voici une liste de traits de caractère qui peuvent ou non "
                 u"vous correspondre. Veuillez indiquer dans quelle mesure vous "
                 u"pensez qu'ils vous correspondent. Veuillez évaluer la paire "
                 u"de caractéristiques, même si une des caractéristiques "
                 u"s'applique plus que l'autre.", html=False)
        layout.addWidget(explanation)

        gridlayout = QtGui.QGridLayout()
        gridlayout.setHorizontalSpacing(20)
        layout.addLayout(gridlayout)

        CURRENT_LINE = 0

        gridlayout.addWidget(QtGui.QLabel(u"Je me considère comme étant"),
                             CURRENT_LINE, 0, 0, 1, 4)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Extraverti, enthousiaste"), CURRENT_LINE, 0)
        self._combo_extraverti = QtGui.QComboBox()
        self._combo_extraverti.addItems(pms.ACCORD)
        self._combo_extraverti.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_extraverti, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Critique, agressif"), CURRENT_LINE, 2)
        self._combo_critique = QtGui.QComboBox()
        self._combo_critique.addItems(pms.ACCORD)
        self._combo_critique.setMaximumWidth(120)
        gridlayout.addWidget(self._combo_critique, CURRENT_LINE, 3)

        # buttons
        buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
        buttons.accepted.connect(self._accept)
        layout.addWidget(buttons)

        self.setWindowTitle(trans_CVQ(u"Questionnaire"))
        self.adjustSize()
        self.setFixedSize(self.size())

        if self._automatique:
            for k, v in self.__dict__.viewitems():
                if "combo" in k:
                    v.setCurrentIndex(randint(1, v.count() - 1))
                elif "group" in k:
                    v.button(randint(0, 1)).click()

            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(
                buttons.button(QtGui.QDialogButtonBox.Ok).click)
            self._timer_automatique.start(7000)

    def reject(self):
        pass

    def _accept(self):
        try:
            self._timer_automatique.stop()
        except AttributeError:
            pass
        answers = {}
        try:

            if self._radio_confiance_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous faites confiance "
                                 u"aux gens")
            answers["COOP_confiance"] = self._radio_confiance_group.checkedId()
            if self._combo_profite.currentIndex() == 0:
                raise ValueError(u"Vous devez précisez si vous pensez que les "
                                 u"gens essaient de profiter de vous")
            answers["COOP_profite"] = self._combo_profite.currentIndex()
            if self._combo_altruiste.currentIndex() == 0:
                raise ValueError(u"Vous devez précisez si vous vous considérez "
                                 u"altruiste")
            answers["COOP_altruiste"] = self._combo_altruiste.currentIndex()
            if self._combo_portefeuille_inconnu.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser si vous pensez que "
                                 u"vous allez récupérer votre portefeuille ou "
                                 u"sac avec l'argent s'il est retrouvé par un "
                                 u"inconnu")
            answers["COOP_portefeuille_inconnu"] = \
                self._combo_portefeuille_inconnu.currentIndex()
            if self._combo_portefeuille_voisin.currentIndex() == 0:
                raise ValueError(u"Vous devez préciser si vous pensez que "
                                 u"vous allez récupérer votre portefeuille ou "
                                 u"sac avec l'argent s'il est retrouvé par un "
                                 u"de vos voisins")
            answers["COOP_portefeuille_voisin"] = \
                self._combo_portefeuille_voisin.currentIndex()

        except ValueError as e:
            QtGui.QMessageBox.warning(
                self, u"Attention", e.message)
            return

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
