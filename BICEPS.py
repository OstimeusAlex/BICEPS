from os import system
from os import name
from os import path
from configparser import ConfigParser
from pathlib import Path as Pth
from shutil import copyfile
from helptext import helpTooltipText as hT
from convert_sra import convert_sra
import PySimpleGUI as sg

#Values
lndsrafle = ''
tposrafle = ''
sra_path = ''
lnd_path = ''
tpo_path = ''

#Toggle Functions
def rstrtfletoggle():  #Restart File
    if values['-TOG_RSTRT_FLE-'] == True:
        window['-PHY_RSTRT_FLE-'].Widget.configure(state='normal')
        window['-RSTRT_FLE_OPN-'].Widget.configure(state='normal')
    else:
        window['-PHY_RSTRT_FLE-'].Widget.configure(state='disabled')
        window['-RSTRT_FLE_OPN-'].Widget.configure(state='disabled')
def stmtoggle():       #Storm
    if values['-TOG_STRM_CLIM-'] == True: window['-TOG_HGH_CDNCE-'].Widget.configure(state='normal')
    else: window['-TOG_HGH_CDNCE-'].Widget.configure(state='disabled')
def hghcdncetoggle():  #High Cadence
    if values['-TOG_HGH_CDNCE-'] == True:
        window['-HGH_CDNCE_STRT-'].Widget.configure(state='normal')
        window['-HGH_CDNCE_END-'].Widget.configure(state='normal')
        window['-HGH_CDNCE_INTRVL-'].Widget.configure(state='normal')
        window['-TOG_STM_CPTRE-'].Widget.configure(state='normal')
    else:
        window['-HGH_CDNCE_STRT-'].Widget.configure(state='disabled')
        window['-HGH_CDNCE_END-'].Widget.configure(state='disabled')
        window['-HGH_CDNCE_INTRVL-'].Widget.configure(state='disabled')
        window['-TOG_STM_CPTRE-'].Widget.configure(state='disabled')
def stmcptretoggle():  #Storm Capture
    if values['-TOG_STM_CPTRE-'] == True:
        window['-TOG_HRCNE-'].Widget.configure(state='normal')
        window['-STM_MIN_TEMP-'].Widget.configure(state='normal')
        window['-STM_MAX_TEMP-'].Widget.configure(state='normal')
        window['-STM_MIN_WIND-'].Widget.configure(state='normal')
        window['-STM_MIN_CLCT-'].Widget.configure(state='normal')
        window['-STM_FIN_CLCT-'].Widget.configure(state='normal')
        window['-STM_GPI-'].Widget.configure(state='normal')
        window['-STM_MPI-'].Widget.configure(state='normal')
        window['-STM_LATM_MAX_WIND-'].Widget.configure(state='normal')
        window['-STM_VNT_IDX-'].Widget.configure(state='normal')
        window['-STM_MIN_TMESTPS-'].Widget.configure(state='normal')
        window['-STM_MAX_TMESTPS-'].Widget.configure(state='normal')
        window['-STM_VRMI-'].Widget.configure(state='normal')
        window['-STM_LAV-'].Widget.configure(state='normal')
    else:
        window['-TOG_HRCNE-'].Widget.configure(state='disabled')
        window['-STM_MIN_TEMP-'].Widget.configure(state='disabled')
        window['-STM_MAX_TEMP-'].Widget.configure(state='disabled')
        window['-STM_MIN_WIND-'].Widget.configure(state='disabled')
        window['-STM_MIN_CLCT-'].Widget.configure(state='disabled')
        window['-STM_FIN_CLCT-'].Widget.configure(state='disabled')
        window['-STM_GPI-'].Widget.configure(state='disabled')
        window['-STM_MPI-'].Widget.configure(state='disabled')
        window['-STM_LATM_MAX_WIND-'].Widget.configure(state='disabled')
        window['-STM_VNT_IDX-'].Widget.configure(state='disabled')
        window['-STM_MIN_TMESTPS-'].Widget.configure(state='disabled')
        window['-STM_MAX_TMESTPS-'].Widget.configure(state='disabled')
        window['-STM_VRMI-'].Widget.configure(state='disabled')
        window['-STM_LAV-'].Widget.configure(state='disabled')
def baltoggle ():      #Run To Balance
    if values['-TOG_RUN_TO_BLNCE-'] == True:
        window['-PHY_RUNTME-'].Widget.configure(state='disabled')
        window['-PHY_THRSHLD-'].Widget.configure(state='normal')
        window['-PHY_BSELNE-'].Widget.configure(state='normal')
        window['-PHY_MAX_YR-'].Widget.configure(state='normal')
        window['-PHY_MIN_YR-'].Widget.configure(state='normal')
    else:
        window['-PHY_RUNTME-'].Widget.configure(state='normal')
        window['-PHY_THRSHLD-'].Widget.configure(state='disabled')
        window['-PHY_BSELNE-'].Widget.configure(state='disabled')
        window['-PHY_MAX_YR-'].Widget.configure(state='disabled')
        window['-PHY_MIN_YR-'].Widget.configure(state='disabled')
def keplertoggle():    #Keplerian Orbit
    if values['-TOG_KPLR_OBT-'] == True: window['-OBT_MNANMLY-'].Widget.configure(state='normal')
    else: window['-OBT_MNANMLY-'].Widget.configure(state='disabled')
def tidaltoggle():     #Tidally Locked
    if values['-TOG_TDL_LCK-'] == True:
        window['-PLNT_SUB_LONG-'].Widget.configure(state='normal')
        window['-PLNT_SUB_DSNC-'].Widget.configure(state='normal')
        window['-PLNT_TMP_CNST-'].Widget.configure(state='normal')
    else:
        window['-PLNT_SUB_LONG-'].Widget.configure(state='disabled')
        window['-PLNT_SUB_DSNC-'].Widget.configure(state='disabled')
        window['-PLNT_TMP_CNST-'].Widget.configure(state='disabled')
def pressuretoggle():  #Pressure
    if values['-TOG_BLK_PR-'] == True: window['-BLK_PR-'].Widget.configure(state='normal')
    else: window['-BLK_PR-'].Widget.configure(state='disabled')
def gascontoggle():    #Gas Constant
    if values['-TOG_GAS_CNST-'] == True: window['-GAS_CNST-'].Widget.configure(state='normal')
    else: window['-GAS_CNST-'].Widget.configure(state='disabled')
def ptoggle():         #Gas Pressure
    if values['-TOG_GAS_PR-'] == True:
        window['-ATM_H2-'].Widget.configure(state='normal')
        window['-ATM_HE-'].Widget.configure(state='normal')
        window['-ATM_N2-'].Widget.configure(state='normal')
        window['-ATM_O2-'].Widget.configure(state='normal')
        window['-ATM_AR-'].Widget.configure(state='normal')
        window['-ATM_NE-'].Widget.configure(state='normal')
        window['-ATM_KR-'].Widget.configure(state='normal')
        window['-ATM_H2O-'].Widget.configure(state='normal')
        window['-ATM_CO2-'].Widget.configure(state='normal')
    else:
        window['-ATM_H2-'].Widget.configure(state='disabled')
        window['-ATM_HE-'].Widget.configure(state='disabled')
        window['-ATM_N2-'].Widget.configure(state='disabled')
        window['-ATM_O2-'].Widget.configure(state='disabled')
        window['-ATM_AR-'].Widget.configure(state='disabled')
        window['-ATM_NE-'].Widget.configure(state='disabled')
        window['-ATM_KR-'].Widget.configure(state='disabled')
        window['-ATM_H2O-'].Widget.configure(state='disabled')
        window['-ATM_CO2-'].Widget.configure(state='disabled')
def aquatoggle():      #Aqua Planet
    if values['-TOG_PLT_AQA-'] == True:
        window['-TOG_IMG_SRA-'].Widget.configure(state='disabled')
        window['-TOG_PLT_DST-'].Widget.configure(state='disabled')
        window['-HGHTMP_IMG_FLE-'].Widget.configure(state='disabled')
        window['-HGHTMP_IMG_OPN-'].Widget.configure(state='disabled')
        window['-HGHTMP_WTR_TRSHLD-'].Widget.configure(state='disabled')
        window['-HGHTMP_ELE_HGH-'].Widget.configure(state='disabled')
        window['-HGHTMP_ELE_LOW-'].Widget.configure(state='disabled')
        window['-TOG_IMG_DBG-'].Widget.configure(state='disabled')
        window['-HGHTMP_SRA_NME-'].Widget.configure(state='disabled')
        window['-HGHTMP_LAND_SRA-'].Widget.configure(state='disabled')
        window['-LAND_SRA_OPN-'].Widget.configure(state='disabled')
        window['-HGHTMP_TOPO_SRA-'].Widget.configure(state='disabled')
        window['-TOPO_SRA_OPN-'].Widget.configure(state='disabled')
    else:
        window['-TOG_IMG_SRA-'].Widget.configure(state='normal')
        window['-TOG_PLT_DST-'].Widget.configure(state='normal')
        if values['-TOG_IMG_SRA-'] == False:
            if values['-TOG_PLT_DST-'] == True:
                window['-HGHTMP_ELE_LOW-'].Widget.configure(state='normal')
            window['-HGHTMP_IMG_FLE-'].Widget.configure(state='normal')
            window['-HGHTMP_IMG_OPN-'].Widget.configure(state='normal')
            window['-HGHTMP_WTR_TRSHLD-'].Widget.configure(state='normal')
            window['-HGHTMP_ELE_HGH-'].Widget.configure(state='normal')
            window['-TOG_IMG_DBG-'].Widget.configure(state='normal')
            window['-HGHTMP_SRA_NME-'].Widget.configure(state='normal')
        elif values['-TOG_IMG_SRA-'] == True:
            window['-HGHTMP_LAND_SRA-'].Widget.configure(state='normal')
            window['-LAND_SRA_OPN-'].Widget.configure(state='normal')
            window['-HGHTMP_TOPO_SRA-'].Widget.configure(state='normal')
            window['-TOPO_SRA_OPN-'].Widget.configure(state='normal')
def imgsratoggle():    #Image/SRA
    if values['-TOG_IMG_SRA-'] == True:
        window['-DIS_IMG_SRA-'].update('SRA Mode')
        window['-HGHTMP_IMG_FLE-'].Widget.configure(state='disabled')
        window['-HGHTMP_IMG_OPN-'].Widget.configure(state='disabled')
        window['-HGHTMP_WTR_TRSHLD-'].Widget.configure(state='disabled')
        window['-HGHTMP_ELE_HGH-'].Widget.configure(state='disabled')
        window['-HGHTMP_ELE_LOW-'].Widget.configure(state='disabled')
        window['-TOG_IMG_DBG-'].Widget.configure(state='disabled')
        window['-HGHTMP_SRA_NME-'].Widget.configure(state='disabled')
        window['-HGHTMP_LAND_SRA-'].Widget.configure(state='normal')
        window['-LAND_SRA_OPN-'].Widget.configure(state='normal')
        window['-HGHTMP_TOPO_SRA-'].Widget.configure(state='normal')
        window['-TOPO_SRA_OPN-'].Widget.configure(state='normal')
    else:
        window['-DIS_IMG_SRA-'].update('Image Mode')
        window['-HGHTMP_IMG_FLE-'].Widget.configure(state='normal')
        window['-HGHTMP_IMG_OPN-'].Widget.configure(state='normal')
        window['-HGHTMP_WTR_TRSHLD-'].Widget.configure(state='normal')
        window['-HGHTMP_ELE_HGH-'].Widget.configure(state='normal')
        window['-TOG_IMG_DBG-'].Widget.configure(state='normal')
        window['-HGHTMP_SRA_NME-'].Widget.configure(state='normal')
        window['-HGHTMP_LAND_SRA-'].Widget.configure(state='disabled')
        window['-LAND_SRA_OPN-'].Widget.configure(state='disabled')
        window['-HGHTMP_TOPO_SRA-'].Widget.configure(state='disabled')
        window['-TOPO_SRA_OPN-'].Widget.configure(state='disabled')
        if values['-TOG_PLT_DST-'] == True:
            window['-HGHTMP_ELE_LOW-'].Widget.configure(state='normal')
