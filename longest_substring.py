

class Substring():

    def longest_substring(self, s):
        max = 0
        s_list = list(s) 
        temp = list()
        m_s = ''
        for c in s_list:
            if c not in temp:
                temp.append(c)    
                if max < len(temp):
                    max = len(temp)
                    m_s = ''.join(temp)
            else:
                temp = list(''.join(temp).split(c)[1])
                temp.append(c)
        print('Size:',max, '\nString:',m_s)
                
Substring().longest_substring('abcdjaabcdefghijjxxxqwertyuioplkjhgfdsazxcvbnm')