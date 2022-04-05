import os
import win32com.client as win32

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")

hwp.Run("FileNew")
hwp.Open(r"C:/Temp/보고서.hwp")

Path = r"C:/Temp/첨부파일"
AppendList = os.listdir(Path)
hwp.MovePos(3)

for i in AppendList:
    InsertDoc(os.path.join(Path, i))
    hwp.MovePos(3)

hwp.Quit()


def InsertDoc(path):
    hwp.HAction.GetDefault("InsertFile", hwp.HParameterSet.HinsertFile.HSet)
    hwp.HParameterSet.HInsertFile.filename = path
    hwp.HParameterSet.HInsertFile.KeepSection = 1
    hwp.HParameterSet.HInsertFile.KeepCharshape = 1
    hwp.HParameterSet.HInsertFile.KeepParashape = 1
    hwp.HParameterSet.HInsertFile.KeepStyle = 1
    hwp.HAction.Execute("IsertFile", hwp.HParameterSet.HinsertFile.Hset)
    