def dsrtoggle():       #Desert Planet
    if values['-TOG_PLT_DST-'] == True:
        window['-TOG_PLT_AQA-'].Widget.configure(state='disabled')
        if values['-TOG_IMG_SRA-'] == False:
            window['-HGHTMP_ELE_LOW-'].Widget.configure(state='normal')
    else:
        window['-TOG_PLT_AQA-'].Widget.configure(state='normal')
        window['-HGHTMP_ELE_LOW-'].Widget.configure(state='disabled')
def soilalbtoggle():   #Soil Albedo
    if values['-TOG_SOIL_ALB-'] == True: window['-SOIL_ALB-'].Widget.configure(state='normal')
    else: window['-SOIL_ALB-'].Widget.configure(state='disabled')
def soildepthtoggle(): #Soil Depth
    if values['-TOG_SOIL_DPTH-'] == True: window['-SOIL_DPTH-'].Widget.configure(state='normal')
    else: window['-SOIL_DPTH-'].Widget.configure(state='disabled')
def capsoiltoggle():   #Soil Heat Capacity
    if values['-TOG_SOIL_HCAP-'] == True: window['-SOIL_HCAP-'].Widget.configure(state='normal')
    else: window['-SOIL_HCAP-'].Widget.configure(state='disabled')
def soilwcptoggle():   #Soil Water Capacity
    if values['-TOG_SOIL_WCAP-'] == True: window['-SOIL_WCAP-'].Widget.configure(state='normal')
    else: window['-SOIL_WCAP-'].Widget.configure(state='disabled')
def soilsattoggle():   #Soil Saturation
    if values['-TOG_SOIL_SAT-'] == True: window['-SOIL_SAT-'].Widget.configure(state='normal')
    else: window['-SOIL_SAT-'].Widget.configure(state='disabled')
def snowalbtoggle():   #Snow Albedo
    if values['-TOG_SNW_ALB-'] == True: window['-SNW_ALB-'].Widget.configure(state='normal')
    else: window['-SNW_ALB-'].Widget.configure(state='disabled')
def mxsnowtoggle():    #Max Snow
    if values['-TOG_MAX_SNW-'] == True: window['-MAX_SNW-'].Widget.configure(state='normal')
    else: window['-MAX_SNW-'].Widget.configure(state='disabled')
def oceanalbtoggle():  #Ocean Albedo
    if values['-TOG_OCN_ALB-'] == True: window['-OCN_ALB-'].Widget.configure(state='normal')
    else: window['-OCN_ALB-'].Widget.configure(state='disabled')
def mldepthtoggle():   #Mixed Layer Depth
    if values['-TOG_OCN_MLD-'] == True: window['-OCN_MLD-'].Widget.configure(state='normal')
    else: window['-OCN_MLD-'].Widget.configure(state='disabled')
def gtoggle():         #Glacier
    if values['-TOG_GLCR-'] == True:
        window['-GLCR_HGT-'].Widget.configure(state='normal')
        window['-GLCR_TRSHLD-'].Widget.configure(state='normal')
    else:
        window['-GLCR_HGT-'].Widget.configure(state='disabled')
        window['-GLCR_TRSHLD-'].Widget.configure(state='disabled')
def vegtoggle():       #Vegetation
    if values['-TOG_VEG_TYPE-'] != 'None':
        window['-VEG_ACC-'].Widget.configure(state='normal')
        window['-VEG_BIOM_GRTH-'].Widget.configure(state='normal')
        window['-VEG_INIT_GRTH-'].Widget.configure(state='normal')
        window['-VEG_STOM_C-'].Widget.configure(state='normal')
        window['-VEG_RGH-'].Widget.configure(state='normal')
        window['-VEG_SCC-'].Widget.configure(state='normal')
        window['-VEG_PCC-'].Widget.configure(state='normal')
    else:
        window['-VEG_ACC-'].Widget.configure(state='disabled')
        window['-VEG_BIOM_GRTH-'].Widget.configure(state='disabled')
        window['-VEG_INIT_GRTH-'].Widget.configure(state='disabled')
        window['-VEG_STOM_C-'].Widget.configure(state='disabled')
        window['-VEG_RGH-'].Widget.configure(state='disabled')
        window['-VEG_SCC-'].Widget.configure(state='disabled')
        window['-VEG_PCC-'].Widget.configure(state='disabled')
def arsltoggle():      #Aerosols
    if values['-TOG_ARSLS-'] == True:
        window['-TOG_BLK_ATM-'].Widget.configure(state='normal')
        window['-TOG_ARSL_TYPE-'].Widget.configure(state='normal')
        window['-ARSL_DNSTY-'].Widget.configure(state='normal')
        window['-ARSL_MS_MX_RTO-'].Widget.configure(state='normal')
        window['-ARSL_RDUS-'].Widget.configure(state='normal')
    else:
        window['-TOG_BLK_ATM-'].Widget.configure(state='disabled')
        window['-TOG_ARSL_TYPE-'].Widget.configure(state='disabled')
        window['-ARSL_DNSTY-'].Widget.configure(state='disabled')
        window['-ARSL_MS_MX_RTO-'].Widget.configure(state='disabled')
        window['-ARSL_RDUS-'].Widget.configure(state='disabled')

#EPS Output text
vegetation_type = ['None', 'Proscribed', 'Dynamic']
class ot():
    iniyear = 'inityear=1,'
    outtype = 'outputtype=".nc"'
    ncpus = ''
    presis = ''
    resltn = ''
    crash = ''
    layers = ''
    recom = ''
    strtmp = 'startemp=5772.0,'
    strflx = 'flux=1367.0,'
    yrlngh = 'year=365.25,'
    ecctrcty = 'eccentricity=0.016715,'
    oblqty = 'obliquity=23.441,'
    lngoperi = 'lonvernaleq=102.7,'
    fxdobt = ''
    kplrobt = ''
    rotprop = ''
    grvty = 'gravity=9.80665,'
    radius = 'radius=1.0,\n'
    vegtn = ''
    wtsl = ''
    slalb = ''
    sldpth = ''
    slhcap = ''
    slwcap = ''
    slsat = ''
    snowalb = ''
    maxsnow = ''
    oceanalb = ''
    mixedlyr = ''
    aquaplanet = ''
    dsrtplanet = ''
    landmap = ''
    topomap = ''
    rstrtfle = ''
    atmosphere = ''
    ppressure = ''
    glacial = ''
    arsl_blk = '1'
    asource = '1'
    arsls = ''
    tmekeep = '				timestep=45.0,'
    snpshts = ''
    physicstext = ''
    stormstext = ''
    stmplus = ''
    runtext = ''
    crashtext = ''
    cleantext = ''

#BICEPS Functions
def system_check():
    #system('cls' if name == 'nt' else 'clear')
    sg.popup_auto_close("Running Compatability Check...", title="Running Check...")
    check_year = float(values['-OBT_LNGH-'])
    check_day = float(values['-PLNT_DAY_LNGH-'])
    check_time = float(values['-PHY_TMESTPS-'])
    check_run = int(values['-PHY_RUNSTPS-'])
    check_nsptw = int(values['-PHY_NSTPW-'])
    time_check = (24*60)/check_time
    time_corct = (24*60)/round(time_check)
    nsptw_check = (check_nsptw*check_time)/1440
    run_check = check_run/check_nsptw
    year_check = (check_year*1440)/(check_run*check_time)
    day_check1 = (check_day*1440)/check_time
    day_check2 = (check_run/12)/((check_day*1440)/check_time)
    year_corct = (round(year_check)*(check_run*check_time))/1440
    if time_check == round(time_check): sg.Print("Timestep: Nominal", text_color='dark green')
    else:
        sg.Print("WARNING: Current Timestep setting places ratio between (24*60) and timestep at "+str(time_check)+" which may cause problems with ExoPlaSim.", text_color='purple1')
        sg.Print("Setting it to "+str(time_corct)+" or a factor of a 24 hour day will work better.", text_color='purple1')
    if run_check == round(run_check): sg.Print("Runsteps: Nominal", text_color='dark green')
    else:
        sg.Print("WARNING: Current Runsteps setting places ratio between runsteps and NSPTW at "+str(run_check)+" which may cause problems with ExoPlaSim.", text_color='purple1')
        sg.Print("Setting it to a factor of a 24 hour day will work better.", text_color='purple1')
    if 4 <= nsptw_check <= 6: sg.Print("NSPTW: Nominal", text_color='dark green')
    else:
        sg.Print("WARNING: Current NSPTW setting places day interval at "+str(nsptw_check)+" which may cause problems with ExoPlaSim.", text_color='purple1')
        sg.Print("Changing this to be between 4 and 6 will work better.", text_color='purple1')
    if year_check == 1: sg.Print("Year: Nominal", text_color='dark green')
    else:
        sg.Print("WARNING: Current Year length places the ratio between (year*1440) and (runsteps*timestep) at "+str(round(year_check, 6))+" which may cause problems with ExoPlaSim.", text_color='purple1')
        sg.Print("Changing this to "+str(year_corct)+" will work better.", text_color='purple1')
    if day_check1 - round(float(day_check1)) <= 0.00001:
        if day_check2 == round(day_check2):
            sg.Print("Day: Nominal", text_color='dark green')
        else:
            sg.Print("WARNING: Current day length places ratio between (runsteps/12) and ((day*1440)/timestep) at "+str(day_check2)+" which may cause problems with ExoPlaSim.", text_color='purple1')
            sg.Print("Changeing this to an integer will work better.", text_color='purple1')
    else:
        sg.Printprint("WARNING: Current day length places ratio between (day*1440) and timestep at "+str(day_check1)+" which may cause problems with ExoPlaSim.", text_color='purple1')
        sg.Printprint("Changing this to an integer will work better.", text_color='purple1')

def save_sra():
    if values['-TOG_PLT_AQA-'] == False:
        if values['-TOG_IMG_SRA-'] == False:
            if values['-HGHTMP_IMG_FLE-'] != '':
                convert_sra(
                    filepath=Pth.cwd(),
                    infile=values['-HGHTMP_IMG_FLE-'],
                    grav=float(values['-PLNT_GRVTY-']),
                    debug_img= (values['-TOG_IMG_DBG-']==True),
                    desert_planet=(values['-TOG_PLT_DST-']==True),
                    floor_value=int(values['-HGHTMP_WTR_TRSHLD-']),
                    peak_value=float(values['-HGHTMP_ELE_HGH-']),
                    trench_value=float(values['-HGHTMP_ELE_LOW-']),
                    resotext=values['-SIM_RES-'],
                    sra_name=values['-HGHTMP_SRA_NME-'])
            else:
                sg.Print('No Image Found', text_color='dark red')
        else:
            lndsrafle = Pth.name(values['-HGHTMP_LAND_SRA-'])
            tposrafle = Pth.name(values['-HGHTMP_TOPO_SRA-'])
            sra_path = Pth.cwd()+'/SRA'
            lnd_path = sra_path+"/"+lndsrafle
            tpo_path = sra_path+"/"+tposrafle
            try:
                os.makedirs(sra_path)
            except FileExistsError:
                # directory already exists
                pass
            shutil.copyfile(values['-HGHTMP_LAND_SRA-'], lnd_path)
            shutil.copyfile(values['-HGHTMP_TOPO_SRA-'], tpo_path)

