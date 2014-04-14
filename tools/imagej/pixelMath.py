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
    infile = sys.argv[1]
    expression = sys.argv[2]
    value = sys.argv[3]
    outfile = sys.argv[4]       
     
    premacro = """
        f=getArgument();
        print (f);
        f= split(f);
        open (f[0]);
        """        
    code = """
		run('"""+expression+"""', 'value="""+value+"""');
		"""
    #print code    
    postmacro = """
        saveAs('Tiff', f[1]);
        tif = getInfo('image.directory')+getInfo('image.filename');
        dat = replace(f[1], '.tif','.dat');
        done = File.rename(tif,dat);"
        close();
        """
    code = premacro+code+postmacro
     
    out = open( "galaxymacro.ijm", 'w' )
    out.write(code)
    out.close()
    command = "java -jar ~/galaxy-dist/tools/imagej/ij.jar -batch '" + os.getcwd() +"/galaxymacro.ijm"+ "' '" + infile + " "+ outfile + "' "
    #print command
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
     
    #print "Successfully applied maro code !"
    #print code
if __name__ == "__main__" : __main__()
