'''
Created on Aug 14, 2013

@author: almin
'''

# alle globalen Variablen hier
# von dieser Datei auf alle zugreifen
distance = [0.0, 0.0, 0.0, 0.0, 0.0]
bodyHandle = 0
leftJoint = 0
rightJoint = 0
sonicJoint = 0
clientID = -1
robot_pos_new = [0.0, 0.0, 0.0]
robot_pos_old = [0.0, 0.0, 0.0]

infra6 = 0
infra2 = 0
infra5 = 0
infra1 = 0

det_state_infra6 = False
detpoint_infra6 = [0.0, 0.0, 0.0]
det_handle_infra6 = 0
det_surf_norm_vec_infra6 = [0.0, 0.0, 0.0]

det_state_infra2 = False
detpoint_infra2 = [0.0, 0.0, 0.0]
det_handle_infra2 = 0
det_surf_norm_vec_infra2 = [0.0, 0.0, 0.0]

det_state_infra5 = False
detpoint_infra5 = [0.0, 0.0, 0.0]
det_handle_infra5 = 0
det_surf_norm_vec_infra5 = [0.0, 0.0, 0.0]

det_state_infra1 = False
detpoint_infra1 = [0.0, 0.0, 0.0]
det_handle_infra1 = 0
det_surf_norm_vec_infra1 = [0.0, 0.0, 0.0]

det_state_sonic = False
detpoint_sonic = [0.0, 0.0, 0.0]
det_handle_sonic = 0
det_surf_norm_vec_sonic = [0.0, 0.0, 0.0]