def open_heightmap(heightmapimg):
    window['-HGHTMP_IMG_FLE-'].update(heightmapimg)

def save_file(savefile):
    print("Inputs gathered...")
    #Conditions
    if values['-SIM_STRT_YR-'] != '1': ot.iniyear = 'inityear='+values['-SIM_STRT_YR-']+','
    if values['-SIM_OUTPT_TYPE-'] != '.nc': ot.outtype = 'outputtype="'+values['-SIM_OUTPT_TYPE-']+'",'
    if values['-SIM_CPUS-'] != '4': ot.ncpus = 'ncpus='+values['-SIM_CPUS-']+','
    if values['-SIM_PRES-'] != '8': ot.presis = 'precision='+values['-SIM_PRES-']+','
    if values['-SIM_RES-'] != 'T21': ot.resltn = 'resolution="'+values['-SIM_RES-']+'",'
    if values['-TOG_CRSH_TLRNT-'] != False: ot.crash = 'crashtolerant=True,'
    if values['-SIM_LYRS-'] != '10': ot.layers = 'layers='+values['-SIM_LYRS-']+','
    if values['-TOG_RCMPLE-'] != False: ot.recom = 'recompile=True,'

    if values['-STR_TMP-'] != '5772.0': ot.strtmp = 'startemp='+values['-STR_TMP-']+','
    if values['-STR_FLX-'] != '1367.0': ot.strflx = 'flux='+values['-STR_FLX-']+','
    if values['-OBT_LNGH-'] != '365.25': ot.yrlngh = 'year='+values['-OBT_LNGH-']+','
    if values['-OBT_ECC-'] != '0.016715': ot.ecctrcty = 'eccentricity='+values['-OBT_ECC-']+','
    if values['-OBT_OBLTY-'] != '23.441': ot.oblqty = 'obliquity='+values['OBT_OBLTY-']+','
    if values['-OBT_LOP-'] != '102.7': ot.lngoperi = 'lonvernaleq='+values['-OBT_LOP-']+','
    if values['-TOG_FXD_OBT-'] != False: ot.fxdobt = 'fixedorbit=True,'
    if values['-TOG_KPLR_OBT-'] != False: ot.kplrobt = 'keplerian=True, meananomaly0='+values['-OBT_MNANMLY-']+','
    if values['-TOG_TDL_LCK-'] != False: ot.rotprop = '				synchronous=True,substellarlon='+values['-PLNT_SUB_LONG-']+',desync='+values['-PLNT_SUB_DSNC-']+',tlcontrast='+values['-PLNT_TMP_CNST-']+',\n'
    else:
        if values['-PLNT_DAY_LNGH-'] != '1.0': ot.rotprop = '				rotationperiod='+values['-PLNT_DAY_LNGH-']+',\n'
    if values['-PLNT_GRVTY-'] != '9.80665': ot.grvty = 'gravity='+values['-PLNT_GRVTY-']+','
    if values['-PLNT_RDUS-'] != '1.0': ot.radius = 'radius='+values['-PLNT_RDUS-']+',\n'
    if values['-TOG_VEG_TYPE-'] != 'None': ot.vegtn = '				vegetation='+str(vegetation_type.index(values['-TOG_VEG_TYPE-']))+',vegaccel='+values['-VEG_ACC-']+',nforestgrowth='+values['-VEG_BIOM_GRTH-']+',initgrowth='+values['-VEG_INIT_GRTH-']+',initstomcond='+values['-VEG_STOM_C-']+',initrough='+values['-VEG_RGH-']+',initsoilcarbon='+values['-VEG_SCC-']+',initplantcarbon='+values['-VEG_PCC-']+',\n'
    if values['-TOG_SOIL_WET-'] != False: ot.wtsl = 'wetsoil=True,'
    if values['-TOG_SOIL_ALB-'] != False: ot.slalb = 'soilalbedo='+values['-SOIL_ALB-']+','
    if values['-TOG_SOIL_DPTH-'] != False: ot.sldpth = 'soildepth='+values['-SOIL_DPTH-']+','
    if values['-TOG_SOIL_HCAP-'] != False: ot.slhcap = 'cpsoil='+values['-SOIL_HCAP-']+','
    if values['-TOG_SOIL_WCAP-'] != False: ot.slwcap = 'soilwatercap='+values['-SOIL_WCAP-']+','
    if values['-TOG_SOIL_SAT-'] != False: ot.slsat = 'soilsaturation='+values['-SOIL_SAT-']+','
    if values['-TOG_SNW_ALB-'] != False: ot.snowalb = 'snowicealbedo='+values['-SNW_ALB-']+','
    if values['-TOG_MAX_SNW-'] != False: ot.maxsnow = 'maxsnow='+values['-MAX_SNW-']+','
    if values['-TOG_OCN_ALB-'] != False: ot.oceanalb = 'oceanalbedo='+values['-OCN_ALB-']+','
    if values['-TOG_OCN_MLD-'] != False: ot.mixedlyr = 'mldepth='+values['-OCN_MLD-']+','
    if values['-TOG_IMG_SRA'] != False:
        landmap = 'landmap="SRA/'+Pth.name(values['-HGHTMP_LAND_SRA-'])+'",'
        topomap = 'topomap="SRA/'+Pth.name(values['-HGHTMP_TOPO_SRA-'])+'",'
    if values['-TOG_PLT_AQA-'] != False:
        ot.aquaplanet = 'aquaplanet=True,'
        ot.landmap = ''
        ot.topomap = ''
    else:
        landmap = 'landmap="SRA/'+values['-HGHTMP_SRA_NME-']+'_surf_0172.sra",'
        topomap = 'topomap="SRA/'+values['-HGHTMP_SRA_NME-']+'_surf_0129.sra",'
    if values['-TOG_PLT_DST-'] != False: ot.dsrtplanet = 'desertplanet=True,'
    if values['-TOG_BLK_PR-'] != False: ot.atmosphere = 'pressure='+values['-BLK_PR-']+','
    if values['-TOG_GAS_CNST-'] != False: ot.atmosphere = ot.atmosphere+'gascon='+values['-GAS_CNST-']+','
    if values['-TOG_DRY_CRE-'] != False: ot.atmosphere = ot.atmosphere+'drycore=True,'
    if values['-TOG_GAS_PR-'] != False and values['-ATM_H2-'] != '0.0': ot.ppressure = 'pH2='+values['-ATM_H2-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_HE-'] != '0.0': ot.ppressure = ot.ppressure+'pHe='+values['-ATM_HE-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_N2-'] != '0.0': ot.ppressure = ot.ppressure+'pN2='+values['-ATM_N2-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_O2-'] != '0.0': ot.ppressure = ot.ppressure+'pO2='+values['-ATM_O2-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_AR-'] != '0.0': ot.ppressure = ot.ppressure+'pAr='+values['-ATM_AR-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_NE-'] != '0.0': ot.ppressure = ot.ppressure+'pNe='+values['-ATM_NE-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_KR-'] != '0.0': ot.ppressure = ot.ppressure+'pKr='+values['-ATM_KR-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_H2O-'] != '0.0': ot.ppressure = ot.ppressure+'pH2O='+values['-ATM_H2O-']+','
    if values['-TOG_GAS_PR-'] != False and values['-ATM_CO2-'] != '0.0': ot.ppressure = ot.ppressure+'pCO2='+values['-ATM_CO2-']+',\n'
    if values['-TOG_GLCR-'] != False: ot.glacial = "				  glaciers={'toggle': True, 'mindepth': "+values['-GLCR_TRSHLD-']+",'initialh': "+values['-GLCR_HGT-']+"},\n"
    if values['-TOG_BLK_ATM-'] == 'N2': ot.arsl_blk = '1'
    elif values['-TOG_BLK_ATM-'] == 'H2': ot.arsl_blk = '2'
    else: ot.arsl_blk = '3'
    if values['-TOG_ARSL_TYPE-'] == 'Photochemical': ot.asource = '1'
    else: ot.asource = '2'
    if values['-TOG_ARSLS-'] != False: ot.arsls = '				aerosol=True, aerobulk='+ot.arsl_blk+', asource='+ot.asource+', rhop='+values['-ARSL_DNSTY-']+', fcoeff='+values['-ARSL_MS_MX_RTO-']+', apart='+values['-ARSL_RDUS-']+',\n'
    if values['-PHY_TMESTPS-'] != '45.0': ot.tmekeep = '				timestep='+values['-PHY_TMESTPS-']+','
    if values['-PHY_RUNSTPS-'] != '11520': ot.tmekeep = ot.tmekeep+'runsteps='+values['-PHY_RUNSTPS-']+','
    if values['-PHY_SNPSHTS-'] != '0': ot.snpshts = 'snapshots='+values['-PHY_SNPSHTS-']+','
    if values['-PHY_FLTR-'] == 'Cesaro':
        if values['-PHY_FLTR_APP-'] == 'None': ot.physicstext = ''
        if values['-PHY_FLTR_APP-'] == 'GP': ot.physicstext = ",physicsfilter='gp|cesaro',\n"
        if values['-PHY_FLTR_APP-'] == 'SP': ot.physicstext = ",physicsfilter='cesaro|sp',\n"
        if values['-PHY_FLTR_APP-'] == 'GP+SP': ot.physicstext = ",physicsfilter='gp|cesaro|sp',\n"
    elif values['-PHY_FLTR-'] == 'Exp':
        if values['-PHY_FLTR_APP-'] == 'None': ot.physicstext = ''
        if values['-PHY_FLTR_APP-'] == 'GP': ot.physicstext = ",physicsfilter='gp|exp',\n"
        if values['-PHY_FLTR_APP-'] == 'SP': ot.physicstext = ",physicsfilter='exp|sp',\n"
        if values['-PHY_FLTR_APP-'] == 'GP+SP': ot.physicstext = ",physicsfilter='gp|exp|sp',\n"
    elif values['-PHY_FLTR-'] == 'Lh':
        if values['-PHY_FLTR_APP-'] == 'None': ot.physicstext = ''
        if values['-PHY_FLTR_APP-'] == 'GP': ot.physicstext = ",physicsfilter='gp|lh',\n"
        if values['-PHY_FLTR_APP-'] == 'SP': ot.physicstext = ",physicsfilter='lh|sp',\n"
        if values['-PHY_FLTR_APP-'] == 'GP+SP': ot.physicstext = ",physicsfilter='gp|lh|sp',\n"
    if values['-TOG_STRM_CLIM-'] != False: ot.stormstext = ",\n				stormclim=True"
    if values['-TOG_HRCNE-'] != False: ot.stmplus = ", 'NKTRIGGER': 1"
    if values['-STM_MIN_TEMP-'] != '298.15': ot.stmplus = ot.stmplus+", 'MINSURFTEMP': "+values['-STM_MIN_TEMP-']
    if values['-STM_MAX_TEMP-'] != '373.15': ot.stmplus = ot.stmplus+", 'MAXSURFTEMP': "+values['-STM_MAX_TEMP-']
    if values['-STM_MIN_WIND-'] != '20.5': ot.stmplus = ot.stmplus+", 'SWINDTHRESH': "+values['-STM_MIN_WIND-']
    if values['-STM_MIN_CLCT-'] != '30': ot.stmplus = ot.stmplus+", 'SIZETHRESH': "+values['-STM_MIN_CLCT-']
    if values['-STM_FIN_CLCT-'] != '16': ot.stmplus = ot.stmplus+", 'ENDTHRESH': "+values['-STM_FIN_CLCT-']
    if values['-STM_GPI-'] != '0.37': ot.stmplus = ot.stmplus+", 'GPITHRESH': "+values['-STM_GPI-']
    if values['-STM_MPI-'] != '33.0': ot.stmplus = ot.stmplus+", 'VMXTHRESH': "+values['-STM_MPI-']
    if values['-STM_LATM_MAX_WIND-'] != '33.0': ot.stmplus = ot.stmplus+", 'WINDTHRESH': "+values['-STM_LATM_MAX_WIND-']
    if values['-STM_VNT_IDX-'] != '0.145': ot.stmplus = ot.stmplus+", 'VITHRESH': "+values['-STM_VNT_IDX-']
    if values['-STM_MIN_TMESTPS-'] != '256': ot.stmplus = ot.stmplus+", 'MINSTORMLEN': "+values['-STM_MIN_TMESTPS-']
    if values['-STM_MAX_TMESTPS-'] != '1024': ot.stmplus = ot.stmplus+", 'MAXSTORMLEN': "+values['-STM_MAX_TMESTPS-']
    if values['-STM_VRMI-'] != '0.577': ot.stmplus = ot.stmplus+", 'VRMTHRESH': "+values['-STM_VRMI-']
    if values['-STM_LAV-'] != '0.000012': ot.stmplus = ot.stmplus+", 'LAVTHRESH': "+values['-STM_LAV-']
    if values['-TOG_STM_CPTRE-'] != False: ot.stormstext = ot.stormstext+",stormcapture={'toggle': 1"+ot.stmplus+"}"
    if values['-TOG_HGH_CDNCE-'] != False: ot.stormstext = ot.stormstext+",highcadence={'toggle': 1, 'start': "+values['-HGH_CDNCE_STRT-']+", 'end': "+values['-HGH_CDNCE_END-']+", 'interval': "+values['-HGH_CDNCE_INTRVL-']+"}"
    if values['-TOG_CRSH_IF_BRKN-'] != False: ot.crashtext = ',crashifbroken=True'
    if values['-TOG_CLN-'] != False: ot.cleantext = ',clean=True'
    if values['-TOG_RUN_TO_BLNCE-'] != False: ot.runtext = values['-SIM_PRJCT_NME-']+'.runtobalance(threshold='+values['-PHY_THRSHLD-']+',baseline='+values['-PHY_BSELNE-']+',maxyears='+values['-PHY_MAX_YR-']+',minyears='+values['-PHY_MIN_YR-']+ot.crashtext+ot.cleantext+')\n'+values['-SIM_PRJCT_NME-']+'.run(years=10)\n'
    elif values['-TOG_RUN_TO_BLNCE-'] == False: ot.runtext = values['-SIM_PRJCT_NME-']+'.run(years='+values['-PHY_RUNTME-']+')\n'

    #Formatting
    format_name = "import exoplasim as exo\n"+values['-SIM_PRJCT_NME-']+' = exo.Model(workdir="'+values['-SIM_PRJCT_NME-']+'",modelname="'+values['-SIM_MDL_NME-']+'",'
    format_model = ot.iniyear+ot.ncpus+ot.presis+ot.resltn+ot.crash+ot.layers+ot.recom+ot.outtype+')\n'
    format_stellar = values['-SIM_PRJCT_NME-']+'.configure('+ot.strtmp+ot.strflx+'\n'
    format_orbit = "				"+ot.yrlngh+ot.ecctrcty+ot.oblqty+ot.lngoperi+ot.fxdobt+ot.kplrobt+'\n'
    format_rotation = ot.rotprop
    format_planet = "				"+ot.grvty+ot.radius
    format_vegetation = ot.vegtn
    format_surface = "				"+ot.wtsl+ot.slalb+ot.sldpth+ot.slhcap+ot.slwcap+ot.slsat+ot.snowalb+ot.maxsnow+'seaice='+str(values['-TOG_SEA_ICE-'])+','+ot.oceanalb+ot.mixedlyr+'oceanzenith="'+values['-TOG_OCN_ZEN-']+'",\n'
    format_geography = ''
    if ot.aquaplanet != '' or ot.dsrtplanet != ''or ot.landmap !='' or ot.topomap !='':
        format_geography = "				"+ot.aquaplanet+ot.dsrtplanet+ot.landmap+ot.topomap+'\n'
    format_atmosphere = "				"+ot.atmosphere+'ozone='+str(values['-TOG_OZNE-'])+',\n'
    format_ppressure = ''
    if values['-TOG_GAS_PR-'] == True:
        format_ppressure = "				"+ot.ppressure
    format_glacier = ot.glacial
    format_aerosol = ot.arsls
    format_timekeep = ot.tmekeep+ot.snpshts+"otherargs={'NSTPW@plasim_namelist':'"+values['-PHY_NSTPW-']+"'}"+ot.physicstext
    format_storms = ot.stormstext+')\n'
    format_export = values['-SIM_PRJCT_NME-']+'.exportcfg()\n'
    format_run = ot.runtext
    format_finalise = values['-SIM_PRJCT_NME-']+'.finalize("'+values['-SIM_PRJCT_NME-']+'",allyears='+str(values['-TOG_ALL_YRS-'])+',keeprestarts='+str(values['-TOG_KEEP_RSTS-'])+')\n'
    print("Formatting Complete...")

    #Writing to file
    print("Saving Main File...")
    with open(savefile, "w") as output_file:
        output_file.write(format_name)
        output_file.write(format_model)
        output_file.write(format_stellar)
        output_file.write(format_orbit)
        output_file.write(format_rotation)
        output_file.write(format_planet)
        output_file.write(format_vegetation)
        output_file.write(format_surface)
        output_file.write(format_geography)
        output_file.write(format_atmosphere)
        output_file.write(format_ppressure)
        output_file.write(format_glacier)
        output_file.write(format_aerosol)
        output_file.write(format_timekeep)
        output_file.write(format_storms)
        output_file.write(format_export)
        output_file.write(format_run)
        output_file.write(format_finalise)
        print("Saving Complete!")

