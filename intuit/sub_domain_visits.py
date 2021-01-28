class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = {}

        for domain in cpdomains:
            count, domainPortion = domain.split()
            count = int(count)

            if domainPortion not in domainCount:
                domainCount[domainPortion] = 0

            domainCount[domainPortion] += count

            for i in range(0, len(domainPortion)):
                if domainPortion[i] == ".":
                    addition = domainPortion[i+1:]
                    if addition not in domainCount:
                        domainCount[addition] = 0
                    domainCount[addition] += count

        result = []
        for key in domainCount:
            result.append(f'{domainCount[key]} {key}')

        return result
