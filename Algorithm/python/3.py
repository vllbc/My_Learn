class Solution:
    def wordPattern(pattern: str, s: str) -> bool:
        sts = s.split()
        pars = list(pattern)
        dicts = {}
        if len(sts) != len(pars):
            return False
        for k,v in zip(pars,sts):
            dicts[k] = v
        if len(dicts.keys()) != len(set(sts)):
            return False
        for k,v in zip(pars,sts):
            if dicts[k] != v:
                return False
        return True