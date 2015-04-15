'''
Rename multiple files in a folder
'''
import os

prank_dir = './prank'

def rename_files():
    """Renames multiple files in a folder
    """
    prank_files = os.listdir(prank_dir)
    cur_dir = os.curdir
    os.chdir(prank_dir)

    for prank_file in prank_files:
        new_file = prank_file
        new_file = prank_file.translate( None, '0123456789' )
        os.rename(prank_file, new_file)
        print(' '.join(['Renamed', prank_file, 'to', new_file]))
    
    os.chdir(cur_dir)

rename_files()
