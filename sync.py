import bpy
import pathlib
import time
import os
import sys
import subprocess

blend_filepath = bpy.context.blend_data.filepath
blend_filename = bpy.path.display_name(
    bpy.context.blend_data.filepath, title_case=False)
skp_file = blend_filename + ".skp"
skp_file_pathlib = pathlib.Path(skp_file)

a = 0
l = 0


def loop():
    global l
    a = skp_file_pathlib.stat().st_mtime_ns
    if a == l:
        return 1.0
    else:

        print("")
        print("Updating")

        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            pass

        name = "Sketchup"
        coll = bpy.data.collections.get(name)
        if coll is None:
            coll = bpy.data.collections.new(name)
        else:
            bpy.data.collections.remove(bpy.data.collections[name])
            coll = bpy.data.collections.new(name)
        if not bpy.context.scene.user_of_id(coll):
            bpy.context.collection.children.link(coll)

        bpy.ops.outliner.orphans_purge()
        
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

        bpy.ops.import_scene.skp(filepath=skp_file,
                                 filter_glob="*.skp",
                                 import_camera=False,
                                 reuse_material=True,
                                 max_instance=10000,
                                 dedub_type='FACE',
                                 dedub_only=False,
                                 scenes_as_camera=False,
                                 import_scene="",
                                 reuse_existing_groups=True)

        bpy.ops.mesh.primitive_cube_add()

        cube = bpy.context.selected_objects[0]

        cube.name = "MyLittleCube"

        for obj in bpy.data.collections['Sketchup'].all_objects:
            obj.select_set(True)

        bpy.ops.object.editmode_toggle()

        bpy.ops.mesh.dissolve_limited()

        bpy.ops.object.editmode_toggle()

        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects['MyLittleCube'].select_set(True)

        bpy.ops.object.delete()

        bpy.ops.wm.save_mainfile()

        print("Updated")
        print("")

        l = skp_file_pathlib.stat().st_mtime_ns
        return 1.0

try:
    bpy.app.timers.unregister(loop)
except:
    bpy.app.timers.register(loop)
