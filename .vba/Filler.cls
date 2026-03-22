VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Filler"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit
'my idea is just to create a class that can fill one with what ever i want

Public withHeader As Boolean
Private plength As Integer
Private defaultValue As Variant
Public table As range


Private Sub Class_Initialize()
    plength = 0
    defaultValue = "Never give in "
End Sub
Private Sub Handler(Optional txt As String)
    MsgBox "An error has occured " & txt, 4, "Error"
End Sub
Private Function verifyer() As VbMsgBoxResult
    verifyer = MsgBox("Are you sure you want to continue?", 3, "Verify")
End Function

Public Sub fill(Optional v As Variant)
    On Error GoTo Handler
    
    If IsMissing(Me.table) Then Exit Sub
    If IsMissing(v) Then
        v = Me.defaultValue
    End If
    If verifyer() = vbNo Then Exit Sub
    
    With Me.table
        .value = v
    End With
    
End Sub

Public Property Get length() As Integer
        length = plength
End Property
