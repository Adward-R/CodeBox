__author__ = 'Adward'
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        spath = []
        for dir in path.split('/'):
            if len(dir) > 0:
                if dir == '..':
                    try:
                        spath.pop()
                    except:
                        pass
                elif dir == '.':
                    pass
                else:
                    spath.append(dir)
        if len(spath):
            res = ''
            for dir in spath:
                res += '/' + dir
            return res
        else:
            return '/'

sol = Solution()
print(sol.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))