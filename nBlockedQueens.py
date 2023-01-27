#Importimi i modulit te constraint solver per python
from ortools.constraint_solver import pywrapcp

#Funksioni i cili shikon te gjitha zgjidhjet per X mbretereshat e dhena si parameter 
#dhe fushat e ndaluara te bashkangjitura si parametra gjithashtu
def blockedNQueens(nrMbretereshave, blockedPos):

    #Variabla e cila do ruaj nje pozicion aktual te mbretereshes kur
    #te behet shfaqja e zgjidhjes
    queenPos = 0;
	
    #Klasa e cila definon dhe menaxhon Constraint Programming problem qe e kemi
    #te emeruar me vetedeshire
    solver = pywrapcp.Solver("Blocked N-Queens Constraint Programming Solver")

    #Vargu me n (nrMbretereshave) fusha per n mbreteresha (nrMbretereshave)
    queens = [solver.IntVar(0, nrMbretereshave - 1, "x%i" % i) for i in range(nrMbretereshave)]

    #Krijo rregulla qe mbretereshat te jene ne fusha unike
    #dhe asnjera te mos jete ne diagonale me njera tjeren
    #apo ne te njejten kolone
    solver.Add(solver.AllDifferent(queens))
    for i in range(nrMbretereshave):
        for j in range(i):
            solver.Add(queens[i] != queens[j])
            solver.Add(queens[i] + i != queens[j] + j)
            solver.Add(queens[i] - i != queens[j] - j)

    #Krijo rregullen qe mbreteresha te mos te jete ne te
    #njejten fushe si njera nga fushat e bllokuara
    for row, col in blockedPos:
        solver.Add(queens[row] != col)

    #Mbledhi te gjitha zgjidhjet ne nje variabel
    solveCollection = solver.AllSolutionCollector()
    solveCollection.Add(queens)

    #Zgjidh problemi dhe ruaje te variabla
    solver.Solve(solver.Phase(queens, solver.INT_VAR_DEFAULT,
                              solver.INT_VALUE_DEFAULT), solveCollection)

    #Shfaq zgjidhjen
    for i in range(solveCollection.SolutionCount()):
        print("Zgjidhja", i)
        for j in range(nrMbretereshave):
            queenPos = solveCollection.Value(i, queens[j]);
            print("\u2B1C"*queenPos + chr(0x1F451) + "\u2B1C"*(nrMbretereshave - queenPos - 1))
        print()

#Thirr funksionin me X mbreteresha dhe nje varg te fushave te ndaluara (0-based)
blockedNQueens(8, [(2, 2), (3, 4)])
