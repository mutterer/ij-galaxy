#!/usr/bin/env python
"""
Input: a multi channel tif input image
Out: a ssingle channel as 32-bit
"""
import sys, os, subprocess

assert sys.version_info[:2] >= ( 2, 4 )

def stop_err( msg ):
    sys.stderr.write( msg )
    sys.exit()

def __main__():
    infile = sys.argv[1]
    channel = sys.argv[2]
    outfile = sys.argv[3]        
    
    code = """
		f=getArgument();
		print (f);
		f= split(f);
		open (f[0]);
		run ('Split Channels');
		id = getImageID;
		selectImage(id+(3-"""+channel+"""));
		
		saveAs('Tiff', f[1]);
		tif = getInfo('image.directory')+getInfo('image.filename');
		dat = replace(f[1], '.tif','.dat');
		done = File.rename(tif,dat);"
		close();
		"""
	
    out = open( "galaxymacro.ijm", 'w' )
    out.write(code)
    out.close()
    command = "java -jar ~/galaxy-dist/tools/imagej/ij.jar -batch '" + os.getcwd() +"/galaxymacro.ijm"+ "' '" + infile + " "+ outfile + "' "
    #print command
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    #print "Successfully applied maro code !"
    #print code
if __name__ == "__main__" : __main__()