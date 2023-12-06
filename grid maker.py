import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Your input string
input_string = "AIYNAGKRCTELUOISGAEELLSONOKONSNAAOTOWDSMSEAATOEPNCEDTLVUNTRLIDDTHHEPTEFAIADGOSWREMUIREINMOUSRSGSIEHNYARSRESNORROEDRELEONPESEEHUAEMAIOCRBRMEIISFELTNIRTEYLVAOTTTESROTRNWAOIQIIKNEANTOAETNTTIEOETNTFUNIDFEETMSRTMHEOCDIEEAYECYFIOHESAPECNRLDWDNSIILNTGEIOAADSEEBSEDOUASLITRTESROSOSTALEEIAYAGLNYOESOEAROOAMEOSNISGAIAHALNSTECITTEUCDRSIWLGMNITEMPENNEDWVUFYLLSNVYRDEEELTRTALODPISSDPRSNTYLASEDEPTRPODNCICBNARNAYHSPOAALVYLEOARRDILNSSYIIECOADEUEETEAPADSAPBREPOLSTIFLECCIVERSAEDOOCWRSGOOEUENNOCLQEFEESNRRCARDQOSAACRRPLNIEHSTEBEMTERSDNLYATREOTNMERTNELNLAIUITFEENTGIFLISWDENCMSE"  # You can modify this string as needed
input_string = input_string.strip(" ")
# Initialize variables for row and column indices
current_row = 1
current_col = 1

# Iterate through the characters of the input string
for char in input_string:
    # Set the current cell value to the current character
    sheet.cell(row=current_row, column=current_col, value=char)

    # Move to the next column
    current_col += 1

    # Move to the next row if the current column exceeds 80
    if current_col > 80:
        current_col = 1
        current_row += 1

        # Break the loop if we reach more than 7 rows
        if current_row > 7:
            break

# Save the workbook to a file
workbook.save("grid_with_string.xlsx")