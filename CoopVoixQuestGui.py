# -*- coding: utf-8 -*-
"""
This module contains the GUI
"""

import logging
from PyQt4 import QtGui, QtCore
from util.utili18n import le2mtrans
from datetime import datetime
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
    def __init__(self, text, align=QtCore.Qt.AlignRight):
        QtGui.QLabel.__init__(self, text)
        self.setAlignment(align | QtCore.Qt.AlignVCenter)


class MyHBoxLayout(QtGui.QHBoxLayout):
    def __init__(self, widgets_to_add):
        QtGui.QHBoxLayout.__init__(self)
        for e in widgets_to_add:
            self.addWidget(e)
        self.addSpacerItem(
            QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Expanding,
                              QtGui.QSizePolicy.Minimum))


class MyComboBox(QtGui.QComboBox):
    def __init__(self, items, width=150):
        QtGui.QComboBox.__init__(self)
        self.addItems(items)
        self.setMaximumWidth(width)


class GuiDemo(QtGui.QDialog):
    def __init__(self, defered, automatique, parent):

        super(GuiDemo, self).__init__(parent)

        self._defered = defered
        self._automatique = automatique

        layout = QtGui.QVBoxLayout(self)

        wexplanation = WExplication(
            text=texts_CVQ.get_text_explanation_demo(),
            size=(450, 60), parent=self)
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
        self._combo_naissance_pays = MyComboBox(pays, 200)
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
        self._combo_couple = MyComboBox(pms.COUPLE_LISTE, 100)
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
        self._combo_etudes = MyComboBox(pms.ANNEES_ETUDES, 100)
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
        self._combo_revenu = MyComboBox(pms.REVENUS)
        gridlayout.addWidget(self._combo_revenu, CURRENT_LINE, 5)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Catégorie socio-professionnelle"), CURRENT_LINE, 0)
        self._combo_csp = MyComboBox(pms.CSP, width=250)
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

        gridlayout.addWidget(MyLabel(u"Combien de cigarettes (hors électronique) par jour?"),
                             CURRENT_LINE, 2)
        self._spin_cigarette = QtGui.QSpinBox()
        self._spin_cigarette.setMinimum(0)
        self._spin_cigarette.setMaximum(100)
        self._spin_cigarette.setSingleStep(1)
        self._spin_cigarette.setButtonSymbols(QtGui.QSpinBox.NoButtons)
        self._spin_cigarette.setValue(0)
        self._spin_cigarette.setMaximumWidth(60)
        gridlayout.addWidget(self._spin_cigarette, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Fumez-vous la cigarette électronique?"),
                             CURRENT_LINE, 4)
        self._radio_cigarette_electronique_oui = QtGui.QRadioButton(u"oui")
        self._radio_cigarette_electronique_non = QtGui.QRadioButton(u"non")
        self._radio_cigarette_electronique_group = QtGui.QButtonGroup()
        self._radio_cigarette_electronique_group.addButton(self._radio_cigarette_electronique_oui, 1)
        self._radio_cigarette_electronique_group.addButton(self._radio_cigarette_electronique_non, 0)
        self._layout_cigarette_electronique = MyHBoxLayout(
            [self._radio_cigarette_electronique_oui, self._radio_cigarette_electronique_non])
        gridlayout.addLayout(self._layout_cigarette_electronique, CURRENT_LINE, 5)

        self._spin_cigarette.setEnabled(False)
        self._radio_cigarette_electronique_oui.setEnabled(False)
        self._radio_cigarette_electronique_non.setEnabled(False)
        self._radio_fumeur_group.buttonClicked.connect(self._enable_cigarette)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"A quelle heure vous êtes-vous levé ce matin?"),
                             CURRENT_LINE, 0)
        self._timeedit_lever = QtGui.QTimeEdit()
        self._timeedit_lever.setDisplayFormat("HH:mm")
        self._timeedit_lever.setMaximumWidth(80)
        gridlayout.addWidget(self._timeedit_lever, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Combien d'heures avez-vous dormi la nuit dernière?"),
                             CURRENT_LINE, 2)
        self._timeedit_sommeil = QtGui.QTimeEdit()
        self._timeedit_sommeil.setDisplayFormat("HH:mm")
        self._timeedit_sommeil.setMaximumWidth(80)
        gridlayout.addWidget(self._timeedit_sommeil, CURRENT_LINE, 3)

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
        self._lineedit_medicaments.setMaximumWidth(200)
        gridlayout.addWidget(self._lineedit_medicaments, CURRENT_LINE, 3, 1, 2)

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


        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Avez-vous pris une douche (un bain) hier soir?"),
                             CURRENT_LINE, 0)
        self._radio_hier_douche_oui = QtGui.QRadioButton(u"oui")
        self._radio_hier_douche_non = QtGui.QRadioButton(u"non")
        self._radio_hier_douche_group = QtGui.QButtonGroup()
        self._radio_hier_douche_group.addButton(self._radio_hier_douche_oui, 1)
        self._radio_hier_douche_group.addButton(self._radio_hier_douche_non, 0)
        self._layout_hier_douche = MyHBoxLayout(
            [self._radio_hier_douche_oui, self._radio_hier_douche_non])
        gridlayout.addLayout(self._layout_hier_douche, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Avez-vous mis du déodorant hier soir?"),
                             CURRENT_LINE, 2)
        self._radio_hier_deodorant_oui = QtGui.QRadioButton(u"oui")
        self._radio_hier_deodorant_non = QtGui.QRadioButton(u"non")
        self._radio_hier_deodorant_group = QtGui.QButtonGroup()
        self._radio_hier_deodorant_group.addButton(self._radio_hier_deodorant_oui, 1)
        self._radio_hier_deodorant_group.addButton(self._radio_hier_deodorant_non, 0)
        self._layout_hier_deodorant = MyHBoxLayout(
            [self._radio_hier_deodorant_oui, self._radio_hier_deodorant_non])
        gridlayout.addLayout(self._layout_hier_deodorant, CURRENT_LINE, 3)
        
        gridlayout.addWidget(MyLabel(u"Avez-vous mis du parfum hier soir?"),
                             CURRENT_LINE, 4)
        self._radio_hier_parfum_oui = QtGui.QRadioButton(u"oui")
        self._radio_hier_parfum_non = QtGui.QRadioButton(u"non")
        self._radio_hier_parfum_group = QtGui.QButtonGroup()
        self._radio_hier_parfum_group.addButton(self._radio_hier_parfum_oui, 1)
        self._radio_hier_parfum_group.addButton(self._radio_hier_parfum_non, 0)
        self._layout_hier_parfum = MyHBoxLayout(
            [self._radio_hier_parfum_oui, self._radio_hier_parfum_non])
        gridlayout.addLayout(self._layout_hier_parfum, CURRENT_LINE, 5)
        
        CURRENT_LINE += 1

        gridlayout.addWidget(
            MyLabel(u"Avez-vous pris une douche (un bain) aujourd'hui?"),
            CURRENT_LINE, 0)
        self._radio_jour_douche_oui = QtGui.QRadioButton(u"oui")
        self._radio_jour_douche_non = QtGui.QRadioButton(u"non")
        self._radio_jour_douche_group = QtGui.QButtonGroup()
        self._radio_jour_douche_group.addButton(self._radio_jour_douche_oui, 1)
        self._radio_jour_douche_group.addButton(self._radio_jour_douche_non, 0)
        self._layout_jour_douche = MyHBoxLayout(
            [self._radio_jour_douche_oui, self._radio_jour_douche_non])
        gridlayout.addLayout(self._layout_jour_douche, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Avez-vous mis du déodorant aujourd'hui?"),
                             CURRENT_LINE, 2)
        self._radio_jour_deodorant_oui = QtGui.QRadioButton(u"oui")
        self._radio_jour_deodorant_non = QtGui.QRadioButton(u"non")
        self._radio_jour_deodorant_group = QtGui.QButtonGroup()
        self._radio_jour_deodorant_group.addButton(
            self._radio_jour_deodorant_oui, 1)
        self._radio_jour_deodorant_group.addButton(
            self._radio_jour_deodorant_non, 0)
        self._layout_jour_deodorant = MyHBoxLayout(
            [self._radio_jour_deodorant_oui, self._radio_jour_deodorant_non])
        gridlayout.addLayout(self._layout_jour_deodorant, CURRENT_LINE, 3)

        gridlayout.addWidget(MyLabel(u"Avez-vous mis du parfum aujourd'hui?"),
                             CURRENT_LINE, 4)
        self._radio_jour_parfum_oui = QtGui.QRadioButton(u"oui")
        self._radio_jour_parfum_non = QtGui.QRadioButton(u"non")
        self._radio_jour_parfum_group = QtGui.QButtonGroup()
        self._radio_jour_parfum_group.addButton(self._radio_jour_parfum_oui, 1)
        self._radio_jour_parfum_group.addButton(self._radio_jour_parfum_non, 0)
        self._layout_jour_parfum = MyHBoxLayout(
            [self._radio_jour_parfum_oui, self._radio_jour_parfum_non])
        gridlayout.addLayout(self._layout_jour_parfum, CURRENT_LINE, 5)

        CURRENT_LINE += 1
        
        gridlayout.addWidget(MyLabel(u"Avez-vous fait du sport aujourd'hui?"),
                             CURRENT_LINE, 0)
        self._radio_jour_sport_oui = QtGui.QRadioButton(u"oui")
        self._radio_jour_sport_non = QtGui.QRadioButton(u"non")
        self._radio_jour_sport_group = QtGui.QButtonGroup()
        self._radio_jour_sport_group.addButton(self._radio_jour_sport_oui, 1)
        self._radio_jour_sport_group.addButton(self._radio_jour_sport_non, 0)
        self._layout_jour_sport = MyHBoxLayout(
            [self._radio_jour_sport_oui, self._radio_jour_sport_non])
        gridlayout.addLayout(self._layout_jour_sport, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Indiquer les autres produits parfumés "
                                     u"que vous avez utilisés depuis hier soir"),
                             CURRENT_LINE, 2)
        self._lineedit_produits_parfumes = QtGui.QLineEdit()
        self._lineedit_produits_parfumes.setMaximumWidth(250)
        gridlayout.addWidget(self._lineedit_produits_parfumes, CURRENT_LINE, 3, 1, 2)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Etes-vous végétarien/végétalien?"),
                             CURRENT_LINE, 0)
        self._radio_vegetarien_oui = QtGui.QRadioButton(u"oui")
        self._radio_vegetarien_non = QtGui.QRadioButton(u"non")
        self._radio_vegetarien_group = QtGui.QButtonGroup()
        self._radio_vegetarien_group.addButton(self._radio_vegetarien_oui, 1)
        self._radio_vegetarien_group.addButton(self._radio_vegetarien_non, 0)
        self._layout_vegetarien = MyHBoxLayout(
            [self._radio_vegetarien_oui, self._radio_vegetarien_non])
        gridlayout.addLayout(self._layout_vegetarien, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Depuis hier après midi, avez-vous "
                                     u"consommé les aliments suivants"),
                             CURRENT_LINE, 0)
        self._checkbox_oignon = QtGui.QCheckBox(u"oignon")
        self._checkbox_ail = QtGui.QCheckBox(u"ail")
        self._checkbox_piment = QtGui.QCheckBox(u"piment")
        self._checkbox_curry = QtGui.QCheckBox(u"curry ou épices fortes")
        self._checkbox_chou = QtGui.QCheckBox(u"chou")
        self._checkbox_celeri = QtGui.QCheckBox(u"céleri")
        self._checkbox_fromages = QtGui.QCheckBox(u"fromage bleu / fort")
        self._checkbox_asperges = QtGui.QCheckBox(u"asperges")
        self._checkbox_alcool = QtGui.QCheckBox(u"alcool")
        self._layout_aliments = MyHBoxLayout(
            [self._checkbox_oignon, self._checkbox_ail, self._checkbox_piment,
             self._checkbox_curry, self._checkbox_chou, self._checkbox_celeri,
             self._checkbox_fromages, self._checkbox_asperges, self._checkbox_alcool])
        gridlayout.addLayout(self._layout_aliments, CURRENT_LINE, 1, 1, 4)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Avez-vous été malade durant les 2 "
                                     u"derniers jours?"), CURRENT_LINE, 0)
        self._radio_malade_oui = QtGui.QRadioButton(u"oui")
        self._radio_malade_non = QtGui.QRadioButton(u"non")
        self._radio_malade_group = QtGui.QButtonGroup()
        self._radio_malade_group.addButton(self._radio_malade_oui, 1)
        self._radio_malade_group.addButton(self._radio_malade_non, 0)
        self._layout_malade = MyHBoxLayout(
            [self._radio_malade_oui, self._radio_malade_non])
        gridlayout.addLayout(self._layout_malade, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Quelle maladie"), CURRENT_LINE, 2)
        self._lineedit_maladie = QtGui.QLineEdit()
        self._lineedit_maladie.setMaximumWidth(200)
        gridlayout.addWidget(self._lineedit_maladie, CURRENT_LINE, 3, 1, 2)

        self._lineedit_maladie.setEnabled(False)
        self._radio_malade_group.buttonClicked.connect(
            lambda _: self._lineedit_maladie.setEnabled(self._radio_malade_group.checkedId()))

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Veuillez indiquer votre niveau de stress "
                                     u"moyen<br />depuis votre arrivée au "
                                     u"laboratoire"),
                             CURRENT_LINE, 0)
        self._combo_stress = MyComboBox(pms.STRESS, 200)
        gridlayout.addWidget(self._combo_stress, CURRENT_LINE, 1)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Cette nuit, avez-vous dormi avec "
                                     u"quelqu’un ou avec votre animal "
                                     u"domestique dans le même lit?"), CURRENT_LINE, 0)
        self._radio_dormi_deux_oui = QtGui.QRadioButton(u"oui")
        self._radio_dormi_deux_non = QtGui.QRadioButton(u"non")
        self._radio_dormi_deux_group = QtGui.QButtonGroup()
        self._radio_dormi_deux_group.addButton(self._radio_dormi_deux_oui, 1)
        self._radio_dormi_deux_group.addButton(self._radio_dormi_deux_non, 0)
        self._layout_dormi_deux = MyHBoxLayout(
            [self._radio_dormi_deux_oui, self._radio_dormi_deux_non])
        gridlayout.addLayout(self._layout_dormi_deux, CURRENT_LINE, 1)
        
        gridlayout.addWidget(MyLabel(u"Avez-vous eu des relations sexuelles "
                                     u"cette nuit?"), CURRENT_LINE, 2)
        self._radio_relation_sexuelle_oui = QtGui.QRadioButton(u"oui")
        self._radio_relation_sexuelle_non = QtGui.QRadioButton(u"non")
        self._radio_relation_sexuelle_group = QtGui.QButtonGroup()
        self._radio_relation_sexuelle_group.addButton(self._radio_relation_sexuelle_oui, 1)
        self._radio_relation_sexuelle_group.addButton(self._radio_relation_sexuelle_non, 0)
        self._layout_relation_sexuelle = MyHBoxLayout(
            [self._radio_relation_sexuelle_oui, self._radio_relation_sexuelle_non])
        gridlayout.addLayout(self._layout_relation_sexuelle, CURRENT_LINE, 3)
        
        CURRENT_LINE += 1
        
        gridlayout.addWidget(MyLabel(u"Avez-vous déjà participé à un jeu de ce "
                                     u"type,<br />avec 20 jetons à répartir entre "
                                     u"votre compte individuel et<br />un compte "
                                     u"collectif?"), CURRENT_LINE, 0)
        self._radio_bien_public_oui = QtGui.QRadioButton(u"oui")
        self._radio_bien_public_non = QtGui.QRadioButton(u"non")
        self._radio_bien_public_group = QtGui.QButtonGroup()
        self._radio_bien_public_group.addButton(self._radio_bien_public_oui, 1)
        self._radio_bien_public_group.addButton(self._radio_bien_public_non, 0)
        self._layout_bien_public = MyHBoxLayout(
            [self._radio_bien_public_oui, self._radio_bien_public_non])
        gridlayout.addLayout(self._layout_bien_public, CURRENT_LINE, 1)

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
                elif "checkbox" in k:
                    v.setChecked(randint(0, 1))

            self._timer_automatique = QtCore.QTimer()
            self._timer_automatique.timeout.connect(
                buttons.button(QtGui.QDialogButtonBox.Ok).click)
            self._timer_automatique.start(7000)

    def _enable_couple(self):
        id_checked = self._radio_couple_group.checkedId()
        self._combo_couple.setEnabled(id_checked)
        self._spin_couple_partenaire_naissance.setEnabled(id_checked)

    def _enable_cigarette(self):
        id_checked = self._radio_fumeur_group.checkedId()
        self._spin_cigarette.setEnabled(id_checked)
        self._radio_cigarette_electronique_oui.setEnabled(id_checked)
        self._radio_cigarette_electronique_non.setEnabled(id_checked)
        if self._automatique:
            self._spin_cigarette.setValue(randint(0, 30))
            self._radio_cigarette_electronique_group.button(randint(0, 1)).click()

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
            if answers["CVQ_fumeur"] == 1:
                answers["CVQ_cigarette"] = self._spin_cigarette.value()
                if self._radio_cigarette_electronique_group.checkedId() == -1:
                    raise ValueError(u"Vous devez préciser si vous fumez "
                                     u"la cigarette électronique")
                answers["CVQ_cigarette_electronique"] = \
                    self._radio_cigarette_electronique_group.checkedId()
            else:
                answers["CVQ_cigarette"] = 0
                answers["CVQ_cigarette_electronique"] = 0
            heure_lever = str(self._timeedit_lever.time().toString("hh:mm"))
            if heure_lever == "00:00":
                raise ValueError(u"Vous devez préciser votre heure de lever")
            answers["CVQ_lever"] = heure_lever
            sommeil = str(self._timeedit_sommeil.time().toString("hh:mm"))
            if sommeil == "00:00":
                raise ValueError(u"Vous devez préciser votre nombre d'heures "
                                 u"de sommeil")
            answers["CVQ_sommeil"] = sommeil
            if self._radio_medicaments_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous prenez des "
                                 u"médicaments")
            answers["CVQ_medicaments"] = self._radio_medicaments_group.checkedId()
            if answers["CVQ_medicaments"] == 1:
                medocs = unicode(self._lineedit_medicaments.text().toUtf8(),
                                     encoding="UTF-8")
                if not medocs:
                    raise ValueError(u"Vous devez préciser les noms de vos "
                                     u"médicaments")
                answers["CVQ_medicaments_noms"] = medocs
            else:
                answers["CVQ_medicaments_noms"] = u""
            if self._radio_chant_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous pratiquez "
                                 u"le chant")
            answers["CVQ_chant"] = self._radio_chant_group.checkedId()
            if self._radio_theatre_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous faites du "
                                 u"théâtre")
            answers["CVQ_theatre"] = self._radio_theatre_group.checkedId()
            if self._radio_hier_douche_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez pris une "
                                 u"douche hier")
            answers["CVQ_hier_douche"] = self._radio_hier_douche_group.checkedId()
            if self._radio_hier_deodorant_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez mis du "
                                 u"déodorant hier")
            answers["CVQ_hier_deodorant"] = self._radio_hier_deodorant_group.checkedId()
            if self._radio_hier_parfum_group.checkedId() == -1:
                raise ValueError(u"Vous devez précisez si vous avez mis du "
                                 u"parfum hier")
            answers["CVQ_hier_parfum"] = self._radio_hier_parfum_group.checkedId()
            if self._radio_jour_douche_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez pris une "
                                 u"douche aujourd'hui")
            answers["CVQ_jour_douche"] = self._radio_jour_douche_group.checkedId()
            if self._radio_jour_deodorant_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez mis du "
                                 u"déodorant aujourd'hui")
            answers["CVQ_jour_deodorant"] = self._radio_jour_deodorant_group.checkedId()
            if self._radio_jour_parfum_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez mis du "
                                 u"parfum aujourd'hui")
            answers["CVQ_jour_parfum"] = self._radio_jour_parfum_group.checkedId()
            if self._radio_jour_sport_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez fait du "
                                 u"sport aujourd'hui")
            answers["CVQ_jour_sport"] = self._radio_jour_sport_group.checkedId()
            answers["CVQ_produits_parfumes"] = \
                unicode(self._lineedit_produits_parfumes.text().toUtf8(), "utf-8")
            if self._radio_vegetarien_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous êtes végétarien")
            answers["CVQ_vegetarien"] = self._radio_vegetarien_group.checkedId()
            answers["CVQ_oignon"] = self._checkbox_oignon.isChecked()
            answers["CVQ_ail"] = self._checkbox_ail.isChecked()
            answers["CVQ_piment"] = self._checkbox_piment.isChecked()
            answers["CVQ_curry"] = self._checkbox_curry.isChecked()
            answers["CVQ_chou"] = self._checkbox_chou.isChecked()
            answers["CVQ_celeri"] = self._checkbox_celeri.isChecked()
            answers["CVQ_fromages"] = self._checkbox_fromages.isChecked()
            answers["CVQ_asperges"] = self._checkbox_asperges.isChecked()
            answers["CVQ_alcool"] = self._checkbox_alcool.isChecked()
            if self._radio_malade_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez été malade "
                                 u"ces deux derniers jours")
            answers["CVQ_malade"] = self._radio_malade_group.checkedId()
            if self._radio_malade_group.checkedId() == 1:
                answers["CVQ_maladie"] = \
                    unicode(self._lineedit_maladie.text().toUtf8(), "utf-8")
            else:
                answers["CVQ_maladie"] = u""
            if self._combo_stress.currentIndex() == 0:
                raise ValueError(u"Vous devez indiquer votre niveau de stress")
            answers["CVQ_stress"] = self._combo_stress.currentIndex()
            if self._radio_dormi_deux_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez dormi à "
                                 u"deux cette nuit")
            answers["CVQ_dormi_deux"] = self._radio_dormi_deux_group.checkedId()
            if self._radio_relation_sexuelle_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez eu une "
                                 u"relation sexuelle cette nuit")
            answers["CVQ_relation_sexuelle"] = self._radio_relation_sexuelle_group.checkedId()
            if self._radio_bien_public_group.checkedId() == -1:
                raise ValueError(u"Vous devez préciser si vous avez déjà "
                                 u"participé à ce type de jeu")
            answers["CVQ_bien_public"] = self._radio_bien_public_group.checkedId()

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


