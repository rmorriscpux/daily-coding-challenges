'''
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
'''

from typing import List

def generateIPs(digits):
    def rGenerateIPs(remaining_digits: str, built_ips: List[str], sub_addrs: List[str]):
        digit_len = len(remaining_digits)
        
        if len(sub_addrs) == 4:
            if digit_len == 0:
                built_ips.append('.'.join(sub_addrs))
            return

        if digit_len >= 1:
            rGenerateIPs(remaining_digits[1:], built_ips, sub_addrs + [remaining_digits[:1]])

        if digit_len >= 2 and remaining_digits[0] != '0':
            rGenerateIPs(remaining_digits[2:], built_ips, sub_addrs + [remaining_digits[:2]])

        if digit_len >= 3 and remaining_digits[0] != '0' and int(remaining_digits[:3]) <= 255:
            rGenerateIPs(remaining_digits[3:], built_ips, sub_addrs + [remaining_digits[:3]])

        return

    # digit_string must be all numerals, and between 4 and 12 characters.
    digit_string = str(digits)
    assert len(digit_string) >= 4 and len(digit_string) <= 12 and all(map(lambda c: c in "0123456789", digit_string))

    built_ips = []
    rGenerateIPs(digit_string, built_ips, [])
    return built_ips

print(generateIPs('2542540123'))