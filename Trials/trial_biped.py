# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:19:27 2021

@author: dasgu
"""

def main():
    pass

if __name__ == '__main__':
    main()


import os
import math
import time
import sys, getopt
import pychrono as chrono
import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr


# ---------------------------------------------------------------------
#
# Parse command-line parameters

m_filename = "vb.py"
m_timestep = 0.01
m_length = 1.0
m_visualization = "irrlicht"
m_datapath = ""

# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]

exported_items = chrono.ImportSolidWorksSystem(m_modulename)

# Add items to the physical system
my_system = chrono.ChSystemNSC()
for my_item in exported_items:
	my_system.Add(my_item)
    
		
# Optionally set some solver parameters.

#my_system.SetMaxPenetrationRecoverySpeed(1.00)
my_solver = chrono.ChSolverBB()
my_system.SetSolver(my_solver)
my_solver.SetMaxIterations(600)
my_solver.EnableWarmStart(True);
my_system.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
    
if m_visualization == "irrlicht":

	# ---------------------------------------------------------------------
	#
	#  Create an Irrlicht application to visualize the system
	#

	myapplication = chronoirr.ChIrrApp(my_system, 'Test', chronoirr.dimension2du(1280,720))

	myapplication.AddTypicalSky(chrono.GetChronoDataPath() + 'skybox/')
	myapplication.AddTypicalLogo(chrono.GetChronoDataPath() + 'logo_pychrono_alpha.png')
	myapplication.AddTypicalCamera(chronoirr.vector3df(1,1,1),chronoirr.vector3df(0.0,0.0,0.0))
	myapplication.AddTypicalLights()
	#myapplication.AddLightWithShadow(chronoirr.vector3df(10,20,10),chronoirr.vector3df(0,2.6,0), 10 ,10,40, 60, 512);

				# ==IMPORTANT!== Use this function for adding a ChIrrNodeAsset to all items
				# in the system. These ChIrrNodeAsset assets are 'proxies' to the Irrlicht meshes.
				# If you need a finer control on which item really needs a visualization proxy in
				# Irrlicht, just use application.AssetBind(myitem); on a per-item basis.

	myapplication.AssetBindAll();

				# ==IMPORTANT!== Use this function for 'converting' into Irrlicht meshes the assets
				# that you added to the bodies into 3D shapes, they can be visualized by Irrlicht!

	myapplication.AssetUpdateAll();

				# ==IMPORTANT!== Use this function for enabling cast soft shadows

	#myapplication.AddShadowAll();

	# ---------------------------------------------------------------------
	#
	#  Run the simulation forever until windows is closed
	#

	myapplication.SetTimestep(m_timestep);
	
	while(myapplication.GetDevice().run()):
		myapplication.BeginScene()
		myapplication.DrawAll()
		myapplication.DoStep()
		myapplication.EndScene()
