from enum import Enum


# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price



test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# TODO: process each order

for order in test_orders:
    price = 0
    print("----------------------")
    for item in order:
        description = ""
        match item:
            case "shirt"|"pants"|"jacket"|"dress" as garment, "L"|"M"|"S" as size,\
             bool() as starch, bool() as same_day:
                price += 12.95
                if starch:
                    price += 2.00
                    description += "starch "
                if same_day:
                    price += 10.00
                    description += "same_day"
                print(f"Dry Cleaning: ({size}) {garment} {description}")
                
            case str() as desc, float() as weight:
                if weight >= 15:
                    price += 4.95 * weight * 0.9
                else:
                    price += 4.95 * weight
                print(f"Wash/fold: {desc}, {weight} lbs")

            case "comforter"|"cover" as item, bool() as dry_clean, "L" | "M" | "S" as size:
                if dry_clean:
                    description = "Dry clean"
                price += 25.00
                print(f"Blanket: ({size}) {item} {description} ")
            case _:
                print(f"{item}:Not recognized")

    print(f"Total price: {price:.2f}\n----------------------")
