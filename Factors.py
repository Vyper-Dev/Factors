import matplotlib.pyplot as plt

Run = True
while Run:
    Num = input("What number would you like to get the factors of?: ")
    Y = []
    try:
        Count = int(Num)
        X = 2
        Factors = []
        for i in range(Count):
            IsFactor = Count % X
            if IsFactor == 0:
                Factor = Count / X
                Factors.append(Factor)
                Y.append(X)
                X += 1
            else:
                X += 1
        print(*Factors, sep=', ')
        print("")
        fig, ax = plt.subplots()
        ax.plot(Factors, Y, color='blue', marker='.', linestyle='-', linewidth=2, markersize=12);
        ax.grid(True, linestyle='-.')
        #ax.tick_params(labelcolor='b', labelsize='medium', width=2)
        plt.show()

    except ValueError:
        print("Only integers are allowed, please enter a whole number")
        print("")
