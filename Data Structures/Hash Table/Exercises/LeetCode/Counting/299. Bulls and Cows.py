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


secret = "1807"
guess = "7810"

execute = Solution()
print(execute.getHint(secret, guess))
