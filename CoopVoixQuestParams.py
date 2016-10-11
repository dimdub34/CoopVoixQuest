# -*- coding: utf-8 -*-
"""=============================================================================
This modules contains the variables and the parameters.
Do not change the variables.
Parameters that can be changed without any risk of damages should be changed
by clicking on the configure sub-menu at the server screen.
If you need to change some parameters below please be sure of what you do,
which means that you should ask to the developer ;-)
============================================================================="""

# variables --------------------------------------------------------------------
# TREATMENTS = {0: "baseline"}
COUPLE_LISTE = [u"Choisir", u"Moins d'un an", u'1 an', u'2 ans', u'3 ans', u'4 ans',
                u'5 ans', u'6 ans', u'7 ans', u'8 ans', u'9 ans', u'10 ans',
                u'11 ans', u'12 ans', u'13 ans', u'14 ans', u'15 ans',
                u'Plus de 15 ans']

ANNEES_ETUDES = [u"Choisir", u"Troisième", u"Seconde", u"Première", u"Terminale",
                 u"Bac", u"Bac+1", u"Bac+2", u"Bac+3", u"Bac+4", u"Bac+5",
                 u"Bac+8"]

CSP = [u"Choisir", u"Agriculteurs exploitants",
       u"Artisans, commerçants et chefs d'entreprise",
       u"Cadres et professions intellectuelles supérieures",
       u"Professions Intermédiaires", u"Employés", u"Ouvriers", u"Retraités",
       u"Autres personnes sans activité professionnelle", u"Etudiant"]

REVENUS = [u"Choisir", u"Moins de 200€", u"De 200 à 500€", u"De 500 à 950€",
           u"De 950 à 1200€", u"De 1200 à 1465€", u"De 1465 à 1745€",
           u"De 1745 à 2050€", u"De 2050 à 2385€", u"De 2385 à 2764€",
           u"De 2764 à 3280€", u"Plus de 3208€"]

# parameters -------------------------------------------------------------------
# TREATMENT = 0
# TAUX_CONVERSION = 1
NOMBRE_PERIODES = 0
TAILLE_GROUPES = 0

# GROUPES_CHAQUE_PERIODE = False
# MONNAIE = u"ecu"
#
# # DECISION
# DECISION_MIN = 0
# DECISION_MAX = 100
# DECISION_STEP = 1
#
#
# def get_treatment(code_or_name):
#     if type(code_or_name) is int:
#         return TREATMENTS.get(code_or_name, None)
#     elif type(code_or_name) is str:
#         for k, v in TREATMENTS.viewitems():
#             if v.lower() == code_or_name.lower():
#                 return k
#     return None
