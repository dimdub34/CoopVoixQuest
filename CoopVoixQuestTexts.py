# -*- coding: utf-8 -*-
"""
This module contains the texts of the part (server and remote)
"""

from util.utiltools import get_pluriel
import CoopVoixQuestParams as pms
from util.utili18n import le2mtrans
import os
import configuration.configparam as params
import gettext
import logging

logger = logging.getLogger("le2m")
localedir = os.path.join(params.getp("PARTSDIR"), "CoopVoixQuest", "locale")
try:
    trans_CVQ = gettext.translation(
      "CoopVoixQuest", localedir, languages=[params.getp("LANG")]).ugettext
except IOError:
    logger.critical(u"Translation file not found")
    trans_CVQ = lambda x: x  # if there is an error, no translation


def get_text_explanation_demo():
    return trans_CVQ(u"Merci de remplir le questionnaire ci-dessous."
                     u"<br />Les informations saisies sont totalement anonymes.")


def get_text_explanation_coop():
    return trans_CVQ(u"")


def get_text_explanation_bigfive():
    return trans_CVQ(u"")

