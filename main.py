from pyscript import document


g7 = {"Hugh Jass", "Sak Madie"}
g8 = {"Emma Niwala", "Aybin Dover"}
g9 = {"Makati Fhukiko", "Mayassis smalls"}
g10 = {"Tom Pearl", "Ben Dover"}

def add_member(e):
    fname = document.querySelector("#first_name").value.strip()
    lname = document.querySelector("#last_name").value.strip()
    
    new_member = {f"{fname} {lname}"}
    master_set = g7 | g8 | g9 | g10 | new_member
    master_set.discard("")
    
    document.querySelector("#output").innerHTML = f"""
        <p><strong>All Members:</strong> {", ".join(master_set)}</p>
        <p><strong>Total Members:</strong> {len(master_set)}</p>
    """
