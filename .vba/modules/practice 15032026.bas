Attribute VB_Name ="MODULE4"
Option Explicit
Public Sub main()
    On Error GoTo Handle
        Dim answer As VbMsgBoxResult
        Dim mrange As range
        Set mrange = range("B12")
      


        'this is just a simple attmpt i guess
        answer = MsgBox("do yo like this ", 3, "Creating macro")
        
        If answer = vbYes And mrange.Value = "" Then
            With mrange
            .Value = "The square is " & square(10, 2)
            .Font.Bold = True
            .Font.Size = 25
            End With
        Else
            mrange.Value = ""
        End If
        
        Exit Sub
Handle:
        MsgBox ("why i keep screwing things up")
End Sub

'This function will let us combine two number in multiply it by itselt of another number
Function square(value1 As Integer, Optional value2 As Variant) As Integer
    Dim result As Integer
    
    If IsMissing(value2) Then
        result = value1 * value1
    Else
        result = value1 * value2
    End If
    'return statemnt
    square = result
End Function


