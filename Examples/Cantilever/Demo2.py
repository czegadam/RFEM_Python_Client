#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import tkinter as tk
import time

baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, LoadDirectionType
from RFEM.initModel import Model, Calculate_all
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.Calculate.meshSettings import GetModelInfo
from tkinter import ttk


def generate_nodes():
    print("Generating RFEM model...")
    time.sleep(0.01)
    info_label.config(text="Model Generating...")

    verSpac = horizontal_spacing_entry.get()
    horSpac = vertical_spacing_entry.get()
    material = material_entry.get()
    profile = profile_entry.get()
    fixed_pinned = fixed_pinned_var.get()
    modelName = modelName_entry.get()
    isNewModel_str = new_Model_var.get()

    # Setting new model flag
    isNewModel = False
    if isNewModel_str == "True":
        isNewModel = True
        
    # Lists of Spacing patterns
    horSpac_list = horSpac.split(sep="-")
    verSpac_list = verSpac.split(sep="-")

    # Calculating Node coordinates
    horNodes = [0]
    for n in horSpac_list:
        xn = horNodes[-1]+float(n)
        horNodes.append(xn)

    verNodes = [0]
    for m in verSpac_list:
        xm = verNodes[-1]+float(m)
        verNodes.append(xm)

    Model(isNewModel, modelName) # get model
    Model.clientModel.service.begin_modification()

    Material(1, material)

    Section(1, profile)

    NodalSupport(1, '1', NodalSupportType.FIXED)

    # Creating Nodes
    iTot = len(horNodes)
    jTot = len(verNodes)
    memberNo = 1
    for j, nodeX in enumerate(verNodes):
        #add code
        for i, nodeZ in enumerate(horNodes):
            #add code
            nodeNo = 1+i+iTot*j
            Node(nodeNo, nodeX, 0.0, -nodeZ)
            # print("Node:")
            # print(nodeNo, nodeX, 0.0, -nodeZ)
            # if nodeNo>1 and memberNo<13 and nodeNo%iTot!=1:
                # print("Member:")
                # print(memberNo, nodeNo-1, nodeNo, 0.0, 1, 1)
                # Member(memberNo, nodeNo-1, nodeNo, 0.0, 1, 1)
                # memberNo +=1    

    Model.clientModel.service.finish_modification()

    if isNewModel:
        info_label.config(text="Nodes Generated.")
    else:
        info_label.config(text="Nodes Updated.")

def generate_elements():
    print("Generating Elements in RFEM model...")
    info_label.config(text="Generating Elements in RFEM model...")

    horSpac = horizontal_spacing_entry.get()
    verSpac = vertical_spacing_entry.get()
    material = material_entry.get()
    profile = profile_entry.get()
    fixed_pinned = fixed_pinned_var.get()
    modelName = modelName_entry.get()
    isNewModel_str = new_Model_var.get()

    # Setting new model flag
    isNewModel = False
    if isNewModel_str == "True":
        isNewModel = True
        
    # Lists of Spacing patterns
    horSpac_list = horSpac.split(sep="-")
    verSpac_list = verSpac.split(sep="-")

    # Calculating Node coordinates
    horNodes = [0]
    for n in horSpac_list:
        xn = horNodes[-1]+float(n)
        horNodes.append(xn)

    verNodes = [0]
    for m in verSpac_list:
        xm = verNodes[-1]+float(m)
        verNodes.append(xm)

    Model(isNewModel, modelName) # get model
    Model.clientModel.service.begin_modification()
    print("service opened")

    Material(1, material)

    Section(1, profile)

    # Creating Nodes
    iTot = len(horNodes)
    jTot = len(verNodes)
    memberNo = 1
    
    # Creating members
    for j, nodeX in enumerate(verNodes):
        for i, nodeZ in enumerate(horNodes):
            nodeNo = 1+i+iTot*j
            if nodeNo>1 and nodeNo%jTot!=1:
                # print("Member:")
                # print(memberNo, nodeNo-1, nodeNo, 0.0, 1, 1)
                Member(memberNo, nodeNo-1, nodeNo, 0.0, 1, 1)
                memberNo +=1    

    Model.clientModel.service.finish_modification()
    
    if isNewModel:
        info_label.config(text="Elements Generated.")
    else:
        info_label.config(text="Elements Updated.")


def load_inputs():
    # Placeholder for loading inputs from database
    print("Loading inputs from database...")

def save_inputs():
    # Placeholder for saving inputs to database
    print("Saving inputs to database...")

root = tk.Tk()
root.title("RFEM Model Generator")
root.configure(bg="#F7F7F7")

frame = ttk.Frame(root, padding=10)
frame.grid(column=0, row=0)

thisRow = 0

