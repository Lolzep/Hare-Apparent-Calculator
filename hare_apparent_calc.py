# makes a pretty table and output
from rich.console import Console
from rich.table import Table
from rich.text import Text
console = Console()
text = Text()

# make all lists, each is a column in the final log table
l_flicker =[]
l_source = []
l_repeats = []
l_rabbits = []
l_copies = []
l_etbs = []

# User input validation
def enter_data(message: str, typ: type):
    while True:
        try:
            v = typ(input(message))
            if (isinstance(v, int) or isinstance(v, float)) and v < 0:
                raise ValueError
        except ValueError:
            print(f"Thats not an {typ}! or you have entered a negative")
            continue
        else:
            break
    return v

# User input
apparents = enter_data("Non-Token Hare Apparents in play being flickered: ", int)

while True:
    try:
        total = enter_data("Total Hare Apparents in play (including token copies): ", int)
        illusions = total - apparents
        if illusions < 0:
            raise ValueError
        break
    except ValueError:
        print("The amount of Hare Apparents being flickered must be less than the total amount of Hare Apparents. You input "+str(apparents)+" to be flickered which is greater than "+str(total)+" as the total.")
        continue

while True:
    try:
        preston = input("Is Preston in play for copy generation? (T/F): ")
        if preston == "T":
            preston = True
            break
        elif preston == "F":
            preston = False
            break
        else:
            raise ValueError
    except ValueError:
        print("Please input 'T' or 'F'")
        continue

flicker = enter_data("Amount of times to flicker: ", int)
hare_repeats = enter_data("How many times is Hare Apparent's triggers being repeated?: ", int)
preston_repeats = enter_data("How many times is Preston's trigger being repeated?: ", int)

# Prints an explanation of the inputs
console.print("")
console.print(f"[white][bold]{apparents} Hare Apparents are flickering {flicker} time(s) with {total} Hare Apparents total in play[/bold][/white]")
if preston == True:
    console.print(f"[white][bold]Preston is in play to generate copies[/bold][/white]")
if hare_repeats > 0:
    console.print(f"[white][bold]The amount of Hare Apparent repeat triggers is {hare_repeats}[/bold][/white]")
if preston_repeats > 0:
    console.print(f"[white][bold]The amount of Preston repeat triggers is {preston_repeats}[/bold][/white]")

# Initial values for everything that enters should be 0
rabbits = 0
copies = 0
etbs = 0

# Initial values for "counting" the amount copies and triggers happening
i = 0 # counts amount of flickers
j = 0 # counts amount of hare_repeats
k = 0 # counts amount of preston_repeats

# To start the flicker, the amount being flickered should remain constant as what was inputted for "apparents"
real_apparents = apparents
# Flicker X amount of times
while i < flicker:
# Hare Apparent leaves and enters X amount of times (flicker). There's only 1 ETB trigger per flicker. hare_repeats included to help visualize.
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

# Hare Apparent's ETB triggers X amount of times (flicker), repeated Y amount of times (if hare_repeats > 0), and Z copies are made
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

        if preston == True and preston_repeats > 0:
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
        elif preston == True:
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

        if preston == True and preston_repeats > 0:
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
        elif preston == True:
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

# Preston's ETB triggers X amount of times and repeated Y amount of times (if preston_repeats > 0)
    if preston == True:
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
p_rabbits = Text.assemble(("There were ","bold"),(str(rabbits)+" 1/1 white Rabbit Tokens","bold green"),(" made","bold"))
p_copies = Text.assemble(("There were ","bold"),(str(copies)+" 0/1 white Illusion Copy Tokens","bold green"),(" made","bold"))
p_etbs = Text.assemble(("There were ","bold"),(str(etbs)+" creatures that entered the battlefield","bold green"),(" this turn","bold"))

console.print(table)
console.print(p_rabbits)
console.print(p_copies)
console.print(p_etbs)