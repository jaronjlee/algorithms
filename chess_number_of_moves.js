Function minMoves(n , startRow, startCol, endRow, endCol) {
	Let seenPos = new Set()
	seenPos.add(`${startRow}-${startCol}`)
	Let queue = [[startRow,startCol]]
possibleDirections = [[2, 1],[2, -1],[-2, 1],[-2, -1],[1, 2],[-1, 2],[1, -2],[-1, -2]]
	Let count = 0 //1

	while(queue.length){   //8 new pos in our queue 
		Let len = queue.len
		for(let i =0 ; i < len;i++){
			Let pos = queue.shift()
			for(let dir of possibleDirections){
				Let newX = pos[0]+dir[0]
Let newY = pos[1]+dir[1]
if(checkIfValid(n, newX,newY) && !seenPos.has(`${newX}-${newY}`) ){
if(endCol === newX && endRow === newY)return count+1
queue.push([newX,newY])
seenPos.add(`${newX}-${newY}`)
}
				
}
}
count++
}
Return-1
}
