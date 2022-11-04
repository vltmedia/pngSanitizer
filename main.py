import glob, os
import argparse
parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter,
                                    description= 'Santize PNGs in a folder for use in applications utilizing FFMPEG')
 
parser.add_argument("-i", "--input", metavar="INPUT", help = "Path to your images")
args = vars(parser.parse_args())
if args['input'] is not None:
    args['input'] = os.path.dirname(__file__)
files = glob.glob(args['input'] + "/*.png")

for file in files:
    tempfile = os.path.splitext(file)[0] + "_temp.png"
    command = ["ffmpeg", '-i', file, tempfile]
    
    #run ffmpeg command
    os.system(" ".join(command))
    
    # delete file
    os.remove(file)
    # rename tempfile to file name
    os.rename(tempfile, file)