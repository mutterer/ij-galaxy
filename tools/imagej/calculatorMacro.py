#!/usr/bin/env python
"""
Input: a tif input image; some imagej macro code
Out: output image in tif format
"""
import sys, os, subprocess
 
assert sys.version_info[:2] >= ( 2, 4 )
 
def stop_err( msg ):
    sys.stderr.write( msg )
    sys.exit()
 
def __main__():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    opera = sys.argv[3]
    outfile = sys.argv[4]       
    #print outfile
    premacro = """
f=getArgument();f=split(f);
open (f[0]);rename('a');
open (f[1]); rename('b');
"""
    #print premacro
    macro = "imageCalculator('"+opera+" create ','a', 'b'); "
    postmacro = """
saveAs('Tiff', f[2]); 
dir = getInfo('image.directory');
tif=dir+getInfo('image.filename');
dat=replace(f[2], '.tif','.dat'); done=File.rename(tif,dat);
run ('Close All');
        """
    code = premacro+macro+postmacro 
    out = open( "galaxymacro.ijm", 'w' )
    out.write(code)
    out.close()
    params = '"'+file1+' '+file2+' '+outfile+'"'
    command = "java -jar ~/galaxy-dist/tools/imagej/ij.jar -batch '" + os.getcwd() +"/galaxymacro.ijm' "+ params
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    #print "Successfully applied maro code !"
    #print code
if __name__ == "__main__" : __main__()