def save_ini(filepath):
    sg.Print("Inputs gathered...", text_color='dark green')
    config = ConfigParser()
    config['Model'] = {'Project Name': values['-SIM_PRJCT_NME-'],
                       'Model Name': values['-SIM_MDL_NME-'],
                       'Start Year': values['-SIM_STRT_YR-'],
                       'Output Type': values['-SIM_OUTPT_TYPE-'],
                       'CPU Count': values['-SIM_CPUS-'],
                       'Precision': values['-SIM_PRES-'],
                       'Resolution': values['-SIM_RES-'],
                       'Crash Tolorant': values['-TOG_CRSH_TLRNT-'],
                       'Layers': values['-SIM_LYRS-'],
                       'Recompile': values['-TOG_RCMPLE-']}
    config['Simulation'] = {'Timestep': values['-PHY_TMESTPS-'],
                            'Runsteps': values['-PHY_RUNSTPS-'],
                            'Snapshots': values['-PHY_SNPSHTS-'],
                            'NSTPW': values['-PHY_NSTPW-'],
                            'Restart File': values['-TOG_RSTRT_FLE-'],
                            'Physics Filter': values['-PHY_FLTR-'],
                            'Filter Application': values['-PHY_FLTR_APP-'],
                            'Run To Balance': values['-TOG_RUN_TO_BLNCE-'],
                            'Run Time': values['-PHY_RUNTME-'],
                            'Threshold': values['-PHY_THRSHLD-'],
                            'Baseline': values['-PHY_BSELNE-'],
                            'Min. Year': values['-PHY_MIN_YR-'],
                            'Max. Year': values['-PHY_MAX_YR-'],
                            'Crash if Broken': values['-TOG_CRSH_IF_BRKN-'],
                            'Clean': values['-TOG_CLN-'],
                            'All Years': values['-TOG_ALL_YRS-'],
                            'Keep Restarts': values['-TOG_KEEP_RSTS-']}
    config['Star'] = {'Star Temperature': values['-STR_TMP-'],
                         'Stellar Flux': values['-STR_FLX-']}
    config['Orbit'] = {'Year Length': values['-OBT_LNGH-'],
                         'Eccentricity': values['-OBT_ECC-'],
                         'Obliquity': values['-OBT_OBLTY-'],
                         'Longitude of Periapsis': values['-OBT_LOP-'],
                         'Fixed Orbit': values['-TOG_FXD_OBT-'],
                         'Keplerian Orbit': values['-TOG_KPLR_OBT-'],
                         'Mean Anomaly': values['-OBT_MNANMLY-']}
    config['Planet'] = {'Gravity': values['-PLNT_GRVTY-'],
                        'Radius': values['-PLNT_RDUS-'],
                        'Day Length': values['-PLNT_DAY_LNGH-'],
                        'Tidally Locked': values['-TOG_TDL_LCK-'],
                        'Substellar Longitude': values['-PLNT_SUB_LONG-'],
                        'Substellar Desync': values['-PLNT_SUB_DSNC-'],
                        'Temperature Contrast': values['-PLNT_TMP_CNST-']}
    config['Heightmap'] = {'Aqua Planet': values['-TOG_PLT_AQA-'],
                           'Image/SRA': values['-TOG_IMG_SRA-'],
                           'Desert Planet': values['-TOG_PLT_DST-'],
                           'Heightmap Image': values['-HGHTMP_IMG_FLE-'],
                           'Water Threshold': values['-HGHTMP_WTR_TRSHLD-'],
                           'Highest Elevation': values['-HGHTMP_ELE_HGH-'],
                           'Lowest Elevation': values['-HGHTMP_ELE_LOW-'],
                           'Image Debug': values['-TOG_IMG_DBG-'],
                           'SRA Name': values['-HGHTMP_SRA_NME-'],
                           'Land SRA': values['-HGHTMP_LAND_SRA-'],
                           'Topographic SRA': values['-HGHTMP_TOPO_SRA-']}
    config['Soil'] = {'Wet Soil': values['-TOG_SOIL_WET-'],
                      'Toggle Soil Albedo': values['-TOG_SOIL_ALB-'],
                      'Soil Albedo': values['-SOIL_ALB-'],
                      'Toggle Soil Depth': values['-TOG_SOIL_DPTH-'],
                      'Soil Depth': values['-SOIL_DPTH-'],
                      'Toggle Heat Capacity': values['-TOG_SOIL_HCAP-'],
                      'Soil Heat Capacity': values['-SOIL_HCAP-'],
                      'Toggle Water Capacity': values['-TOG_SOIL_WCAP-'],
                      'Soil Water Capacity': values['-SOIL_WCAP-'],
                      'Toggle Saturation': values['-TOG_SOIL_SAT-'],
                      'Soil Saturation': values['-SOIL_SAT-']}
    config['Snow/Ocean'] = {'Toggle Snow Albedo': values['-TOG_SNW_ALB-'],
                            'Snow Albedo': values['-SNW_ALB-'],
                            'Toggle Max Snow': values['-TOG_MAX_SNW-'],
                            'Max Snow': values['-MAX_SNW-'],
                            'Sea Ice': values['-TOG_SEA_ICE-'],
                            'Toggle Ocean Albedo': values['-TOG_OCN_ALB-'],
                            'Ocean Albedo': values['-OCN_ALB-'],
                            'Toggle MDL': values['-TOG_OCN_MLD-'],
                            'Mixed Layer Depth': values['-OCN_MLD-'],
                            'Ocean Zenith': values['-TOG_OCN_ZEN-']}
    config['Glacier'] = {'Glaciers': values['-TOG_GLCR-'],
                         'Glacier Height': values['-GLCR_HGT-'],
                         'Glacier Threshold': values['-GLCR_TRSHLD-']}
    config['Vegetation'] = {'Vegetation Type': values['-TOG_VEG_TYPE-'],
                            'Vegetation Acceleration': values['-VEG_ACC-'],
                            'Biomass Growth': values['-VEG_BIOM_GRTH-'],
                            'Initial Growth': values['-VEG_INIT_GRTH-'],
                            'Stomatal Conductance': values['-VEG_STOM_C-'],
                            'Vegetation Roughness': values['-VEG_RGH-'],
                            'Soil Carbon Content': values['-VEG_SCC-'],
                            'Plant Carbon Content': values['-VEG_PCC-']}
    config['Atmosphere'] = {'Toggle Bulk Pressure': values['-TOG_BLK_PR-'],
                            'Bulk Pressure': values['-BLK_PR-'],
                            'Toggle Gas Constant': values['-TOG_GAS_CNST-'],
                            'Gas Constant': values['-GAS_CNST-'],
                            'Dry Core': values['-TOG_DRY_CRE-'],
                            'Ozone': values['-TOG_OZNE-'],
                            'Gas Pressure': values['-TOG_GAS_PR-'],
                            'H2': values['-ATM_H2-'],
                            'He': values['-ATM_HE-'],
                            'N2': values['-ATM_N2-'],
                            'O2': values['-ATM_O2-'],
                            'Ar': values['-ATM_AR-'],
                            'Ne': values['-ATM_NE-'],
                            'Kr': values['-ATM_KR-'],
                            'H2O': values['-ATM_H2O-'],
                            'CO2': values['-ATM_CO2-']}
    config['Aerosol'] = {'Aerosols': values['-TOG_ARSLS-'],
                         'Bulk Atmosphere': values['-TOG_BLK_ATM-'],
                         'Aerosol Type': values['-TOG_ARSL_TYPE-'],
                         'Aerosol Density': values['-ARSL_DNSTY-'],
                         'Aerosol Mass Mixing Ratio': values['-ARSL_MS_MX_RTO-'],
                         'Aerosol Particle Radius': values['-ARSL_RDUS-']}
    config['Storm'] = {'Storm Climatology': values['-TOG_STRM_CLIM-'],
                       'High Cadence': values['-TOG_HGH_CDNCE-'],
                       'HC Start': values['-HGH_CDNCE_STRT-'],
                       'HC End': values['-HGH_CDNCE_END-'],
                       'HC Interval': values['-HGH_CDNCE_INTRVL-'],
                       'Storm Capture': values['-TOG_STM_CPTRE-'],
                       'Hurricane Cyclogenesis': values['-TOG_HRCNE-'],
                       'Min Surface Temperature': values['-STM_MIN_TEMP-'],
                       'Max Surface Temperature': values['-STM_MAX_TEMP-'],
                       'Min Surface Windspeed': values['-STM_MIN_WIND-'],
                       'Min Cell Count': values['-STM_MIN_CLCT-'],
                       'Final Cell Count': values['-STM_FIN_CLCT-'],
                       'Genesis Potential Index': values['-STM_GPI-'],
                       'Max Potential Intensity': values['-STM_MPI-'],
                       'Low-Atmosphere Max Wind': values['-STM_LATM_MAX_WIND-'],
                       'Ventilation Index': values['-STM_VNT_IDX-'],
                       'Min Timesteps': values['-STM_MIN_TMESTPS-'],
                       'Max Timesteps': values['-STM_MAX_TMESTPS-'],
                       'Vent-Reduced Max Intensity': values['-STM_VRMI-'],
                       'Low Atm. Vorticity': values['-STM_LAV-']}
    config['ToggleValues'] = {'A': '1'}
    with open(filepath, "w") as output_file:
        config.write(output_file)
    sg.Print('Config saved!', text_color='dark green')

