# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 03:07:56 2021

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
import pychrono.vehicle as veh



# ---------------------------------------------------------------------
#
# Parse command-line parameters
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\ChronoStuffs\Single_Leg\leg_shapes")
m_filename = "leg.py"
m_timestep = 0.01
m_length = 1.0
m_visualization = "irrlicht"
m_datapath = ""



###Soil Parameters
var_params = True

class MySoilParams (veh.SoilParametersCallback):
    def __init__(self):
        veh.SoilParametersCallback.__init__(self)
    def Set(self, x, y):
        if y > 0 :
            self.m_Bekker_Kphi = 0.2e6
            self.m_Bekker_Kc = 0
            self.m_Bekker_n = 1.1
            self.m_Mohr_cohesion = 0
            self.m_Mohr_friction = 30
            self.m_Janosi_shear = 0.01
            self.m_elastic_K = 4e7
            self.m_damping_R = 3e4
        else:
            self.m_Bekker_Kphi = 5301e3
            self.m_Bekker_Kc = 102e3
            self.m_Bekker_n = 0.793
            self.m_Mohr_cohesion = 1.3e3
            self.m_Mohr_friction = 31.1
            self.m_Janosi_shear = 1.2e-2
            self.m_elastic_K = 4e8
            self.m_damping_R = 3e4

# Global parameters for tire
tire_rad = 0.8
tire_vel_z0 = -3
tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
tire_w0 = tire_vel_z0 / tire_rad

# ----------------------------
# Create the mechanical system
# ----------------------------

mysystem = chrono.ChSystemSMC()
it = []
# Create the ground
ground = chrono.ChBody()
#it.append(ground)
ground.SetBodyFixed(True)
mysystem.Add(ground)# Remove the trailing .py and add / in case of file without ./
m_absfilename = os.path.abspath(m_filename)
m_modulename = os.path.splitext(m_absfilename)[0]

exported_items = chrono.ImportSolidWorksSystem(m_modulename)

# Add items to the physical system
mysystem = chrono.ChSystemNSC()

j=0
it = []
it1 = []
for my_item in exported_items:
    it.append(my_item)
    

#printing Component names

# Print exported items
for my_item in exported_items:
	print (my_item.GetName())

for my_item in exported_items:
    if(j==1):
        
        #it.append(my_item)
        #my_item.SetMass(10)
        # Load mesh
        my_item.SetMass(10)
        #my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
        #tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
        #my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
        mesh = chrono.ChTriangleMeshConnected()
        mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
        mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
        # Set visualization assets
        vis_shape = chrono.ChTriangleMeshShape()
        vis_shape.SetMesh(mesh)
        my_item.AddAsset(vis_shape)
        my_item.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))

        # Set collision shape
        material = chrono.ChMaterialSurfaceSMC()

        my_item.GetCollisionModel().ClearModel()
        my_item.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                                    mesh,                    # the mesh 
                                                    False,                   # is it static?
                                                    False,                 # is it convex?
                                                    chrono.ChVectorD(0,0,0), # position on body
                                                    chrono.ChMatrix33D(1),   # orientation on body 
                                                    0.01)                    # "thickness" for increased robustness
        my_item.GetCollisionModel().BuildModel()
        my_item.SetCollide(True)
        it1.append(my_item)
        mysystem.Add(my_item)
        #it.append(my_item)
        j = j+1
    
    if(j==2):
        
        #it.append(my_item)
        #my_item.SetMass(10)
        # Load mesh
        my_item.SetMass(10)
        #my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
        #tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
        #my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
        mesh = chrono.ChTriangleMeshConnected()
        mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
        mesh.Transform(chrono.ChVectorD(1,0,0), chrono.ChMatrix33D(1))
        # Set visualization assets
        vis_shape = chrono.ChTriangleMeshShape()
        vis_shape.SetMesh(mesh)
        my_item.AddAsset(vis_shape)
        my_item.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))

        # Set collision shape
        material = chrono.ChMaterialSurfaceSMC()

        my_item.GetCollisionModel().ClearModel()
        my_item.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                                    mesh,                    # the mesh 
                                                    False,                   # is it static?
                                                    False,                  # is it convex?
                                                    chrono.ChVectorD(0,0,0), # position on body
                                                    chrono.ChMatrix33D(1),   # orientation on body 
                                                    0.01)                    # "thickness" for increased robustness
        my_item.GetCollisionModel().BuildModel()
        my_item.SetCollide(True)
        it1.append(my_item)
        mysystem.Add(my_item)
        #it.append(my_item)
        j = j+1
        
    if(j==3):
        
        #it.append(my_item)
        #my_item.SetMass(10)
        # Load mesh
        my_item.SetMass(10)
        #my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
        #tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
        #my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
        mesh = chrono.ChTriangleMeshConnected()
        mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
        #mesh.Transform(chrono.ChVectorD(-1,0,0), chrono.ChMatrix33D(1))
        # Set visualization assets
        vis_shape = chrono.ChTriangleMeshShape()
        vis_shape.SetMesh(mesh)
        my_item.AddAsset(vis_shape)
        my_item.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))

        # Set collision shape
        material = chrono.ChMaterialSurfaceSMC()

        my_item.GetCollisionModel().ClearModel()
        my_item.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                                    mesh,                    # the mesh 
                                                    False,                   # is it static?
                                                    False,                   # is it convex?
                                                    chrono.ChVectorD(0,0,0), # position on body
                                                    chrono.ChMatrix33D(1),   # orientation on body 
                                                    0.01)                    # "thickness" for increased robustness
        my_item.GetCollisionModel().BuildModel()
        my_item.SetCollide(True)
        it1.append(my_item)
        mysystem.Add(my_item)
        #it.append(my_item)
        j = j+1
    elif(j>3):
        it1.append(my_item)
        mysystem.Add(my_item)
        #it.append(my_item)
        #it.append(my_item)
        j = j+1
        #it.append(my_item)
    else :
        it1.append(my_item)
        #it.append(my_item)
        j= j+1
    

