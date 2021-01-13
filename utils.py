from Family import Female,Male
import Family


Queen=Female(name="Queen Anga",gender="Female")

def get_initial_tree():
    # 1st level
    queen=Female(name="Queen Anga",gender="Female")

    king=Male(name="King Shan",gender="Male")

    chit=Male(name="Chit",gender="Male",father=king,mother=queen)

    ish=Male(name="Ish",gender="Male",father=king,mother=queen)

    vich=Male(name="Vich",gender="Male",father=king,mother=queen)

    aras=Male(name="Aras",gender="Male",father=king,mother=queen)

    satya=Female(name="Satya",father=king,mother=queen)

    king.sons=[chit,ish,vich,aras]

    king.daughters=[satya]

    queen.daughters=king.daughters

    queen.sons=king.sons

    # 2nd level
    amba=Female(name="Amba")

    lika=Female(name="Lika")

    chitra=Female(name="Chitra")

    vyan=Male(name="Vyan")

    chit.set_wife(amba)

    amba.set_husband(chit)

    vich.set_wife(lika)

    lika.set_husband(vich)

    aras.set_wife(chitra)

    chitra.set_husband(aras)

    satya.set_husband(vyan)

    vyan.set_wife(satya)

    # 3rd level

    dritha=Female(name="Dritha",father=chit,mother=amba)

    tritha=Female(name="Tritha",father=chit,mother=amba)

    vritha=Male(name="Vritha",father=chit,mother=amba)

    jaya=Male(name="Jaya")

    dritha.set_husband(jaya)

    jaya.set_wife(dritha)

    chit.sons=amba.sons=[vritha]

    chit.daughters=amba.daughters=[dritha,tritha]

    vila=Female(name="Vila",father=vich,mother=lika)

    chika=Female(name="Chika")

    vich.daughters=lika.daughters=[vila,chika]

    jnki=Female(name="Jnki",father=aras,mother=chitra)

    ahit=Male(name="Ahit",father=aras,mother=chitra)

    arit=Male(name="Arit")

    arit.set_wife(jnki)

    jnki.set_husband(arit)

    aras.sons=chitra.sons=[ahit]

    aras.daughters=chitra.daughters=[jnki]

    asva=Male(name="Asva",father=vyan,mother=satya)

    vyas=Male(name="Vyas",father=vyan,mother=satya)

    atya=Female(name="Atya",father=vyan,mother=satya)

    # 4th level

    satvy=Female(name="Satvy")

    krpi=Female(name="Krpi")

    asva.set_wife(satvy)

    satvy.set_husband(asva)

    krpi.set_husband(vyas)

    vyas.set_wife(krpi)

    satya.sons=vyan.sons=[asva,vyas]

    satya.daughters=vyan.daughters=[atya]

    yodhan=Male(name="Yodhan",father=jaya,mother=dritha)

    dritha.sons=jaya.sons=[yodhan]

    laki=Male(name="Laki",father=arit,mother=jnki)

    lavnya=Female(name="Lavnya",father=arit,mother=jnki)

    arit.sons=jnki.sons=[laki]

    arit.daughters=jnki.daughters=[lavnya]

    vasa=Male(name="Vasa",father=asva,mother=satvy)

    asva.sons=satvy.sons=[vasa]

    kriya=Male(name="Kriya",father=vyan,mother=krpi)

    krithi=Female(name="Krithi",father=vyan,mother=krpi)

    vyan.sons=krpi.sons=[kriya]

    vyan.daughters=krpi.daughters=[krithi]

    return queen
# factory design pattern to map the relationship

def call_get_paternal_uncle(queen,command_line_args):

    return Family.get_paternal_uncle(root=queen,name=command_line_args[1])

def call_get_maternal_uncle(queen,command_line_args):

    return Family.get_maternal_uncle(root=queen,name=command_line_args[1])

def call_get_paternal_aunt(queen,command_line_args):

    return Family.get_paternal_aunt(root=queen,name=command_line_args[1])

def call_get_maternal_aunt(queen,command_line_args):

    return Family.get_maternal_aunt(root=queen,name=command_line_args[1])

def call_get_sisters_in_law(queen,command_line_args):

    return Family.get_sisters_in_law(root=queen,name=command_line_args[1])


def call_get_brothers_in_law(queen,command_line_args):

    return Family.get_brothers_in_law(root=queen,name=command_line_args[1])

def call_get_sons(queen,command_line_args):

    return Family.get_sons(root=queen,name=command_line_args[1])

def call_get_daughters(queen,command_line_args):

    return Family.get_daughters(root=queen,name=command_line_args[1])


def call_find_siblings(queen,command_line_args):

    return Family.find_siblings(root=queen,name=command_line_args[1])

def factory(queen,command_line_args):
    

    if command_line_args[0]=="ADD_CHILD":

        return Family.add_child(root=queen,mother_name=command_line_args[1],child_name=command_line_args[2],gender=command_line_args[3])

    if not Family.does_father_exist(queen,command_line_args[1]) and not Family.does_mother_exist(queen,command_line_args[1]):
        
        print("PERSON_NOT_FOUND ")
        
        return None

    # for mapping the function calls

    switcher={
    "Paternal-Uncle": call_get_paternal_uncle,

    "Maternal-Uncle": call_get_maternal_uncle,

    "Paternal-Aunt": call_get_paternal_aunt,
    
    "Maternal-Aunt": call_get_maternal_aunt,

    "Sister-In-Law": call_get_sisters_in_law,

    "Brother-In-Law": call_get_brothers_in_law,

    "Son": call_get_sons,

    "Daughter": call_get_daughters,

    "Siblings": call_find_siblings
    }

    return switcher[command_line_args[2]](queen,command_line_args)

        
        
# function to format the output in the cli


def formatted_output(output):

    if type(output)==list and  output==[]:
        print("NONE")
        return 
    if not output or type(output)!=list:
        return
    output_set=set(output)

    # get the names from the objects

    segments=[]
    for person in output:
        if person  in output_set:
            segments.append(person.get_name())
            output_set.remove(person)
    # # sorting the names lexicographically

    # segments=sorted(segments)
    print(" ".join(segments))


