# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'block_shapes/' 

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
body_1.SetPos(chrono.ChVectorD(0.035,0.05,0.045))
body_1.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0))
body_1.SetMass(0.027)
body_1.SetInertiaXX(chrono.ChVectorD(4.05e-06,4.05e-06,4.05e-06))
body_1.SetInertiaXY(chrono.ChVectorD(-7.12456352594538e-23,-1.40424510127607e-22,-1.05879118406788e-22))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.45090551867564e-18,-2.07394448555683e-18,0.015),chrono.ChQuaternionD(1,0,0,0)))
body_1.SetBodyFixed(True)

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
body_2.SetPos(chrono.ChVectorD(0.115,0.05,0.045))
body_2.SetRot(chrono.ChQuaternionD(0.707106781186548,0.707106781186547,0,0))
body_2.SetMass(0.027)
body_2.SetInertiaXX(chrono.ChVectorD(4.05e-06,4.05e-06,4.05e-06))
body_2.SetInertiaXY(chrono.ChVectorD(-7.12456352594538e-23,-1.40424510127607e-22,-1.05879118406788e-22))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.45090551867564e-18,-2.07394448555683e-18,0.015),chrono.ChQuaternionD(1,0,0,0)))
body_2.SetBodyFixed(True)

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_2.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_2)




# Mate constraint: Coincident1 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.035,0.02,0.045)
cB = chrono.ChVectorD(0.115,0.02,0.045)
dA = chrono.ChVectorD(0,-1,1.22464679914735e-16)
dB = chrono.ChVectorD(0,-1,1.22464679914735e-16)
link_1.Initialize(body_1,body_2,False,cA,cB,dB)
link_1.SetDistance(0)
link_1.SetName("Coincident1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.035,0.02,0.045)
dA = chrono.ChVectorD(0,-1,1.22464679914735e-16)
cB = chrono.ChVectorD(0.115,0.02,0.045)
dB = chrono.ChVectorD(0,-1,1.22464679914735e-16)
link_2.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_2.SetName("Coincident1")
exported_items.append(link_2)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.02,0.02,0.06)
cB = chrono.ChVectorD(0.1,0.02,0.06)
dA = chrono.ChVectorD(0,1.22464679914735e-16,1)
dB = chrono.ChVectorD(0,1.22464679914735e-16,1)
link_3.Initialize(body_1,body_2,False,cA,cB,dB)
link_3.SetDistance(0)
link_3.SetName("Coincident2")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.02,0.02,0.06)
dA = chrono.ChVectorD(0,1.22464679914735e-16,1)
cB = chrono.ChVectorD(0.1,0.02,0.06)
dB = chrono.ChVectorD(0,1.22464679914735e-16,1)
link_4.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_4.SetName("Coincident2")
exported_items.append(link_4)


# Mate constraint: Distance1 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_2 , SW name: Part1-2 ,  SW ref.type:2 (2)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.05,0.02,0.06)
cB = chrono.ChVectorD(0.1,0.02,0.06)
dA = chrono.ChVectorD(1,2.83256473634769e-32,2.31296463463574e-16)
dB = chrono.ChVectorD(-1,0,0)
link_5.Initialize(body_1,body_2,False,cA,cB,dB)
link_5.SetDistance(-0.05)
link_5.SetName("Distance1")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.05,0.02,0.06)
dA = chrono.ChVectorD(1,2.83256473634769e-32,2.31296463463574e-16)
cB = chrono.ChVectorD(0.1,0.02,0.06)
dB = chrono.ChVectorD(-1,0,0)
link_6.SetFlipped(True)
link_6.Initialize(body_1,body_2,False,cA,cB,dA,dB)
link_6.SetName("Distance1")
exported_items.append(link_6)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_7 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.02,0.02,0.03)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,-1.22464679914735e-16,-1)
dB = chrono.ChVectorD(0,0,1)
link_7.Initialize(body_1,body_0,False,cA,cB,dB)
link_7.SetDistance(-0.03)
link_7.SetName("Distance3")
exported_items.append(link_7)

link_8 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.02,0.02,0.03)
dA = chrono.ChVectorD(0,-1.22464679914735e-16,-1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_8.SetFlipped(True)
link_8.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_8.SetName("Distance3")
exported_items.append(link_8)


# Mate constraint: Distance4 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)

link_9 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0.02,0.02,0.06)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(-1,0,0)
link_9.Initialize(body_0,body_1,False,cA,cB,dB)
link_9.SetDistance(-0.02)
link_9.SetName("Distance4")
exported_items.append(link_9)

link_10 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0.02,0.02,0.06)
dB = chrono.ChVectorD(-1,0,0)
link_10.SetFlipped(True)
link_10.Initialize(body_0,body_1,False,cA,cB,dA,dB)
link_10.SetName("Distance4")
exported_items.append(link_10)


# Mate constraint: Distance5 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)

link_11 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0.035,0.02,0.045)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,-1,1.22464679914735e-16)
link_11.Initialize(body_0,body_1,False,cA,cB,dB)
link_11.SetDistance(-0.02)
link_11.SetName("Distance5")
exported_items.append(link_11)

link_12 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.035,0.02,0.045)
dB = chrono.ChVectorD(0,-1,1.22464679914735e-16)
link_12.SetFlipped(True)
link_12.Initialize(body_0,body_1,False,cA,cB,dA,dB)
link_12.SetName("Distance5")
exported_items.append(link_12)

