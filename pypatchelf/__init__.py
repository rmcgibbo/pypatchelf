import os.path

__all__ = ['patchelf']

patchelf = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'patchelf')
