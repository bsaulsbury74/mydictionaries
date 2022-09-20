outfile= open('sometext.txt','r')

Dict={}

for report in outfile:

    report= report.lower()
    report= report.replace(',','')
    report= report.replace('.','')

    sec= report.split(' ')

    for record in sec:
        if record in Dict:
            Dict[record]= Dict[record]+1


        else:
            Dict[record]=1

for key in list(Dict.keys()):
    print(key, ':', Dict[key])
#print(Dict)

outfile.close()
