def validStartingCity(distances, fuel, mpg):
    startCity = 0


startCityMilesRemaining = 0

milesRemaining = 0

for i in range(1, len(distances)):
		fuelFromPrevCity = fuel[i-1]
		distanceFromPrevCity = distances[i-1]
		milesRemaining += fuelFromPrevCity*mpg - distanceFromPrevCity

		if milesRemaining < startCityMilesRemaining:
			startCityMilesRemaining = milesRemaining
			startCity = i

	return startCity
