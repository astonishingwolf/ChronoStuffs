# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'block_1_shapes/' 

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
body_1.SetPos(chrono.ChVectorD(0.035,0.045,0.02))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.027)
body_1.SetInertiaXX(chrono.ChVectorD(4.05e-06,4.05e-06,4.05e-06))
body_1.SetInertiaXY(chrono.ChVectorD(1.40424510127607e-22,-7.12456352594538e-23,1.05879118406788e-22))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-2.40188740830212e-18,-2.14846769911989e-18,0.015),chrono.ChQuaternionD(1,0,0,0)))

# Visualization shape 
body_1_1_shape = chrono.ChObjShapeFile() 
body_1_1_shape.SetFilename(shapes_dir +'body_1_1.obj') 
body_1_1_level = chrono.ChAssetLevel() 
body_1_1_level.GetFrame().SetPos(chrono.ChVectorD(0,0,0)) 
body_1_1_level.GetFrame().SetRot(chrono.ChQuaternionD(1,0,0,0)) 
body_1_1_level.GetAssets().push_back(body_1_1_shape) 
body_1.GetAssets().push_back(body_1_1_level) 

exported_items.append(body_1)




# Mate constraint: Distance1 [MateDistanceDim] type:5 align:0 flip:True
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_1 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.035,0.045,0.05)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_1.Initialize(body_1,body_0,False,cA,cB,dB)
link_1.SetDistance(0.05)
link_1.SetName("Distance1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.035,0.045,0.05)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_2.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_2.SetName("Distance1")
exported_items.append(link_2)


# Mate constraint: Distance2 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)
#   Entity 1: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,0,0)
cB = chrono.ChVectorD(0.02,0.03,0.05)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,-1,0)
link_3.Initialize(body_0,body_1,False,cA,cB,dB)
link_3.SetDistance(-0.03)
link_3.SetName("Distance2")
exported_items.append(link_3)

link_4 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0.02,0.03,0.05)
dB = chrono.ChVectorD(0,-1,0)
link_4.SetFlipped(True)
link_4.Initialize(body_0,body_1,False,cA,cB,dA,dB)
link_4.SetName("Distance2")
exported_items.append(link_4)


# Mate constraint: Distance3 [MateDistanceDim] type:5 align:1 flip:False
#   Entity 0: C::E name: body_1 , SW name: Part1-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: Assem1 ,  SW ref.type:4 (4)

link_5 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0.02,0.06,0.05)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(-1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_5.Initialize(body_1,body_0,False,cA,cB,dB)
link_5.SetDistance(-0.02)
link_5.SetName("Distance3")
exported_items.append(link_5)

link_6 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0.02,0.06,0.05)
dA = chrono.ChVectorD(-1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_6.SetFlipped(True)
link_6.Initialize(body_1,body_0,False,cA,cB,dA,dB)
link_6.SetName("Distance3")
exported_items.append(link_6)

