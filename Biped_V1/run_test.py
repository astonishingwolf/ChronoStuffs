#-------------------------------------------------------------------------------
# Name:        modulo1
# Purpose:
#
# Author:      tasora
#
# Created:     1/1/2019
# Copyright:   (c) tasora 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

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

try:
	opts, args = getopt.getopt(sys.argv[1:],"f:d:T:v:p:",["filename=","timestep=","Tlength=","visualization=","datapath="])
except getopt.GetoptError:
	#print ("run_test.py -f <filename> [-d <timestep> -T <length> -v <pov|irrlicht> -p <chronodatapath>]")
	sys.exit(2)
for opt, arg in opts:
	print ("opt:", opt, "  arg", arg)
	if   opt in ("-d", "--timestep"):
		m_timestep = float(arg)
	elif opt in ("-T", "--Tlength"):
		m_length = float(arg)
	elif opt in ("-f", "--filename"):
		m_filename = arg
	elif opt in ("-v", "--visualization"):
		m_visualization = arg
	elif opt in ("-p", "--datapath"):
		m_datapath = arg
		
if m_filename == "":
	print ("run_test.py -f <filename> [-d <timestep> -T <length> -v <pov|irrlicht> -p <chronodatapath>]")
	sys.exit(2)

if not os.path.isfile(m_filename):
	print ("Error. Filename " + m_filename + " does not exist.")
	sys.exit(2)
    
chrono.SetChronoDataPath(m_datapath)

print ("  file to load is ", m_filename)
print ("  timestep is ", m_timestep)
print ("  length is ", m_length)
print ("  data path for fonts etc.: ", m_datapath)



# ---------------------------------------------------------------------
#
#  load the file generated by the SolidWorks CAD plugin
#  and add it to the ChSystem.
#

# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]

print ("Loading C::E scene...");

exported_items = chrono.ImportSolidWorksSystem(m_modulename)

print ("...loading done!");


# Print exported items
for my_item in exported_items:
	print (my_item.GetName())

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
	
		
		
if m_visualization == "pov":

	# ---------------------------------------------------------------------
	#
	#  Render a short animation by generating scripts
	#  to be used with POV-Ray
	#

	pov_exporter = postprocess.ChPovRay(my_system)

	 # Sets some file names for in-out processes.
	pov_exporter.SetTemplateFile        ("_template_POV.pov")
	pov_exporter.SetOutputScriptFile    ("rendering_frames.pov")
	if not os.path.exists("output"):
		os.mkdir("output")
	if not os.path.exists("anim"):
		os.mkdir("anim")
	pov_exporter.SetOutputDataFilebase("output/my_state")
	pov_exporter.SetPictureFilebase("anim/picture")

	 # Sets the viewpoint, aimed point, lens angle
	pov_exporter.SetCamera(chrono.ChVectorD(0.2,0.3,0.5), chrono.ChVectorD(0,0,0), 35)

	 # Sets the default ambient light and default light lamp
	pov_exporter.SetAmbientLight(chrono.ChColor(1,1,1))
	pov_exporter.SetLight(chrono.ChVectorD(-2,2,-1), chrono.ChColor(1.1,1.2,1.2), True)

	 # Sets other settings
	pov_exporter.SetPictureSize(640,480)
	pov_exporter.SetAmbientLight(chrono.ChColor(2,2,2))

	 # Turn on the rendering of xyz axes for the centers of gravity or reference frames:
	#pov_exporter.SetShowCOGs  (1, 0.05)
	#pov_exporter.SetShowFrames(1, 0.02)
	#pov_exporter.SetShowLinks(1, 0.03)
	pov_exporter.SetShowContacts(True,
								postprocess.ChPovRay.SYMBOL_VECTOR_SCALELENGTH,
								0.2,    # scale
								0.0007, # width
								0.1,    # max size
								True,0,0.5 ) # colormap on, blue at 0, red at 0.5

	 # Add additional POV objects/lights/materials in the following way, entering
	 # an optional text using the POV scene description laguage. This will be
	 # appended to the generated .pov file.
	 # For multi-line strings, use the python ''' easy string delimiter.
	pov_exporter.SetCustomPOVcommandsScript(
	'''
	light_source{ <1,3,1.5> color rgb<1.1,1.1,1.1> }
	''')

	 # Tell which physical items you want to render
	pov_exporter.AddAll()


	 # Create the two .pov and .ini files for POV-Ray (this must be done
	 # only once at the beginning of the simulation).
	pov_exporter.ExportScript()


	 # Perform a short simulation
	nstep =0
	while (my_system.GetChTime() < m_length) :

		my_system.DoStepDynamics(m_timestep)

		#if math.fmod(nstep,10) ==0 :
		print ('time=', my_system.GetChTime() )

			# Create the incremental nnnn.dat and nnnn.pov files that will be load
			# by the pov .ini script in POV-Ray (do this at each simulation timestep)
		pov_exporter.ExportData()

		nstep = nstep +1

	print ("\n\nOk, Simulation done!");
	time.sleep(2)

	
	
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
