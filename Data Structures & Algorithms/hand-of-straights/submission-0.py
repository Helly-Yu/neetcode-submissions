class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False

        counts = Counter(hand)
        sorted_cards = sorted(counts.keys())
        print(counts)
        for card in sorted_cards:
            if counts[card]>0:
                num_needed = counts[card] # We need 'num_needed' groups starting with this card
                # Check if the next consecutive cards are available
                for i in range(card, card+groupSize):
                    print(counts[i])
                    if counts[i] < num_needed:
                        return False
                    counts[i]-=num_needed
        
        return True
                