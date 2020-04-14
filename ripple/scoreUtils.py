from common.constants import gameModes, mods
from objects import glob

def isRankable(m):
	"""
	Checks if `m` contains unranked mods
	:param m: mods enum
	:return: True if there are no unranked mods in `m`, else False
	"""
	# TODO: Check other modes unranked mods ...?
	return not ((m & mods.RELAX2 > 0) or (m & mods.AUTOPLAY > 0))

def readableGameMode(gameMode):
	"""
	Convert numeric gameMode to a readable format. Can be used for db too.

	:param gameMode:
	:return:
	"""
	# TODO: Same as common.constants.gameModes.getGameModeForDB, remove one
	if gameMode == 0:
		return "std"
	elif gameMode == 1:
		return "taiko"
	elif gameMode == 2:
		return "ctb"
	else:
		return "mania"

def readableMods(m):
	"""
	Return a string with readable std mods.
	Used to convert a mods number for oppai

	:param m: mods bitwise number
	:return: readable mods string, eg HDDT
	"""
	r = ""
	if m == 0:
		return "nomod"
	if m & mods.NOFAIL > 0:
		r += "NF"
	if m & mods.EASY > 0:
		r += "EZ"
	if m & mods.HIDDEN > 0:
		r += "HD"
	if m & mods.HARDROCK > 0:
		r += "HR"
	if m & mods.DOUBLETIME > 0:
		r += "DT"
	if m & mods.HALFTIME > 0:
		r += "HT"
	if m & mods.FLASHLIGHT > 0:
		r += "FL"
	if m & mods.SPUNOUT > 0:
		r += "SO"
	if m & mods.TOUCHSCREEN > 0:
		r += "TD"
	if m & mods.RELAX > 0:
		r += "RX"
	return r

def updateRankCounter(rank, gameMode, userID):
	"""
	This updates the users rank counter.
	So I don't have to struggle doing the work of counting in golang :nausated_face:
	"""
	if rank == "F":
		return False
	if rank == "F":
		return False
	elif rank == "D":
		return False
	elif rank == "C":
		return False
	elif rank == "B":
		return False
	else:
		modeForDB = gameModes.getGameModeForDB(gameMode)
		glob.db.execute("""
			UPDATE users_rank SET {rank}_{gameMode}={rank}_{gameMode}+1 WHERE userid = %s LIMIT 1""".format(rank=rank, gameMode=modeForDB), [userID])

def updateRankCounterRX(rank, gameMode, userID):
	"""
	This updates the users rank counter.
	So I don't have to struggle doing the work of counting in golang :nausated_face:
	"""
	modeForDB = gameModes.getGameModeForDB(gameMode)

	if rank == "F":
		return False
	elif rank == "D":
		return False
	elif rank == "C":
		return False
	elif rank == "B":
		return False
	else:
		glob.db.execute("""
			UPDATE rx_rank SET {rank}_{gameMode}={rank}_{gameMode}+1 WHERE userid = %s LIMIT 1""".format(rank=rank, gameMode=modeForDB), [userID])
