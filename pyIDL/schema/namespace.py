from pydantic import BaseModel, Field

class NameSpace(BaseModel):

    name: str
    parent: 'NameSpace' = None
    description: str = None
    children: list['NameSpace'] = Field(default_factory=list, exclude=True)

    def add_branch(self, branch_name):
        branch = NameSpace(name=branch_name, parent=self)
        self.children.append(branch)
        return branch

    def export(self, parent_path=""):
        current_path = f"{parent_path}.{self.name}" if parent_path else self.name
        print(current_path)
        for child in self.children:
            child.export(current_path)

    @property
    def path(self) -> str:
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.path}.{self.name}"