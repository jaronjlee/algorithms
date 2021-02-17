#home win = 1
#away win = 0

from collections import defaultdict


def tournamentWinner(competitions, results):
    scores = defaultdict(int)


maxScore = 0
winner = ""

for i in range(0, len(competitions)):
		home = competitions[i][0]
		away = competitions[i][1]
		result = results[i]

		if result == 1:
			scores[home] += 3
			if scores[home] > maxScore:
				maxScore = scores[home]
				winner = home
		else:
			scores[away] += 3
			if scores[away] > maxScore:
				maxScore = scores[away]
				winner = away

	return winner
