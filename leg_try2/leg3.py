# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'leg3_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Part1-1')
body_1.SetPos(chrono.ChVectorD(0.03,0.03,0))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.630035180670545)
body_1.SetInertiaXX(chrono.ChVectorD(0.0067540220144884,0.00672552980409845,0.000563154205536241))
body_1.SetInertiaXY(chrono.ChVectorD(1.07004529171912e-21,2.27474668452083e-19,-6.88920130433497e-20))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.68026550497764e-18,1.05276606986086e-17,0.175),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material = chrono.ChMaterialSurfaceSMC()
body_1.GetCollisionModel().ClearModel()
body_1.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                            mesh,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_1.GetCollisionModel().BuildModel()
body_1.SetBodyFixed(True)
body_1.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Part1-2')
body_2.SetPos(chrono.ChVectorD(0.09,0.0361375699422959,-0.189930232162322))
body_2.SetRot(chrono.ChQuaternionD(0.99993539806359,0.0113666045681759,0,0))
body_2.SetMass(0.630035180670545)
body_2.SetInertiaXX(chrono.ChVectorD(0.0067540220144884,0.00672234550726188,0.000566338502372811))
body_2.SetInertiaXY(chrono.ChVectorD(6.24066393238186e-21,2.27391565142585e-19,-0.000140045326155197))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(4.68026550497764e-18,1.05276606986086e-17,0.175),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
#vis_shape = chrono.ChTriangleMeshShape()
#vis_shape.SetMesh(mesh)
#my_item.AddAsset(vis_shape)
#my_item.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material = chrono.ChMaterialSurfaceSMC()

body_2.GetCollisionModel().ClearModel()
body_2.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                            mesh,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_2.GetCollisionModel().BuildModel()
#body_1.SetBodyFixed(True)
body_2.SetBodyFixed(False)
body_2.SetCollide(True)
#body_2.SetCollide(True)'

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_2)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.315,0.03,0.08)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.255,0.0300000000000003,0.0799999999999973)
dB = chrono.ChVectorD(1,0,0)
link_1.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.315,0.03,0.08)
cB = chrono.ChVectorD(-0.255,0.0300000000000003,0.0799999999999973)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.06,0,0.35)
cB = chrono.ChVectorD(0.06,-0.00181078726019682,0.159297375832281)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_3.Initialize(body_1,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.06,0,0.35)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.06,-0.00181078726019682,0.159297375832281)
dB = chrono.ChVectorD(-1,0,0)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.03,0.03,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_5.Initialize(body_1,body_0,False,cA,cB,dB)
link_5.SetDistance(0)
link_5.SetName("Coincident3")
#exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.03,0.03,0)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_6.SetFlipped(True)
link_6.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_6.SetName("Coincident3")
#exported_items.append(link_6)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.35)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(0,1,0)
link_7.Initialize(body_1,body_0,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident4")
#exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.35)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_8.SetName("Coincident4")
#exported_items.append(link_8)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_9 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.35)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_9.Initialize(body_1,body_0,False,cA,cB,dB)
link_9.SetDistance(0)
link_9.SetName("Coincident5")
#exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(6.93889390390723e-18,0,0.35)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_10.SetFlipped(True)
link_10.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_10.SetName("Coincident5")
#exported_items.append(link_10)

