class SolverFactory:
    def __init__(self):
        self.Default = "leftturn"
        self.Choices = ["dijkstra", "leftturn"]

    def createSolver(self, type):
        if type == "leftturn":
            import leftturn
            return ["Left turn only", leftturn.solve]
        else:
            import dijkstra
            return ["Dijkstra", dijkstra.solve]
