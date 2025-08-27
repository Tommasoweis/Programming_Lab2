class ExamException:
    pass
class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
        try:
            with open (self.name,'r') as file:
                pass
        except FileNotFoundError:
            print('File non trovato')
        except FileExistsError:
            print('Errore con il file')
    def get_data(self):
        dati=[]
        with open (self.name,'r') as file:
            for line in file:
                element=line.strip().split(',')
                try:
                    if(float(element[1])<0 ):
                        pass
                    else:
                        dati.append([element[0],float(element[1])])
                except:
                    pass
        return dati

def compute_variations2(time_series,first_year,last_year,N):
    if(N>(last_year-first_year)):
        raise ExamException
    data={}
    for line in time_series:
        year=int(line[0].split('/')[0])
        if year not in data:
            data[year]=[]
            data[year].append(line[1])
        else:
            data[year].append(line[1])
    media={}
    variazione={}
    min_year=min(data.keys())
    for year in data:
        media[year]=[]
        media[year].append(sum(data[year])/len(data[year]))
        if year> min_year+N:
            variazione[year]=[]
            somma=0
            for i in range(1,N+1):
                somma+=media[year-i][0]
            variazione[year].append(media[year][0]-(somma/N))
    dict={} 
    for year in variazione:
        if year>=first_year and year<=last_year:
            dict[year]=[]
            dict[year].append(variazione[year][0])
    return dict            


    










percorso = r'C:\Users\tomma\Downloads\GlobalTemperatures.csv'
time_series_file=CSVTimeSeriesFile(name=percorso)
time_series=time_series_file.get_data()

d=compute_variations2(time_series,1931,1999,12)
print(d)