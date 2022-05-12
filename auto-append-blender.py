import bpy
import pathlib
import time
import os
import sys
import subprocess

filepath = bpy.data.filepath
directory = os.path.dirname(filepath)
newfile_name = os.path.join( directory , "test.blend")
path = newfile_name + "\\Collection\\"
object_name = "Sketchup"

fname = pathlib.Path(newfile_name)


a = 0
l = 0

def loop():
    global l
    a = fname.stat().st_mtime_ns
    if a == l:
        return 1.0
    else:
        
        print("")
        print("Updating")
        
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass
        
        context = bpy.context
        name = "Sketchup"
        scene = context.scene
        coll = bpy.data.collections.get(name)
        if coll is None:
            coll = bpy.data.collections.new(name)
        if not scene.user_of_id(coll):
            context.collection.children.link(coll)
            
        for obj in bpy.data.collections['Sketchup'].all_objects:
                            obj.select_set(True)
                            bpy.ops.object.delete(use_global=False, confirm=False)

        def recurLayerCollection(layerColl, collName):
            found = None
            if (layerColl.name == collName):
                return layerColl
            for layer in layerColl.children:
                found = recurLayerCollection(layer, collName)
                if found:
                    return found


        layer_collection = bpy.context.view_layer.layer_collection
        layerColl = recurLayerCollection(layer_collection, 'Sketchup')
        bpy.context.view_layer.active_layer_collection = layerColl
        
        
        
        
        
        bpy.ops.wm.append(filename=object_name, directory=path)
        
        print("Updated")
        print("")
        
        l = fname.stat().st_mtime_ns
        return 1.0

bpy.app.timers.register(loop)