from os import access
import pandas as pd

db = pd.read_csv("final.csv")

del db['hyperlink']
del db['temp_planet_date']
del db['temp_planet_mass']
del db['pl_letter']
del db['pl_name']
del db['pl_controvflag']
del db['pl_pnum']
del db['pl_orbper']
del db['pl_orbpererr1']
del db['pl_orbpererr2'] 
del db['pl_orbperlim'] 
del db['pl_orbsmax']
del db['pl_orbsmaxerr1']
del db['pl_orbsmaxerr2'] 
del db['pl_orbsmaxlim'] 
del db['pl_orbeccen']
del db['pl_orbeccenerr1']
del db['pl_orbeccenerr2'] 
del db['pl_orbeccenlim'] 
del db['pl_orbincl']
del db['pl_orbinclerr1']
del db['pl_orbinclerr2'] 
del db['pl_orbincllim'] 
del db['pl_bmassj'] 
del db['pl_bmassjerr1']
del db['pl_bmassjerr2'] 
del db['pl_bmassjlim'] 
del db['pl_bmassprov']
del db['pl_radj']
del db['pl_radjerr1']
del db['pl_radjerr2']
del db['pl_radjlim']
del db['pl_denserr1']
del db['pl_denserr2']
del db['pl_denslim']
del db['pl_ttvflag']
del db['pl_kepflag']
del db['pl_k2flag']
del db['pl_nnotes']
del db['ra_str']
del db['ra']
del db["dec"] 
del db["st_dist"] 
del db["st_disterr1"] 
del db["st_disterr2"] 
del db["st_distlim"] 
del db["gaia_dist"] 
del db["gaia_disterr1"] 
del db["gaia_disterr2"] 
del db["gaia_distlim"] 
del db["st_optmag"] 
del db["st_optmagerr"] 
del db["st_optmaglim"] 
del db["st_optband"] 
del db["gaia_gmag"] 
del db["gaia_gmagerr"] 
del db["gaia_gmaglim"] 
del db["st_tefferr1"] 
del db["st_tefferr2"] 
del db["st_tefflim"] 
del db["st_masserr1"] 
del db["st_masserr2"] 
del db["st_masslim"] 
del db["st_raderr1"] 
del db["st_raderr2"] 
del db["st_radlim"] 
del db["rowupdate"] 
del db["pl_facility"]

db = db.rename({
    'pl_hostname':'solar_system_name',
    'pl_discmethod':'planet_discovery_method',
    'pl_dens':'planet_density',
    'dec_str':'declination_star',
    'st_teff':'host_temperature',
    'st_mass':'host_mass',
    'st_rad':'host_radius',
},axis = 'columns')

print(db.columns)
print(db.shape)
db.to_csv('tidy_final.csv')