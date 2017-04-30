import pandas as pd
import urllib

ohio_url_list = ['ftp://sosftp.sos.state.oh.us/free/Voter/ADAMS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ALLEN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ASHLAND.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ASHTABULA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ATHENS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/AUGLAIZE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/BELMONT.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/BROWN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/BUTLER.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CARROLL.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CHAMPAIGN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CLARK.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CLERMONT.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CLINTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/COLUMBIANA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/COSHOCTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CRAWFORD.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/CUYAHOGA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/DARKE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/DEFIANCE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/DELAWARE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ERIE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/FAIRFIELD.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/FAYETTE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/FRANKLIN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/FULTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/GALLIA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/GEAUGA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/GREENE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/GUERNSEY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HAMILTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HANCOCK.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HARDIN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HARRISON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HENRY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HIGHLAND.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HOCKING.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HOLMES.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/HURON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/JACKSON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/JEFFERSON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/KNOX.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LAKE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LAWRENCE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LICKING.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LOGAN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LORAIN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/LUCAS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MADISON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MAHONING.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MARION.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MEDINA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MEIGS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MERCER.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MIAMI.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MONROE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MONTGOMERY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MORGAN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MORROW.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/MUSKINGUM.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/NOBLE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/OTTAWA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PAULDING.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PERRY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PICKAWAY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PIKE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PORTAGE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PREBLE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/PUTNAM.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/RICHLAND.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/ROSS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/SANDUSKY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/SCIOTO.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/SENECA.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/SHELBY.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/STARK.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/SUMMIT.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/TRUMBULL.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/TUSCARAWAS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/UNION.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/VANWERT.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/VINTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WARREN.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WASHINGTON.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WAYNE.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WILLIAMS.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WOOD.zip',
'ftp://sosftp.sos.state.oh.us/free/Voter/WYANDOT.zip']

r = urllib.urlopen('ftp://sosftp.sos.state.oh.us/free/Voter/ADAMS.zip')
df = pd.read_csv(io.BytesIO(r.read()), compression='zip', sep=',', header=0)

for ftp in ohio_url_list:
    current = pd.read_csv(ftp, compression='infer', header=0, sep=',',error_bad_lines=False)
    import pdb; pdb.set_trace()