def load_ini(filepath):
    print('Loading Config parameters...')
    cfg = ConfigParser()
    cfg.read(filepath)
    mdelprm = cfg['Model']
    window['-SIM_PRJCT_NME-'].update(mdelprm.get('Project Name'))
    window['-SIM_MDL_NME-'].update(mdelprm.get('Model Name'))
    window['-SIM_STRT_YR-'].update(mdelprm.get('Start Year'))
    window['-SIM_OUTPT_TYPE-'].update(mdelprm.get('Output Type'))
    window['-SIM_CPUS-'].update(mdelprm.get('CPU Count'))
    window['-SIM_PRES-'].update(mdelprm.get('Precision'))
    window['-SIM_RES-'].update(mdelprm.get('Resolution'))
    window['-TOG_CRSH_TLRNT-'].update(mdelprm.get('Crash Tolorant'))
    window['-SIM_LYRS-'].update(mdelprm.get('Layers'))
    window['-TOG_RCMPLE-'].update(mdelprm.get('Recompile'))
    simnprm = cfg['Simulation']
    window['-PHY_TMESTPS-'].update(simprm.get('Timestep'))
    window['-PHY_RUNSTPS-'].update(simprm.get('Runsteps'))
    window['-PHY_SNPSHTS'].update(simprm.get('Snapshots'))
    window['-PHY_NSTPW-'].update(simprm.get('NSTPW'))
    window['-PHY_RSTRT_FLE-'].update(simprm.get('Restart File'))
    window['-PHY_FLTR-'].update(simprm.get('Physics Filter'))
    window['-PHY_FLTR_APP-'].update(simprm.get('Filter Application'))
    window['-TOG_RUN_TO_BLNCE-'].update(simprm.get('Run To Balance'))
    window['-PHY_RUNTME-'].update(simprm.get('Run Time'))
    window['-PHY_THRSHLD-'].update(simprm.get('Threshold'))
    window['-PHY_BSELNE-'].update(simprm.get('Baseline'))
    window['-PHY_MIN_YR-'].update(simprm.get('Min. Year'))
    window['-PHY_MAX_YR-'].update(simprm.get('Max. Year'))
    window['-TOG_CRSH_IF_BRKN-'].update(simprm.get('Crash if Broken'))
    window['-TOG_CLN-'].update(simprm.get('Clean'))
    window['-TOG_ALL_YRS-'].update(simprm.get('All Years'))
    window['-TOG_KEEP_RSTS-'].update(simprm.get('Keep Restarts'))
    starprm = cfg['Star']
    window['-STR_TMP-'].update(starprm.get('Star Temperature'))
    window['-STR_FLX-'].update(starprm.get('Stellar Flux'))
    orbtprm = cfg['Orbit']
    window['-OBT_LNGH-'].update(orbtprm.get('Year Length'))
    window['-OBT_ECC-'].update(orbtprm.get('Eccentricity'))
    window['-OBT_OBLTY-'].update(orbtprm.get('Obliquity'))
    window['-OBT_LOP-'].update(orbtprm.get('Longitude of Periapsis'))
    window['-TOG_FXD_OBT-'].update(orbtprm.get('Fixed Orbit'))
    window['-TOG_KPLR_OBT-'].update(orbtprm.get('Keplerian Orbit'))
    window['-OBT_MNANMLY-'].update(orbtprm.get('Mean Anomaly'))
    plntprm = cfg['Planet']
    window['-PLNT_GRVTY-'].update(plntprm.get('Gravity'))
    window['-PLNT_RDUS-'].update(plntprm.get('Radius'))
    window['-PLNT_DAY_LNGH-'].update(plntprm.get('Day Length'))
    window['-TOG_TDL_LCK-'].update(plntprm.get('Tidally Locked'))
    window['-PLNT_SUB_LONG-'].update(plntprm.get('Substellar Longitude'))
    window['-PLNT_SUB_DSNC-'].update(plntprm.get('Substellar Desync'))
    window['-PLNT_TMP_CNST-'].update(plntprm.get('Temperature Contrast'))
    hghtprm = cfg['Heightmap']
    window['-TOG_PLT_AQA-'].update(hghtprm.get('Aqua Planet'))
    window['-TOG_IMG_SRA-'].update(hghtprm.get('Image/SRA'))
    window['-TOG_PLT_DST-'].update(hghtprm.get('Desert Planet'))
    window['-HGHTMP_IMG_FLE-'].update(hghtprm.get('Heightmap Image'))
    window['-HGHTMP_WTR_TRSHLD-'].update(hghtprm.get('Water Threshold'))
    window['-HGHTMP_ELE_HGH-'].update(hghtprm.get('Highest Elevation'))
    window['-HGHTMP_ELE_LOW-'].update(hghtprm.get('Lowest Elevation'))
    window['-TOG_IMG_DBG-'].update(hghtprm.get('Image Debug'))
    window['-HGHTMP_SRA_NME-'].update(hghtprm.get('SRA Name'))
    window['-HGHTMP_LAND_SRA-'].update(hghtprm.get('Land SRA'))
    window['-HGHTMP_TOPO_SRA-'].update(hghtprm.get('Topographic SRA'))
    soilprm = cfg['Soil']
    window['-TOG_SOIL_WET-'].update(soilprm.get('Wet Soil'))
    window['-TOG_SOIL_ALB-'].update(soilprm.get('Toggle Soil Albedo'))
    window['-SOIL_ALB-'].update(soilprm.get('Soil Albedo'))
    window['-TOG_SOIL_DPTH-'].update(soilprm.get('Toggle Soil Depth'))
    window['-SOIL_DPTH-'].update(soilprm.get('Soil Depth'))
    window['-TOG_SOIL_HCAP-'].update(soilprm.get('Toggle Heat Capacity'))
    window['-SOIL_HCAP-'].update(soilprm.get('Soil Heat Capacity'))
    window['-TOG_SOIL_WCAP-'].update(soilprm.get('Toggle Water Capacity'))
    window['-SOIL_WCAP-'].update(soilprm.get('Soil Water Capacity'))
    window['-TOG_SOIL_SAT-'].update(soilprm.get('Toggle Saturation'))
    window['-SOIL_SAT-'].update(soilprm.get('Soil Saturation'))
    snocprm = cfg['Snow/Ocean']
    window['-TOG_SNW_ALB-'].update(snocprm.get('Toggle Snow Albedo'))
    window['-SNW_ALB-'].update(snocprm.get('Snow Albedo'))
    window['-TOG_MAX_SNW-'].update(snocprm.get('Toggle Max Snow'))
    window['-MAX_SNW-'].update(snocprm.get('Max Snow'))
    window['-TOG_SEA_ICE-'].update(snocprm.get('Sea Ice'))
    window['-TOG_OCN_ALB-'].update(snocprm.get('Toggle Ocean Albedo'))
    window['-OCN_ALB-'].update(snocprm.get('Ocean Albedo'))
    window['-TOG_OCN_MLD-'].update(snocprm.get('Toggle MDL'))
    window['-OCN_MLD-'].update(snocprm.get('Mixed Layer Depth'))
    window['-TOG_OCN_ZEN-'].update(snocprm.get('Ocean Zenith'))
    glcrprm = cfg['Glacier']
    window['-TOG_GLCR-'].update(glcrprm.get('Glaciers'))
    window['-GLCR_HGT-'].update(glcrprm.get('Clacier Height'))
    window['-GLCR_TRSHLD-'].update(glcrprm.get('Glacier Threshold'))
    vgtnprm = cfg['Vegetation']
    window['-TOG_VEG_TYPE-'].update(vgtnprm.get('Vegetation Type'))
    window['-VEG_ACC-'].update(vgtnprm.get('Vegetation Acceleration'))
    window['-VEG_BIOM_GRTH-'].update(vgtnprm.get('Biomass Growth'))
    window['-VEG_INIT_GRTH-'].update(vgtnprm.get('Initial Growth'))
    window['-VEG_STOM_C-'].update(vgtnprm.get('Stomatal Conductance'))
    window['-VEG_RGH-'].update(vgtnprm.get('Vegetation Roughness'))
    window['-VEG_SCC-'].update(vgtnprm.get('Soil Carbon Content'))
    window['-VEG_PCC-'].update(vgtnprm.get('Plant Carbon Content'))
    atmsprm = cfg['Atmosphere']
    window['-TOG_BLK_PR-'].update(atmsprm.get('Toggle Bulk Pressure'))
    window['-BLK_PR-'].update(atmsprm.get('Bulk Pressure'))
    window['-TOG_GAS_CNST-'].update(atmsprm.get('Toggle Gas Constant'))
    window['-GAS_CNST-'].update(atmsprm.get('Gas Constant'))
    window['-TOG_DRY_CRE-'].update(atmsprm.get('Dry Core'))
    window['-TOG_OZNE-'].update(atmsprm.get('Ozone'))
    window['-TOG_GAS_PR-'].update(atmsprm.get('Gas Pressure'))
    window['-ATM_H2-'].update(atmsprm.get('H2'))
    window['-ATM_HE-'].update(atmsprm.get('Ne'))
    window['-ATM_N2-'].update(atmsprm.get('N2'))
    window['-ATM_O2-'].update(atmsprm.get('O2'))
    window['-ATM_AR-'].update(atmsprm.get('Ar'))
    window['-ATM_NE-'].update(atmsprm.get('Ne'))
    window['-ATM_KR-'].update(atmsprm.get('Kr'))
    window['-ATM_H2O-'].update(atmsprm.get('H2O'))
    window['-ATM_CO2-'].update(atmsprm.get('CO2'))
    arslprm = cfg['Aerosol']
    window['-TOG_ARSLS-'].update(arslprm.get('Aerosols'))
    window['-TOG_BLK_ATM-'].update(arslprm.get('Bulk Atmosphere'))
    window['-TOG_ARSL_TYPE-'].update(arslprm.get('Aerosol Type'))
    window['-ARSL_DNSTY-'].update(arslprm.get('Aerosol Density'))
    window['-ARSL_MS_MX_RTO-'].update(arslprm.get('Aerosol Mas Mixing Ratio'))
    window['-ARSL_RDUS-'].update(arslprm.get('Aerosol Particle Radius'))
    strmprm = cfg['Storm']
    window['-TOG_STRM_CLIM-'].update(strmprm.get('Storm Climatology'))
    window['-TOG_HGH_CDNCE-'].update(strmprm.get('High Cadence'))
    window['-HGH_CDNCE_STRT-'].update(strmprm.get('HC Start'))
    window['-HGH_CDNCE_END-'].update(strmprm.get('HC End'))
    window['-HGH_CDNCE_INTRVL-'].update(strmprm.get('HC Interval'))
    window['-TOG_STM_CPTRE-'].update(strmprm.get('Storm Capture'))
    window['-TOG_HRCNE-'].update(strmprm.get('Hurricane Cyclogenesis'))
    window['-STM_MIN_TEMP-'].update(strmprm.get('Min Surface Temperature'))
    window['-STM_MAX_TEMP-'].update(strmprm.get('Max Surface Temperature'))
    window['-STM_MIN_WIND-'].update(strmprm.get('Min Surface Windspeed'))
    window['-STM_MIN_CLCT-'].update(strmprm.get('Min Cell Count'))
    window['-STM_FIN_CLCT-'].update(strmprm.get('Final Cell Count'))
    window['-STM_GPI-'].update(strmprm.get('Genesis Potential Index'))
    window['-STM_MPI-'].update(strmprm.get('Max Potential Intensity'))
    window['-STM_LATM_MAX_WIND-'].update(strmprm.get('Low-Atmosphere Max Wind'))
    window['-STM_VNT_IDX-'].update(strmprm.get('Ventilation Index'))
    window['-STM_MIN_TMESTPS-'].update(strmprm.get('Min Timesteps'))
    window['-STM_MAX_TMESTPS-'].update(strmprm.get('Max Timesteps'))
    window['-STM_VRMI-'].update(strmprm.get('Vent-Reduced Max Intensity'))
    window['-STM_LAV-'].update(strmprm.get('Low Atm. Vorticity'))
    rstrtfletoggle()
    stmtoggle()
    hghcdncetoggle()
    stmcptretoggle()
    baltoggle ()
    keplertoggle()
    tidaltoggle()
    pressuretoggle()
    gascontoggle()
    ptoggle()
    aquatoggle()
    imgsratoggle()
    dsrtoggle()
    soilalbtoggle()
    soildepthtoggle()
    capsoiltoggle()
    soilwcptoggle()
    soilsattoggle()
    snowalbtoggle()
    mxsnowtoggle()
    oceanalbtoggle()
    mldepthtoggle()
    gtoggle()
    vegtoggle()
    arsltoggle()
    print('Config parameters loaded!')
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
default_layout = [[sg.Text('This is our persistent window')],
          [sg.Button('1'), sg.Button('2'), sg.Button('Exit')]]
