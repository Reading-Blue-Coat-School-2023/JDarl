def insert_spaces(input_string, every_n):
    result = ""
    for i, char in enumerate(input_string):
        if i % every_n == 0 and i != 0:
            result += " "
        result += char
    return result

# Input string
input_string = "PLEASECONFIRMDATEYOURAGENTISLESARRIVINGNEWYORKWILLARRANGEACCOMMODATIONASREQUIREDLISTREQUIREDBOOKSMISSINGPLEASESENDAGAINSOCANENSURETHEYAREONDISPLAYWILLLEAVEINSTRUCTIONSFORENTRYATHOTELDESKISLESTOENSURENOONEOBSERVESENTRYTOMANORESTATEDATEOFDEPARTUREALSONEEDEDWILLSENDDETAILSFORPAYMENTBYASEPARATETELEGRAMSOPLEASEDONOTREPLYTOTHISONEMUSTEMPHASISENEEDFORCOMPLETECAREANDDISCRETIONCOLLECTIONVERYVALUABLEMANYRAREITEMSSOURCEEASILYIDENTIFIEDIFDISPOSEDOFTOGETHERCANHELPWITHSTORAGEANDSHIPPINGAFTERCOLLECTIONIFNECESSARYBUTWILLNEEDADVANCEDWARNINGDONOTCONTACTMSSTYLESWITHQUERIES"

# Insert a space every 5 characters
output_string = insert_spaces(input_string, 5)

# Print the result
print(output_string)