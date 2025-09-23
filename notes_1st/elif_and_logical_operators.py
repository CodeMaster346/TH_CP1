# TH 2nd elif and conditionals notes

homework = False
chores = False
room = False

if homework and chores and room:
    print("You can go to your friends house if you have done your chores.")
elif not chores or not room:
    print("go do your chores!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("go do youer homework!!!!!!!!!!!!!!!!!!!!!!!!")