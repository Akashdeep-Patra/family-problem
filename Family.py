class Person(object):
    def __init__(self,name,gender, father=None,mother=None):
        self.__name=name
        self.__gender=gender
        self.__father=father
        self.__mother=mother
        self.sons=[]
        self.daughters=[]
    def __hash__(self):
        return hash(self.get_name())
    def __eq__(self,other):
        return self.get_name()==other.get_name()
    def append_sons(self,son):
        self.sons.append(son)
        return son
    def append_daughters(self,daughter):
        self.daughters.append(daughter)
        return daughter
    def get_gender(self):
        return self.__gender
    def get_name(self):
        return self.__name
    def set_father(self,father):
        self.__father=father
    def set_mother(self,mother):
        self.__mother=mother
    def get_father(self):
        return self.__father
    def get_mother(self):
        return self.__mother
    def get_sons(self):
        return self.sons
    def get_daughters(self):
        return self.daughters
    def get_children(self):
        return self.get_sons()+self.get_daughters()
    def get_next_gen(self):
        collection=[]
        for son in self.get_sons():
            collection.append(son)
            collection.append(son.get_wife())
        for daughter in self.get_daughters():
            collection.append(daughter)
            collection.append(daughter.get_husband())
        return collection

# inherits from person


class Male(Person):
    def __init__(self,name,gender="Male", father=None,mother=None):
        Person.__init__(self,name,gender,father,mother)
        self.__wife=None
    def set_wife(self,wife):
        self.__wife=wife
        return wife
    def get_wife(self):
        return self.__wife

# inherits from person


class Female(Person):
    def __init__(self,name,gender="Female", father=None,mother=None):
        Person.__init__(self,name,gender,father,mother)
        self.__husband=None
       
    def set_husband(self,husband):
        self.__husband=husband
        return husband
    def get_husband(self):
        return self.__husband



# instead of class function , implemented auxilary function for clarity

# checks if any female exits with this name
def does_mother_exist(root,mother_name):
    if not root:
        return False
    if root.get_name()==mother_name:
        return root.get_gender()=="Female"
    exist=False
    for child in root.get_next_gen():
        exist = exist or does_mother_exist(child,mother_name) 
    return exist

# checks if any male exists with this name 
def does_father_exist(root,father_name):
    if not root:
        return False
    if  root.get_name()==father_name:
        return root.get_gender()=="Male"
    exist=False
    for child in root.get_next_gen():
        exist = exist or does_father_exist(child,father_name) 
    return exist

# for adding child in the tree

def add_child_util(root,mother_name,child_name,gender,child_aded):
    if not root:
        return
    if root.get_name()==mother_name:
        if gender=="Female":
            daughter=Female(child_name,gender,mother=root,father=root.get_husband())
            root.append_daughters(daughter)
            child_aded.append(daughter)
            root.get_husband().append_daughters(daughter)
        else:
            son=Male(child_name,gender,mother=root,father=root.get_husband())
            root.append_sons(son)
            child_aded.append(son)
            root.get_husband().append_sons(son)
        return 
    for child in root.get_next_gen():
        add_child_util(child,mother_name,child_name,gender,child_aded)

def add_child(root,mother_name,child_name,gender):
    if does_father_exist(root,mother_name):
        print("CHILD_ADDITION_FAILED")
        return None
    if not does_mother_exist(root,mother_name):
        print("PERSON_NOT_FOUND")
        return None
    child_aded=[]
    add_child_util(root,mother_name,child_name,gender,child_aded)
    print("CHILD_ADDITION_SUCCEEDED")
    return child_aded[0]
    

"""this returns a list of Male objects which brothers"""

def get_brothers_util(root,name,ans):
    if root.get_name()==name:
        mother=root.get_mother()
        for brother in mother.get_sons():
            if brother.get_name()!=name:
                ans.append(brother)
        return
    for child in root.get_next_gen():
        get_brothers_util(child,name,ans)
        

def get_brothers(root,name):
    ans=[]
    get_brothers_util(root,name,ans)
    return ans


"""this returns a list of Female objects which are sisters"""


def get_sisters_util(root,name,ans):
    if root.get_name()==name:
        mother=root.get_mother()
        for sister in mother.get_daughters():
            if sister.get_name()!=name:
                ans.append(sister)
        return
    for child in root.get_next_gen():
        get_sisters_util(child,name,ans)
        

def get_sisters(root,name):
    ans=[]
    get_sisters_util(root,name,ans)
    return ans


"""get siblings as a list of object """

