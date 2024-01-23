from tkinter import *
import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import requests


root = ttkb.Window(themename="solar")

#program title
root.title("DMPK Tracker")

#program window size
window_width = 1775  
window_height = 1200  
root.geometry(f"{window_width}x{window_height}")

#Section 1 - Molecule Look Up Field:

#Frame for Molecule Look Up
query_frame = ttkb.Labelframe(root, text=" Molecule Lookup", bootstyle = "light", borderwidth=2, relief="ridge")
query_frame.place(x = 400, y=10)

    #1 - Molecule Entry
molecule_name = ttkb.Entry(query_frame, bootstyle = "secondary", font = ("Helvetica", 10))
molecule_name_text = molecule_name.get()
molecule_name.grid(row=0, column=0, padx=10, pady=10)
molecule_name.insert(0, "Molecule Name")

protocol_list = []
mol_id = []

def search_molecule():
    mol_id.clear()
    protocol_list.clear()
    molecule_name_text = molecule_name.get()
    base_url = "https://link to database"
    api_token = {'Token': "token_here"}
    mol_name_url = base_url + "molecules?names=" + molecule_name_text
    mol_name_response = requests.request("GET", mol_name_url, headers=api_token)

    if mol_name_response.status_code == 200:
        mol_name_data = mol_name_response.json()          
        mol_name_objects = mol_name_data.get('objects', [])  
        
    else:
        print("Request failed with status code:", mol_name_response.status_code)

    
    for obj in mol_name_objects:
        id = obj.get('id')  
        mol_id.append(id)
        

    mol_id_string = str(mol_id[0])
    print(mol_id_string)
    base_url = "https://link to database"
    api_token = {'Token': "token_here"}
    url = base_url + "protocols?molecules=" + mol_id_string
    response = requests.request("GET",url, headers = api_token)


        # Check if the request was successful (status code 200) and parse the JSON content into Python dict (data variable)
    if response.status_code == 200:
        data = response.json()  
                
    else:
        print("Request failed with status code: ", response.status_code)

    #the "objects" attribute of Data is a list. We have to iterate over it to access individual dictionary items and then extract the "name" key from each dictionary. 
    objects = data.get('objects', [])  # Retrieve the list of objects, default to an empty list if 'objects' key is not present
        
    for obj in objects:
        protocol_name = obj.get('name')  # Retrieve the 'name' attribute from each object
        protocol_list.append(protocol_name)

    update_checkboxes()
    for item in protocol_list:
        list_text.insert(tk.END, f"{item}\n") 
    
    #2 - Batch Entry
molecule_batch = ttkb.Entry(query_frame, bootstyle = "secondary", font = ("Helvetica", 10))
molecule_batch.grid(row=0, column=1, padx=10, pady=10)
molecule_batch.insert(0, "Molecule Batch")

    #3 - Molecule Search Button - Query  API
search_button = ttkb.Button(query_frame, text="Search Molecule", style=("warning.TButton", OUTLINE), command=search_molecule) 
search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="e")



#
#section to define necessary functions
#
    #Function to turn on checkboxes
def checkbox_on(IntVar, text, list):
    if text in list:
        IntVar.set(1)
    else:
        IntVar.set(0)


def update_checkboxes():
        for text, IntVar in checkbox_dict.items():
            checkbox_on(checkbox_dict[text], text, protocol_list )

#__________________________________________________


#
#Section 2 - DMPK Phases
#


#Frame for Phase 1
phase1_frame = ttkb.Labelframe(root, text= "Step 1", bootstyle = "light", borderwidth=2, relief="ridge")
phase1_frame.place(x=25, y=385, anchor=  W)

#Scrollbar Configuration
p1_canvas = Canvas(phase1_frame, width=350)
p1_canvas.pack(side=LEFT)

p1_scrollbar = ttkb.Scrollbar(phase1_frame, orient=VERTICAL, bootstyle="warning round", command=p1_canvas.yview)
p1_scrollbar.pack(side=RIGHT, fill=Y)

