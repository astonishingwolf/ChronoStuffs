# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\ChronoStuffs\dl_trail\Cad\double.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'dl_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Part1-3')
body_1.SetPos(chrono.ChVectorD(0.075,-0.155,-0.02))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186548,0,0))
body_1.SetMass(0.0422867258771282)
body_1.SetInertiaXX(chrono.ChVectorD(0.000139006448574143,1.12111953274713e-05,0.000138575840941091))
body_1.SetInertiaXY(chrono.ChVectorD(-3.72231275648862e-21,-1.05129141318091e-22,-1.37597358291107e-20))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.81195036356879e-17,-1.30793215643074e-17,0.1),chrono.ChQuaternionD(1,0,0,0)))
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
body_1.SetBodyFixed(False)
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
body_2.SetPos(chrono.ChVectorD(0.045,0.00499999999999999,-0.02))
body_2.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186548,0,0))
body_2.SetMass(0.0422867258771282)
body_2.SetInertiaXX(chrono.ChVectorD(0.000139006448574143,1.12111953274713e-05,0.000138575840941091))
body_2.SetInertiaXY(chrono.ChVectorD(-3.72231275648862e-21,-1.05129141318091e-22,-1.5527275355154e-20))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.81195036356879e-17,-1.30793215643074e-17,0.1),chrono.ChQuaternionD(1,0,0,0)))
mesh_2 = chrono.ChTriangleMeshConnected()
mesh_2.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh_2.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_2 = chrono.ChMaterialSurfaceSMC()
body_2.GetCollisionModel().ClearModel()
body_2.GetCollisionModel().AddTriangleMesh(material_2,                # contact material
                                            mesh_2,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_2.GetCollisionModel().BuildModel()
body_2.SetBodyFixed(False)
body_2.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Part1-1')
body_3.SetPos(chrono.ChVectorD(0.015,-0.015,-0.2))
body_3.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_3.SetMass(0.0422867258771282)
body_3.SetInertiaXX(chrono.ChVectorD(0.000139006448574143,0.000138575840941091,1.12111953274713e-05))
body_3.SetInertiaXY(chrono.ChVectorD(1.05129141318091e-22,-3.72231275648862e-21,1.46435055921323e-20))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.81195036356879e-17,-1.30793215643074e-17,0.1),chrono.ChQuaternionD(1,0,0,0)))
mesh_3 = chrono.ChTriangleMeshConnected()
mesh_3.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_1_1.obj'))
mesh_3.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
material_3 = chrono.ChMaterialSurfaceSMC()
body_3.GetCollisionModel().ClearModel()
body_3.GetCollisionModel().AddTriangleMesh(material_3,                # contact material
                                            mesh_3,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_3.GetCollisionModel().BuildModel()
body_3.SetBodyFixed(False)
body_3.SetCollide(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_3.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_3)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.17,-0.015,-0.02)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.14,-0.015,-0.02)
dB = chrono.ChVectorD(1,0,0)
link_1.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
#exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.17,-0.015,-0.02)
cB = chrono.ChVectorD(-0.14,-0.015,-0.02)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_2.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
#exported_items.append(link_2)
#

# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.03,-0.03,0)
cB = chrono.ChVectorD(0.03,-0.195,-0.035)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_3.Initialize(body_3,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
#exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.03,-0.03,0)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.03,-0.195,-0.035)
dB = chrono.ChVectorD(-1,0,0)
link_4.SetFlipped(True)
link_4.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
#exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Part1-3 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.14,-0.175,-0.02)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(-0.11,-0.175,-0.02)
dB = chrono.ChVectorD(1,0,0)
link_5.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
#exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.14,-0.175,-0.02)
cB = chrono.ChVectorD(-0.11,-0.175,-0.02)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_6.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
#exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Part1-3 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.06,-0.195,-0.035)
cB = chrono.ChVectorD(0.06,-0.355,-0.035)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_7.Initialize(body_2,body_1,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
#exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.06,-0.195,-0.035)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.06,-0.355,-0.035)
dB = chrono.ChVectorD(-1,0,0)
link_8.SetFlipped(True)
link_8.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
#exported_items.append(link_8)


# Mate constraint: Parallel1 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.015,-0.015,0)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.03,-0.195,-0.00499999999999998)
dB = chrono.ChVectorD(0,6.93889390390723e-18,1)
link_9.Initialize(body_3,body_2,False,cA,cB,dA,dB)
link_9.SetName("Parallel1")
#exported_items.append(link_9)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: Part1-3 ,  SW ref.type:2 (2)

link_10 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.03,-0.195,-0.00499999999999998)
cB = chrono.ChVectorD(0.06,-0.355,-0.00499999999999998)
dA = chrono.ChVectorD(0,6.93889390390723e-18,1)
dB = chrono.ChVectorD(0,-6.93889390390723e-18,1)
link_10.Initialize(body_2,body_1,False,cA,cB,dB)
link_10.SetDistance(0)
link_10.SetName("Coincident4")
#exported_items.append(link_10)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.03,-0.195,-0.00499999999999998)
dA = chrono.ChVectorD(0,6.93889390390723e-18,1)
cB = chrono.ChVectorD(0.06,-0.355,-0.00499999999999998)
dB = chrono.ChVectorD(0,-6.93889390390723e-18,1)
link_11.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_11.SetName("Coincident4")
#exported_items.append(link_11)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: double ,  SW ref.type:4 (4)

link_12 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_12.Initialize(body_3,body_0,False,cA,cB,dB)
link_12.SetDistance(0)
link_12.SetName("Coincident5")
#exported_items.append(link_12)

link_13 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_13.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_13.SetName("Coincident5")
#exported_items.append(link_13)


# Mate constraint: Coincident6 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: double ,  SW ref.type:4 (4)

link_14 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.015,-0.015,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_14.Initialize(body_3,body_0,False,cA,cB,dB)
link_14.SetDistance(0)
link_14.SetName("Coincident6")
#exported_items.append(link_14)

link_15 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.015,-0.015,0)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_15.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_15.SetName("Coincident6")
#exported_items.append(link_15)


# Mate constraint: Coincident7 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_3 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: double ,  SW ref.type:4 (4)

link_16 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-0.03,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_16.Initialize(body_3,body_0,False,cA,cB,dB)
link_16.SetDistance(0)
link_16.SetName("Coincident7")
#exported_items.append(link_16)

link_17 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-0.03,0)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_17.SetFlipped(True)
link_17.Initialize(body_3,body_0,False,cA,cB,dA,dB)
link_17.SetName("Coincident7")
#exported_items.append(link_17)

