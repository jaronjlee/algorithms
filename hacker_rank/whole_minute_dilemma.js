// #get mod of every num
// #create counter hash for each 


function playlist(songs) {
    songs = songs.map(time => time % 60)
    const counter = {}
    let pairs = 0

    songs.forEach(song => {
        const diff = (60 - song) % 60
        if (counter[diff]) pairs += counter[diff]
        if (!counter[song]){
            counter[song] = 0
        }
        counter[song]++
    })

    return pairs
}