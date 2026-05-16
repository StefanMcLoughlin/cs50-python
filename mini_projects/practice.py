alter = int(input("Wie alt bist Du? "))
if alter < 18:
    print("Du bist minderjährig")
elif alter < 65:
    print("Du bist erwachsen")
else:
    print("Du bist Rentner")
