from BattleBase import *
import random
import math
from direct.directnotify import DirectNotifyGlobal
from toontown.suit import SuitLocalizerGlobals
notify = DirectNotifyGlobal.directNotify.newCategory('SuitBattleGlobals')
#NEEDS ALOT OF WORK ON, NOT COMPLETE, GAME NEEDS TO BE CODED THAT IT DEFINES ALL THE COG TIERS, BUSINESS CLASSES, ATTACK DAMAGE, ACCURACY, AND CHANCE BEING USED. CRITICAL HIT SYSTEM NEEDS TO BE ADDED. 
#BOSSBOTS HAVE SLIGHTLY MORE HP THAN OTHER COGS, SELLBOTS ARE GROUP ATTACK HEAVY, CASHBOTS HAVE SOMEWHAT MORE DAMAGE, LAWBOTS I'M NOT SURE

#DEF TIER FUCTION NOT COMPLETE. NEEDS ADDING/REWORKING

SuitAttributes = {'f':  {'name': SuitLocalizerGlobals.SuitFlunky,
		'singularname': SuitLocalizerGlobals.SuitFlunkyS,
		'pluralname': SuitLocalizerGlobals.SuitFlunkyP,
		'class': SuitLocalizerGlobals.BossbotClass,
		'tier': 1,
		'hp': (19, 25, 33, 43, 58),
		'attacks':
			(('PoundKey', (3, 7, 12, 15, 18), (75, 75, 80, 80, 85), (30, 30, 30, 30, 30)),
			 ('Shred', (2, 5, 9, 12, 14, 15), (80, 80, 85, 85, 90), (30, 30, 30, 30, 30)),
			 ('ClipOnTie', (2, 6, 11, 14, 17), (75, 75, 80, 80, 85), (30, 30, 30, 30, 30)))},
 'p': {'name': SuitLocalizerGlobals.SuitPencilPusher,
	   'singularname': SuitLocalizerGlobals.SuitPencilPusherS,
	   'pluralname': SuitLocalizerGlobals.SuitPencilPusherP,
	   'class': SuitLocalizerGlobals.BossbotClass,
	   'tier': 2,
	   'hp': (25, 33, 43, 58, 71),
	   'attacks':
		   (('FountainPen', (3, 8, 13, 15, 17), (75, 75, 80, 80, 85), (25, 25, 25, 25, 25)),
		    ('RubOut', (5, 9, 14, 17, 19), (60, 60, 60, 65, 65), (25, 25, 25, 25, 25)),
		    ('FingerWag', (3, 6, 9, 13, 15), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
		    ('WriteOff', (4, 7, 11, 14, 17), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
		    ('FillWithLead', (6, 10, 14, 16, 20), (60, 60, 65, 65, 70), (20, 20, 20, 20, 20)))},
 'ym': {'name': SuitLocalizerGlobals.SuitYesman,
        'singularname': SuitLocalizerGlobals.SuitYesmanS,
        'pluralname': SuitLocalizerGlobals.SuitYesmanP,
        'class': SuitLocalizerGlobals.BossbotClass,
        'tier': 3, 
        'hp': (33, 43, 58, 71, 89),
        'attacks':
			(('RubberStamp', (6, 9, 13, 17, 20), (70, 70, 70, 75, 80), (30, 30, 30, 30, 30)),
			 ('RazzleDazzle', (4, 7, 11, 15, 21), (70, 70, 70, 75, 80), (30, 30, 30, 30, 30)),
			 ('Synergy', (5, 8, 12, 16, 18), (70, 70, 75, 75, 75), (30, 30, 30, 30, 30)),
			 ('TeeOff', (5, 7, 11, 14, 16), (70, 70, 70, 75, 80), (30, 30, 30, 30, 30)))},
 'mm': {'name': SuitLocalizerGlobals.SuitMicromanager,
		'singularname': SuitLocalizerGlobals.SuitMicromanagerS,
		'pluralname': SuitLocalizerGlobals.SuitMicromanagerP,
		'class': SuitLocalizerGlobals.BossbotClass,
		'tier': 4, 
		'hp': (43, 58, 71, 89, 110),
		'attacks':
			(('Demotion', (8, 12, 16, 18, 22), (65, 65, 65, 70, 70), (25, 25, 25, 25, 25)),
			 ('FingerWag', (7, 10, 13, 16, 19), (75, 75, 75, 80, 80), (25, 25, 25, 25, 25)),
			 ('FountainPen', (5, 7, 11, 14, 17), (75, 80, 80, 80, 85), (25, 25, 25, 25, 25)),
			 ('BrainStorm', (10, 14, 18, 21, 25), (40, 40, 40, 40, 40), (15, 15, 15, 15, 15)),
			 ('BuzzWord', (6, 9, 12, 15, 17, 20), (60, 60, 65, 65, 70), (20, 20, 20, 20, 20)))},
 'ds': {'name': SuitLocalizerGlobals.SuitDownsizer,
		'singularname': SuitLocalizerGlobals.SuitDownsizerS,
		'pluralname': SuitLocalizerGlobals.SuitDownsizerP,
		'class': SuitLocalizerGlobals.BossbotClass,
		'tier': 5,
		'hp': (58, 71, 89, 110, 130),
		'attacks':
			(('Canned', (9, 13, 16, 19, 24), (65, 65, 70, 75, 80), (25, 25, 30, 30, 35)),
			 ('Downsize', (10, 14, 17, 20, 25), (65, 65, 70, 70, 75), (20, 20, 20, 25, 25)),
			 ('PinkSlip', (8, 12, 15, 18, 21), (70, 70, 75, 75, 80), (20, 20, 20, 20, 20)),
			 ('Sacked', (12, 16, 20, 22, 26), (60, 60, 60, 65, 65), (10, 10, 10, 10, 10)))},
 'hh': {'name': SuitLocalizerGlobals.SuitHeadHunter,
		'singularname': SuitLocalizerGlobals.SuitHeadHunterS,
		'pluralname': SuitLocalizerGlobals.SuitHeadHunterP,
		'class': SuitLocalizerGlobals.BossbotClass,
		'tier': 6,
		'hp': (71, 89, 110, 130, 155),
		'attacks':
			(('FountainPen', (8, 12, 16, 18, 21), (65, 65, 70, 75, 75), (25, 25, 25, 25, 25)),
			 ('GlowerPower', (9, 14, 17, 20, 23), (65, 65, 65, 70, 75), (25, 25, 25, 25, 25)),
			 ('HalfWindsor', (7, 11, 15, 17, 20), (70, 75, 75, 80, 85), (25, 25, 25, 25, 25)),
			 ('HeadShrink', (11, 15, 19, 23, 28), (60, 65, 65, 70, 75), (20, 20, 20, 20, 20)),
			 ('ReOrg', (10, 14, 18, 22, 26), (60, 60, 65, 65, 70), (20, 20, 20, 20, 20)),
			 ('Rolodex', (9, 12, 15, 17, 21), (70, 70, 70, 75, 75), (25, 25, 25, 25, 25)))},
 'cr': {'name': SuitLocalizerGlobals.SuitCorporateRaider,
		'singularname': SuitLocalizerGlobals.CorporateRaiderS,
		'pluralname': SuitLocalizerGlobals.CorporateRaiderP,
		'class': SuitLocalizerGlobals.BossbotClass,
		'tier': 7,
		'hp': (89, 110, 130, 155, 180),
		'attacks':
			(('Canned', (10, 14, 18, 21, 26), (65, 65, 70, 70, 75), (25, 25, 25, 25, 25)),
			 ('EvilEye', (12, 16, 20, 24, 30), (60, 60, 65, 65, 70), (25, 25, 25, 25, 25)),
			 ('PickPocket', (11, 13, 19, 22, 28), (65, 65, 65, 70, 75), (25, 25, 25, 25, 25)),
			 ('PlayHardball', (10, 12, 15, 19, 23), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)),
			 ('PowerTie', (10, 12, 14, 17, 20), (70, 80, 80, 80, 80), (25, 25, 25, 25, 25)))},
 'tbc': {'name': SuitLocalizerGlobals.SuitTheBigCheese,
		 'singularname': SuitLocalizerGlobals.SuitTheBigCheeseS,
		 'pluralname': SuitLocalizerGlobals.SuitTheBigCheeseP,
		 'class': SuitLocalizerGlobals.BossbotClass,
		 'tier': 8,
		 'hp': (110, 130, 155, 180, 230),
		 'attacks':
			 (('SongAndDance', (12, 16, 23, 26, 32), (70, 70, 70, 70, 75), (25, 25, 25, 25, 25)),
			  ('CigarSmoke', (11, 14, 20, 24, 30), (70, 70, 70, 70, 75), (25, 25, 25, 25, 25)),
			  ('GlowerPower', (14, 17, 21, 26, 34) (70, 70, 70, 70, 75), (25, 25, 25, 25, 25)),
			  ('TeeOff', (10, 12, 17, 20, 23, 28), (70, 75, 75, 80, 85), (25, 25, 25, 25, 25)))},
 'cc': {'name': SuitLocalizerGlobals.SuitColdCaller,
		'singularname': SuitLocalizerGlobals.SuitColdCallerS,
		'pluralname': SuitLocalizerGlobals.SuitColdCallerP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 1, 
		'hp': (9, 15, 23, 33, 48),
		'attacks':
			(('FreezeAssets', (4, 8, 12, 15, 18), (65, 65, 70, 70, 75), (30, 30, 30, 30, 30)),
			 ('PoundKey', (3, 5, 10, 12, 16), (70, 70, 75, 75, 80), (30, 30, 30, 30, 30)),
			 ('DoubleTalk', (3, 4, 9, 11, 14), (90, 90, 90, 90, 90), (30, 30, 30, 30, 30)),
			 ('HotAir', (3, 7, 11, 14, 17), (65, 65, 70, 70, 75), (30, 30, 30, 30, 30)))},
 'tm': {'name': SuitLocalizerGlobals.SuitTelemarketer,
		'singularname': SuitLocalizerGlobals.SuitTelemarketerS,
		'pluralname': SuitLocalizerGlobals.SuitTelemarketerP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 2,
		'hp': (15, 23, 33, 48, 61),
		'attacks':
			(('ClipOnTie', (5, 9, 13, 15, 17), (65, 70, 70, 75, 80), (30, 30, 30, 30, 30)),
			 ('PickPocket', (6, 10, 14, 18, 19), (65, 70, 70, 70, 75), (30, 30, 30, 30, 30)),
			 ('DoubleTalk', (4, 7, 10, 13, 15), (80, 80, 80, 80, 85), (30, 30, 30, 30, 30)),
			 ('Rolodex', (7, 11, 14, 17, 20), (60, 60, 65, 70, 70), (30, 30, 30, 30, 30)))},
 'nd': {'name': SuitLocalizerGlobals.SuitNameDropper,
		'singularname': SuitLocalizerGlobals.SuitNameDropperS,
		'pluralname': SuitLocalizerGlobals.SuitNameDropperP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 3,
		'hp': (23, 33, 48, 61, 79),
		'attacks':
			(('RazzleDazzle', (7, 13, 17, 20, 23), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Rolodex', (5, 10, 14, 17, 20), (75, 75, 75, 80, 80), (30, 30, 30, 30, 30)),
			 ('Synergy', (4, 9, 13, 16, 19), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('PickPocket', (3, 7, 11, 14, 17), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)))},
 'gh': {'name': SuitLocalizerGlobals.SuitGladHander,
		'singularname': SuitLocalizerGlobals.SuitGladHanderS,
		'pluralname': SuitLocalizerGlobals.SuitGladHanderP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 4,
		'hp': (33, 48, 61, 79, 100),
		'attacks':
			(('RubberStamp', (10, 10, 10, 10, 10), (100, 100, 100, 100, 100), (25, 25, 25, 25, 25)),
			 ('FountainPen', (12, 12, 12, 12, 12), (100, 100, 100, 100, 100), (25, 25, 25, 25, 25)),
			 ('Filibuster', (7, 13, 15, 17, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Schmooze', (10, 12, 16, 20, 25), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'ms': {'name': SuitLocalizerGlobals.SuitMoverShaker,
		'singularname': SuitLocalizerGlobals.SuitMoverShakerS,
		'pluralname': SuitLocalizerGlobals.SuitMoverShakerP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 5,
		'hp': (48, 61, 79, 100, 120),
		'attacks':
			(('Quake', (10, 13, 16, 19, 24), (70, 75, 75, 75, 80), (30, 30, 30, 30, 30)),
			 ('Shake', (7, 10, 13, 16, 21), (75, 75, 75, 80, 85), (30, 30, 30, 30, 30)),
			 ('Tremor', (5, 9, 11, 14, 19), (75, 75, 80, 85, 90), (30, 30, 30, 30, 30)),
			 ('BrainStorm', (5, 8, 12, 15, 20), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('HalfWindsor', (6, 9, 13, 16, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'tf': {'name': SuitLocalizerGlobals.SuitTwoFace,
		'singularname': SuitLocalizerGlobals.SuitTwoFaceS,
		'pluralname': SuitLocalizerGlobals.SuitTwoFaceP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 6,
		'hp': (61, 79, 100, 120, 145),
		'attacks':
			(('EvilEye', (12, 15, 19, 22, 25), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('HangUp', (10, 13, 17, 20, 23), (70, 70, 70, 70, 75), (25, 25, 25, 25, 25)),
			 ('RazzleDazzle', (11, 14, 18, 21, 24), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('ReOrg', (14, 18, 22, 24, 26), (65, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('RedTape', (9, 11, 15, 17, 20), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)))},
 'm': {'name': SuitLocalizerGlobals.SuitTheMingler,
	   'singularname': SuitLocalizerGlobals.SuitTheMinglerS,
	   'pluralname': SuitLocalizerGlobals.SuitTheMinglerP,
	   'class': SuitLocalizerGlobals.SellbotClass,
	   'tier': 7,
	   'hp': (79, 100, 120, 145, 170),
	   'attacks':
		   (('ParadigmShift', (14, 17, 20, 23, 29), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
		    ('BuzzWord', (11, 14, 17, 20, 26), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
		    ('PowerTrip', (12, 15, 18, 21, 27), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
		    ('Schmooze', (9, 12, 15, 19, 23), (85, 85, 85, 85, 85), (25, 25, 25, 25, 25)),
		    ('TeeOff', (7, 9, 13, 17, 21), (90, 90, 90, 90, 90), (25, 25, 25, 25, 25)))},
 'mh': {'name': SuitLocalizerGlobals.SuitMrHollywood,
		'singularname': SuitLocalizerGlobals.SuitMrHollywoodS,
		'pluralname': SuitLocalizerGlobals.SuitMrHollywoodP,
		'class': SuitLocalizerGlobals.SellbotClass,
		'tier': 8,
		'hp': (100, 120, 145, 170, 220),
		'attacks':
			(('SongAndDance', (15, 19, 23, 27, 32), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)),
			 ('CigarSmoke', (13, 17, 21, 25, 30), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)),
			 ('PowerTrip', (14, 18, 22, 26, 31), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)),
			 ('RazzleDazzle', (14, 18, 22, 26, 31), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)))},
 'sc': {'name': SuitLocalizerGlobals.SuitShortChange,
		'singularname': SuitLocalizerGlobals.SuitShortChangeS,
		'pluralname': SuitLocalizerGlobals.SuitShortChangeP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 1,
		'hp': (9, 15, 23, 33, 48),
		'attacks':
			(('Watercooler', (3, 7, 12, 14, 18), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('BounceCheck', (4, 9, 14, 16, 19), (75, 75, 75, 75, 75), (15, 15, 15, 15, 15)),
			 ('ClipOnTie', (2, 5, 10, 13, 15), (90, 90, 90, 90, 90), (25, 25, 25, 25, 25)),
			 ('PickPocket', (3, 6, 11, 14, 16), (90, 90, 90, 90, 90), (25, 25, 25, 25, 25)))},
 'pp': {'name': SuitLocalizerGlobals.SuitPennyPincher,
		'singularname': SuitLocalizerGlobals.SuitPennyPincherS,
		'pluralname': SuitLocalizerGlobals.SuitPennyPincherP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 2,
		'hp': (15, 23, 33, 48, 61),
		'attacks':
			(('BounceCheck', (6, 10, 14, 18, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('FreezeAssets', (4, 8, 12, 16, 19), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('FingerWag', (3, 7, 11, 15, 18), (80, 80, 85, 85, 85), (25, 25, 25, 25, 25)))},
 'tw': {'name': SuitLocalizerGlobals.SuitTightwad,
		'singularname': SuitLocalizerGlobals.SuitTightwadS,
		'pluralname': SuitLocalizerGlobals.SuitTightwadP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 3,
		'hp': (23, 33, 48, 61, 79),
		'attacks':
			(('Fired', (7, 11, 15, 19, 22), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('GlowerPower', (9, 13, 17, 20, 23), (65, 65, 65, 65, 70), (25, 25, 25, 25, 25)),
			 ('FingerWag', (4, 9, 12, 15, 18), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('FreezeAssets', (5, 10, 13, 16, 19), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('BounceCheck', (7, 12, 15, 18, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'bc': {'name': SuitLocalizerGlobals.SuitBeanCounter,
		'singularname': SuitLocalizerGlobals.SuitBeanCounterS,
		'pluralname': SuitLocalizerGlobals.SuitBeanCounterP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 4,
		'hp': (33, 48, 61, 79, 100),
		'attacks':
			(('Audit', (10, 14, 17, 21, 24), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('Calculate', (10, 14, 17, 21, 24), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('Tabulate', (10, 14, 17, 21, 24), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('WriteOff', (10, 14, 17, 21, 24), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)))},
 'nc': {'name': SuitLocalizerGlobals.SuitNumberCruncher,
		'singularname': SuitLocalizerGlobals.SuitNumberCruncherS,
		'pluralname': SuitLocalizerGlobals.SuitNumberCruncherP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 5,
		'hp': (48, 61, 79, 100, 120),
		'attacks':
			(('Audit', (10, 14, 17, 21, 24), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('Calculate', (11, 15, 18, 22, 25), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('Tabulate', (12, 16, 19, 23, 26), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('Crunch', (14, 18, 21, 25, 28), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)))},
 'mb': {'name': SuitLocalizerGlobals.SuitMoneyBags,
		'singularname': SuitLocalizerGlobals.SuitMoneyBagsS,
		'pluralname': SuitLocalizerGlobals.SuitMoneyBagsP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 6,
		'hp': (61, 79, 100, 120, 145),
		'attacks':
			(('Liquidate', (12, 15, 18, 21, 27), (70, 70, 70, 75, 75), (25, 25, 25, 25, 25)),
			 ('MarketCrash', (14, 17, 21, 24, 30), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('PowerTie', (11, 14, 17, 20, 25), (80, 80, 80, 85, 85), (25, 25, 25, 25, 25)))},
 'ls': {'name': SuitLocalizerGlobals.SuitLoanShark,
		'singularname': SuitLocalizerGlobals.SuitLoanSharkS,
		'pluralname': SuitLocalizerGlobals.SuitLoanSharkP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 7,
		'hp': (79, 100, 120, 145, 170),
		'attacks':
			(('Bite', (14, 17, 21, 25, 31), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Chomp', (16, 19, 23, 27, 33), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Quake', (15, 18, 22, 26, 32), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('PlayHardball', (13, 16, 20, 24, 30), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('WriteOff', (11, 14, 18, 22, 28), (85, 85, 85, 85, 85), (25, 25, 25, 25, 25)))},
 'rb': {'name': SuitLocalizerGlobals.SuitRobberBaron,
		'singularname': SuitLocalizerGlobals.SuitRobberBaronS,
		'pluralname': SuitLocalizerGlobals.SuitRobberBaronP,
		'class': SuitLocalizerGlobals.CashbotClass,
		'tier': 8,
		'hp': (100, 120, 145, 170, 220),
		'attacks':
			(('PowerTrip', (16, 19, 23, 27, 34), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('TeeOff', (15, 18, 22, 26, 33), (70, 70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('CigarSmoke', (15, 18, 22, 26, 32), (80, 80, 80, 80, 80), (25, 25, 25, 25, 25)),
			 ('PickPocket', (18, 22, 26, 31, 36, (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'bf': {'name': SuitLocalizerGlobals.SuitBottomFeeder,
		'singularname': SuitLocalizerGlobals.SuitBottomFeederS,
		'pluralname': SuitLocalizerGlobals.SuitBottomFeederP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 1,
		'hp': (9, 15, 23, 33, 48),
		'attacks':
			(('RubberStamp', (3, 7, 11, 14, 17), (70, 70, 70, 75, 80), (25, 25, 25, 25, 25)),
			 ('Shred', (4, 9, 13, 17, 19), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Watercooler', (2, 6, 9, 11, 15), (90, 90, 90, 90, 90), (25, 25, 25, 25, 25)),
			 ('PickPocket', (4, 8, 12, 16, 18), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'b': {'name': SuitLocalizerGlobals.SuitBloodsucker,
	   'singularname': SuitLocalizerGlobals.SuitBloodsuckerS,
	   'pluralname': SuitLocalizerGlobals.SuitBloodsuckerP,
	   'class': SuitLocalizerGlobals.LawbotClass,
	   'tier': 2,
	   'hp': (15, 23, 33, 48, 61),
	   'attacks':
		   (('EvictionNotice', (4, 8, 12, 14, 17), (70, 70, 75, 75, 80), (25, 25, 25, 25, 25)),
			('RedTape', (4, 6, 8, 12, 18), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			('Withdrawal', (6, 12, 17, 19, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			('Liquidate', (3, 5, 9, 12, 16), (75, 75, 75, 80, 80), (25, 25, 25, 25, 25)))},
 'dt': {'name': SuitLocalizerGlobals.SuitDoubleTalker,
		'singularname': SuitLocalizerGlobals.SuitBloodsuckerS,
		'pluralname': SuitLocalizerGlobals.SuitBloodsuckerP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 3,
		'hp': (23, 33, 48, 61, 79),
		'attacks':
			(('RubberStamp', (7, 10, 15, 17, 19), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('BounceCheck', (5, 8, 13, 15, 17), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('BuzzWord', (6, 9, 14, 16, 18), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('DoubleTalk', (11, 14, 19, 21, 23), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Jargon', (7, 11, 16, 18, 20), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('MumboJumbo', (5, 9, 14, 16, 18), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)))},
 'ac': {'name': SuitLocalizerGlobals.SuitAmbulanceChaser,
		'singularname': SuitLocalizerGlobals.SuitAmbulanceChaserS,
		'pluralname': SuitLocalizerGlobals.SuitAmbulanceChaserP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 4,
		'hp': (33, 48, 61, 79, 100),
		'attacks':
			(('Shake', (9, 11, 16, 19, 21), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('RedTape', (11, 16, 19, 21, 24), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Rolodex', (7, 9, 13, 16, 19), (80, 80, 85, 85, 85), (25, 25, 25, 25, 25)),
			 ('HangUp', (6, 8, 12, 15, 18), (80, 80, 85, 85, 85), (25, 25, 25, 25, 25)))},
 'bs': {'name': SuitLocalizerGlobals.SuitBackStabber,
		'singularname': SuitLocalizerGlobals.SuitBackStabberS,
		'pluralname': SuitLocalizerGlobals.SuitBackStabberP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 5,
		'hp': (48, 61, 79, 100, 120),
		'attacks':
			(('GuiltTrap', (10, 12, 14, 18, 24), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('CigarSmoke', (11, 13, 15, 18, 25), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('RestrainingOrder', (8, 10, 12, 16, 22), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('FingerWag', (6, 8, 10, 14, 20), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)))},
 'sd': {'name': SuitLocalizerGlobals.SuitSpinDoctor,
		'singularname': SuitLocalizerGlobals.SuitSpinDoctorS,
		'pluralname': SuitLocalizerGlobals.SuitSpinDoctorP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 6,
		'hp': (61, 79, 100, 120, 145),
		'attacks':
			(('ParadigmShift', (12, 15, 18, 21, 26), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Spin', (14, 17, 20, 23, 28), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('Quake', (10, 13, 16, 19, 21), (80, 80, 80, 80, 85), (25, 25, 25, 25, 25)),
			 ('WriteOff', (9, 12, 15, 18, 20), (80, 80, 80, 85, 86), (25, 25, 25, 25, 25)),
			 ('ReOrg', (11, 14, 17, 20, 22), (70, 70, 70, 70, 75), (25, 25, 25, 25, 25)))},
 'le': {'name': SuitLocalizerGlobals.SuitLegalEagle,
		'singularname': SuitLocalizerGlobals.SuitLegalEagleS,
		'pluralname': SuitLocalizerGlobals.SuitLegalEagleP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 7, 
		'hp': (79, 100, 120, 145, 170),
		'attacks':
			(('EvilEye', (14, 18, 21, 24, 27), (70, 70, 75, 75, 80), (25, 25, 25, 25, 25)),
			 ('Jargon', (12, 16, 19, 22, 25), (70, 70, 75, 75, 75), (25, 25, 25, 25, 25)),
			 ('Legalese', (15, 19, 22, 25, 28), (70, 70, 70, 70, 70), (25, 25, 25, 25, 25)),
			 ('PeckingOrder' (16, 20, 23, 26, 29), (70, 70, 75, 75, 75), (25, 25, 25, 25)))},
 'bw': {'name': SuitLocalizerGlobals.SuitBigWig,
		'singularname': SuitLocalizerGlobals.SuitBigWigS,
		'pluralname': SuitLocalizerGlobals.SuitBigWigP,
		'class': SuitLocalizerGlobals.LawbotClass,
		'tier': 8,
		'hp': (100, 120, 145, 170, 220),
		'attacks':
			(('PowerTrip', (16, 20, 23, 26, 30), (70, 70, 75, 75, 80), (25, 25, 25, 25, 25)),
			 ('ThrowBook', (18, 22, 25, 28, 33), (70, 70, 75, 75, 80), (25, 25, 25, 25, 25)),
			 ('FingerWag', (16, 20, 23, 26, 30), (70, 70, 75, 75, 80), (25, 25, 25, 25, 25)))}}
			 
ATK_TGT_UNKNOWN = 1
ATK_TGT_SINGLE = 2
ATK_TGT_GROUP = 3
SuitAttacks = {'Audit': ('phone', ATK_TGT_SINGLE),
 'Bite': ('throw-paper', ATK_TGT_SINGLE),
 'BounceCheck': ('throw-paper', ATK_TGT_SINGLE),
 'BrainStorm': ('effort', ATK_TGT_SINGLE),
 'BuzzWord': ('speak', ATK_TGT_SINGLE),
 'Calculate': ('phone', ATK_TGT_SINGLE),
 'Canned': ('throw-paper', ATK_TGT_SINGLE),
 'Chomp': ('throw-paper', ATK_TGT_SINGLE),
 'CigarSmoke': ('cigar-smoke', ATK_TGT_SINGLE),
 'ClipOnTie': ('throw-paper', ATK_TGT_SINGLE),
 'Crunch': ('throw-object', ATK_TGT_SINGLE),
 'Demotion': ('magic1', ATK_TGT_SINGLE),
 'DoubleTalk': ('speak', ATK_TGT_SINGLE),
 'Downsize': ('magic2', ATK_TGT_SINGLE),
 'EvictionNotice': ('throw-paper', ATK_TGT_SINGLE),
 'EvilEye': ('glower', ATK_TGT_SINGLE),
 'Filibuster': ('speak', ATK_TGT_SINGLE),
 'FillWithLead': ('pencil-sharpener', ATK_TGT_SINGLE),
 'FingerWag': ('finger-wag', ATK_TGT_SINGLE),
 'Fired': ('magic2', ATK_TGT_SINGLE),
 'FiveOClockShadow': ('glower', ATK_TGT_SINGLE),
 'FloodTheMarket': ('glower', ATK_TGT_SINGLE),
 'FountainPen': ('pen-squirt', ATK_TGT_SINGLE),
 'FreezeAssets': ('glower', ATK_TGT_SINGLE),
 'Gavel': ('throw-object', ATK_TGT_SINGLE),
 'GlowerPower': ('glower', ATK_TGT_SINGLE),
 'GuiltTrip': ('magic1', ATK_TGT_GROUP),
 'HalfWindsor': ('throw-paper', ATK_TGT_SINGLE),
 'HangUp': ('phone', ATK_TGT_SINGLE),
 'HeadShrink': ('magic1', ATK_TGT_SINGLE),
 'HotAir': ('speak', ATK_TGT_SINGLE),
 'Jargon': ('speak', ATK_TGT_SINGLE),
 'Legalese': ('speak', ATK_TGT_SINGLE),
 'Liquidate': ('magic1', ATK_TGT_SINGLE),
 'MarketCrash': ('throw-paper', ATK_TGT_SINGLE),
 'MumboJumbo': ('speak', ATK_TGT_SINGLE),
 'ParadigmShift': ('magic2', ATK_TGT_GROUP),
 'PeckingOrder': ('throw-object', ATK_TGT_SINGLE),
 'PickPocket': ('pickpocket', ATK_TGT_SINGLE),
 'PinkSlip': ('throw-paper', ATK_TGT_SINGLE),
 'PlayHardball': ('throw-paper', ATK_TGT_SINGLE),
 'PoundKey': ('phone', ATK_TGT_SINGLE),
 'PowerTie': ('throw-paper', ATK_TGT_SINGLE),
 'PowerTrip': ('magic1', ATK_TGT_GROUP),
 'PositiveReinforcement': ('speak', ATK_TGT_SINGLE),
 'Quake': ('quick-jump', ATK_TGT_GROUP),
 'RazzleDazzle': ('smile', ATK_TGT_SINGLE),
 'RedTape': ('throw-object', ATK_TGT_SINGLE),
 'ReOrg': ('magic3', ATK_TGT_SINGLE),
 'RestrainingOrder': ('throw-paper', ATK_TGT_SINGLE),
 'Rolodex': ('roll-o-dex', ATK_TGT_SINGLE),
 'RubberStamp': ('rubber-stamp', ATK_TGT_SINGLE),
 'RubOut': ('hold-eraser', ATK_TGT_SINGLE),
 'Sacked': ('throw-paper', ATK_TGT_SINGLE),
 'SandTrap': ('golf-club-swing', ATK_TGT_SINGLE),
 'Schmooze': ('speak', ATK_TGT_SINGLE),
 'Shake': ('stomp', ATK_TGT_GROUP),
 'Shred': ('shredder', ATK_TGT_SINGLE),
 'SongAndDance': ('song-and-dance', ATK_TGT_SINGLE),
 'Spin': ('magic3', ATK_TGT_SINGLE),
 'Synergy': ('magic3', ATK_TGT_GROUP),
 'Tabulate': ('phone', ATK_TGT_SINGLE),
 'TeeOff': ('golf-club-swing', ATK_TGT_SINGLE),
 'ThrowBook': ('throw-object', ATK_TGT_SINGLE),
 'Tremor': ('stomp', ATK_TGT_GROUP),
 'Watercooler': ('watercooler', ATK_TGT_SINGLE),
 'Withdrawal': ('magic1', ATK_TGT_SINGLE),
 'WriteOff': ('hold-pencil', ATK_TGT_SINGLE)}
AUDIT = SuitAttacks.keys().index('Audit')
BITE = SuitAttacks.keys().index('Bite')
BOUNCE_CHECK = SuitAttacks.keys().index('BounceCheck')
BRAIN_STORM = SuitAttacks.keys().index('BrainStorm')
BUZZ_WORD = SuitAttacks.keys().index('BuzzWord')
CALCULATE = SuitAttacks.keys().index('Calculate')
CANNED = SuitAttacks.keys().index('Canned')
CHOMP = SuitAttacks.keys().index('Chomp')
CIGAR_SMOKE = SuitAttacks.keys().index('CigarSmoke')
CLIPON_TIE = SuitAttacks.keys().index('ClipOnTie')
CRUNCH = SuitAttacks.keys().index('Crunch')
DEMOTION = SuitAttacks.keys().index('Demotion')
DOWNSIZE = SuitAttacks.keys().index('Downsize')
DOUBLE_TALK = SuitAttacks.keys().index('DoubleTalk')
EVICTION_NOTICE = SuitAttacks.keys().index('EvictionNotice')
EVIL_EYE = SuitAttacks.keys().index('EvilEye')
FILIBUSTER = SuitAttacks.keys().index('Filibuster')
FILL_WITH_LEAD = SuitAttacks.keys().index('FillWithLead')
FINGER_WAG = SuitAttacks.keys().index('FingerWag')
FIRED = SuitAttacks.keys().index('Fired')
FIVE_O_CLOCK_SHADOW = SuitAttacks.keys().index('FiveOClockShadow')
FLOOD_THE_MARKET = SuitAttacks.keys().index('FloodTheMarket')
FOUNTAIN_PEN = SuitAttacks.keys().index('FountainPen')
FREEZE_ASSETS = SuitAttacks.keys().index('FreezeAssets')
GAVEL = SuitAttacks.keys().index('Gavel')
GLOWER_POWER = SuitAttacks.keys().index('GlowerPower')
GUILT_TRIP = SuitAttacks.keys().index('GuiltTrip')
HALF_WINDSOR = SuitAttacks.keys().index('HalfWindsor')
HANG_UP = SuitAttacks.keys().index('HangUp')
HEAD_SHRINK = SuitAttacks.keys().index('HeadShrink')
HOT_AIR = SuitAttacks.keys().index('HotAir')
JARGON = SuitAttacks.keys().index('Jargon')
LEGALESE = SuitAttacks.keys().index('Legalese')
LIQUIDATE = SuitAttacks.keys().index('Liquidate')
MARKET_CRASH = SuitAttacks.keys().index('MarketCrash')
MUMBO_JUMBO = SuitAttacks.keys().index('MumboJumbo')
PARADIGM_SHIFT = SuitAttacks.keys().index('ParadigmShift')
PECKING_ORDER = SuitAttacks.keys().index('PeckingOrder')
PICK_POCKET = SuitAttacks.keys().index('PickPocket')
PINK_SLIP = SuitAttacks.keys().index('PinkSlip')
PLAY_HARDBALL = SuitAttacks.keys().index('PlayHardball')
POUND_KEY = SuitAttacks.keys().index('PoundKey')
POWER_TIE = SuitAttacks.keys().index('PowerTie')
POWER_TRIP = SuitAttacks.keys().index('PowerTrip')
POSITIVE_REINFORCEMENT = SuitAttacks.keys().index('PositiveReinforcement')
QUAKE = SuitAttacks.keys().index('Quake')
RAZZLE_DAZZLE = SuitAttacks.keys().index('RazzleDazzle')
RED_TAPE = SuitAttacks.keys().index('RedTape')
RE_ORG = SuitAttacks.keys().index('ReOrg')
RESTRAINING_ORDER = SuitAttacks.keys().index('RestrainingOrder')
ROLODEX = SuitAttacks.keys().index('Rolodex')
RUBBER_STAMP = SuitAttacks.keys().index('RubberStamp')
RUB_OUT = SuitAttacks.keys().index('RubOut')
SACKED = SuitAttacks.keys().index('Sacked')
SANDTRAP = SuitAttacks.keys().index('SandTrap')
SCHMOOZE = SuitAttacks.keys().index('Schmooze')
SHAKE = SuitAttacks.keys().index('Shake')
SHRED = SuitAttacks.keys().index('Shred')
SONG_AND_DANCE = SuitAttacks.keys().index('SongAndDance')
SPIN = SuitAttacks.keys().index('Spin')
SYNERGY = SuitAttacks.keys().index('Synergy')
TABULATE = SuitAttacks.keys().index('Tabulate')
TEE_OFF = SuitAttacks.keys().index('TeeOff')
THROW_BOOK = SuitAttacks.keys().index('ThrowBook')
TREMOR = SuitAttacks.keys().index('Tremor')
WATERCOOLER = SuitAttacks.keys().index('Watercooler')
WITHDRAWAL = SuitAttacks.keys().index('Withdrawal')
WRITE_OFF = SuitAttacks.keys().index('WriteOff')			 
			 
			
			 
			
			  
