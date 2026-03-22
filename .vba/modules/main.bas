Attribute VB_Name = "main"
'this only fill the table with a value
Public Sub main2()
    Dim mcl  As CellFormat
    Dim tst As Testing
    Set tst = New Testing
    'tst.name = "Craice"
    tst.age = 19
    tst.greet
    MsgBox tst.version
End Sub

Private Function verifyer() As VbMsgBoxResult
    verifyer = MsgBox("Are you sure you want to continue?", 3, "Verify")
End Function

Public Sub main()
    Dim f As Filler
    Dim f2 As Filler
    Dim txt As String
    Dim selector As range
    
    If verifyer() = vbNo Then Exit Sub
    
    txt = "learning something new every day"
    Set selector = Selection

    Set f = New Filler
    Set f2 = New Filler
    
    Set f.table = range("D2:D10")
    Set f2.table = Cells(1, 4)

    f.fill "Konosuba is the best comedy anime!"
    
  ' If Not f.ok And Not f2.ok Then Exit Sub
    
   
    With f2.table
        .Interior.Color = vbBlack
        .ColumnWidth = 120
        .Font.Color = vbWhite
        .Font.Bold = True
        .Font.Size = 45
        .Font.Italic = True
        .Font.name = "Elephant"
        .Font.Underline = True
        .Select
    End With
    
    range("D1:D11").Select
    
    With selector
        .HorizontalAlignment = xlCenter
    End With
    
    With selector.Borders(xlEdgeBottom)
        .LineStyle = xlContinuous
        .Weight = xlThick
        .Color = RGB(255, 0, 0)
    End With
    
    
    
    
End Sub


