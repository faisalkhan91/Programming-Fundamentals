"""
299. Bulls and Cows
https://leetcode.com/problems/bulls-and-cows/?envType=study-plan&envId=level-1&plan=leetcode-75

Bulls and Cows game:
https://en.wikipedia.org/wiki/Bulls_and_Cows
"""


class Solution:
    def remove_value(self, value, hash_map):
        print(value, hash_map)
        for k, v in hash_map.items():
            if value == v:
                return k

    def getHint(self, secret: str, guess: str) -> str:
        """
        This is the initial attempt using hash table. This solution partially works but using remove_value function to
        remove false positives for cows ends up not working for an input like; secret:"1122", guess:"1222".
        :param secret:
        :param guess:
        :return:
        """

        secret_hash = {}
        bulls = 0
        cows = 0

        for digit in range(len(secret)):
            secret_hash[digit] = secret[digit]

        for digit in range(len(secret)):
            if guess[digit] == secret[digit]:
                bulls += 1
                secret_hash.pop(self.remove_value(guess[digit], secret_hash))

            elif guess[digit] in secret_hash.values():
                cows += 1
                secret_hash.pop(self.remove_value(guess[digit], secret_hash))

        return str(bulls) + "A" + str(cows) + "B"

    def getHint2(self, secret: str, guess: str) -> str:
        """
        In this solution we make use of 2 hash maps to store the frequency of the digits that are visited for the cows
        case scenario. If the digit in secret is in the guess map we know that the digit is a cow, and we subtract the
        frequency of the digit, else we add the secret digit to the secret map with frequency 1. Similarly, for the
        digit in guess, we check if the digit is in secret map, if so we subtract the frequency, else we add the digit
        to guess map.
        :param secret:
        :param guess:
        :return:
        """
        secret_map = {}
        guess_map = {}

        bulls = 0
        cows = 0

        for digit in range(len(secret)):
            if guess[digit] == secret[digit]:
                bulls += 1
            else:
                if secret[digit] in guess_map and guess_map[secret[digit]] > 0:
                    cows += 1
                    guess_map[secret[digit]] -= 1
                else:
                    # Here, get is used to get the value or if not present send 0.
                    secret_map[secret[digit]] = secret_map.get(secret[digit], 0) + 1
                if guess[digit] in secret_map and secret_map[guess[digit]] > 0:
                    cows += 1
                    secret_map[guess[digit]] -= 1
                else:
                    guess_map[guess[digit]] = guess_map.get(guess[digit], 0) + 1
        return str(bulls) + "A" + str(cows) + "B"


secret = "1807"
guess = "7810"

execute = Solution()
print(execute.getHint2(secret, guess))
