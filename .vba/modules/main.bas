Attribute VB_Name = "Main"
Option Explicit

Public Function youcan() As String
    youcan = "Everything is useful no matter how hard it would be "
End Function
Public Function add(a As Integer, b As Integer) As Integer
    add = a + b
End Function

Public Function findheader(table As Range, data As Variant) As Variant
    Dim foundCell As Range
    Dim v As Range
    
    Set foundCell = table.Find(what:=data, LookIn:=xlValues, lookat:=xlWhole)
    
    
    If foundCell Is Nothing Then
        findheader = ""
        Exit Function
    End If
    
    ' Fix 4: Corrected the typo from "fondcell" to "foundcell"
    findheader = Cells(1, foundCell.Column).Value
End Function

Public Function findheaderindata(table1 As Range, table2 As Range) As String
    Dim v As Range
    Dim result As New Collection
    Dim a As Variant
    

    For Each v In table2
         a = findheader(data:=v, table:=table1)
         If a <> "" Then
            result.add a
         End If
    Next v
    
    findheaderindata = result.Item & ""
End Function



