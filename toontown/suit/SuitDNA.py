import random
from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
import SuitLocalizerGlobals
import random
from zones import ZoneIdLocalizer
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
notify = directNotify.newCategory('SuitDNA')
suitHeadTypes = ['f', 'p', 'ym', 'mm', 'ds', 'hh', 'cr', 'tbc', 'bf', 'b', 'dt', 'ac', 'bs', 'sd', 'le', 'bw', 'sc', 'pp', 'tw', 'bc', 'nc', 'mb', 'ls', 'rb', 'cc', 'tm', 'nd', 'gh', 'ms', 'm', 'mh']
suitATypes = ['ym', 'hh', 'tbc', 'dt', 'bs', 'le', 'bw', 'pp', 'nc', 'rb', 'nd', 'tf', 'm', 'mh']
suitBTypes = ['p', 'ds', 'b', 'ac', 'sd', 'bc', 'ls', 'tm', 'ms'] 
suitCTypes = ['f', 'mm', 'cr', 'bf', 'sc', 'tw', 'mb', 'cc', 'gh']
suitClasses = ['c', 'l', 'm', 's']
suitClassZones = [ZoneIdLocalizer.BossbotHQ, ZoneIdLocalizer.LawbotHQ, ZoneIdLocalizer.CashbotHQ, ZoneIdLocalizer.SellbotHQ]
#under construction


		
