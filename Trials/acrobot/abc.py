# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: C:\Users\dasgu\Documents\ChronoStuffs\Trials\acrobot\assem.SLDASM


import pychrono as chrono 
import builtins 

shapes_dir = 'abc_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('link-2')
body_1.SetPos(chrono.ChVectorD(-0.015,-0.045,-0.09))
body_1.SetRot(chrono.ChQuaternionD(0,0,1,0))
body_1.SetMass(0.129698562397067)
body_1.SetInertiaXX(chrono.ChVectorD(0.00025160361890319,0.000251926675257118,1.97778407134888e-05))
body_1.SetInertiaXY(chrono.ChVectorD(1.13925931405703e-22,-8.02797543504791e-21,-4.65974538262256e-21))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-6.06577003523177e-18,-3.61193125576236e-18,0.0768393780757694),chrono.ChQuaternionD(1,0,0,0)))

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
body_2.SetName('link-1')
body_2.SetPos(chrono.ChVectorD(-0.015,-0.015,-0.15))
body_2.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_2.SetMass(0.129698562397067)
body_2.SetInertiaXX(chrono.ChVectorD(0.00025160361890319,0.000251926675257118,1.97778407134888e-05))
body_2.SetInertiaXY(chrono.ChVectorD(-1.13925931405703e-22,-8.02797543504791e-21,4.65974538262256e-21))
body_2.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-6.06577003523177e-18,-3.61193125576236e-18,0.0768393780757694),chrono.ChQuaternionD(1,0,0,0)))

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
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: link-2 ,  SW ref.type:2 (2)

link_1 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.015,0.12,-0.12)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(-0.015,0.09,-0.12)
dB = chrono.ChVectorD(0,-1,0)
link_1.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_1.SetName("Concentric1")
exported_items.append(link_1)

link_2 = chrono.ChLinkMateGeneric()
link_2.SetConstrainedCoords(False, True, True, False, False, False)
cA = chrono.ChVectorD(-0.015,0.12,-0.12)
cB = chrono.ChVectorD(-0.015,0.09,-0.12)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(0,-1,0)
link_2.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_2.SetName("Concentric1")
exported_items.append(link_2)


# Mate constraint: Parallel1 [MateParallel] type:3 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: link-2 ,  SW ref.type:2 (2)

link_3 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.015,-0.015,-0.15)
dA = chrono.ChVectorD(0,0,-1)
cB = chrono.ChVectorD(-0.015,-0.045,-0.24)
dB = chrono.ChVectorD(0,0,-1)
link_3.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_3.SetName("Parallel1")
exported_items.append(link_3)


# Mate constraint: Coincident2 [MateCoincident] type:0 align:1 flip:False
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name: body_1 , SW name: link-2 ,  SW ref.type:2 (2)

link_4 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.03,-0.03,0)
cB = chrono.ChVectorD(1.04083408558608e-17,-0.03,-0.24)
dA = chrono.ChVectorD(0,-1,0)
dB = chrono.ChVectorD(0,1,0)
link_4.Initialize(body_2,body_1,False,cA,cB,dB)
link_4.SetDistance(0)
link_4.SetName("Coincident2")
exported_items.append(link_4)

link_5 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.03,-0.03,0)
dA = chrono.ChVectorD(0,-1,0)
cB = chrono.ChVectorD(1.04083408558608e-17,-0.03,-0.24)
dB = chrono.ChVectorD(0,1,0)
link_5.SetFlipped(True)
link_5.Initialize(body_2,body_1,False,cA,cB,dA,dB)
link_5.SetName("Coincident2")
exported_items.append(link_5)


# Mate constraint: Coincident3 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: assem ,  SW ref.type:4 (4)

link_6 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(0,-0.03,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(1,0,0)
dB = chrono.ChVectorD(1,0,0)
link_6.Initialize(body_2,body_0,False,cA,cB,dB)
link_6.SetDistance(0)
link_6.SetName("Coincident3")
exported_items.append(link_6)

link_7 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(0,-0.03,0)
dA = chrono.ChVectorD(1,0,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(1,0,0)
link_7.Initialize(body_2,body_0,False,cA,cB,dA,dB)
link_7.SetName("Coincident3")
exported_items.append(link_7)


# Mate constraint: Coincident4 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: assem ,  SW ref.type:4 (4)

link_8 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.015,-0.015,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,0,1)
dB = chrono.ChVectorD(0,0,1)
link_8.Initialize(body_2,body_0,False,cA,cB,dB)
link_8.SetDistance(0)
link_8.SetName("Coincident4")
exported_items.append(link_8)

link_9 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.015,-0.015,0)
dA = chrono.ChVectorD(0,0,1)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,0,1)
link_9.Initialize(body_2,body_0,False,cA,cB,dA,dB)
link_9.SetName("Coincident4")
exported_items.append(link_9)


# Mate constraint: Coincident5 [MateCoincident] type:0 align:0 flip:False
#   Entity 0: C::E name: body_2 , SW name: link-1 ,  SW ref.type:2 (2)
#   Entity 1: C::E name:  , SW name: assem ,  SW ref.type:4 (4)

link_10 = chrono.ChLinkMateXdistance()
cA = chrono.ChVectorD(-0.03,3.46944695195361e-18,0)
cB = chrono.ChVectorD(0,0,0)
dA = chrono.ChVectorD(0,1,0)
dB = chrono.ChVectorD(0,1,0)
link_10.Initialize(body_2,body_0,False,cA,cB,dB)
link_10.SetDistance(0)
link_10.SetName("Coincident5")
exported_items.append(link_10)

link_11 = chrono.ChLinkMateParallel()
cA = chrono.ChVectorD(-0.03,3.46944695195361e-18,0)
dA = chrono.ChVectorD(0,1,0)
cB = chrono.ChVectorD(0,0,0)
dB = chrono.ChVectorD(0,1,0)
link_11.Initialize(body_2,body_0,False,cA,cB,dA,dB)
link_11.SetName("Coincident5")
exported_items.append(link_11)

