# -*- coding: utf-8 -*-

import logging
from twisted.internet import defer
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from server.servbase import Base
from server.servparties import Partie
from util.utiltools import get_module_attributes
import CoopVoixQuestParams as pms


logger = logging.getLogger("le2m")


class PartieCVQ(Partie):
    __tablename__ = "partie_CoopVoixQuest"
    __mapper_args__ = {'polymorphic_identity': 'CoopVoixQuest'}
    partie_id = Column(Integer, ForeignKey('parties.id'), primary_key=True)
    repetitions = relationship('RepetitionsCVQ')

    def __init__(self, le2mserv, joueur):
        super(PartieCVQ, self).__init__(
            nom="CoopVoixQuest", nom_court="CVQ",
            joueur=joueur, le2mserv=le2mserv)
        self.CVQ_gain_ecus = 0
        self.CVQ_gain_euros = 0

    @defer.inlineCallbacks
    def configure(self):
        logger.debug(u"{} Configure".format(self.joueur))
        yield (self.remote.callRemote("configure", get_module_attributes(pms)))
        self.joueur.info(u"Ok")

    @defer.inlineCallbacks
    def newperiod(self, period):
        """
        Create a new period and inform the remote
        If this is the first period then empty the historic
        :param periode:
        :return:
        """
        logger.debug(u"{} New Period".format(self.joueur))
        self.currentperiod = RepetitionsCVQ(period)
        self.le2mserv.gestionnaire_base.ajouter(self.currentperiod)
        self.repetitions.append(self.currentperiod)
        yield (self.remote.callRemote("newperiod", period))
        logger.info(u"{} Ready for period {}".format(self.joueur, period))

    @defer.inlineCallbacks
    def display_decision(self):
        logger.debug(u"{} Decision".format(self.joueur))
        answers_demo = yield(self.remote.callRemote("display_demo"))
        for k, v in answers_demo.viewitems():
            setattr(self.currentperiod, k, v)
        self.joueur.info(u"Ok quest. démo")
        answers_coop = yield(self.remote.callRemote("display_coop"))
        for k, v in answers_coop.viewitems():
            setattr(self.currentperiod, k, v)
        self.joueur.info(u"Ok quest. coop")
        answers_bigfive = yield(self.remote.callRemote("display_bigfive"))
        for k, v in answers_bigfive.viewitems():
            setattr(self.currentperiod, k, v)
        self.joueur.info(u"Ok quest. bigfive")
        self.joueur.remove_waitmode()


class RepetitionsCVQ(Base):
    __tablename__ = 'partie_CoopVoixQuest_repetitions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    partie_partie_id = Column(
        Integer,
        ForeignKey("partie_CoopVoixQuest.partie_id"))

    CVQ_period = Column(Integer)

    # demo
    CVQ_naissance_mois = Column(Integer)
    CVQ_naissance_annee = Column(Integer)
    CVQ_naissance_pays = Column(Integer)
    CVQ_naissance_pere = Column(Integer)
    CVQ_naissance_mere = Column(Integer)
    CVQ_couple = Column(Integer)
    CVQ_couple_temps = Column(Integer)
    CVQ_couple_partenaire_naissance = Column(Integer)
    CVQ_partenaires_heteros = Column(Integer)
    CVQ_partenaires_homos = Column(Integer)
    CVQ_etudes = Column(Integer)
    CVQ_proprietaire = Column(Integer)
    CVQ_revenu = Column(Integer)
    CVQ_csp = Column(Integer)
    CVQ_fumeur = Column(Integer)
    CVQ_cigarette = Column(Integer)
    CVQ_cigarette_electronique = Column(Integer)
    CVQ_lever = Column(String)
    CVQ_sommeil = Column(String)
    CVQ_medicaments = Column(Integer)
    CVQ_medicaments_noms = Column(String)
    CVQ_chant = Column(Integer)
    CVQ_theatre = Column(Integer)
    CVQ_hier_douche = Column(Integer)
    CVQ_hier_deodorant = Column(Integer)
    CVQ_hier_parfum = Column(Integer)
    CVQ_jour_douche = Column(Integer)
    CVQ_jour_deodorant = Column(Integer)
    CVQ_jour_parfum = Column(Integer)
    CVQ_jour_sport = Column(Integer)

    # coop
    COOP_confiance = Column(Integer)
    COOP_profite = Column(Integer)
    COOP_altruiste = Column(Integer)
    COOP_portefeuille_inconnu = Column(Integer)
    COOP_portefeuille_voisin = Column(Integer)

    # big five
    BFT_extraverti = Column(Integer)
    BFT_critique = Column(Integer)
    BFT_confiance = Column(Integer)
    BFT_anxieux = Column(Integer)
    BFT_complexe = Column(Integer)
    BFT_reserve = Column(Integer)
    BFT_sympathique = Column(Integer)
    BFT_desorganise = Column(Integer)
    BFT_calme = Column(Integer)
    BFT_conventionnel = Column(Integer)

    def __init__(self, period):
        self.CVQ_period = period


    def todict(self, joueur=None):
        temp = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        if joueur:
            temp["joueur"] = joueur
        return temp