font = ("Verdana", 12)

Sim_text        = [[sg.Text('Model Properties', font='Verdana 13 underline')],
                     [sg.Text('Project Name:', tooltip=hT("helpjctnme"))],
                     [sg.Text('Model Name:', tooltip=hT("helmdlnme"))],
                     [sg.Text('Start Year:', tooltip=hT("helpstrtyr"))],
                     [sg.Text('Output Type:', tooltip=hT("helpotptype"))],
                     [sg.Text('CPU Count:', tooltip=hT("helpcpucnt"))],
                     [sg.Text('Precision:', tooltip=hT("helpresision"))],
                     [sg.Text('Resolution:', tooltip=hT("helpresolution"))],
                     [sg.Text('Crash Tolorant:', tooltip=hT("helpcrshtlrnt"))],
                     [sg.Text('Layers:', tooltip=hT("helplayers"))],
                     [sg.Text('Recompile:', tooltip=hT("helprecompile"))]]
Sim_input       = [[sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='Earth', key='-SIM_PRJCT_NME-', s=15)],
                     [sg.Input(default_text='earth_model', key='-SIM_MDL_NME-', s=15)],
                     [sg.Input(default_text='1', key='-SIM_STRT_YR-', s=5)],
                     [sg.Combo(['.nc', '.nc', '.npy', '.npz', '.hdf5', '.he5', '.h5', '.csv', '.gz', '.txt', '.tar', '.tar.gz', '.tar.xz', '.tar.bz2'], default_value='.nc', key='-SIM_OUTPT_TYPE-', s=7)],
                     [sg.Combo(['1', '2', '4', '8', '16', '32'], default_value='4', key='-SIM_CPUS-', s=5)],
                     [sg.Combo(['4', '8'], default_value='8', key='-SIM_PRES-', s=5)],
                     [sg.Combo(['T21', 'T42', 'T63', 'T85', 'T106', 'T127', 'T170'], default_value='T21', key='-SIM_RES-', s=5)],
                     [sg.Checkbox('', default=True, enable_events=True, key='-TOG_CRSH_TLRNT-')],
                     [sg.Input(default_text='10', key='-SIM_LYRS-', s=5)],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_RCMPLE-')]]
Dynamics_text     = [[sg.Text('Simulation Properties', font='Verdana 13 underline')],
                     [sg.Text('Timestep (min):', tooltip=hT("helptimestep"))],
                     [sg.Text('Runsteps:', tooltip=hT("helprunsteps"))],
                     [sg.Text('Snapshots:', tooltip=hT("helpsnapshots"))],
                     [sg.Text('NSTPW:', tooltip=hT("helpnstpw"))],
                     [sg.Text('Restart File:', tooltip=hT("helprestrtfle"))],
                     [sg.Text('Physics Filter:', tooltip=hT("helphysfltr"))],
                     [sg.Text('Filter Application:', tooltip=hT("helpfltrapp"))],
                     [sg.Text('Run to Balance:', tooltip=hT("helprntbal"))],
                     [sg.Text('Run Time (years):', tooltip=hT("helprntme"))],
                     [sg.Text('Threshold:', tooltip=hT("helpthrshld"))],
                     [sg.Text('Baseline (years):', tooltip=hT("helpbslne"))],
                     [sg.Text('Min. Year (years):', tooltip=hT("helpmxyr"))],
                     [sg.Text('Max. Year (years):', tooltip=hT("helpmnyr"))],
                     [sg.Text('Crash if Broken:', tooltip=hT("helpcrshibrkn"))],
                     [sg.Text('Clean:', tooltip=hT("helpcln"))],
                     [sg.Text('All Years:', tooltip=hT("helpalrstrts"))],
                     [sg.Text('Keep Restarts:', tooltip=hT("helpkprstrts"))]]
Dynamics_input    = [[sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='45.0', key='-PHY_TMESTPS-', s=6)],
                     [sg.Input(default_text='11520', key='-PHY_RUNSTPS-', s=6)],
                     [sg.Input(default_text='0', key='-PHY_SNPSHTS-', s=6)],
                     [sg.Input(default_text='160', key='-PHY_NSTPW-', s=6)],
                     [sg.Input(default_text='', key='-PHY_RSTRT_FLE-', s=20, disabled=True), sg.FileBrowse(key='-RSTRT_FLE_OPN-', disabled=True), sg.Checkbox('', default=False, enable_events=True, key='-TOG_RSTRT_FLE-')],
                     [sg.Combo(['None', 'Cesaro', 'Exp', 'Lh'], default_value='None', enable_events=True, key='-PHY_FLTR-')],
                     [sg.Combo(['None', 'GP', 'SP', 'GP+SP'], default_value='None', enable_events=True, key='-PHY_FLTR_APP-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_RUN_TO_BLNCE-')],
                     [sg.Input(default_text='100', key='-PHY_RUNTME-', s=6)],
                     [sg.Input(default_text='0.0005', key='-PHY_THRSHLD-', s=6, disabled=True)],
                     [sg.Input(default_text='10', key='-PHY_BSELNE-', s=6, disabled=True)],
                     [sg.Input(default_text='100', key='-PHY_MIN_YR-', s=6, disabled=True)],
                     [sg.Input(default_text='10', key='-PHY_MAX_YR-', s=6, disabled=True)],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_CRSH_IF_BRKN-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_CLN-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_ALL_YRS-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_KEEP_RSTS-')]]
Model_layout      = [[sg.Column(Sim_text), sg.Column(Sim_input), sg.Column(Dynamics_text), sg.Column(Dynamics_input)]]


