class Straight():
    'A class that defines the possible sequences for a straight'

    def __init__(self):
        self.sequences = []
        self.__generateSequences()
        pass

    def __generateSequences(self):
        """Creates all valid sequences for a straight"""
        seq = []

        # Generate non-numeric sequences first
        straight = ['A', 'K', 'Q', 'J', '10']
        seq.append(straight)

        straight = ['K', 'Q', 'J', '10', '9']
        seq.append(straight)

        straight = ['Q', 'J', '10', '9', '8']
        seq.append(straight)

        straight = ['J', '10', '9', '8', '7']
        seq.append(straight)

        startingValue = 10
        while startingValue > 5:
            temp = []
            for i in range(5):
                decrement = startingValue - i
                temp.append(str(decrement))
                decrement -= 1
            seq.append(temp)

            startingValue -= 1

        self.sequences = seq

