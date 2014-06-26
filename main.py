''' 
Created on Aug 12, 2013

@author: almin
'''
import _dr20_login_vrep_func
import vrep
import Variables

def main():
    _clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

# get all sensors from robot dr_20
    if _clientID != -1:
        print "Verbindung zu Server aufgebaut"
        print "ClientID: %d" % _clientID    
    else:
        print "Keine Vebindung zum Server moeglich"   
        exit(0)
        
    (err_h_body, err_h_leftJoint, err_h_rightJoint, err_h_sonicJoint,
    err_h_rightWheel, err_h_leftWheel, _bodyHandle, _leftJoint,
    _rightJoint, _sonicJoint, _rightWheel, 
    _leftWheel) = _dr20_login_vrep_func.getJointHandles_dr20_(_clientID)

    (err_h_infra6, err_h_infra2, err_h_infra5, err_h_infra1, err_h_sonic,
    infra6, infra2, infra5, infra1, sonic) = _dr20_login_vrep_func.getSensorHandles_dr20_(_clientID)
        
    Variables.clientID = _clientID
    print Variables.clientID
    
    # pruefe, ob Objekte einen Fehler zurueckgeben
    _dr20_login_vrep_func.areJointHandlesValid(err_h_body, err_h_leftJoint,
                                               err_h_rightJoint, err_h_sonicJoint,
                                               err_h_rightWheel, err_h_leftWheel)
    
    _dr20_login_vrep_func.areSensorHandlesValid_dr20_(err_h_infra6, err_h_infra2, err_h_infra5, err_h_infra1, err_h_sonic)
    
    Variables.bodyHandle = _bodyHandle
    Variables.leftJoint = _leftJoint
    Variables.rightJoint = _rightJoint
    Variables.sonicJoint = _sonicJoint
    '''
    errShape, rightWheel_high_min = vrep.simxGetObjectFloatParameter(_clientID, _rightWheel,
                                            23, vrep.simx_opmode_oneshot_wait)
    errShape2, rightWheel_high_max = vrep.simxGetObjectFloatParameter(_clientID, _rightWheel,
                                            26, vrep.simx_opmode_oneshot_wait)

    print rightWheel_high_min
    print rightWheel_high_max
    ''' 
    (err_r_infra6,det_state_infra6,detpoint_infra6,det_handle_infra6,
    det_surf_norm_vec_infra6) = vrep.simxReadProximitySensor(_clientID,infra6,
                                                             vrep.simx_opmode_streaming)
    
    (err_r_infra2,det_state_infra2,detpoint_infra2,det_handle_infra2,
    det_surf_norm_vec_infra2) = vrep.simxReadProximitySensor(_clientID,infra2,
                                                             vrep.simx_opmode_streaming)
    
    (err_r_infra5,det_state_infra5,detpoint_infra5,det_handle_infra5,
    det_surf_norm_vec_infra5) = vrep.simxReadProximitySensor(_clientID,infra5,
                                                             vrep.simx_opmode_streaming)
    
    (err_r_infra1,det_state_infra1,detpoint_infra1,det_handle_infra1,
    det_surf_norm_vec_infra1) = vrep.simxReadProximitySensor(_clientID,infra1,
                                                             vrep.simx_opmode_streaming)
    
    (err_r_sonic,det_state_sonic,detpoint_sonic,det_handle_sonic,
    det_surf_norm_vec_sonic) = vrep.simxReadProximitySensor(_clientID,sonic,
                                                            vrep.simx_opmode_streaming)
    
    while(True):          
        # _dr20_login_vrep_func.moveRobotRaw_dr20_(_leftJoint, _rightJoint, _clientID)
        print _clientID
        print Variables.clientID
        print Variables.leftJoint
        _dr20_login_vrep_func.moveLeftJoint(2)
        _dr20_login_vrep_func.moveRightJoint(2)
        
        _dr20_login_vrep_func.odometryData()
        
        (err_r_infra6,det_state_infra6,detpoint_infra6,det_handle_infra6,
        det_surf_norm_vec_infra6) = vrep.simxReadProximitySensor(_clientID,infra6,
                                                                 vrep.simx_opmode_buffer)
    
        Variables.det_state_infra6 = det_state_infra6
        
        (err_r_infra2,det_state_infra2,detpoint_infra2,det_handle_infra2,
        det_surf_norm_vec_infra2) = vrep.simxReadProximitySensor(_clientID,infra2,
                                                                 vrep.simx_opmode_buffer)
    
        Variables.det_state_infra2 = det_state_infra2
        
        (err_r_infra5,det_state_infra5,detpoint_infra5,det_handle_infra5,
        det_surf_norm_vec_infra5) = vrep.simxReadProximitySensor(_clientID,infra5,
                                                                 vrep.simx_opmode_buffer)
    
        Variables.det_state_infra5 = det_state_infra5
        
        (err_r_infra1,det_state_infra1,detpoint_infra1,det_handle_infra1,
        det_surf_norm_vec_infra1) = vrep.simxReadProximitySensor(_clientID,infra1,
                                                                 vrep.simx_opmode_buffer)
    
        Variables.det_state_infra1 = det_state_infra1
        
        (err_r_sonic,det_state_sonic,detpoint_sonic,det_handle_sonic,
        det_surf_norm_vec_sonic) = vrep.simxReadProximitySensor(_clientID,sonic,
                                                                 vrep.simx_opmode_buffer)
    
        Variables.det_state_sonic = det_state_sonic
    
        _dr20_login_vrep_func.areSensorReadsValid_dr20_(err_r_infra6, err_r_infra2, err_r_infra5, err_r_infra1, err_r_sonic)
    
        _dr20_login_vrep_func.getDistanceSensors(detpoint_infra6, detpoint_infra2,
                                             detpoint_infra5, detpoint_infra1, 
                                             detpoint_sonic)
        print Variables.distance
        print Variables.robot_pos_old
        print Variables.robot_pos_new
        
    vrep.simxFinish(_clientID)

if __name__ == '__main__':
    main()
    
    