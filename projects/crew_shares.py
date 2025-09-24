# TH Crew Shares Project

cash = float(input("How much money did the crew collect(dont put a dollar sign)? "))
members = int(input("How many crew members are there (not including captian and first mate)? "))
one_share = cash / (members + 10)
if one_share - 500 < 0:
    print(f"The captian gets: ${one_share * 7:.2f}")
    print(f"The first mate gets: ${one_share * 3:.2f}")
    print("The crew members indivdually each get: $0")
else:
    print(f"The captian gets: ${one_share * 7:.2f}")
    print(f"The first mate gets: ${one_share * 3:.2f}")
    print(f"The crew members indivdually each get: {one_share - 500:.2f}")