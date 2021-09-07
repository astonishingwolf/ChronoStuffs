# PyChrono script generated from SolidWorks using Chrono::SolidWorks add-in 
# Assembly: 


import pychrono as chrono 
import builtins 

shapes_dir = 'block_2_shapes/' 

if hasattr(builtins, 'exported_system_relpath'): 
    shapes_dir = builtins.exported_system_relpath + shapes_dir 

exported_items = [] 

body_0= chrono.ChBodyAuxRef()
body_0.SetName('ground')
body_0.SetBodyFixed(True)
exported_items.append(body_0)

# Rigid body part
body_1= chrono.ChBodyAuxRef()
body_1.SetName('block_2-1')
body_1.SetPos(chrono.ChVectorD(0.0022871923259299,0.0155335298919823,0.027812742428255))
body_1.SetRot(chrono.ChQuaternionD(1,0,0,0))
body_1.SetMass(0.0141371669411541)
body_1.SetInertiaXX(chrono.ChVectorD(1.27234502470387e-06,1.27234502470387e-06,1.27234502470387e-06))
body_1.SetInertiaXY(chrono.ChVectorD(-1.00445073922803e-38,0,0))
body_1.SetFrame_COG_to_REF(chrono.ChFrameD(chrono.ChVectorD(-3.44431912260193e-19,0,0),chrono.ChQuaternionD(1,0,0,0)))
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



