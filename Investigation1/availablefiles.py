# Initial version of availablefiles.py
# Simply outputs a list of available readings for the house

def av_files():
    files = ['Cumulative.csv',
             'Morning.csv',
             'Midday.csv',
             'Nightly.csv', ]
    print('The current recorded energy usages are: ' + str(files))
av_files()

