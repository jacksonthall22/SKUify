Function SKUify(title As String) As String
    ' Create a seller SKU from the alphanumeric characters in the Amazon product title.
    ' Thanks ChatGPT!

    Dim maxSkuLength As Integer
    maxSkuLength = 40 ' Define the maximum length for the SKU

    ' Replace non-breaking spaces with regular spaces
    title = Replace(title, Chr(160), " ")
    title = Replace(title, "-", " ")

    ' Remove special characters except spaces, numbers, and alphabets
    Dim cleanTitle As String
    cleanTitle = ""
    Dim i As Integer
    For i = 1 To Len(title)
        Dim character As String
        character = Mid(title, i, 1)
        If IsNumeric(character) Or (Asc(UCase(character)) >= 65 And Asc(UCase(character)) <= 90) Or character = " " Then
            cleanTitle = cleanTitle & LCase(character)
        End If
    Next i

    ' Remove duplicate whitespaces and hyphens, then limit to 40 characters
    cleanTitle = Application.WorksheetFunction.Trim(cleanTitle)
    cleanTitle = Replace(cleanTitle, "-", " ") ' Replace hyphens with spaces
    cleanTitle = Application.WorksheetFunction.Trim(cleanTitle) ' Trim spaces again

    ' Amazon SKUs are limited to 40 characters.
    ' Join words on '-' and return the first 40 chars.
    Dim words() As String
    words = Split(cleanTitle, " ")
    Dim sku As String
    sku = Join(words, "-")
    If Len(sku) > maxSkuLength Then
        SKUify = Left(sku, maxSkuLength)
    Else
        SKUify = sku
    End If
End Function
