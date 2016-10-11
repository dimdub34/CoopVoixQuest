# -*- coding: utf-8 -*-

import logging
import random

from twisted.internet import defer
from client.cltremote import IRemote
import CoopVoixQuestParams as pms
from CoopVoixQuestGui import GuiDemo
import CoopVoixQuestTexts as texts_CVQ


logger = logging.getLogger("le2m")


class RemoteCVQ(IRemote):
    """
    Class remote, remote_ methods can be called by the server
    """
    def __init__(self, le2mclt):
        IRemote.__init__(self, le2mclt)
        # self._histo_vars = [
        #     "CVQ_period", "CVQ_decision",
        #     "CVQ_periodpayoff", "CVQ_cumulativepayoff"]
        # self._histo.append(texts_CVQ.get_histo_head())

    def remote_configure(self, params):
        """
        Set the same parameters as in the server side
        :param params:
        :return:
        """
        logger.info(u"{} configure".format(self._le2mclt.uid))
        for k, v in params.viewitems():
            setattr(pms, k, v)

    def remote_newperiod(self, period):
        """
        Set the current period and delete the history
        :param period: the current period
        :return:
        """
        logger.info(u"{} Period {}".format(self._le2mclt.uid, period))
        self.currentperiod = period
        if self.currentperiod == 1:
            del self.histo[1:]


    def remote_display_demo(self):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} quest. demo".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            answers = {}
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else: 
            defered = defer.Deferred()
            ecran_demo = GuiDemo(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_demo.show()
            return defered


    def remote_display_coop(self):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} quest. coop".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            answers = {}
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else:
            defered = defer.Deferred()
            ecran_demo = GuiDemo(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_demo.show()
            return defered

    def remote_display_bigfive(self):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} quest. bigfive".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            answers = {}
            logger.info(
                u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else:
            defered = defer.Deferred()
            ecran_demo = GuiDemo(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_demo.show()
            return defered

