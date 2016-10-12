# -*- coding: utf-8 -*-

import logging
from collections import OrderedDict
from twisted.internet import defer
from time import strftime
from util.utili18n import le2mtrans
import CoopVoixQuestParams as pms


logger = logging.getLogger("le2m.{}".format(__name__))


class Serveur(object):
    def __init__(self, le2mserv):
        self._le2mserv = le2mserv
        actions = OrderedDict()
        actions[le2mtrans(u"Start")] = lambda _: self._demarrer()
        self._le2mserv.gestionnaire_graphique.add_topartmenu(
            u"Questionnaire Cooperation Voix", actions)

    @defer.inlineCallbacks
    def _demarrer(self):
        """
        Start the part
        :return:
        """
        # check conditions =====================================================
        if not self._le2mserv.gestionnaire_graphique.question(
                        le2mtrans(u"Start") + u" CoopVoixQuest?"):
            return

        # init part ============================================================
        yield (self._le2mserv.gestionnaire_experience.init_part(
            "CoopVoixQuest", "PartieCVQ",
            "RemoteCVQ", pms))
        self._tous = self._le2mserv.gestionnaire_joueurs.get_players(
            'CoopVoixQuest')

        # set parameters on remotes
        yield (self._le2mserv.gestionnaire_experience.run_step(
            le2mtrans(u"Configure"), self._tous, "configure"))
        
        # Start part ===========================================================
        for period in range(1 if pms.NOMBRE_PERIODES else 0,
                        pms.NOMBRE_PERIODES + 1):

            if self._le2mserv.gestionnaire_experience.stop_repetitions:
                break

            yield (self._le2mserv.gestionnaire_experience.run_func(
                self._tous, "newperiod", period))
            
            yield(self._le2mserv.gestionnaire_experience.run_step(
                le2mtrans(u"Decision"), self._tous, "display_decision"))
            
        self._le2mserv.gestionnaire_graphique.infoserv(
            le2mtrans(u"End time: {et}").format(et=strftime("%H:%M:%S")))
        self._le2mserv.gestionnaire_graphique.infoclt(
            u'Ok {}'.format("CoopVoixQuest").upper(), fg="white", bg="blue")
        self._le2mserv.gestionnaire_graphique.infoserv(
            u'Ok {}'.format("CoopVoixQuest").upper(), fg="white", bg="blue")
