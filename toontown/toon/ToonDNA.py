import random
from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
notify = directNotify.newCategory('ToonDNA')
#work in progress by leo
toonSpeciesNames = ('dog', 'cat', 'horse', 'mouse', 'rabbit', 'duck', 'monkey', 'bear', 'pig')
toonSpeciesTypes = ['d', 'c', 'h', 'm', 'r', 'f', 'p', 'b', 's']
toonHeadTypes = ['dls', 'dss', 'dsl', 'dll', 'cls', 'css', 'csl', 'cll', 'hls', 'hss', 'hsl', 'hll', 'mls', 'mss', 'rls', 'rss', 'rsl', 'rll', 'fls', 'fss', 'fsl', 'fll', 'pls', 'pss', 'psl', 'pll', 'bls', 'bss', 'bsl', 'bll', 'sls', 'sss', 'ssl', 'sll']

def getHeadList(species):
    headList = []
    for head in toonHeadTypes:
        if head[0] == species:
            headList.append(head)

    return headList

def getHeadStartIndex(species):
    for head in toonHeadTypes:
        if head[0] == species:
            return toonHeadTypes.index(head)
            
def getSpecies(head):
    for species in toonSpeciesTypes:
        if species == head[0]:
            return species

def getSpeciesNames(head)
	species = getSpecies(head)
	if species = 'd':
		speciesName = 'dog'
	elif species = 'c':
		speciesName = 'cat'
	elif species = 'h':
		speciesName = 'horse'
	elif species = 'm':
		speciesName = 'mouse'
	elif species = 'r':
		speciesName = 'rabbit'
	elif species = 'f':
		speciesName = 'duck'
	elif species = 'p':
		speciesName = 'monkey'
	elif species = 'b':
		speciesName = 'bear'
	elif species = 's':
		speciesName = 'pig'
	return speciesName

toonHeadAnimalIndices = [0, 4, 8, 12, 14, 18, 22, 26, 30]
toonHeadAnimalIndicesTrial = [0, 4, 12, 14, 18, 30]
allToonHeadAnimalIndices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
allToonHeadAnimalIndicesTrial = [0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 30, 31, 32, 33]
toonTorsoTypes = ['ss', 'ms', 'ls', 'sd', 'md', 'ld', 's', 'm', 'l']
toonLegTypes = ['s', 'm', 'l']

toonHeadAnimalIndices = [0,
 4,
 8,
 12,
 14,
 18,
 22,
 26,
 30]
toonHeadAnimalIndicesTrial = [0,
 4,
 12,
 14,
 18,
 30]
allToonHeadAnimalIndices = [0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33]
allToonHeadAnimalIndicesTrial = [0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 30,
 31,
 32,
 33]
toonTorsoTypes = ['ss',
 'ms',
 'ls',
 'sd',
 'md',
 'ld',
 's',
 'm',
 'l']
toonLegTypes = ['s', 'm', 'l']

	
