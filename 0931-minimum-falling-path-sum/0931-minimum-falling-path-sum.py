storedTerms = {}


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        storedTerms.clear()

        minSum = recMinFall(0, 0, matrix)

        for i in range(len(matrix) - 1):
            newSum = recMinFall(0, i + 1, matrix)
            if minSum > newSum:
                minSum = newSum
        return minSum


def recMinFall(rowNumber, columnNumber, matrix):
    if (rowNumber, columnNumber) in storedTerms:
        return storedTerms[(rowNumber, columnNumber)]

    # this means the function has reached the bottom ::BASE CASE::
    if rowNumber == len(matrix) - 1:
        storedTerms[(rowNumber, columnNumber)] = matrix[rowNumber][columnNumber]
        return storedTerms[(rowNumber, columnNumber)]
    else:
        # print(rowNumber)
        smallestSum = recMinFall(rowNumber + 1, columnNumber, matrix)
        newSum = 0
        if not columnNumber == 0:
            newSum = recMinFall(rowNumber + 1, columnNumber - 1, matrix)
            if newSum < smallestSum:
                smallestSum = newSum

        if not columnNumber == len(matrix[0]) - 1:
            newSum = recMinFall(rowNumber + 1, columnNumber + 1, matrix)
            if newSum < smallestSum:
                smallestSum = newSum

        storedTerms[(rowNumber, columnNumber)] = (
            matrix[rowNumber][columnNumber] + smallestSum
        )
    return storedTerms[(rowNumber, columnNumber)]
