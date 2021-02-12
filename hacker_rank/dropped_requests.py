


hash = {
    1: {"ones":1, "tens":1, "mins":1},
    2: {"ones":1, "tens":1, "mins":1},
    3: {"ones":1, "tens":1, "mins":1},
    4: {"ones":1, "tens":1, "mins":1},
    5: {"ones":1, "tens":1, "mins":1},
    6: {"ones":1, "tens":1, "mins":1},
    7: {"ones":1, "tens":1, "mins":1},
    11: {"ones":1, "tens":1, "mins":1},
    
}

#create unique set of times
#create hash
#iterate through request times
#at eeach i, create key/value in hash if not there
    #ones += 1
#then nested loop j from 0 to 60
#newRequestTime = i + j
#if newRequestTime not in unique set of times, continue
#if newRequestTime not in hash, add key/value to hash
#if j < 10, hash[newRT]["tens"] += 1
#hash[newRT]["mins"] += 1
#if hash[reqTime]["ones"] > 3 || ["tens"] > 20 || "mins" > 60:
    #dropRequests += 1

def droppedRequests(requestTimes):
    uniqueSetOfTimes = set(requestTimes)
    freqs = {}
    droppedRequests = 0

    for i in range(0, len(requestTimes)):
        reqTime = requestTimes[i]
        if reqTime not in freqs:
            freqs[reqTime] = {"ones":0, "tens":0, "mins":0}
        freqs[reqTime]["ones"] += 1

        for j in range(0, 60):
            newRT = reqTime + j
            if newRT not in uniqueSetOfTimes:
                continue
            if newRT not in freqs:
                freqs[newRT] = {"ones": 0, "tens": 0, "mins": 0}
            if j < 10:
                freqs[newRT]["tens"] += 1
            freqs[newRT]["mins"] += 1
        if freqs[reqTime]["ones"] > 3 or freqs[reqTime]["tens"] > 20 or freqs[reqTime]["mins"] > 60:
            droppedRequests += 1

    return droppedRequests