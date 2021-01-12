class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = {}
        result = []

        for cpDomain in cpdomains:
            # split = cpDomain.split(" ")
            # count = int(split[0])
            # domain = split[1]

            spaceIdx = cpDomain.find(" ")
            count = int(cpDomain[0:spaceIdx])
            domain = cpDomain[spaceIdx+1:]

            for i in reversed(range(0, len(domain))):
                if domain[i] == '.':
                    subString = domain[i+1:len(domain)]
                    if subString in domainCount:
                        domainCount[subString] += count
                    else:
                        domainCount[subString] = count
                elif i == 0:
                    subString = domain[i:len(domain)]
                    if subString in domainCount:
                        domainCount[subString] += count
                    else:
                        domainCount[subString] = count

        # for domain in domainCount:
        #     result.append(f'{domainCount[domain]} {domain}')
        # return result

        return ['{} {}'.format(v, k) for k, v in domainCount.items()]

        # for k,v in domainCount.items():
        #     result.append(f'{v} {k}')
        # return result
