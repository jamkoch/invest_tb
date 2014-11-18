import arcpy
import os
import ctypes

arcpy.env.workspace = "C:/tmp/invest/"
wksp = arcpy.env.workspace

desc = arcpy.Describe(wksp + "/data/water.shp")

try:
    desc.shapeType == "Polygon"
except:
    print "Make sure the watershead shapefile is a polygon."

wtr = arcpy.da.SearchCursor(wksp + "/water.shp", "HUC12")

for row in wtr:
    newpath = wksp + "/" + row[0]
    if not os.path.exists(newpath): os.makedirs(newpath)
    inpath = newpath + "/Input"
    os.makedirs(inpath)
    arcpy.CopyFeatures_management(row[0] ,inpath)
    os.makedirs(newpath + "/Output")

    kdll = ctypes.windll.LoadLibrary("kernel32.dll")
    for thing in rasterlist:
        kdll.CreateSymbolicLinkA(wksp + "\\data\\" + thing, inpath + "\\" + thing, 0)
    for thing in csvlist:
        kdll.CreateSymbolicLinkA(wksp + "\\data\\" + thing, inpath + "\\" + thing, 0)

del wtr