# Row 1
thisRow += 1
new_Model_label = ttk.Label(frame, text="New Model?")
new_Model_label.grid(column=0, row=thisRow, pady=10)
new_Model_var = tk.StringVar(frame)
new_Model_var.set("True")
new_Model_option = ttk.OptionMenu(frame, new_Model_var, "True", *["True", "False"])
new_Model_option.grid(column=1, row=1, pady=10)

# Row 2
thisRow += 1
modelName_label = ttk.Label(frame, text="Model Name:")
modelName_label.grid(column=0, row=thisRow, pady=10)
modelName_entry = ttk.Entry(frame)
modelName_entry.insert(0,"NewModel")
modelName_entry.grid(column=1, row=thisRow, pady=10)

# Row 3
thisRow += 1
horizontal_spacing_label = ttk.Label(frame, text="Horizontal spacing pattern:")
horizontal_spacing_label.grid(column=0, row=thisRow, pady=10)
horizontal_spacing_entry = ttk.Entry(frame)
horizontal_spacing_entry.insert(0,"1-2-3-4-3-2-1")
horizontal_spacing_entry.grid(column=1, row=thisRow, pady=10)

# Row 4
thisRow += 1
vertical_spacing_label = ttk.Label(frame, text="Vertical spacing pattern:")
vertical_spacing_label.grid(column=0, row=thisRow, pady=10)
vertical_spacing_entry = ttk.Entry(frame)
vertical_spacing_entry.insert(0,"2-5-5-5-2")
vertical_spacing_entry.grid(column=1, row=thisRow, pady=10)

# Row 5
thisRow += 1
material_label = ttk.Label(frame, text="Material:")
material_label.grid(column=0, row=thisRow, pady=10)
material_entry = ttk.Entry(frame)
material_entry.insert(0,"S235")
material_entry.grid(column=1, row=thisRow, pady=10)

# Row 6
thisRow += 1
profile_label = ttk.Label(frame, text="Profile:")
profile_label.grid(column=0, row=thisRow, pady=10)
profile_entry = ttk.Entry(frame)
profile_entry.insert(0,"IPE 200")
profile_entry.grid(column=1, row=thisRow, pady=10)

# Row 7
thisRow += 1
fixed_pinned_label = ttk.Label(frame, text="Supports:")
fixed_pinned_label.grid(column=0, row=thisRow, pady=10)
fixed_pinned_var = tk.StringVar(frame)
fixed_pinned_var.set('Fixed')
fixed_pinned_option = ttk.OptionMenu(frame, fixed_pinned_var, 'Fixed', *['Fixed', 'Pinned'])
fixed_pinned_option.grid(column=1, row=thisRow, pady=10)

# Row 8
thisRow += 1
info_label = ttk.Label(frame, text="Standby...", foreground='#f00')
info_label.grid(column=0, row=thisRow, pady=10)

# Row 9
thisRow += 1
generate_nodes_button = ttk.Button(frame, text="Generate Nodes", command=generate_nodes)
generate_nodes_button.grid(column=0, row=thisRow, pady=10)

load_button = ttk.Button(frame, text="Load", command=load_inputs)
load_button.grid(column=1, row=thisRow, pady=10)

save_button = ttk.Button(frame, text="Save", command=save_inputs)
save_button.grid(column=2, row=thisRow, pady=10)

# Row 10
thisRow += 1
generate_members_button = ttk.Button(frame, text="Generate Members", command=generate_elements)
generate_members_button.grid(column=0, row=thisRow, pady=10)

root.mainloop()

#if __name__ == '__main__':



# model status
modelStatus = GetModelInfo()
print("Model is calculated" if modelStatus.property_has_results else "Model is not calculated")
print("Model contains printout report" if modelStatus.property_has_printout_report else "Model has not printout report")
print ("Model contains " +  str(modelStatus.property_node_count) + " nodes")
print ("Model contains " +  str(modelStatus.property_line_count) + " lines")
print ("Model contains " +  str(modelStatus.property_member_count) + " members")
print ("Model contains " +  str(modelStatus.property_surface_count) + " surfaces")
print ("Model contains " +  str(modelStatus.property_solid_count) + " solids")
print ("Model contains " +  str(modelStatus.property_lc_count) + " load cases")
print ("Model contains " +  str(modelStatus.property_co_count) + " load combinations")
print ("Model contains " +  str(modelStatus.property_rc_count) + " result classes")
print ("Model weight " +   str(modelStatus.property_weight))
print ("Model dimension x " + str(modelStatus.property_dimensions.x))
print ("Model dimension y " + str(modelStatus.property_dimensions.y))
print ("Model dimension z " + str(modelStatus.property_dimensions.z))

