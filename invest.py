__author__ = 'mill1909'
import arcpy
from arcpy import env
env = "workspace here"

flist = "work folder"
rasterlist = []
csvlist = []

for f in flist:
    desc = arcpy.Describe(f)
    format = desc.format
    if format == ('BIL', 'BIP', 'BMP', 'BSQ', 'DAT', 'GIF', 'Grid', 'IMAGINE Image', 'JP2000', 'JPEG', 'PNG', 'TIFF'):
        rasterlist.append(f)
    elif format == '.csv':
        csvlist.append(f)

for raster in rasterlist:
    try:
        desc = arcpy.Describe(raster)
        format = desc.format
        if format == ('BIL', 'BIP', 'BMP', 'BSQ', 'DAT', 'GIF', 'Grid', 'IMAGINE Image', 'JP2000', 'JPEG', 'PNG', 'TIFF'):
            print '%s is the correct format' % raster.name
    except:
        print '%s is not a raster layer.' % raster.name

for csv in csvlist:
    try:
        desc = arcpy.Describe(csv)
        fields = desc.fields
        if fields[0] == 'LULC_desc' and fields[1] == 'lucode' and fields[2] == 'Kc' and fields[3] == 'root_depth' and fields[4] == 'load_n' and fields[5] == 'eff_n' and fields[6] == 'load_p' and fields[7] == 'eff_p':
            print '.csv table is correctly formatted.'
    except:
        print '.csv table is not correct.'

try:
    if rasterlist.len() == 6 and csvlist.len() == 1:
        print "It's all there."
except:
    print 'Files are missing.'

for raster in rasterlist:
    if raster.spatialReference != 'NAD 1983':
        arcpy.ProjectRaster_management(raster, 'output location.tif', 'NAD 1983')