# class GuiCoop(QtGui.QDialog):
#     def __init__(self, defered, automatique, parent):
#
#         super(GuiCoop, self).__init__(parent)
#
#         self._defered = defered
#         self._automatique = automatique
#
#         layout = QtGui.QVBoxLayout(self)
#
#         gridlayout = QtGui.QGridLayout()
#         gridlayout.setHorizontalSpacing(20)
#         layout.addLayout(gridlayout)
#
#         CURRENT_LINE = 0
#
#         gridlayout.addWidget(MyLabel(u"De manière générale, diriez-vous que "
#                                      u"vous faites confiance à la plupart des "
#                                      u"gens,<br />ou que vous êtes très prudent "
#                                      u"quand vous avez affaire à eux?"),
#                              CURRENT_LINE, 0)
#         self._radio_confiance_oui = QtGui.QRadioButton(u"Je fais confiance à "
#                                                        u"la plupart des gens")
#         self._radio_confiance_non = QtGui.QRadioButton(u"Je suis très prudent "
#                                                        u"vis à vis d'eux")
#         self._radio_confiance_group = QtGui.QButtonGroup()
#         self._radio_confiance_group.addButton(self._radio_confiance_oui, 1)
#         self._radio_confiance_group.addButton(self._radio_confiance_non, 0)
#         self._layout_confiance = MyHBoxLayout([self._radio_confiance_oui,
#                                                self._radio_confiance_non])
#         gridlayout.addLayout(self._layout_confiance, CURRENT_LINE, 1)
#
#         CURRENT_LINE += 1
#
#         gridlayout.addWidget(MyLabel(u"Pensez-vous qu'en général les gens<br />"
#                                      u"essaient de profiter de vous lorsqu'ils "
#                                      u"en ont l'occasion,<br />ou essaient d' "
#                                      u"être justes?"),
#                              CURRENT_LINE, 0)
#         self._combo_profite = MyComboBox(pms.PROFITE, width=200)
#         gridlayout.addWidget(self._combo_profite, CURRENT_LINE, 1)
#
#         CURRENT_LINE += 1
#
#         gridlayout.addWidget(MyLabel(u"Vous considérez comme quelqu'un "
#                                      u"d'altruiste/généreux?"), CURRENT_LINE, 0)
#         self._combo_altruiste = MyComboBox(pms.DEGRES)
#         gridlayout.addWidget(self._combo_altruiste, CURRENT_LINE, 1)
#
#         CURRENT_LINE += 1
#
#         gridlayout.addWidget(MyLabel(u"Si vous perdiez votre portefeuille "
#                                      u"ou votre sac à main qui contient 200€<br />"
#                                      u"et que le portefeuille ou sac à main "
#                                      u"est retrouvé <strong>par un "
#                                      u"inconnu</strong>.<br />Allez-vous "
#                                      u"le récupérer avec l'argent?"),
#                              CURRENT_LINE, 0)
#         self._combo_portefeuille_inconnu = MyComboBox(pms.PROBABLE)
#         gridlayout.addWidget(self._combo_portefeuille_inconnu, CURRENT_LINE, 1)
#
#         CURRENT_LINE += 1
#
#         gridlayout.addWidget(MyLabel(u"Si vous perdiez votre portefeuille "
#                                      u"ou votre sac à main qui contient 200€<br />"
#                                      u"et que le portefeuille ou sac à main "
#                                      u"est retrouvé <strong>par un de vos "
#                                      u"voisins</strong>.<br />Allez-vous "
#                                      u"le récupérer avec l'argent?"),
#                              CURRENT_LINE, 0)
#         self._combo_portefeuille_voisin = MyComboBox(pms.PROBABLE)
#         gridlayout.addWidget(self._combo_portefeuille_voisin, CURRENT_LINE, 1)
#
#         # buttons
#         buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok)
#         buttons.accepted.connect(self._accept)
#         layout.addWidget(buttons)
#
#         self.setWindowTitle(trans_CVQ(u"Questionnaire"))
#         self.adjustSize()
#         self.setFixedSize(self.size())
#
#         if self._automatique:
#             for k, v in self.__dict__.viewitems():
#                 if "combo" in k:
#                     v.setCurrentIndex(randint(1, v.count() - 1))
#                 elif "group" in k:
#                     v.button(randint(0, 1)).click()
#
#             self._timer_automatique = QtCore.QTimer()
#             self._timer_automatique.timeout.connect(
#                 buttons.button(QtGui.QDialogButtonBox.Ok).click)
#             self._timer_automatique.start(7000)
#
#     def reject(self):
#         pass
#
#     def _accept(self):
#         try:
#             self._timer_automatique.stop()
#         except AttributeError:
#             pass
#         answers = {}
#         try:
#
#             if self._radio_confiance_group.checkedId() == -1:
#                 raise ValueError(u"Vous devez préciser si vous faites confiance "
#                                  u"aux gens")
#             answers["COOP_confiance"] = self._radio_confiance_group.checkedId()
#             if self._combo_profite.currentIndex() == 0:
#                 raise ValueError(u"Vous devez précisez si vous pensez que les "
#                                  u"gens essaient de profiter de vous")
#             answers["COOP_profite"] = self._combo_profite.currentIndex()
#             if self._combo_altruiste.currentIndex() == 0:
#                 raise ValueError(u"Vous devez précisez si vous vous considérez "
#                                  u"altruiste")
#             answers["COOP_altruiste"] = self._combo_altruiste.currentIndex()
#             if self._combo_portefeuille_inconnu.currentIndex() == 0:
#                 raise ValueError(u"Vous devez préciser si vous pensez que "
#                                  u"vous allez récupérer votre portefeuille ou "
#                                  u"sac avec l'argent s'il est retrouvé par un "
#                                  u"inconnu")
#             answers["COOP_portefeuille_inconnu"] = \
#                 self._combo_portefeuille_inconnu.currentIndex()
#             if self._combo_portefeuille_voisin.currentIndex() == 0:
#                 raise ValueError(u"Vous devez préciser si vous pensez que "
#                                  u"vous allez récupérer votre portefeuille ou "
#                                  u"sac avec l'argent s'il est retrouvé par un "
#                                  u"de vos voisins")
#             answers["COOP_portefeuille_voisin"] = \
#                 self._combo_portefeuille_voisin.currentIndex()
#
#         except ValueError as e:
#             QtGui.QMessageBox.warning(
#                 self, u"Attention", e.message)
#             return
#
#         if not self._automatique:
#             confirmation = QtGui.QMessageBox.question(
#                 self, le2mtrans(u"Confirmation"),
#                 le2mtrans(u"Do you confirm your choice?"),
#                 QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
#             if confirmation != QtGui.QMessageBox.Yes:
#                 return
#         logger.info(u"Send back {}".format(answers))
#         self.accept()
#         self._defered.callback(answers)


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
                 u"s'applique plus que l'autre.", html=False, size=(600, 80))
        layout.addWidget(explanation)

        gridlayout = QtGui.QGridLayout()
        gridlayout.setHorizontalSpacing(20)
        layout.addLayout(gridlayout)

        CURRENT_LINE = 0

        gridlayout.addWidget(MyLabel(u"<strong>Je me considère comme étant</strong>",
                                     align=QtCore.Qt.AlignHCenter),
                             CURRENT_LINE, 0, 1, 4)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Extraverti, enthousiaste"), CURRENT_LINE, 0)
        self._combo_extraverti = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_extraverti, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Critique, agressif"), CURRENT_LINE, 2)
        self._combo_critique = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_critique, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Digne de confiance, autodiscipliné"),
                             CURRENT_LINE, 0)
        self._combo_confiance = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_confiance, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Anxieux, facilement troublé"),
                             CURRENT_LINE, 2)
        self._combo_anxieux = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_anxieux, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Ouvert à de nouvelles expériences, "
                                     u"d'une personnalité complexe"),
                             CURRENT_LINE, 0)
        self._combo_complexe = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_complexe, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Réservé, tranquille"), CURRENT_LINE, 2)
        self._combo_reserve = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_reserve, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Sympathique, chaleureux"), CURRENT_LINE, 0)
        self._combo_sympathique = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_sympathique, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Désorganisé, négligent"), CURRENT_LINE, 2)
        self._combo_desorganise = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_desorganise, CURRENT_LINE, 3)

        CURRENT_LINE += 1

        gridlayout.addWidget(MyLabel(u"Calme, émotionnellement stable"),
                             CURRENT_LINE, 0)
        self._combo_calme = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_calme, CURRENT_LINE, 1)

        gridlayout.addWidget(MyLabel(u"Conventionnel, peu créatif"), CURRENT_LINE, 2)
        self._combo_conventionnel = MyComboBox(pms.ACCORD)
        gridlayout.addWidget(self._combo_conventionnel, CURRENT_LINE, 3)

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

            for k, v in self.__dict__.viewitems():
                if "combo" in k:
                    if v.currentIndex() == 0:
                        raise ValueError(u"Vous devez évaluer chacune des "
                                         u"paires de caractéristiques")
                    answers["BFT_{}".format(k.split("_", 2)[2])] = v.currentIndex()

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

        explication = WExplication(parent=self, size=(600, 50), html=False,
                                   text=u"Pour chacune des actions ci-dessous "
                                        u"sélectionner la fréquence avec laquelle "
                                        u"vous les avez effectuées")
        layout.addWidget(explication)

        gridlayout = QtGui.QGridLayout()
        gridlayout.setHorizontalSpacing(20)
        layout.addLayout(gridlayout)

        CURRENT_LINE = 0

        for k, v in sorted(pms.COOPERATION.viewitems()):
            if k % 2:  # num impairs
                gridlayout.addWidget(MyLabel(v), CURRENT_LINE, 0)
                setattr(self, "_combo_coop_{}".format(k),
                        MyComboBox(pms.FREQUENCE))
                gridlayout.addWidget(getattr(self, "_combo_coop_{}".format(k)),
                                     CURRENT_LINE, 1)
            else:  # num pairs
                gridlayout.addWidget(MyLabel(v), CURRENT_LINE, 2)
                setattr(self, "_combo_coop_{}".format(k),
                        MyComboBox(pms.FREQUENCE))
                gridlayout.addWidget(getattr(self, "_combo_coop_{}".format(k)),
                                     CURRENT_LINE, 3)
                CURRENT_LINE += 1

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

            for k, v in self.__dict__.viewitems():
                if "combo" in k:
                    if v.currentIndex() == 0:
                        raise ValueError(u"Vous avez oublié au moins une action")
                    answers[k.split("_", 2)[2].upper()] = v.currentIndex()

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
