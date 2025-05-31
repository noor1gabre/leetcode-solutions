class Solution(object):
    def minLength(self, s):
        s1 = s
        sub = 'AB'
        sub2 = 'CD'
        new_s2 = ''
        c = 0
        for i in range(len(s)):
            if sub in s or sub2 in s:
                new_s = s.replace(sub, '')
                new_s2 = new_s.replace(sub2, '')
                s = new_s2
                c += 1
        if(c != 0):
            return(len(s))
        else:
            return(len(s1))

            
