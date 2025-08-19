#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script includes all the steps of transfering an OpenSim model to Mujoco.

Created on Tue Jul 27 23:19:13 2021

@author: hwang

"""
from myoconverter.O2MPipeline import O2MPipeline

# define pipline configurations
kwargs = {}  # define kwargs inputs
kwargs['convert_steps'] = [1, 2, 3]    # All three steps selected
kwargs['muscle_list'] = None           # No specific muscle selected, optimize all of them
kwargs['osim_data_overwrite'] = True   # Overwrite the Osim model state files
kwargs['conversion'] = True            # Yes, perform 'Cvt#' process
kwargs['validation'] = True            # Yes, perform 'Vlt#' process
kwargs['speedy'] = False                # Do not reduce the checking notes to increase speed
kwargs['generate_pdf'] = True          # Do not generate validation pdf report
kwargs['add_ground_geom'] = True       # Add ground to the model
kwargs['treat_as_normal_path_point'] = False    # Using constraints to represent moving and conditional path points

############### Simple 2D Gait 10 DoFs 18 Muscles ##############
if __name__ == '__main__':
    osim_file = './models/osim/Gait10dof18musc/gait10dof18musc.osim'
    geometry_folder = './models/osim/Gait10dof18musc/Geometry'
    output_folder = './models/mjc/Gait10dof18musc'
    O2MPipeline(osim_file, geometry_folder, output_folder, **kwargs)