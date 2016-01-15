from glob import glob
from os.path import dirname, abspath
from os.path import join as pjoin
import ctypes


def patchelf(filename, set_rpath=b''):
    matches = glob(pjoin(abspath(dirname(__file__)), 'bin', 'patchelf*'))
    assert len(matches) == 1
    h = ctypes.CDLL(matches[0])

    if isinstance(filename, str):
        filename = filename.encode('utf-8')
        
    L = [b'--set-rpath', set_rpath, filename]
    print(L)
    arr = (ctypes.c_char_p * len(L))()
    arr[:] = L
    h.main(len(L), arr)
    
    

patchelf(b'/home/rmcgibbo/projects/test-linkerstuff/libblas.so', set_rpath=b'$ORIGIN')
    
