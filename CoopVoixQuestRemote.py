# -*- coding: utf-8 -*-

import logging
from random import randint

from twisted.internet import defer
from client.cltremote import IRemote
import CoopVoixQuestParams as pms
from CoopVoixQuestGui import GuiDemo, GuiCoop, GuiBigFiveTen


logger = logging.getLogger("le2m")


class RemoteCVQ(IRemote):
    """
    Class remote, remote_ methods can be called by the server
    """
    def __init__(self, le2mclt):
        IRemote.__init__(self, le2mclt)

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
            answers["CVQ_naissance_mois"] = randint(1, 12)
            answers["CVQ_naissance_annee"] = randint(1975, 2000)
            answers["CVQ_naissance_pays"] = randint(1, 182)
            answers["CVQ_naissance_pere"] = randint(1940, 1965)
            answers["CVQ_naissance_mere"] = randint(1940, 1965)
            answers["CVQ_couple"] = randint(0, 1)
            if answers["CVQ_couple"] == 1:
                answers["CVQ_couple_temps"] = randint(1, 16)
                answers["CVQ_couple_partenaire_naissance"] = randint(1975, 2000)
            answers["CVQ_partenaires_heteros"] = randint(0, 15)
            answers["CVQ_partenaires_homos"] = randint(0, 15)
            answers["CVQ_etudes"] = randint(1, 8)
            answers["CVQ_proprietaire"] = randint(0, 1)
            answers["CVQ_revenu"] = randint(0, 7)
            answers["CVQ_csp"] = randint(0, 6)
            answers["CVQ_fumeur"] = randint(0, 1)
            answers["CVQ_cigarette"] = randint(0, 30)
            answers["CVQ_cigarette_electronique"] = randint(0, 1)
            answers["CVQ_lever"] = "0{}:00".format(randint(6, 8))
            answers["CVQ_sommeil"] = "0{}:00".format(randint(6, 9))
            answers["CVQ_medicaments"] = randint(0, 1)
            if answers["CVQ_medicaments"] == 1:
                answers["CVQ_medicaments_noms"] = u"aspirine"
            else:
                answers["CVQ_medicaments_noms"] = u""
            answers["CVQ_chant"] = randint(0, 1)
            answers["CVQ_theatre"] = randint(0, 1)
            answers["CVQ_hier_douche"] = randint(0, 1)
            answers["CVQ_hier_deodorant"] = randint(0, 1)
            answers["CVQ_hier_parfum"] = randint(0, 1)
            answers["CVQ_jour_douche"] = randint(0, 1)
            answers["CVQ_jour_deodorant"] = randint(0, 1)
            answers["CVQ_jour_parfum"] = randint(0, 1)
            answers["CVQ_jour_sport"] = randint(0, 1)
            answers["CVQ_produits_parfumes"] = u"Texte automatique"
            answers["CVQ_vegetarien"] = randint(0, 1)
            answers["CVQ_oignon"] = randint(0, 1)
            answers["CVQ_ail"] = randint(0, 1)
            answers["CVQ_piment"] = randint(0, 1)
            answers["CVQ_curry"] = randint(0, 1)
            answers["CVQ_chou"] = randint(0, 1)
            answers["CVQ_celeri"] = randint(0, 1)
            answers["CVQ_fromages"] = randint(0, 1)
            answers["CVQ_asperges"] = randint(0, 1)
            answers["CVQ_alcool"] = randint(0, 1)
            answers["CVQ_malade"] = randint(0, 1)
            if answers["CVQ_malade"]:
                answers["CVQ_maladie"] = u"Rhume"
            else:
                answers["CVQ_maladie"] = u""
            answers["CVQ_stress"] = randint(1, 9)
            answers["CVQ_dormi_deux"] = randint(0, 1)
            answers["CVQ_relation_sexuelle"] = randint(0, 1)
            answers["CVQ_bien_public"] = randint(0, 1)

            logger.info(u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else: 
            defered = defer.Deferred()
            ecran_demo = GuiDemo(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_demo.show()
            return defered

    # def remote_display_coop(self):
    #     """
    #     Display the decision screen
    #     :return: deferred
    #     """
    #     logger.info(u"{} quest. coop".format(self._le2mclt.uid))
    #     if self._le2mclt.simulation:
    #         answers = {}
    #         answers["COOP_confiance"] = randint(0, 1)
    #         answers["COOP_profite"] = randint(1, 9)
    #         answers["COOP_altruiste"] = randint(1, 4)
    #         answers["COOP_portefeuille_inconnu"] = randint(1, 4)
    #         answers["COOP_portefeuille_voisin"] = randint(1, 4)
    #         logger.info(u"{} Send back {}".format(self._le2mclt.uid, answers))
    #         return answers
    #     else:
    #         defered = defer.Deferred()
    #         ecran_coop = GuiCoop(
    #             defered, self._le2mclt.automatique,
    #             self._le2mclt.screen)
    #         ecran_coop.show()
    #         return defered

    def remote_display_bigfive(self):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} quest. bigfive".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            answers = {}
            answers["BFT_extraverti"] = randint(1, 6)
            answers["BFT_critique"] = randint(1, 6)
            answers["BFT_confiance"] = randint(1, 6)
            answers["BFT_anxieux"] = randint(1, 6)
            answers["BFT_complexe"] = randint(1, 6)
            answers["BFT_reserve"] = randint(1, 6)
            answers["BFT_sympathique"] = randint(1, 6)
            answers["BFT_desorganise"] = randint(1, 6)
            answers["BFT_calme"] = randint(1, 6)
            answers["BFT_conventionnel"] = randint(1, 6)
            logger.info(
                u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else:
            defered = defer.Deferred()
            ecran_bigfive = GuiBigFiveTen(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_bigfive.show()
            return defered


    def remote_display_coop(self):
        """
        Display the decision screen
        :return: deferred
        """
        logger.info(u"{} quest. coop".format(self._le2mclt.uid))
        if self._le2mclt.simulation:
            answers = {}
            for i in range(1, 21):
                answers["COOP_{}".format(i)] = randint(1, 5)
            logger.info(u"{} Send back {}".format(self._le2mclt.uid, answers))
            return answers
        else:
            defered = defer.Deferred()
            ecran_coop = GuiCoop(
                defered, self._le2mclt.automatique,
                self._le2mclt.screen)
            ecran_coop.show()
            return defered

