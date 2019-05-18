"""
Creating the class University there for the parts linked to it.
"""
class University():
        """
        First definition of all the parts linked.
        """
	def __init__(self,campus,departments,carreers,curriculum):
                """
                Each one of them.
                """
                self.campus = campus
                self.departments = departements
                self.carreers = carreres
                self.curriculum = curriculum
                
        def setCampus(self,campus):
                """
                
                """
                self.campus = camp

        def setDepartments(self,departments):
                """
                
                """
                self.departments = dep

        def setCarrers(self,carrers):
                """
                
                """
                self.carreers = carr
                
         def setCurriculum(self,curriculum):
                """
                
                """
                self.curriculum = curr

        def getCampus(self,campus):
                """
                
                """
                return self.campus

        def getDepartments(self,departments):
                """
                
                """
                return self.departments

        def getCarrers(self,carrers):
                """
                
                """
                return self.carreers
                
         def getCurriculum(self,curriculum):
                """
                
                """
                return self.curriculum

        def __str__(self):
                """

                """
                return (self.campus,self.departments,self.carreers,self.curriculum)
