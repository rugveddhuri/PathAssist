#!/usr/bin/env python

"""
Title: Python Library for Path Manipulation and Value Extraction
Date: 13 Aug 2023
"""

import os
import uuid

# Begin: Functions

def getFileExtension(file_path):
    """
    Title     : Get File Extension
    Parameter : Path (String)
    Dependency: None
    """
    substring = os.path.splitext(file_path)
    return substring[1].replace('.', '').lower()

def getFileName(file_path):
    """
    Title     : Get File Name
    Parameter : Path (String)
    Dependency: None
    """
    return os.path.basename(file_path)

def isFileExists(file_path):
    """
    Title     : Check if a file is available
    Parameter : Path (String)
    Dependency: None
    """
    if(os.path.exists(file_path)):
        if(os.path.isfile(file_path)):
            return True
    return False

def getParentDirName(file_path):
    """
    Title     : Get Parent Directory Name
    Parameter : Path (String)
    Dependency: None
    """
    return os.path.basename(os.path.dirname(file_path))

def getNewFileName(file_format):
    """
    Title     : Get Unique file name
    Parameter : file_format (String)
    Dependency: None
    """
    return str(uuid.uuid1()) + '.' + file_format.lower()

# End: Functions