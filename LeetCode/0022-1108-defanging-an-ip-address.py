# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_addr = ""
        for ch in address:
            if ch == ".":
                ip_addr += "[.]"
            else:
                ip_addr += ch
        return ip_addr