StarOrbit_text    = [[sg.Text('Stellar Properties', font='Verdana 13 underline')],
                     [sg.Text('Star Temperature (K):', tooltip=hT("helpstrtmp"))],
                     [sg.Text('Stellar Flux (W/m²):', tooltip=hT("helpstlrflx"))],
                     [sg.Text('')],
                     [sg.Text('Orbital Properties', font='Verdana 13 underline')],
                     [sg.Text('Year Length (Earth Days):', tooltip=hT("helpyrlngth"))],
                     [sg.Text('Eccentricity:', tooltip=hT("helpeccentr"))],
                     [sg.Text('Obliquity (°):', tooltip=hT("helpoblqty"))],
                     [sg.Text('Longitude of Periapsis (°):', tooltip=hT("helplngpri"))],
                     [sg.Text('Fixed Orbit:', tooltip=hT("helpfxdobt"))],
                     [sg.Text('Keplerian Orbit:', tooltip=hT("helpkplrobt"))],
                     [sg.Text('Mean Anomaly:', tooltip=hT("helpmnanmly"))],
                     [sg.Text('')],
                     [sg.Text('Planet Properties', font='Verdana 13 underline')],
                     [sg.Text('Gravity (m/s²):', tooltip=hT("helpgrvty"))],
                     [sg.Text('Radius (Earth Radii):', tooltip=hT("helprdus"))],
                     [sg.Text('Day Length (Earth Days):', tooltip=hT("helpdaylngth"))],
                     [sg.Text('Tidally Locked:', tooltip=hT("helptdlkd"))],
                     [sg.Text('Substellar Longitude (°):', tooltip=hT("helpsbstlrlng"))],
                     [sg.Text('Substellar Desync (°/min):', tooltip=hT("helpsbstlrdsync"))],
                     [sg.Text('Temperature Contrast (K):', tooltip=hT("helptmpcntrst"))]]
StarOrbit_input   = [[sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='5772.0', key='-STR_TMP-', s=8)],
                     [sg.Input(default_text='1367.0', key='-STR_FLX-', s=8)],
                     [sg.Text('')],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='365.25', key='-OBT_LNGH-', s=8)],
                     [sg.Input(default_text='0.016715', key='-OBT_ECC-', s=8)],
                     [sg.Input(default_text='23.441', key='-OBT_OBLTY-', s=8)],
                     [sg.Input(default_text='102.7', key='-OBT_LOP-', s=8)],
                     [sg.Checkbox('', default=True, enable_events=True, key='-TOG_FXD_OBT-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_KPLR_OBT-')],
                     [sg.Input(default_text='358.617', key='-OBT_MNANMLY-', s=8, disabled=True)],
                     [sg.Text('')],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='9.80665', key='-PLNT_GRVTY-', s=8)],
                     [sg.Input(default_text='1.0', key='-PLNT_RDUS-', s=8)],
                     [sg.Input(default_text='1.0', key='-PLNT_DAY_LNGH-', s=8)],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_TDL_LCK-')],
                     [sg.Input(default_text='180.0', key='-PLNT_SUB_LONG-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-PLNT_SUB_DSNC-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-PLNT_TMP_CNST-', s=8, disabled=True)]]
Physics_layout  = [[sg.Column(StarOrbit_text), sg.Column(StarOrbit_input)]]


Heightmap_text    = [[sg.Text('Aqua Planet:', tooltip=hT("helpaquaplnt"))],
                     [sg.Text('Image/SRA:', tooltip=hT("helpimgsratog"))],
                     [sg.Text('Desert Planet:', tooltip=hT("helpdsrtplnt"))],
                     [sg.Text('', font='Verdana 12')],
                     [sg.Text('Heightmap Image:', tooltip=hT("helphghtmpimg"))],
                     [sg.Text('Water Threshold:', tooltip=hT("helpwtrthrshld"))],
                     [sg.Text('Highest Elevation (m):', tooltip=hT("helphghstelvtn"))],
                     [sg.Text('Lowest Elevation (m):', tooltip=hT("helplwstelvtn"))],
                     [sg.Text('', font='Verdana 16')],
                     [sg.Text('Image Debug:', tooltip=hT("helpimgdbg"))],
                     [sg.Text('SRA Name:', tooltip=hT("helpsranme"))],
                     [sg.Text('Land SRA:', tooltip=hT("helplndsra"))],
                     [sg.Text('Topographic SRA:', tooltip=hT("helptposra"))]]
Heightmap_input   = [[sg.Checkbox('', default=False, enable_events=True, key='-TOG_PLT_AQA-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_IMG_SRA-'), sg.Text('Image Mode', enable_events=True, key='-DIS_IMG_SRA-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_PLT_DST-')],
                     [sg.Text('', font='Verdana 0')],
                     [sg.Input(default_text='', key='-HGHTMP_IMG_FLE-'), sg.FileBrowse(key='-HGHTMP_IMG_OPN-')],
                     [sg.Input(default_text='0', key='-HGHTMP_WTR_TRSHLD-', s=8)],
                     [sg.Input(default_text='8849.0', key='-HGHTMP_ELE_HGH-', s=8)],
                     [sg.Input(default_text='-11034.0', key='-HGHTMP_ELE_LOW-', s=8)],
                     [sg.Text('', font='Verdana 3')],
                     [sg.Checkbox('', default=False, enable_events=True, expand_y=True, key='-TOG_IMG_DBG-')],
                     [sg.Input(default_text='earth', key='-HGHTMP_SRA_NME-', s=8)],
                     [sg.Input(default_text='', key='-HGHTMP_LAND_SRA-', disabled=True), sg.FileBrowse(key='-LAND_SRA_OPN-', disabled=True)],
                     [sg.Input(default_text='', key='-HGHTMP_TOPO_SRA-', disabled=True), sg.FileBrowse(key='-TOPO_SRA_OPN-', disabled=True)]]
Heightmap_layout  = [[sg.Column(Heightmap_text), sg.Column(Heightmap_input)]]


Terrain_text      = [[sg.Text('Soil Properties', font='Verdana 13 underline')],
                     [sg.Text('Wet Soil:', tooltip=hT("helpwtsl"))],
                     [sg.Text('Soil Albedo:', tooltip=hT("helpslalbdo"))],
                     [sg.Text('Soil Depth (m):', tooltip=hT("helpsldpth"))],
                     [sg.Text('Soil Heat Capacity:', tooltip=hT("helpslhtcpsty"))],
                     [sg.Text('Soil Water Capacity:', tooltip=hT("helpslwtrcpsty"))],
                     [sg.Text('Soil Saturation:', tooltip=hT("helpslstrtn"))],
                     [sg.Text('')],
                     [sg.Text('Snow/Ocean Properties', font='Verdana 13 underline')],
                     [sg.Text('Snow Albedo:', tooltip=hT("helpsnwalb"))],
                     [sg.Text('Max Snow (m):', tooltip=hT("helpmxsnw"))],
                     [sg.Text('Sea Ice:', tooltip=hT("helpseaice"))],
                     [sg.Text('Ocean Albedo:', tooltip=hT("helpocnalb"))],
                     [sg.Text('Mixed Layer Depth (m):', tooltip=hT("helpmxdlyrdpth"))],
                     [sg.Text('Ocean Zenith:', tooltip=hT("helpocnznth"))],
                     [sg.Text('')],
                     [sg.Text('Glacier Properties', font='Verdana 13 underline')],
                     [sg.Text('Glaciers:', tooltip=hT("helpglcrs"))],
                     [sg.Text('Height (m):', tooltip=hT("helpgrhght"))],
                     [sg.Text('Threshold (m):', tooltip=hT("helpgrthrshld"))]]
Terrain_input     = [[sg.Text('', font='Verdana 13')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_WET-')],
                     [sg.Input(default_text='0.0', s=5, disabled=True, key='-SOIL_ALB-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_ALB-')],
                     [sg.Input(default_text='12.4', s=5, disabled=True, key='-SOIL_DPTH-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_DPTH-')],
                     [sg.Input(default_text='2.4', s=5, disabled=True, key='-SOIL_HCAP-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_HCAP-')],
                     [sg.Input(default_text='0.5', s=5, disabled=True, key='-SOIL_WCAP-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_WCAP-')],
                     [sg.Input(default_text='0.0', s=5, disabled=True, key='-SOIL_SAT-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SOIL_SAT-')],
                     [sg.Text('')],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='0.0', s=5, disabled=True, key='-SNW_ALB-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_SNW_ALB-')],
                     [sg.Input(default_text='5.0', s=5, disabled=True, key='-MAX_SNW-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_MAX_SNW-')],
                     [sg.Checkbox('', default=True, enable_events=True, key='-TOG_SEA_ICE-')],
                     [sg.Input(default_text='0.0', s=5, disabled=True, key='-OCN_ALB-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_OCN_ALB-')],
                     [sg.Input(default_text='50.0', s=5, disabled=True, key='-OCN_MLD-'), sg.Checkbox('', default=False, enable_events=True, key='-TOG_OCN_MLD-')],
                     [sg.Combo(['Lambertian', 'uniform', 'ECHAM-3', 'plasim', 'default', 'ECHAM-6'], default_value='ECHAM-3', enable_events=True, key='-TOG_OCN_ZEN-')],
                     [sg.Text('')],
                     [sg.Text('', font='Verdana 8')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_GLCR-')],
                     [sg.Input(default_text='0.0', key='-GLCR_HGT-', s=5, disabled=True)],
                     [sg.Input(default_text='2.0', key='-GLCR_TRSHLD-', s=5, disabled=True)]]
Vegetation_text   = [[sg.Text('Vegetation Properties', font='Verdana 13 underline')],
                     [sg.Text('Vegetation Type:', tooltip=hT("helpvgtn"))],
                     [sg.Text('Vegetation Acceleration:', tooltip=hT("helpvgaclrtn"))],
                     [sg.Text('Biomass Growth:', tooltip=hT("helpbiomsgrwth"))],
                     [sg.Text('Initial Growth:', tooltip=hT("helpintlgrth"))],
                     [sg.Text('Stomatal Conductance:', tooltip=hT("helpstmtlcndtnce"))],
                     [sg.Text('Vegetation Roughness:', tooltip=hT("helpvgtnrghns"))],
                     [sg.Text('Soil Carbon Content:', tooltip=hT("helpslcbncntnt"))],
                     [sg.Text('Plant Carbon Content:', tooltip=hT("helplntcbncntnt"))]]
Vegetation_input  = [[sg.Text('', font='Verdana 13')],
                     [sg.Combo(['None', 'Proscribed', 'Dynamic'], default_value='None', enable_events=True, key='-TOG_VEG_TYPE-')],
                     [sg.Input(default_text='1', key='-VEG_ACC-', s=5, disabled=True)],
                     [sg.Input(default_text='1.0', key='-VEG_BIOM_GRTH-', s=5, disabled=True)],
                     [sg.Input(default_text='0.5', key='-VEG_INIT_GRTH-', s=5, disabled=True)],
                     [sg.Input(default_text='1.0', key='-VEG_STOM_C-', s=5, disabled=True)],
                     [sg.Input(default_text='2.0', key='-VEG_RGH-', s=5, disabled=True)],
                     [sg.Input(default_text='0.0', key='-VEG_SCC-', s=5, disabled=True)],
                     [sg.Input(default_text='0.0', key='-VEG_PCC-', s=5, disabled=True)]]
Terrain_layout    = [[sg.Column(Terrain_text), sg.Column(Terrain_input), sg.Column(Vegetation_text), sg.Column(Vegetation_input)]]


