#!/usr/bin/env python
# coding: utf-8

# In[2]:


def remove_nested_files_by_ext(directory, file_ext):
#     directory should be pathlib Path variable formatted as Path("string"),
#     for windows: ex: directory = Path(r"C:\Users\root\Calibre Library")
#     file_ext argument should be extention formated as string.
#     ex: ".epub" or ".mp3"
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith((file_ext)):
                os.remove(filepath)