#printing Component names

# Print exported items
for my_item in exported_items:
	print (my_item.GetName())



       
# Optionally set some solver parameters.
#Motors Variables
st = chrono.ChVectorD(0.0122275345305963,0.00120884241999014,0.0332147998549766)
sc = chrono.ChVectorD(0.245,0.0,0.0)
#Between Torso_backet-2 and torso
my_motor = chrono.ChLinkMotorRotationSpeed()
my_motor.Initialize(it1[1],   # the first connected body
                    it1[2],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.0354978494402492,0.0296733424655571,0.00525565296559194))) # where to create the motor in abs.space
#my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI*0) # ang.speed: 180°/s
my_motor.SetMotorFunction(my_angularspeed)
mysystem.Add(my_motor)
#Between Torso_backet-2 and torso
my_motor1 = chrono.ChLinkMotorRotationSpeed()
my_motor1.Initialize(it1[2],   # the first connected body
                    it1[3],   # the second connected body
                    chrono.ChFrameD(chrono.ChVectorD(0.141018628033538,-0.090598704515718,0.0952556529655919))) # where to create the motor in abs.space
my_angularspeed = chrono.ChFunction_Const(chrono.CH_C_PI) # ang.speed: 180°/s
my_motor1.SetMotorFunction(my_angularspeed)
mysystem.Add(my_motor1)





terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,-0.15,0), chrono.Q_from_AngX(-math.pi/2)))
terrain.Initialize(2.0, 6.0, 0.04)

my_params = MySoilParams()
if var_params:
    # Location-dependent soil properties
    terrain.RegisterSoilParametersCallback(my_params)
else :
    # Constant soil properties
    terrain.SetSoilParameters(0.2e6,  # Bekker Kphi
                               0,      # Bekker Kc
                               1.1,    # Bekker n exponent
                               0,      # Mohr cohesive limit (Pa)
                               30,     # Mohr friction limit (degrees)
                               0.01,   # Janosi shear coefficient (m)
                               4e7,    # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
                               3e4     # Damping (Pa s/m), proportional to negative vertical speed (optional)
    )

# Set terrain visualization mode
terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)


#my_system.SetMaxPenetrationRecoverySpeed(1.00)
my_solver = chrono.ChSolverBB()
mysystem.SetSolver(my_solver)
my_solver.SetMaxIterations(600)
my_solver.EnableWarmStart(True);
mysystem.Set_G_acc(chrono.ChVectorD(0,-9.8,0))
    
if m_visualization == "irrlicht":

    # ---------------------------------------------------------------------
    #
    #  Create an Irrlicht application to visualize the system
    #

    myapplication = chronoirr.ChIrrApp(mysystem, 'Deformable soil', chronoirr.dimension2du(1280,720), False, True)
    myapplication.AddTypicalSky()
    #myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
    myapplication.AddTypicalCamera(chronoirr.vector3df(2.0,1.4,0.0), chronoirr.vector3df(0,tire_rad,0))
    myapplication.AddTypicalLights()
    myapplication.AddLightWithShadow(chronoirr.vector3df(1.5,5.5,-2.5),    # point
                                 chronoirr.vector3df(0,0,0),           # aim point
                                 3,                                    # radius (power)
                                 2.2, 7.2,                             # near, far
                                 40,                                   # angle of FOV
                                 512,                                  # resoluition
                                 chronoirr.SColorf(0.8,0.8,1))         # light color
    myapplication.AssetBindAll()
    myapplication.AssetUpdateAll()
    myapplication.AddShadowAll()

    
    while(myapplication.GetDevice().run()):
        myapplication.BeginScene()
        myapplication.DrawAll()
        myapplication.DoStep()
        myapplication.EndScene()
        