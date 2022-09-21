infile= open('info_security.txt','r')
read_file= infile.read()

encryption= open('encrypted.txt','w')

Enc={'A':'@','B':'#','C':'!','D':':','E':']','F':';','G':'$','H':'%','I':'^','J':'<',
'K':'>','L':'/','M':'&','N':'*','O':'-','P':'_','Q':'=','R':'+','S':',','T':'|','U':'.',
'V':'1','W':'2','X':'3','Y':'4','Z':'5','a':'6','b':'7','c':'8','d':'9','e':'`','f':'~','g':'l',
'h':'q','i':'e','j':'u','k':'m','l':'z','m':'g','n':'0','o':'P','p':'x','q':'b','r':'B','s':'F','t':'T','u':'W',
'v':'r','w':'c','x':'Y','y':'O','z':'H'}

for item in read_file:
    if item in Enc:
        encryption.write(Enc[item])

    else:
        encryption.write(item)

infile.close()
encryption.close()