p1_canvas.configure(yscrollcommand=p1_scrollbar.set)

p1_checkbox_frame = Frame(p1_canvas)
p1_canvas.create_window((0,0), window = p1_checkbox_frame, anchor = NW)
def on_configure():
    p1_canvas.configure(scrollregion=p1_canvas.bbox("all"))

p1_canvas.bind('<Configure>', on_configure)

    #step 1a label 
step1a_label = ttkb.Label(p1_checkbox_frame, text="Step 1a", font=("Helvetica", 10), bootstyle = "warning" )

    #Checkboxes in step 1a
Protocol_1 = IntVar()
protocol_1 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_1, 
                                       text="Protocol 1",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_1, "Protocol_1", protocol_list) ) 
Protocol_2 = IntVar()
protocol_2 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_2, 
                                       text="Protocol 2",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_2, "Protocol_2", protocol_list) ) 
Protocol_3 = IntVar()
protocol_3 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_3, 
                                       text="Protocol 3",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_3, "Protocol_3", protocol_list)  )
Protocol_4 = IntVar()
protocol_4 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 4",
                                       variable = Protocol_4,
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_4, "Protocol_4", protocol_list)  )


    #step 1b label 
step1b_label = ttkb.Label(p1_checkbox_frame, text="Step 1b", font=("Helvetica", 10), bootstyle = "warning" )

     #Checkboxes in step1b
Protocol_5 = IntVar()
protocol_5 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 5",
                                       variable = Protocol_5,
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_5, "Protocol_5", protocol_list)  )
Protocol_6 = IntVar()
protocol_6 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 6",
                                       variable = Protocol_6,
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_6, "Protocol_6", protocol_list)  )
Protocol_7 = IntVar()
protocol_7 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 7",
                                       variable = Protocol_7,
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_7, "Protocol_7", protocol_list)  )

 #step 1c label 
step1c_label = ttkb.Label(p1_checkbox_frame, text="Step 1c", font=("Helvetica", 10), bootstyle = "warning" )

     #Checkboxes in step1c
Protocol_8 = IntVar()
protocol_8 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_8, 
                                       text="Protocol_8",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_8, "Protocol_8", protocol_list) ) 
Protocol_9 = IntVar()
protocol_9 = ttkb.Checkbutton(p1_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_9, 
                                       text="Protocol_9",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_9, "Protocol_9", protocol_list) ) 



    #Geometry/Widget Placement
step1a_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)
protocol_1.grid(row=1, column=0, padx=20, pady=10, sticky=W)
protocol_2.grid(row=2, column=0, padx=20, pady=10, sticky=W)
protocol_3.grid(row=3, column=0, padx=20, pady=10, sticky=W)
protocol_4.grid(row=4, column=0, padx=20, pady=10, sticky=W)


step1b_label.grid(row=8, column=0, padx=20, pady=10, sticky=W)
protocol_5.grid(row=9, column=0, padx=20, pady=10, sticky=W)
protocol_6.grid(row=10, column=0, padx=20, pady=10, sticky=W)
protocol_7.grid(row=11, column=0, padx=20, pady=10, sticky=W)

step1c_label.grid(row=18, column=0, padx=20, pady=10, sticky=W)
protocol_8.grid(row=19, column=0, padx=20, pady=10, sticky=W)
protocol_9.grid(row=20, column=0, padx=20, pady=10, sticky=W)



#Frame for Phase 2
phase2_frame = ttkb.Labelframe(root, text= "Step 2", bootstyle = "light", borderwidth=2, relief="ridge")
phase2_frame.place(x=420, y=385, anchor=  W)

#Scrollbar Configuration
p2_canvas = Canvas(phase2_frame, width=350)
p2_canvas.pack(side=LEFT)

p2_scrollbar = ttkb.Scrollbar(phase2_frame, orient=VERTICAL, bootstyle="warning round", command=p2_canvas.yview)
p2_scrollbar.pack(side=RIGHT, fill=Y)

p2_canvas.configure(yscrollcommand=p2_scrollbar.set)

