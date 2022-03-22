import shutil
import win32com.client as win32
import pandas as pd
from datetime import datetime as dt
excel = pd.read_excel(r"C:/Temp/명단.xlsx")
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")

shutil.copyfile(r"C:/Temp/원본.hwp", r"C:/Temp/완료.hwp")

hwp.Open(r"C:/Temp/완료.hwp")

field_list = [i for i in hwp.GetFieldList().split("\x02")]
hwp.Run('SelectAll')
hwp.Run('Copy')
hwp.MovePos(3)

for i in range(len(excel)-1):
    hwp.Run('Paste')
    hwp.MovePos(3)

for page in range(len(excel)):
    for field in field_list:
        hwp.MoveToField(f'{field}{{{{{page}}}}}')
        hwp.PutFieldText(f'{field}{{{{{page}}}}}',
                        excel[field].iloc[page])

hwp.Save()
hwp.Quit()
