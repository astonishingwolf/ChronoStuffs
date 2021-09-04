# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:10:17 2021

@author: dasgu
"""


import pychrono.core as chrono
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh
import math

chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\ChronoStuffs\Deform_trial_2\block_1_shapes")

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
        
print ("Example: create a rigid body based on a .obj mesh file");


mysystem      = chrono.ChSystemNSC()


chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.001);
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.001);

contact_material = chrono.ChMaterialSurfaceNSC()




body_A= chrono.ChBodyEasyMesh(chrono.GetChronoDataFile('/body_1_1.obj'), # mesh filename
                              700,             # density kg/m^3
                              True,             # automatically compute mass and inertia
                              True,             # visualize?>
                              True,             # collide?
                              contact_material, # contact material
                              )
body_A.SetPos(chrono.ChVectorD(0.5,0.5,0))
mysystem.Add(body_A)


# Rigid body part
body_B= chrono.ChBodyAuxRef()
body_B.SetPos(chrono.ChVectorD(0,0.5,0))
body_B.SetMass(16)
body_B.SetInertiaXX(chrono.ChVectorD(0.270,0.400,0.427))
body_B.SetInertiaXY(chrono.ChVectorD(0.057,0.037,-0.062))
body_B.SetFrame_COG_to_REF(chrono.ChFrameD(
            chrono.ChVectorD( 0.12,0.0,0),
            chrono.ChQuaternionD(1,0,0,0)))

# Attach a visualization shape .
# First load a .obj from disk into a ChTriangleMeshConnected:
mesh_for_visualization = chrono.ChTriangleMeshConnected()
mesh_for_visualization.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
# Optionally: you can scale/shrink/rotate the mesh using this:
mesh_for_visualization.Transform(chrono.ChVectorD(0.01,0,0), chrono.ChMatrix33D(1))
# Now the  triangle mesh is inserted in a ChTriangleMeshShape visualization asset, 
# and added to the body
visualization_shape = chrono.ChTriangleMeshShape()
visualization_shape.SetMesh(mesh_for_visualization)
body_B.AddAsset(visualization_shape)


# Add the collision shape.
# Again load a .obj file in Wavefront file format. NOTE: in this
# example we use the same .obj file as for visualization, but here one
# could do a better thing: using a different low-level-of-detail mesh for the 
# collision, so the simulation performance is not affected by many details such 
# as bolts and chamfers that may be wanted only for visualization.
mesh_for_collision = chrono.ChTriangleMeshConnected()
mesh_for_collision.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
# Optionally: you can scale/shrink/rotate the mesh using this:
mesh_for_collision.Transform(chrono.ChVectorD(0.01,0,0), chrono.ChMatrix33D(1))
body_B.GetCollisionModel().ClearModel()
body_B.GetCollisionModel().AddTriangleMesh(
            contact_material, # contact material
            mesh_for_collision, # the mesh 
            False,  # is it static?
            False)  # is it convex?
            # , mpos, mr,  # pos of mesh respect to REF and rotation matr.respect to REF 
            # 0.01) # 'inflating' radiust for triangles for increased robustness
body_B.GetCollisionModel().BuildModel()
body_B.SetCollide(True)

mysystem.Add(body_B)

terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(chrono.ChCoordsysD(chrono.ChVectorD(0,0.2,0), chrono.Q_from_AngX(-math.pi/2)))
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






# ---------------------------------------------------------------------
#
#  Create an Irrlicht application to visualize the system
#

myapplication = chronoirr.ChIrrApp(mysystem, 'PyChrono example', chronoirr.dimension2du(1024,768))

myapplication.AddTypicalSky()
#myapplication.AddTypicalLogo(chrono.GetChronoDataFile('logo_pychrono_alpha.png'))
myapplication.AddTypicalCamera(chronoirr.vector3df(0.5,0.5,1), chronoirr.vector3df(0,0,0))
#myapplication.AddTypicalLights()
myapplication.AddLightWithShadow(chronoirr.vector3df(3,6,2),    # point
                                 chronoirr.vector3df(0,0,0),    # aimpoint
                                 12,                 # radius (power)
                                 1,11,              # near, far
                                 55)                # angle of FOV

            # ==IMPORTANT!== Use this function for adding a ChIrrNodeAsset to all items
			# in the system. These ChIrrNodeAsset assets are 'proxies' to the Irrlicht meshes.
			# If you need a finer control on which item really needs a visualization proxy in
			# Irrlicht, just use application.AssetBind(myitem); on a per-item basis.

myapplication.AssetBindAll();

			# ==IMPORTANT!== Use this function for 'converting' into Irrlicht meshes the assets
			# that you added to the bodies into 3D shapes, they can be visualized by Irrlicht!

myapplication.AssetUpdateAll();

            # If you want to show shadows because you used "AddLightWithShadow()'
            # you must remember this:
myapplication.AddShadowAll();


# ---------------------------------------------------------------------
#
#  Run the simulation
#


myapplication.SetTimestep(0.005)

while(myapplication.GetDevice().run()):
    myapplication.BeginScene()
    myapplication.DrawAll()
    myapplication.DoStep()
    myapplication.EndScene()