p2_checkbox_frame = Frame(p2_canvas)
p2_canvas.create_window((0,0), window = p2_checkbox_frame, anchor = NW)
def on_configure_2():
    p2_canvas.configure(scrollregion=p2_canvas.bbox("all"))

p2_canvas.bind('<Configure>', on_configure_2)

    #Checkboxes for P2
Protocol_1a = IntVar()
protocol_1a = ttkb.Checkbutton(p2_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 1a",
                                       variable = Protocol_1a,
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_1a, "Protocol_1a", protocol_list)  )
Protocol_2a = IntVar()
protocol_2a = ttkb.Checkbutton(p2_checkbox_frame, bootstyle = "warning-round-toggle", 
                                       variable = Protocol_2a, 
                                       text="Protocol 2a",
                                        onvalue= 1,
                                        offvalue= 0, command=lambda: checkbox_on(Protocol_2a, "Protocol_2a", protocol_list) ) 


    #Geometry/Widget Placement
protocol_1a.grid(row=0, column=0, padx=20, pady=10, sticky=W)
protocol_2a.grid(row=1, column=0, padx=20, pady=10, sticky=W)


#Frame for Phase 3
phase3_frame = ttkb.Labelframe(root, text= "Phase 3", bootstyle = "light", borderwidth=2, relief="ridge")
phase3_frame.place(x=25, y=825, anchor=  W)

#Scrollbar Configuration
p3_canvas = Canvas(phase3_frame, width=350)
p3_canvas.pack(side=LEFT)

p3_scrollbar = ttkb.Scrollbar(phase3_frame, orient=VERTICAL, bootstyle="warning round", command=p3_canvas.yview)
p3_scrollbar.pack(side=RIGHT, fill=Y)

p3_canvas.configure(yscrollcommand=p3_scrollbar.set)

p3_checkbox_frame = Frame(p3_canvas)
p3_canvas.create_window((0,0), window = p3_checkbox_frame, anchor = NW)
def on_configure_3(event):
    p3_canvas.configure(scrollregion=p3_canvas.bbox("all"))

p3_canvas.bind('<Configure>', on_configure_3)

    #Checkboxes for P3


Protocol_1b = IntVar()
protocol_1b = ttkb.Checkbutton(p3_checkbox_frame, bootstyle = "warning-round-toggle", 
                                    text="Protocol 1b",
                                       variable = Protocol_1b,
                                        onvalue= 1,
                                        offvalue= 0 ) 
protocol_1b.grid(row=1, column=0, padx=20, pady=20, sticky=W)

#
#Section for returning all the studies done.
#
#Frame for studies
studies_frame = ttkb.Labelframe(root, text= "Completed Studies", bootstyle = "light", borderwidth=2, relief="ridge")
studies_frame.place(x=850, y=510, anchor=  W)

#scrollbar for studies
studies_scroll = ttkb.Scrollbar(studies_frame, orient=VERTICAL, bootstyle = "warning round")
studies_scroll.pack(side=RIGHT, fill =Y)

# Create a Text widget to display the list
list_text = ttkb.Text(studies_frame, yscrollcommand=studies_scroll.set)   
list_text.pack(padx=20, pady=20, fill="both", expand=True)
studies_scroll.config(command=list_text.yview)

# Display items in the Text widget

    

#Dictionary containing all the checkboxes used here. This dict is used in the update_checkboxes() Function. 
checkbox_dict = {
                    #Step1a-c
                    "Protocol_1": Protocol_1,
                    "Protocol_2":Protocol_2,
                    "Protocol_3":Protocol_3,
                    "Protocol_4" : Protocol_4,
                    "Protocol_5":Protocol_5,
                    "Protocol_6":Protocol_6,
                    "Protocol_7":Protocol_7,
                    "Protocol_8":Protocol_8,
                    "Protocol_9":Protocol_9,

                     #Step2
                    'Protocol_1a':Protocol_1a,
                    "Protocol_2a":Protocol_2a,

                     #Step3
                    'Protocol_1b':Protocol_1b,
}

root.mainloop()