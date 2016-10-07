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
COUPLE_LISTE = [u"Moins d'un an", u'1 an', u'2 ans', u'3 ans', u'4 ans',
                u'5 ans', u'6 ans', u'7 ans', u'8 ans', u'9 ans', u'10 ans',
                u'11 ans', u'12 ans', u'13 ans', u'14 ans', u'15 ans',
                u'Plus de 15 ans']


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
