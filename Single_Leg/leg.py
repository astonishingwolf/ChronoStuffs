# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\ChronoStuffs\Single_Leg\Assem1.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'leg_shapes/' 
chrono.SetChronoDataPath(r"C:\Users\dasgu\Documents\ChronoStuffs\Single_Leg\leg_shapes")

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 
material = chrono.ChMaterialSurfaceSMC()
body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)
#vector = chrono.ChVectorD(0.1104978494402492,0.1296733424655571,0.1402556529655919)
# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('Part1-1')
#body_1.SetPos(vector)
body_1.SetPos(chrono.ChVectorD(0.0104978494402492,0.0296733424655571,0.0402556529655919))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.0396985623970672)
body_1.SetInertiaXX(chrono.ChVectorD(6.2778407134888e-06,1.22778407134888e-05,1.26008970674175e-05))
body_1.SetInertiaXY(chrono.ChVectorD(7.94093388050907e-23,8.73502726855997e-22,-3.97046694025453e-22))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(0.025,-1.3335384458986e-18,-1.33353844589861e-20),chrono.ChQuaternionD(1,0,0,0)))
#body_1.SetBodyFixed(True)
#body_1.SetMass(10)
#my_item.SetInertiaXX(chrono.ChVectorD(20, 20, 20))
#tire_center = chrono.ChVectorD(0, 0.02 + tire_rad, -1.5)
#my_item.SetPos(tire_center + chrono.ChVectorD(0, 0.3, 0))
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
#it1.append(my_item)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
#body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)



# Rigid body part
body_2= chrono.ChBodyAuxRef()
body_2.SetName('Part2-1')
body_2.SetPos(chrono.ChVectorD(0.025605276447128,0.0409488468700518,0.0102556529655919))
body_2.SetRot(chrono.ChQuaternionD(0.249148402747755,-0.249148402747755,0.661759075047893,-0.661759075047893))
body_2.SetMass(0.160397124794135)
body_2.SetInertiaXX(chrono.ChVectorD(0.00045872830467923,2.47056814269776e-05,0.000458812368247504))
body_2.SetInertiaXY(chrono.ChVectorD(2.66861361471055e-21,3.20310375941796e-07,-9.24640055028983e-21))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.57931825172969e-18,-1.293807930433e-18,0.095),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
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
body_2.SetBodyFixed(True)
body_2.SetCollide(True)
#body_2.SetCollide(True)

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
#body_2.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_2)



# Rigid body part
body_3= chrono.ChBodyAuxRef()
body_3.SetName('Part2-2')
body_3.SetPos(chrono.ChVectorD(0.150903303044148,-0.0793162757020887,0.0402556529655919))
body_3.SetRot(chrono.ChQuaternionD(0.661846266309028,0.661846266309028,-0.248916692435038,-0.248916692435038))
body_3.SetMass(0.160397124794135)
body_3.SetInertiaXX(chrono.ChVectorD(0.000458727856132399,2.47056814269776e-05,0.000458812816794334))
body_3.SetInertiaXY(chrono.ChVectorD(9.51601863854212e-21,3.20251197179075e-07,-1.43624894497348e-21))
body_3.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-9.57931825172969e-18,-1.293807930433e-18,0.095),chrono.ChQuaternionD(1,0,0,0)))
mesh = chrono.ChTriangleMeshConnected()
mesh.LoadWavefrontMesh(chrono.GetChronoDataFile('/body_2_1.obj'))
mesh.Transform(chrono.ChVectorD(0,0,0), chrono.ChMatrix33D(1))
# Set visualization assets
#vis_shape = chrono.ChTriangleMeshShape()
#vis_shape.SetMesh(mesh)
#my_item.AddAsset(vis_shape)
#my_item.AddAsset(chrono.ChColorAsset(0.3, 0.3, 0.3))
# Set collision shape
material = chrono.ChMaterialSurfaceSMC()

body_3.GetCollisionModel().ClearModel()
body_3.GetCollisionModel().AddTriangleMesh(material,                # contact material
                                            mesh,                    # the mesh 
                                            False,                   # is it static?
                                            False,                   # is it convex?
                                            chrono.ChVectorD(0,0,0), # position on body
                                            chrono.ChMatrix33D(1),   # orientation on body 
                                            0.01)                    # "thickness" for increased robustness
body_3.GetCollisionModel().BuildModel()
#body_1.SetBodyFixed(True)
body_3.SetBodyFixed(True)
body_3.SetCollide(True)
#body_3.SetCollide(True)

# Visualization shape 
body_2_1_shape = chrono.ChObjShapeFile() 
body_2_1_shape.SetFilename(shapes_dir +'body_2_1.obj') 
body_2_1_level = chrono.ChAssetLevel() 
body_2_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_2_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_2_1_level.GetAssets().push_back(body_2_1_shape) 
#body_3.GetAssets().push_back(body_2_1_level) 

exported_items.append(body_3)




# Mate constraint: Concentric1 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part2-1 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0354978494402492,0.0296733424655571,0.00525565296559194)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.0354978494402489,0.0296733424655573,0.0952556529655919)
dB = chrono.ChVectorD(0,0,-1)
link_1.SetFlipped(True)
link_1.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.0354978494402492,0.0296733424655571,0.00525565296559194)
cB = chrono.ChVectorD(0.0354978494402489,0.0296733424655573,0.0952556529655919)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Coincident1 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part2-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.0604978494402492,0.0146733424655571,0.0252556529655919)
cB = chrono.ChVectorD(0.162186705431153,-0.0919816359270917,0.0252556529655919)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_3.Initialize(body_1,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident1")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.0604978494402492,0.0146733424655571,0.0252556529655919)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.162186705431153,-0.0919816359270917,0.0252556529655919)
dB = chrono.ChVectorD(0,0,1)
link_4.SetFlipped(True)
link_4.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident1")
exported_items.append(link_4)


# Mate constraint: Concentric2 [MateConcentric] type:1 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Part2-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.141018628033538,-0.090598704515718,0.0952556529655919)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(0.141018628033541,-0.0905987045157207,-0.0447443470344081)
dB = chrono.ChVectorD(0,0,1)
link_5.SetFlipped(True)
link_5.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_5.SetName("Concentric2")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateGeneric()
link_6.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(0.141018628033538,-0.090598704515718,0.0952556529655919)
cB = chrono.ChVectorD(0.141018628033541,-0.0905987045157207,-0.0447443470344081)
dA = chrono.ChVectorD(0,0,-1)
dB = chrono.ChVectorD(0,0,1)
link_6.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_6.SetName("Concentric2")
exported_items.append(link_6)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: Part2-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_3 , SW name: Part2-2 ,  SW ref.type:2 (2)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.162186705431153,-0.0919816359270917,0.0252556529655919)
cB = chrono.ChVectorD(0.0144149907628232,-0.212342365664154,0.0252556529655919)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,-1)
link_7.Initialize(body_2,body_3,False,cA,cB,dB)
link_7.SetDistance(0)
link_7.SetName("Coincident2")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.162186705431153,-0.0919816359270917,0.0252556529655919)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0.0144149907628232,-0.212342365664154,0.0252556529655919)
dB = chrono.ChVectorD(0,0,-1)
link_8.SetFlipped(True)
link_8.Initialize(body_2,body_3,False,cA,cB,dA,dB)
link_8.SetName("Coincident2")
exported_items.append(link_8)

