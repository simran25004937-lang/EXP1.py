# Case Study 1 - Branching Statements

# Player 1
runs1 = 148
balls1 = 50
wickets1 = 4
conceded1 = 29
overs1 = 2
catches1 = 3

sr1 = (runs1 / balls1) * 100
eco1 = conceded1 / overs1

if runs1 >= 50 and sr1 >= 120:
    bat1 = "Excellent Batter"
elif runs1 >= 30 and sr1 >= 100:
    bat1 = "Good Batter"
elif runs1 >= 20:
    bat1 = "Average Batter"
else:
    bat1 = "Poor Batter"

if wickets1 >= 3 and eco1 <= 6:
    bowl1 = "Excellent Bowler"
elif wickets1 >= 2 and eco1 <= 8:
    bowl1 = "Good Bowler"
elif wickets1 >= 1:
    bowl1 = "Average Bowler"
else:
    bowl1 = "Poor Bowler"

if catches1 >= 2:
    field1 = "Outstanding Fielder"
elif catches1 == 1:
    field1 = "Active Fielder"
else:
    field1 = "Needs Improvement"

if bat1 == "Excellent Batter" and bowl1 == "Excellent Bowler":
    overall1 = "Star All-Rounder"
elif bat1 == "Good Batter" and bowl1 == "Good Bowler":
    overall1 = "Strong All-Rounder"
elif bat1 == "Good Batter" or bowl1 == "Good Bowler":
    overall1 = "Supporting All-Rounder"
else:
    overall1 = "Needs Improvement"

print("Player 1")
print("Strike Rate:", sr1)
print("Economy Rate:", eco1)
print("Batting:", bat1)
print("Bowling:", bowl1)
print("Fielding:", field1)
print("Overall:", overall1)


# Player 2
runs2 = 179
balls2 = 62
wickets2 = 8
conceded2 = 32
overs2 = 3
catches2 = 2

sr2 = (runs2 / balls2) * 100
eco2 = conceded2 / overs2

if runs2 >= 50 and sr2 >= 120:
    bat2 = "Excellent Batter"
elif runs2 >= 30 and sr2 >= 100:
    bat2 = "Good Batter"
elif runs2 >= 20:
    bat2 = "Average Batter"
else:
    bat2 = "Poor Batter"

if wickets2 >= 3 and eco2 <= 6:
    bowl2 = "Excellent Bowler"
elif wickets2 >= 2 and eco2 <= 8:
    bowl2 = "Good Bowler"
elif wickets2 >= 1:
    bowl2 = "Average Bowler"
else:
    bowl2 = "Poor Bowler"

if catches2 >= 2:
    field2 = "Outstanding Fielder"
elif catches2 == 1:
    field2 = "Active Fielder"
else:
    field2 = "Needs Improvement"

if bat2 == "Excellent Batter" and bowl2 == "Excellent Bowler":
    overall2 = "Star All-Rounder"
elif bat2 == "Good Batter" and bowl2 == "Good Bowler":
    overall2 = "Strong All-Rounder"
elif bat2 == "Good Batter" or bowl2 == "Good Bowler":
    overall2 = "Supporting All-Rounder"
else:
    overall2 = "Needs Improvement"

print("Player 2")
print("Strike Rate:", sr2)
print("Economy Rate:", eco2)
print("Batting:", bat2)
print("Bowling:", bowl2)
print("Fielding:", field2)
print("Overall:", overall2)


# Player 3
runs3 = 156
balls3 = 59
wickets3 = 6
conceded3 = 29
overs3 = 4
catches3 = 2

sr3 = (runs3 / balls3) * 100
eco3 = conceded3 / overs3

if runs3 >= 50 and sr3 >= 120:
    bat3 = "Excellent Batter"
elif runs3 >= 30 and sr3 >= 100:
    bat3 = "Good Batter"
elif runs3 >= 20:
    bat3 = "Average Batter"
else:
    bat3 = "Poor Batter"

if wickets3 >= 3 and eco3 <= 6:
    bowl3 = "Excellent Bowler"
elif wickets3 >= 2 and eco3 <= 8:
    bowl3 = "Good Bowler"
elif wickets3 >= 1:
    bowl3 = "Average Bowler"
else:
    bowl3 = "Poor Bowler"

if catches3 >= 2:
    field3 = "Outstanding Fielder"
elif catches3 == 1:
    field3 = "Active Fielder"
else:
    field3 = "Needs Improvement"

if bat3 == "Excellent Batter" and bowl3 == "Excellent Bowler":
    overall3 = "Star All-Rounder"
elif bat3 == "Good Batter" and bowl3 == "Good Bowler":
    overall3 = "Strong All-Rounder"
elif bat3 == "Good Batter" or bowl3 == "Good Bowler":
    overall3 = "Supporting All-Rounder"
else:
    overall3 = "Needs Improvement"

print("Player 3")
print("Strike Rate:", sr3)
print("Economy Rate:", eco3)
print("Batting:", bat3)
print("Bowling:", bowl3)
print("Fielding:", field3)
print("Overall:", overall3)


# Player 4
runs4 = 117
balls4 = 41
wickets4 = 5
conceded4 = 31
overs4 = 3
catches4 = 2

sr4 = (runs4 / balls4) * 100
eco4 = conceded4 / overs4

if runs4 >= 50 and sr4 >= 120:
    bat4 = "Excellent Batter"
elif runs4 >= 30 and sr4 >= 100:
    bat4 = "Good Batter"
elif runs4 >= 20:
    bat4 = "Average Batter"
else:
    bat4 = "Poor Batter"

if wickets4 >= 3 and eco4 <= 6:
    bowl4 = "Excellent Bowler"
elif wickets4 >= 2 and eco4 <= 8:
    bowl4 = "Good Bowler"
elif wickets4 >= 1:
    bowl4 = "Average Bowler"
else:
    bowl4 = "Poor Bowler"

if catches4 >= 2:
    field4 = "Outstanding Fielder"
elif catches4 == 1:
    field4 = "Active Fielder"
else:
    field4 = "Needs Improvement"

if bat4 == "Excellent Batter" and bowl4 == "Excellent Bowler":
    overall4 = "Star All-Rounder"
elif bat4 == "Good Batter" and bowl4 == "Good Bowler":
    overall4 = "Strong All-Rounder"
elif bat4 == "Good Batter" or bowl4 == "Good Bowler":
    overall4 = "Supporting All-Rounder"
else:
    overall4 = "Needs Improvement"

print("Player 4")
print("Strike Rate:", sr4)
print("Economy Rate:", eco4)
print("Batting:", bat4)
print("Bowling:", bowl4)
print("Fielding:", field4)
print("Overall:", overall4)