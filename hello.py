import git


class BranchCheck:
    def __init__(self):
        self.branches = git.Git().branch().split()
    
    def current_branch(self):
        return self.branches[self.branches.index("*") + 1]

print(BranchCheck().current_branch())