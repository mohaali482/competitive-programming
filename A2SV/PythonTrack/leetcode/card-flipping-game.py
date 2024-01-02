class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid_cards = set()
        cards = set(fronts+backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid_cards.add(fronts[i])
        valid_cards = cards-invalid_cards
        card = [i for i in valid_cards]
        return min(card) if card else 0