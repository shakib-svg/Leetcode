import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""  # Correction: Renvoie une chaîne vide au lieu d'un espace
        
        gcd_length = math.gcd(len(str1), len(str2))
        return str1[:gcd_length]  # Correction: Indentation correcte

# Création d'une instance de Solution
solution = Solution()
print(solution.gcdOfStrings("ABCABC","ABC"))
# Test de la fonction
print(solution.gcdOfStrings("ABCABCABC", "ABC"))  # Résultat attendu : "ABC"