def get_siblings(root,name):
    return get_brothers(root,name)+get_sisters(root,name)

"""

get paternal uncles as an array of Male objects

"""

def get_paternal_uncle_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        father=root.get_father()
        fathers_brothers=get_brothers(father,father.get_name())
        for uncle in fathers_brothers:
            ans.append(uncle)
        return 
    for child in root.get_next_gen():
        get_paternal_uncle_util(child,name,ans)
def get_paternal_uncle(root,name):
    ans=[]
    get_paternal_uncle_util(root,name,ans)
    return ans
    




"""
get maternal uncles as an array of Male objects

"""

def get_maternal_uncle_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        mother=root.get_mother()
        mothers_brothers=get_brothers(mother,mother.get_name())
        for uncle in mothers_brothers:
            ans.append(uncle)
    for child in root.get_next_gen():
        get_maternal_uncle_util(child,name,ans)
def get_maternal_uncle(root,name):
    ans=[]
    get_maternal_uncle_util(root,name,ans)
    return ans

"""
get paternal aunts as an array of Female objects

"""

def get_paternal_aunt_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        father=root.get_father()
        fathers_sisters=get_sisters(father,father.get_name())
        for aunt in fathers_sisters:
            ans.append(aunt)
    for child in root.get_next_gen():
        get_paternal_aunt_util(child,name,ans)
def get_paternal_aunt(root,name):
    ans=[]
    get_paternal_aunt_util(root,name,ans)
    return ans


"""get maternal aunts as an array of Female objects"""
def get_maternal_aunt_util(root,name,ans):
    if root.get_name()==name:
        mother=root.get_mother()
        mothers_sisters=get_sisters(mother,mother.get_name())
        for aunt in mothers_sisters:
            ans.append(aunt)
    for child in root.get_next_gen():
        get_maternal_aunt_util(child,name,ans)

def get_maternal_aunt(root,name):
    ans=[]
    get_maternal_aunt_util(root,name,ans)
    return ans
"""
gets a list of sister in laws if any as Female objects
"""

def get_sisters_in_law_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        if root.get_gender()=="Female" and root.get_husband():
            sisters_in_law=get_sisters(root.get_husband(),root.get_husband().get_name())
            for sister in sisters_in_law:
                ans.append(sister)
            return
        else:
            brothers=get_brothers(root,name)
            for brother in brothers:
                ans.append(brother.get_wife())
            return
    for child in root.get_next_gen():
        get_sisters_in_law_util(child,name,ans)


def get_sisters_in_law(root,name):
    ans=[]
    get_sisters_in_law_util(root,name,ans)
    return ans 

"""
gets a list of brothers in laws if any as Male objects
"""



def get_brothers_in_law_util(root,name,ans):
    if not root or root==[]:
        print("NONE") 
    if root.get_name()==name:
        if root.get_gender()=="Female" and root.get_husband():
            brothers_in_law=get_brothers(root.get_husband(),root.get_husband().get_name())
            for brother in brothers_in_law:
                ans.append(brother)
            return
        else:
            sisters=get_sisters(root,name)
            for sister in sisters:
                ans.append(sister.get_husband())
            return
    for child in root.get_next_gen():
        get_brothers_in_law_util(child,name,ans)


def get_brothers_in_law(root,name):
    ans=[]
    get_brothers_in_law_util(root,name,ans)
    return ans 
"""
gets sons as a list of male objects
"""
def get_sons_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        sons=root.get_sons()
        for son in sons:
            ans.append(son)
        return
    for child in root.get_next_gen():
        get_sons_util(child,name,ans)

def get_sons(root,name):
    ans=[]
    get_sons_util(root,name,ans)
    return ans

"""
gets daughters as a list of male objects
"""
def get_daughters_util(root,name,ans):
    if root.get_name()==name:
        daughters=root.get_daughters()
        for daughter in daughters:
            ans.append(daughter)
        return
    for child in root.get_next_gen():
        get_daughters_util(child,name,ans)

def get_daughters(root,name):
    ans=[]
    get_daughters_util(root,name,ans)
    return ans

"""
gets sibliongs as a list of  objects
"""
def get_siblings_util(root,name,ans):
    if not root:
        return 
    if root.get_name()==name:
        siblings=get_siblings(root,name)
        for sibling in siblings:
            ans.append(sibling)
        return
    for child in root.get_next_gen():
        get_siblings_util(child,name,ans)

def find_siblings(root,name):
    ans=[]
    get_siblings_util(root,name,ans)
    return ans