#import os
from os import makedirs
from numpy import amax, min, max, reshape, array
from PIL import Image
import PySimpleGUI as sg
import numpy as np

def writeSRA(path,name,kcode,fmap,NLAT,NLON): #Format array and header into sra file, as well as saving it!
    """Write a lat-lon field to a formatted .sra file."""
    try: makedirs(path)
    except FileExistsError: pass #Directory already exists
    sra_label=path+name+'_surf_%04d.sra'%kcode
    sra_header=[kcode,0,11111111,0,NLON,NLAT,0,0]
    sheader = ''
    for h in sra_header: sheader+=" %9d"%h
    lines=[]
    i=0
    while i<NLAT*NLON/8:
        l=''
        for n in fmap[i,:]:
            l+=' %9.3f'%n
        lines.append(l)
        i+=1
    sra_text=sheader+'\n'+'\n'.join(lines)
    with open(sra_label, "w") as f:
        f.write(sra_text)
        f.close()

#               string,   string  float boolean     boolean         integer     float        float  String, see dict String
def convert_sra(filepath, infile, grav, debug_img, desert_planet, floor_value, peak_value, trench_value, resotext, sra_name):
    global chunked

    #Image setup
    sg.Print("Beginning Image -> SRA Conversion...", text_color='dark green')
    sra_path = str(filepath)+'/'

    #Find resolution
    options = {"T21": 32,"T42": 64,"T63": 96,"T85": 128,"T106": 160,"T127": 192,"T170": 256}
    if resotext in options:
        height = options[resotext]
        width = 2*height

    if debug_img: sg.Print("Debug Images Enabled...", text_color='dark green')
    
    in_file = Image.open(infile).convert('L')    #Opens Image as Greyscale
    im_resized = in_file.resize((width, height)) #Resizes Image to desired resolution
    im_resized = np.array(im_resized)            #Converts Image to numpy array

    img_width = len(im_resized[0])                 #finds image width
    img_height = len(im_resized)                   #finds image height

    msk_file = Image.open(infile).convert('L')   #Opens Image as Greyscale
    msk_file = in_file.point(lambda p: 0 if p == 0 else 255) #Converts to Land Mask
    msk_file = msk_file.resize((width, height))  #Resizes Image to desired resolution
    msk_file = np.array(msk_file)                #Converts Image to numpy array

    #altitude ranges
    if not desert_planet:
        greyscale_img = im_resized                   #converts 0-1 to 0-255
        max_img = amax(greyscale_img)-(floor_value)  #max value lowered by floor value
        rescaled_img = (greyscale_img-(floor_value)) #array lowered by floor value
        rescaled_img[rescaled_img <= 0] = 0          #any negative value becomes 0 (ocean)
        rescaled_img = (rescaled_img/max_img)*peak_value*grav       #array converted to 0-1, before multiplied by max height and gravity (geopotential)
    else:
        range_value = peak_value-trench_value
        rescaled_img = (((im_resized/255)*range_value)-trench_value)*grav #converts 0-1 to trench-peak times gravity (geopotential)

    #Debug image 1 generation
    if debug_img:
        img = in_file
        img = img.point(lambda p: 0 if p == 0 else 255)
        img.save(sra_path+"LandMaskOriginal.png")
        sg.Print("Debug Image 1 printed...", text_color='dark green')

    if not desert_planet: b_w = rescaled_img
    else: b_w = rescaled_img #simpler approach, since there's no ocean there's no need to check for it, so just average all the land to 1d list

    if debug_img:
        img = Image.fromarray(msk_file)   #print resized image
        img.save(sra_path+"LandMaskSmall.png")
        sg.Print("Debug Image 2 printed...", text_color='dark green')

    list_image = rescaled_img.flatten()             #Flattens 2d arrays into lists
    b_w = b_w.flatten()
    sra_129 = array(list_image).reshape(-1, 8)      #Rearranges list into 2d array that matches sra format
    sra_172 = array(b_w).reshape(-1, 8)

    if desert_planet: sra_172[:,:] = 1              #Everything becomes land

    fl_height = float(height)                       #Apparently it doesn't like integers
    fl_width = float(width)
    sra_final_path = sra_path+'SRA/'
    writeSRA(sra_final_path,sra_name,172,sra_172,fl_height,fl_width)
    writeSRA(sra_final_path,sra_name,129,sra_129,fl_height,fl_width)
    sg.Print("Conversion successful!", text_color='dark green') #Nice!
    landmaptext = 'landmap="SRA/'+sra_name+'_surf_0172.sra",'
    topomaptext = 'topomap="SRA/'+sra_name+'_surf_0129.sra",'
