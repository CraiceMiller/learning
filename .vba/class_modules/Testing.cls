VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Testing"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
Option Explicit
'this is my attempt of creating my very firts class in excel
rem creating on 22/03/2025


'these are properties
Private pversion As String
Private pname As String
Public age As Integer

'this is a class constructor
Private Sub Class_Initialize()
    pversion = "0.0.1"
End Sub

'this is a getter
Public Property Get version() As String
    version = pversion
End Property

' a getter,
Public Property Get name() As String
    name = Me.pname
End Property
' a setter,
Public Property Let name(ByVal name As String)
    If name = "" Then Exit Property
    Me.pname = name
End Property

Public Function greet()
    MsgBox "Hello I am " & Me.name
End Function


