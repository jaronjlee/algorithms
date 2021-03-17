def classPhotos(redShirtHeights, blueShirtHeights):
    backRow = None


frontRow = None

redShirtHeights.sort()
blueShirtHeights.sort()

if redShirtHeights[-1] > blueShirtHeights[-1]:
		backRow = redShirtHeights
		frontRow = blueShirtHeights
	else:
		frontRow = redShirtHeights
		backRow = blueShirtHeights

	for i in range(0, len(backRow)):
		if backRow[i] <= frontRow[i]:
			return False

	return True
