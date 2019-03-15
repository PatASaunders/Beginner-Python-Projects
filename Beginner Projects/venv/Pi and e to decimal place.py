while True:
    try:
        dec_places = int(input("Please Enter a number up to 17, this number will determine to how many places pi and e shall be calculated"))
        if 0 <= dec_places <= 17:
            break
    except ValueError:
        continue
print("Please wait while pi and e are generated.")
multiplier=2
pi=3
pi_positives=0
pi_negatives=0
while multiplier <= 50000000:
    pi_pos_calc=4/(multiplier * (multiplier + 1) * (multiplier + 2))
    pi_neg_calc=4/((multiplier + 2) * (multiplier + 3) * (multiplier + 4))
    pi_positives=pi_positives+pi_pos_calc
    pi_negatives=pi_negatives+pi_neg_calc
    multiplier=multiplier + 4
e=(1+(1/multiplier))**multiplier
pi=3 + pi_positives - pi_negatives
print(round(pi,dec_places))
print(round(e,dec_places))