# makes a pretty table and output
from rich.console import Console
from rich.table import Table
from rich.text import Text

# make all lists, each is a column in the final log table
l_flicker =[]
l_source = []
l_repeats = []
l_rabbits = []
l_copies = []
l_etbs = []

apparents = int(input("Current Number of Hare Apparents (NOT including copies): "))
illusions = int(input("Current Number of 0/1 Illusion copies: "))
amount = input("Are we flickering all Hare Apparents or just one? (All/1): ")
preston = input("Is Preston in play for copy generation? (T/F): ")
flicker = int(input("Amount of times to flicker: "))
hare_repeats = int(input("How many times is Hare Apparent's triggers being repeated?: "))
preston_repeats = int(input("How many times is Preston's trigger being repeated?: "))

rabbits = 0
copies = 0
etbs = 0
i = 0
j = 0
k = 0

# Order of Triggers
real_apparents = apparents
# Flicker X amount of times
while i < flicker:
# Hare Apparent leaves and enters X amount of times and repeated Y amount of times (if hare_repeats > 0)
    if amount == "All":
        if hare_repeats > 0:
            for j in range(hare_repeats+1):
                if j == min(range(hare_repeats+1)):
                    etbs += real_apparents
                    c_etbs = real_apparents

                    l_flicker.append("Flicker "+ str(i + 1))
                    if j==min(range(hare_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(j))
                    l_source.append("HA ETB")
                    l_rabbits.append("0")
                    l_copies.append("0")
                    l_etbs.append(str(c_etbs))
                else:
                    etbs += 0
                    c_etbs = 0

        else:
            etbs += real_apparents
            c_etbs = real_apparents

            l_flicker.append("Flicker "+ str(i + 1))
            if j==min(range(hare_repeats+1)):
                l_repeats.append("Original")
            else:
                l_repeats.append("Repeat "+ str(j))
            l_source.append("HA ETB")
            l_rabbits.append("0")
            l_copies.append("0")
            l_etbs.append(str(c_etbs))
    else:
        if hare_repeats > 0:
            for j in range(hare_repeats+1):
                if j == min(range(hare_repeats+1)):
                    etbs += 1
                    c_etbs = 1

                    l_flicker.append("Flicker "+ str(i + 1))
                    if j==min(range(hare_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(j))
                    l_source.append("HA ETB")
                    l_rabbits.append("0")
                    l_copies.append("0")
                    l_etbs.append(str(c_etbs))
                else:
                    etbs += 0
                    c_etbs = 0
        else:
            etbs += 1
            c_etbs = 1

            l_flicker.append("Flicker "+ str(i + 1))
            if j==min(range(hare_repeats+1)):
                l_repeats.append("Original")
            else:
                l_repeats.append("Repeat "+ str(j))
            l_source.append("HA ETB")
            l_rabbits.append("0")
            l_copies.append("0")
            l_etbs.append(str(c_etbs))

# Hare Apparent's ETB triggers X amount of times and repeated Y amount of times (if hare_repeats > 0)
    if amount == "All":
        if hare_repeats > 0:
            for j in range(hare_repeats+1):
                rabbits += (real_apparents) * (apparents + illusions - 1)
                c_rabbits = (real_apparents) * (apparents + illusions - 1)

                etbs += c_rabbits
                c_etbs = c_rabbits

                l_flicker.append("Flicker "+ str(i + 1))
                if j==min(range(hare_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(j))
                l_source.append("HA Trigger")
                l_rabbits.append(str(c_rabbits))
                l_copies.append("0")
                l_etbs.append(str(c_etbs))

            if preston == "T" and preston_repeats > 0:
                for k in range(preston_repeats+1):
                    copies += real_apparents
                    c_copies = real_apparents

                    etbs += c_copies
                    c_etbs = c_copies

                    l_flicker.append("Flicker "+ str(i + 1))
                    if k==min(range(preston_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(k))
                    l_source.append("P Trigger")
                    l_rabbits.append("0")
                    l_copies.append(str(c_copies))
                    l_etbs.append(str(c_etbs))
            elif preston == "T":
                copies += real_apparents
                c_copies = real_apparents

                etbs += c_copies
                c_etbs = c_copies

                l_flicker.append("Flicker "+ str(i + 1))
                if k==min(range(preston_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(k))
                l_source.append("P Trigger")
                l_rabbits.append("0")
                l_copies.append(str(c_copies))
                l_etbs.append(str(c_etbs))

        else:
            rabbits += (real_apparents) * (apparents + illusions - 1)
            c_rabbits = (real_apparents) * (apparents + illusions - 1)

            etbs += c_rabbits
            c_etbs = c_rabbits

            l_flicker.append("Flicker "+ str(i + 1))
            if j==min(range(hare_repeats+1)):
                l_repeats.append("Original")
            else:
                l_repeats.append("Repeat "+ str(j))
            l_source.append("HA Trigger")
            l_rabbits.append(str(c_rabbits))
            l_copies.append("0")
            l_etbs.append(str(c_etbs))

            if preston == "T" and preston_repeats > 0:
                for k in range(preston_repeats+1):
                    copies += real_apparents
                    c_copies = real_apparents

                    etbs += c_copies
                    c_etbs = c_copies

                    l_flicker.append("Flicker "+ str(i + 1))
                    if k==min(range(preston_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(k))
                    l_source.append("P Trigger")
                    l_rabbits.append("0")
                    l_copies.append(str(c_copies))
                    l_etbs.append(str(c_etbs))
            elif preston == "T":
                copies += real_apparents
                c_copies = real_apparents

                etbs += c_copies
                c_etbs = c_copies

                l_flicker.append("Flicker "+ str(i + 1))
                if k==min(range(preston_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(k))
                l_source.append("P Trigger")
                l_rabbits.append("0")
                l_copies.append(str(c_copies))
                l_etbs.append(str(c_etbs))

    else:
        if hare_repeats > 0:
            for j in range(hare_repeats+1):
                rabbits += 1 * (apparents + illusions - 1)
                c_rabbits = 1 * (apparents + illusions - 1)

                etbs += c_rabbits
                c_etbs = c_rabbits

                l_flicker.append("Flicker "+ str(i + 1))
                if j==min(range(hare_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(j))
                l_source.append("HA Trigger")
                l_rabbits.append(str(c_rabbits))
                l_copies.append("0")
                l_etbs.append(str(c_etbs))

            if preston == "T" and preston_repeats > 0:
                for k in range(preston_repeats+1):
                    copies += 1
                    c_copies = 1

                    etbs += c_copies
                    c_etbs = c_copies

                    l_flicker.append("Flicker "+ str(i + 1))
                    if k==min(range(preston_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(k))
                    l_source.append("P Trigger")
                    l_rabbits.append("0")
                    l_copies.append(str(c_copies))
                    l_etbs.append(str(c_etbs))
                    
            elif preston == "T":
                copies += 1
                c_copies = 1

                etbs += c_copies
                c_etbs = c_copies

                l_flicker.append("Flicker "+ str(i + 1))
                if k==min(range(preston_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(k))
                l_source.append("P Trigger")
                l_rabbits.append("0")
                l_copies.append(str(c_copies))
                l_etbs.append(str(c_etbs))               
        else:
            rabbits += 1 * (apparents + illusions - 1)
            c_rabbits = 1 * (apparents + illusions - 1)

            etbs += c_rabbits
            c_etbs = c_rabbits

            l_flicker.append("Flicker "+ str(i + 1))
            if j==min(range(hare_repeats+1)):
                l_repeats.append("Original")
            else:
                l_repeats.append("Repeat "+ str(j))
            l_source.append("HA Trigger")
            l_rabbits.append(str(c_rabbits))
            l_copies.append("0")
            l_etbs.append(str(c_etbs))

            if preston == "T" and preston_repeats > 0:
                for k in range(preston_repeats+1):
                    copies += 1
                    c_copies = 1

                    etbs += c_copies
                    c_etbs = c_copies

                    l_flicker.append("Flicker "+ str(i + 1))
                    if k==min(range(preston_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(k))
                    l_source.append("P Trigger")
                    l_rabbits.append("0")
                    l_copies.append(str(c_copies))
                    l_etbs.append(str(c_etbs))
            elif preston == "T":
                copies += 1
                c_copies = 1

                etbs += c_copies
                c_etbs = c_copies

                l_flicker.append("Flicker "+ str(i + 1))
                if k==min(range(preston_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(k))
                l_source.append("P Trigger")
                l_rabbits.append("0")
                l_copies.append(str(c_copies))
                l_etbs.append(str(c_etbs))

# Preston's ETB triggers X amount of times and repeated Y amount of times (if preston_repeats > 0)
    if preston == "T":
        if amount == "All":
            apparents += c_copies * (hare_repeats + 1)
            if hare_repeats > 0:
                for j in range(hare_repeats+1):
                    rabbits += (c_copies) * (apparents + illusions - 1)
                    c_rabbits = (c_copies) * (apparents + illusions - 1)

                    etbs += c_rabbits
                    c_etbs = c_rabbits

                    l_flicker.append("Flicker "+ str(i + 1))
                    if j==min(range(hare_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(j))
                    l_source.append("Copy Triggers")
                    l_rabbits.append(str(c_rabbits))
                    l_copies.append("0")
                    l_etbs.append(str(c_etbs))

            else:
                rabbits += (c_copies) * (apparents + illusions - 1)
                c_rabbits = (c_copies) * (apparents + illusions - 1)

                etbs += c_rabbits
                c_etbs = c_rabbits

                l_flicker.append("Flicker "+ str(i + 1))
                if j==min(range(hare_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(j))
                l_source.append("Copy Triggers")
                l_rabbits.append(str(c_rabbits))
                l_copies.append("0")
                l_etbs.append(str(c_etbs))

        else:
            apparents += c_copies * (hare_repeats + 1)
            if hare_repeats > 0:
                for j in range(hare_repeats+1):
                    rabbits += (c_copies) * (apparents + illusions - 1)
                    c_rabbits = (c_copies) * (apparents + illusions - 1)

                    etbs += c_rabbits
                    c_etbs = c_rabbits

                    l_flicker.append("Flicker "+ str(i + 1))
                    if j==min(range(hare_repeats+1)):
                        l_repeats.append("Original")
                    else:
                        l_repeats.append("Repeat "+ str(j))
                    l_source.append("Copy Triggers")
                    l_rabbits.append(str(c_rabbits))
                    l_copies.append("0")
                    l_etbs.append(str(c_etbs))

            else:
                rabbits += (c_copies) * (apparents + illusions - 1)
                c_rabbits = (c_copies) * (apparents + illusions - 1)

                etbs += c_rabbits
                c_etbs = c_rabbits

                l_flicker.append("Flicker "+ str(i + 1))
                if j==min(range(hare_repeats+1)):
                    l_repeats.append("Original")
                else:
                    l_repeats.append("Repeat "+ str(j))
                l_source.append("Copy Triggers")
                l_rabbits.append(str(c_rabbits))
                l_copies.append("0")
                l_etbs.append(str(c_etbs))
                
    i += 1

# append all lists into a list of lists where each list is a column in the final table
master_list = [l_flicker,l_repeats,l_source,l_rabbits,l_copies,l_etbs]

# make table columns with headers and make them pretty
table = Table(title="Hare Apparent Trigger Log")
table.add_column("Flicker", justify="left", style="magenta")
table.add_column("Repeat", justify="left", style="magenta")
table.add_column("Source", justify="left", style="cyan")
table.add_column("Rabbits", justify="left", style="green")
table.add_column("Copies", justify="left", style="green")
table.add_column("ETBs", justify="left", style="green")

# make the rows of the table
for row in zip(*master_list):
    table.add_row(*row)

# print output in the console
console = Console()
text = Text()
p_rabbits = Text.assemble(("There were ","bold"),(str(rabbits)+" 1/1 white Rabbit Tokens","bold green"),(" made","bold"))
p_copies = Text.assemble(("There were ","bold"),(str(copies)+" 0/1 white Illusion Copy Tokens","bold green"),(" made","bold"))
p_etbs = Text.assemble(("There were ","bold"),(str(etbs)+" creatures that entered the battlefield","bold green"),(" this turn","bold"))

console.print(table)
console.print(p_rabbits)
console.print(p_copies)
console.print(p_etbs)