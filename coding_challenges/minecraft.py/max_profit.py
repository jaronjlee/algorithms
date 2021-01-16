
#___________________________________________________________________________________________
# public static long calculateMaximumProfit(int cost_per_cut, int metal_price, int[] lengths) {

#     long maxProfit = 0;
#     long curProfit = 0;
#     int maxLength = 0;
#     int totalRods = 0;
#     int totalCuts = 0;
#     Arrays.sort(lengths);
#     // Find out maximum length
#     for (int curLength : lengths) {
#         maxLength = Math.max(maxLength, curLength);
#     }

#     // For each of the possible rod lengths, calculate possible profit
#     for (int curLength = 1; curLength <=maxLength; curLength++) {
#         int prevSum=0;
#         // Cut each of the rods into smaller rods of size curLength
#         // Count total rods and total cuts
#         for (int length : lengths) {
#             int cut = 0;
#             int waste = 0;
#             if(length%curLength==0){
#                 cut=(length/curLength)-1;
#             }else{
#                 cut=length/curLength;
#             }
#             waste=length%curLength;
#             int profit=Math.max(prevSum,prevSum+(length*metal_price-cut*cost_per_cut-waste*metal_price));
#             prevSum=profit;
#         }

#         curProfit=prevSum;
#         // Calculate maximum profit
#         maxProfit = Math.max(maxProfit, curProfit);
#     }

#     return maxProfit;
# }

'''
2. Cutting Metal Surplus

The owner of a construction company has a surplus of rods of arbitrary lengths. 
A local contractor offers to buy any of the surplus, as long as all the rods have the 
same exact integer length, referred to as saleLength. The number of sellable rods can 
be increased by cutting each rod zero or more times, but each cut has a cost denoted 
by costPerCut. After all cuts have been made, any leftover rods having a length other than 
saleLength must be discarded for no profit. The owner's total profit for the sale is 
calculated as:

totalProfit = totalUniformRods * saleLength * salePrice - totalCuts * costPerCut

where totalUniformRods is the number of sellable rods, salePrice is the per unit length
price that the contractor agrees to pay, and totalCuts is the total number of times the 
rod needs to be cut. 

Example:
lengths = [30, 59, 110]
costPerCut = 1
salePrice = 10 per unit length

output = 1913

testing length 30:
revenue = (10 * 5 * 30) - (4 * 1) = 1496
'''


def calculateMaximumProfit(costPerCut, metalPrice, lengths):
    maxProfit = 0
    maxLength = min(lengths)

    for currentLength in range(1, maxLength+1):
      tempSum = 0
      for rod in lengths:

        cuts = None
        if rod % currentLength == 0:
          cuts = (rod/currentLength) - 1
        else:
          cuts = rod // currentLength

        rods = rod // currentLength
        profit = (metalPrice * rods * currentLength) - (cuts * costPerCut)
        tempSum = max(tempSum, tempSum + profit)

      maxProfit = max(maxProfit, tempSum)

    return int(maxProfit)


print(calculateMaximumProfit(10, 10, [2, 3]))  # =>
print(calculateMaximumProfit(1, 10, [30, 59, 110]))  # => 1913
print(calculateMaximumProfit(1, 10, [26, 103, 59]))  # => 1170