Atmosphere_text   = [[sg.Text('Atmospheric Properties', font='Verdana 13 underline')],
                     [sg.Text('Pressure:', tooltip=hT("helprsure"))],
                     [sg.Text('Gas Constant:', tooltip=hT("helpgscnstnt"))],
                     [sg.Text('Dry Core:', tooltip=hT("helpdrycre"))],
                     [sg.Text('Ozone:', tooltip=hT("helpozne"))],
                     [sg.Text('Gas Pressure:', tooltip=hT("helpgsprsurs"))],
                     [sg.Text('H2:')],
                     [sg.Text('He:')],
                     [sg.Text('N2:')],
                     [sg.Text('O2:')],
                     [sg.Text('Ar:')],
                     [sg.Text('Ne:')],
                     [sg.Text('Kr:')],
                     [sg.Text('H2O:')],
                     [sg.Text('CO2:')],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Text('Aerosol Properties', font='Verdana 13 underline')],
                     [sg.Text('Aerosols:', tooltip=hT("helparsls"))],
                     [sg.Text('Bulk Atmosphere:', tooltip=hT("helpblkatm"))],
                     [sg.Text('Aerosol Type:', tooltip=hT("helparsltype"))],
                     [sg.Text('Aerosol Density:', tooltip=hT("helparsldnsty"))],
                     [sg.Text('Aerosol Mass Mixing Ratio:', tooltip=hT("helparslmmr"))],
                     [sg.Text('Aerosol Particle Radius:', tooltip=hT("helparslrdus"))]]
Atmosphere_input  = [[sg.Text('', font='Verdana 13')],
                     [sg.Input(default_text='1.0', key='-BLK_PR-', s=8, disabled=True), sg.Checkbox('', default=False, enable_events=True, key='-TOG_BLK_PR-')],
                     [sg.Input(default_text='287.0', key='-GAS_CNST-', s=8, disabled=True), sg.Checkbox('', default=False, enable_events=True, key='-TOG_GAS_CNST-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_DRY_CRE-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_OZNE-')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_GAS_PR-')],
                     [sg.Input(default_text='0.0', key='-ATM_H2-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-ATM_HE-', s=8, disabled=True)],
                     [sg.Input(default_text='0.7809', key='-ATM_N2-', s=8, disabled=True)],
                     [sg.Input(default_text='0.2095', key='-ATM_O2-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0093', key='-ATM_AR-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-ATM_NE-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-ATM_KR-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0', key='-ATM_H2O-', s=8, disabled=True)],
                     [sg.Input(default_text='0.0003', key='-ATM_CO2-', s=8, disabled=True)],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Text('', font='Verdana 13')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_ARSLS-')],
                     [sg.Combo(['N2', 'H2', 'CO2'], default_value='N2', enable_events=True, disabled=True, key='-TOG_BLK_ATM-')],
                     [sg.Combo(['Photochemical', 'Dust'], default_value='Photochemical', enable_events=True, disabled=True, key='-TOG_ARSL_TYPE-')],
                     [sg.Input(default_text='1000.0', key='-ARSL_DNSTY-', s=8, disabled=True)],
                     [sg.Input(default_text='1e-12', key='-ARSL_MS_MX_RTO-', s=8, disabled=True)],
                     [sg.Input(default_text='5e-09', key='-ARSL_RDUS-', s=8, disabled=True)]]
Weather_text      = [[sg.Text('Storm Properties', font='Verdana 13 underline')],
                     [sg.Text('Storm Climatology:', tooltip=hT("helpstmclmtlgy"))],
                     [sg.Text('High Cadence:', tooltip=hT("helphghcdnce"))],
                     [sg.Text('HC Start:', tooltip=hT("helphghcdncestrt"))],
                     [sg.Text('HC End:', tooltip=hT("helphghcdnceend"))],
                     [sg.Text('HC Interval:', tooltip=hT("helphghcdnceintrvl"))],
                     [sg.Text('Storm Capture:', tooltip=hT("helpstmcptre"))],
                     [sg.Text('Hurricane Cyclogenesis:', tooltip=hT("helphrcnegns"))],
                     [sg.Text('Min Surface Temp.:', tooltip=hT("helpminsfcetmp"))],
                     [sg.Text('Max Surface Temp.:', tooltip=hT("helpmaxsfcetmp"))],
                     [sg.Text('Min Surface Windspeed:', tooltip=hT("helpminsfcews"))],
                     [sg.Text('Min Cell Count:', tooltip=hT("helpmincelcount"))],
                     [sg.Text('Final Cell Count:', tooltip=hT("helpfnlcelcount"))],
                     [sg.Text('Genesis Potential Index:', tooltip=hT("helpgpithrshld"))],
                     [sg.Text('Max Potential Intensity:', tooltip=hT("helpmpithrshld"))],
                     [sg.Text('Low Atm. Max Wind:', tooltip=hT("helplamwthrshld"))],
                     [sg.Text('Ventilation Index:', tooltip=hT("helpvntidxthrshld"))],
                     [sg.Text('Min Timesteps:', tooltip=hT("helpmintmestps"))],
                     [sg.Text('Max Timesteps:', tooltip=hT("helpmaxtmestps"))],
                     [sg.Text('Vent-Reduced Max Intensity:', tooltip=hT("helpvrmithrshld"))],
                     [sg.Text('Low Atm. Vorticity:', tooltip=hT("helplmvthrshld"))]]
Weather_input     = [[sg.Text('', font='Verdana 13')],
                     [sg.Checkbox('', default=False, enable_events=True, key='-TOG_STRM_CLIM-')],
                     [sg.Checkbox('', default=False, disabled=True, enable_events=True, key='-TOG_HGH_CDNCE-')],
                     [sg.Input(default_text='320', key='-HGH_CDNCE_STRT-', s=8, disabled=True)],
                     [sg.Input(default_text='576', key='-HGH_CDNCE_END-', s=8, disabled=True)],
                     [sg.Input(default_text='4', key='-HGH_CDNCE_INTRVL-', s=8, disabled=True)],
                     [sg.Checkbox('', default=False, disabled=True, enable_events=True, key='-TOG_STM_CPTRE-')],
                     [sg.Checkbox('', default=False, disabled=True, enable_events=True, key='-TOG_HRCNE-')],
                     [sg.Input(default_text='298.15', key='-STM_MIN_TEMP-', s=8, disabled=True)],
                     [sg.Input(default_text='373.15', key='-STM_MAX_TEMP-', s=8, disabled=True)],
                     [sg.Input(default_text='20.5', key='-STM_MIN_WIND-', s=8, disabled=True)],
                     [sg.Input(default_text='30', key='-STM_MIN_CLCT-', s=8, disabled=True)],
                     [sg.Input(default_text='16', key='-STM_FIN_CLCT-', s=8, disabled=True)],
                     [sg.Input(default_text='0.37', key='-STM_GPI-', s=8, disabled=True)],
                     [sg.Input(default_text='33.0', key='-STM_MPI-', s=8, disabled=True)],
                     [sg.Input(default_text='33.0', key='-STM_LATM_MAX_WIND-', s=8, disabled=True)],
                     [sg.Input(default_text='0.145', key='-STM_VNT_IDX-', s=8, disabled=True)],
                     [sg.Input(default_text='256', key='-STM_MIN_TMESTPS-', s=8, disabled=True)],
                     [sg.Input(default_text='1024', key='-STM_MAX_TMESTPS-', s=8, disabled=True)],
                     [sg.Input(default_text='0.577', key='-STM_VRMI-', s=8, disabled=True)],
                     [sg.Input(default_text='0.000012', key='-STM_LAV-', s=8, disabled=True)]]
AtmospherePlus_layout    = [[sg.Column(Atmosphere_text), sg.Column(Atmosphere_input), sg.Column(Weather_text), sg.Column(Weather_input)]]

menu_def = [['&File', ['&Import', ['Import BICEPS (.ini)', 'Heightmap (.png, .jpg)'], '&Export', ['Export BICEPS (.ini)', 'EPS File (.py)', 'SRA files (.sra)'], '---', '&Compatability Check', '---', '&Options', 'E&xit']],
            ['&Help', ['!&About...']]]

layout = [[sg.Menu(menu_def, tearoff=False, font='Verdana 14', key='-MENU-')],
          [sg.TabGroup([[sg.Tab("Model", Model_layout),
                         sg.Tab("Physics", Physics_layout),
                         sg.Tab("Heightmap", Heightmap_layout),
                         sg.Tab("Geography", Terrain_layout),
                         sg.Tab("Atmosphere+", AtmospherePlus_layout)]], font='Verdana 14 bold underline')]]

window = sg.Window('Basic Input Config for ExoPlaSim (BICEPS) v1.0.0', layout, font=font, enable_close_attempted_event=True, resizable=False, icon =str(Pth.cwd())+"/BICEPS.ico")
while True: #While Open
    event, values = window.read()
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Are you sure?') == 'Yes':
        system('cls' if name == 'nt' else 'clear')
        break

#Non-Exit Events
    match event:
        case 'Compatability Check': system_check()
        case 'Options': sg.main_global_pysimplegui_settings()
        case 'Import BICEPS (.ini)':
            import_BICEPS_path = sg.popup_get_file("Import File", no_window=True, default_extension=".ini", file_types=[("BICEPS Files", "*.ini")])
            load_ini(import_BICEPS_path)
        case 'Heightmap (.png, .jpg)':
            import_heightmap_path = sg.popup_get_file("Import File", no_window=True, default_extension=".png", file_types=[("PNG Files", "*.png"), ("JPG Files", "*.jpg")])
            open_heightmap(import_heightmap_path)
        case 'Export BICEPS (.ini)':
            export_BICEPS_path = sg.popup_get_file("Export File", no_window=True, save_as=True, default_extension=".ini", file_types=[("BICEPS Files", "*.ini")])
            save_ini(export_BICEPS_path)
        case 'EPS File (.py)':
            export_py_path = sg.popup_get_file("Export File", no_window=True, save_as=True, default_extension=".py", file_types=[("Python Files", "*.py")])
            save_file(export_py_path)
        case 'SRA files (.sra)': save_sra()
        case '-TOG_RSTRT_FLE-': rstrtfletoggle()
        case '-TOG_STRM_CLIM-': stmtoggle()
        case '-TOG_HGH_CDNCE-': hghcdncetoggle()
        case '-TOG_STM_CPTRE-': stmcptretoggle()
        case '-TOG_RUN_TO_BLNCE-': baltoggle ()
        case '-TOG_KPLR_OBT-': keplertoggle()
        case '-TOG_TDL_LCK-': tidaltoggle()
        case '-TOG_BLK_PR-': pressuretoggle()
        case '-TOG_GAS_CNST-': gascontoggle()
        case '-TOG_GAS_PR-': ptoggle()
        case '-TOG_ARSLS-': arsltoggle()
        case '-TOG_PLT_AQA-': aquatoggle()
        case '-TOG_IMG_SRA-': imgsratoggle()
        case '-TOG_PLT_DST-': dsrtoggle()
        case '-TOG_SOIL_ALB-': soilalbtoggle()
        case '-TOG_SOIL_DPTH-': soildepthtoggle()
        case '-TOG_SOIL_HCAP-': capsoiltoggle()
        case '-TOG_SOIL_WCAP-': soilwcptoggle()
        case '-TOG_SOIL_SAT-': soilsattoggle()
        case '-TOG_SNW_ALB-': snowalbtoggle()
        case '-TOG_MAX_SNW-': mxsnowtoggle()
        case '-TOG_OCN_ALB-': oceanalbtoggle()
        case '-TOG_OCN_MLD-': mldepthtoggle()
        case '-TOG_GLCR-': gtoggle()
        case '-TOG_VEG_TYPE-': vegtoggle()

window.close()
