#!/usr/bin/env python

"""
Perform a Laplacian smoothing operation on the mesh and return a new mesh
"""

import numpy as np

def laplacian_smooth(mesh, scale=0.15, repeat=1, preserve_limits="False"):
    n = 0
    while (n < repeat):  
        mesh.enable_connectivity()
        mesh.add_attribute("vertex_laplacian")
        displace = -mesh.get_vertex_attribute("vertex_laplacian")
        displace = displace * scale
        if (preserve_limits=="True"):
            nullpts = np.concatenate((np.asarray(np.where(mesh.vertices[:, 0] <= np.amin(mesh.vertices[:, 0]))),
                                      np.asarray(np.where(mesh.vertices[:, 0] >= np.amax(mesh.vertices[:, 0]))),
                                      np.asarray(np.where(mesh.vertices[:, 1] <= np.amin(mesh.vertices[:, 1]))),
                                      np.asarray(np.where(mesh.vertices[:, 1] >= np.amax(mesh.vertices[:, 1]))),
                                      np.asarray(np.where(mesh.vertices[:, 2] <= np.amin(mesh.vertices[:, 2]))),
                                      np.asarray(np.where(mesh.vertices[:, 2] >= np.amax(mesh.vertices[:, 2])))),
                                    axis=1).T
            displace[nullpts,:]=0
        mesh = pymesh.form_mesh(mesh.vertices + displace, mesh.faces)
        n = n + 1
    return mesh
