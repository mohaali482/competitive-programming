class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = [0 if image[i][j] == 1 else 1 for j in range(len(image[0])-1, -1, -1)]
        
        return image