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
Public ok As Boolean
Public table As range


Private Sub Class_Initialize()
    plength = 0
    defaultValue = "Never give in "
    Me.ok = False
End Sub
Private Sub Handler(Optional txt As String)
    MsgBox "An error has occured: " & txt, vbCritical, "Error"
End Sub


Public Sub fill(Optional v As Variant)
    On Error GoTo Catch
    
    If Me.table Is Nothing Then Exit Sub
    
    If IsMissing(v) Then
        v = defaultValue
    End If
    
    Me.table.value = v
    
    Me.ok = True
    
    Exit Sub
Catch:
    Handler Err.Description
End Sub


Public Property Get length() As Integer
        length = plength
End Property
