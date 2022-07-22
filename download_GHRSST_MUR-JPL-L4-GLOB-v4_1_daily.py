#####################################################
# download GHRSST, MUR-JPL-L4-GLOB-v4.1 daily
#####################################################
import os
import sys
import datetime as dt
from urllib.request import urlopen, urlretrieve
from pydap.client import open_url

start_date = dt.datetime.now()-dt.timedelta(days=2)
end_date = dt.datetime.now()-dt.timedelta(days=1)
print(start_date)
print(end_date)

# start_date = paste(Sys.Date()-2, "T12:00:00Z", sep='') # just one day
# end_date = paste(Sys.Date()-2, "T12:00:00Z", sep='') # today minus 2 days


def download_griddap(filename: str, datasetID: str, query: str=None):
    """
    """
    if query is None:
        url = os.path.join("https://upwell.pfeg.noaa.gov/erddap/griddap/", \
                            f"{datasetID}.nc")
    else:
        url = os.path.join("https://upwell.pfeg.noaa.gov/erddap/griddap/", \
                            f"{datasetID}.nc?{query}")
    
    filename = os.path.join('data', filename)
    
    outfile, _ = urlretrieve(url, filename)

    if os.path.exists(outfile):
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")
        sys.exit(1)
    
    


def main():
    print('Running program...')
    datasets = {
        'New Zealand': 'nasa_jpl_dde5_3be1_897b',
        'California': 'nasa_jpl_dde5_3be1_897b',
    }

    # queries = {
    #     'New Zealand': f'analysed_sst%5B({2022-07-20T09:00:00Z})%5D%5B(-89.99):(89.99)%5D%5B(-179.99):(180.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=%7C%7C%7C%7C%7C&.bgColor=0xffccccff'
    #     'California': 'analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(30.0):(45.0)%5D%5B(-130.0):(-115.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff'
    # }

    files = {
        'New Zealand': 'MUR_SST_New_Zealand.nc',
        'California': 'MUR_SST_California.nc',
    }


    print('Done.')

    for region, datasetID in datasets.items():
        print()
        download_griddap(files[region], datasetID, None)
        print()        

if __name__ == '__main__':
    from pathlib import Path
    print('\nProgram: ', Path(__file__).name)
    main()
    print('Program complete.\n')
    