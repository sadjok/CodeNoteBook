"About Program Project"

class Projects():
    def __init__(self,projectname,psn = False,psntext = None,type = "Python",**args):
        self.projectname = projectname
        self.psn = psn
        self.psntext = psntext
        self.type = type
        self.args = args

    def ProjectSolutionNote(self):
        if self.psn:
            with open(".psn","w",encoding = "utf-8") as psnfile:
                psnfile.write(self.psntext)

    def ProjectInformation(self):
        """
        Name
        Main
        Psn
        Run
        Workspace
        Runargs
        Types
        """
        args = self.args
        name = args["name"]
        main = args["main"]
        psn = args["psn"]
        run = args["run"]
        workspace = args["workspace"]
        runargs = args["runargs"]
        types = self.type
        types = lower(types[2])
        with open(projectname + "." + types + "obj","w",encoding = "utf-8") as objectfile:
            objectfile.write(name)
            objectfile.write(main)
            objectfile.write(psn)
            objectfile.write(run)
            objectfile.write(workspace)
            objectfile.write(runargs)
            objectfile.write(types)


