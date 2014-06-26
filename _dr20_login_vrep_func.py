'''
Created on Aug 12, 2013

@author: almin
'''

import vrep
import Variables

def getJointHandles_dr20_(clientID):
    err_h_body, bodyHandle = vrep.simxGetObjectHandle(clientID,'dr20_body_', vrep.simx_opmode_oneshot_wait)
    err_h_leftJoint, leftJoint = vrep.simxGetObjectHandle(clientID,'dr20_leftWheelJoint_', vrep.simx_opmode_oneshot_wait)
    err_h_rightJoint, rightJoint = vrep.simxGetObjectHandle(clientID,'dr20_rightWheelJoint_', vrep.simx_opmode_oneshot_wait)
    err_h_sonicJoint, sonicJoint = vrep.simxGetObjectHandle(clientID,'dr20_ultrasonicSensorJoint_', vrep.simx_opmode_oneshot_wait)
    err_h_rightWheel, rightWheel = vrep.simxGetObjectHandle(clientID,'dr20_dynamicRightWheel', vrep.simx_opmode_oneshot_wait)
    err_h_leftWheel, leftWheel = vrep.simxGetObjectHandle(clientID,'dr20_dynamicLeftWheel', vrep.simx_opmode_oneshot_wait)
    return (err_h_body, err_h_leftJoint, err_h_rightJoint, err_h_sonicJoint,
            err_h_rightWheel, err_h_leftWheel, bodyHandle, leftJoint,
            rightJoint, sonicJoint, rightWheel, leftWheel)
    
def areJointHandlesValid(err_h_body, err_h_leftJoint, err_h_rightJoint,
                         err_h_sonicJoint, err_h_rightWheel, err_h_leftWheel):
    if (err_h_body != vrep.simx_error_noerror or
       err_h_leftJoint != vrep.simx_error_noerror or 
       err_h_rightJoint != vrep.simx_error_noerror or
       err_h_sonicJoint != vrep.simx_error_noerror or
       err_h_rightWheel != vrep.simx_error_noerror or
       err_h_leftWheel != vrep.simx_error_noerror):
        print "Fehler beim Einlesen der Joints des Roboters dr20"
        exit(0)
    
def getSensorHandles_dr20_(clientID):
    err_h_infra6, infra6 = vrep.simxGetObjectHandle(clientID,'dr20_infraredSensor6_', vrep.simx_opmode_oneshot_wait)
    err_h_infra2, infra2 = vrep.simxGetObjectHandle(clientID,'dr20_infraredSensor2_', vrep.simx_opmode_oneshot_wait)
    err_h_infra5, infra5 = vrep.simxGetObjectHandle(clientID,'dr20_infraredSensor5_', vrep.simx_opmode_oneshot_wait)
    err_h_infra1, infra1 = vrep.simxGetObjectHandle(clientID,'dr20_infraredSensor1_', vrep.simx_opmode_oneshot_wait)
    err_h_sonic, sonic = vrep.simxGetObjectHandle(clientID,'dr20_ultrasonicSensor_', vrep.simx_opmode_oneshot_wait)
    return (err_h_infra6, err_h_infra2, err_h_infra5, err_h_infra1, err_h_sonic,
           infra6, infra2, infra5, infra1, sonic)

def areSensorHandlesValid_dr20_(err_h_infra6, err_h_infra2, err_h_infra5, err_h_infra1, err_h_sonic):
    if (err_h_infra6 != vrep.simx_error_noerror or
       err_h_infra2 != vrep.simx_error_noerror or
       err_h_infra5 != vrep.simx_error_noerror or
       err_h_infra1 != vrep.simx_error_noerror or
       err_h_sonic != vrep.simx_error_noerror):
        print "Fehler beim Einlesen der Sensoren des Roboters dr20" 
        exit(0)

def areSensorReadsValid_dr20_(err_r_infra6, err_r_infra2, err_r_infra5, err_r_infra1, err_r_sonic):
    if (err_r_infra6 == vrep.simx_error_noerror and
       err_r_infra2 == vrep.simx_error_noerror and
       err_r_infra5 == vrep.simx_error_noerror and
       err_r_infra1 == vrep.simx_error_noerror and
       err_r_sonic == vrep.simx_error_noerror):
        print "Die Sensoren haben ein Objekt entdeckt"        
    else:
        if (err_r_infra6 == vrep.simx_error_novalue_flag and
           err_r_infra2 == vrep.simx_error_novalue_flag and
           err_r_infra5 == vrep.simx_error_novalue_flag and
           err_r_infra1 == vrep.simx_error_novalue_flag and
           err_r_sonic == vrep.simx_error_novalue_flag):
            print "Die Sensoren haben keine Objekte entdeckt"
        else:
            print "Das Lesen der Sensorwerte hat einen Fehler ergeben"
    
def moveRobotRaw_dr20_(leftJoint, rightJoint, clientID):
    err_move_leftJ = vrep.simxSetJointTargetVelocity(clientID, leftJoint, 2, vrep.simx_opmode_oneshot)
    err_move_rightJ = vrep.simxSetJointTargetVelocity(clientID, rightJoint, 2, vrep.simx_opmode_oneshot)
    if err_move_leftJ != vrep.simx_error_noerror:
        print "Das linke Gelenk konnte nicht bewegt werden!"
    if err_move_rightJ != vrep.simx_error_noerror:
        print "Das rechte Gelenk konnte nicht bewegt werden!"
    
def getDistanceSensors(detpoint_infra6, detpoint_infra2, detpoint_infra5,
                       detpoint_infra1, detpoint_sonic):
    _distance = []
    
    infra6_productX = detpoint_infra6[0] * detpoint_infra6[0]
    infra6_productY = detpoint_infra6[1] * detpoint_infra6[1]
    infra6_productZ = detpoint_infra6[2] * detpoint_infra6[2]
    distance_infra6 = (infra6_productX + infra6_productY + infra6_productZ)**.5
    
    infra2_productX = detpoint_infra2[0] * detpoint_infra2[0]
    infra2_productY = detpoint_infra2[1] * detpoint_infra2[1]
    infra2_productZ = detpoint_infra2[2] * detpoint_infra2[2]
    distance_infra2 = (infra2_productX + infra2_productY + infra2_productZ)**.5
    
    infra5_productX = detpoint_infra5[0] * detpoint_infra5[0]
    infra5_productY = detpoint_infra5[1] * detpoint_infra5[1]
    infra5_productZ = detpoint_infra5[2] * detpoint_infra5[2]
    distance_infra5 = (infra5_productX + infra5_productY + infra5_productZ)**.5
    
    infra1_productX = detpoint_infra1[0] * detpoint_infra1[0]
    infra1_productY = detpoint_infra1[1] * detpoint_infra1[1]
    infra1_productZ = detpoint_infra1[2] * detpoint_infra1[2]
    distance_infra1 = (infra1_productX + infra1_productY + infra1_productZ)**.5
    
    sonic_productX = detpoint_sonic[0] * detpoint_sonic[0]
    sonic_productY = detpoint_sonic[1] * detpoint_sonic[1]
    sonic_productZ = detpoint_sonic[2] * detpoint_sonic[2]
    distance_sonic = (sonic_productX + sonic_productY + sonic_productZ)**.5
    
    _distance.append(distance_infra6)
    _distance.append(distance_infra2)
    _distance.append(distance_infra5)
    _distance.append(distance_infra1)
    _distance.append(distance_sonic)
    
    Variables.distance = _distance

def moveLeftJoint(velocity):
    print "prille"
    err_left = vrep.simxSetJointTargetVelocity(Variables.clientID, Variables.leftJoint, velocity, vrep.simx_opmode_oneshot)
    if err_left != vrep.simx_error_noerror and err_left == vrep.simx_error_novalue_flag:
        print "Fehler beim Bewegen des linken Gelenks des Roboters dr20"
    
def moveRightJoint(velocity):
    err_right = vrep.simxSetJointTargetVelocity(Variables.clientID, Variables.rightJoint, velocity, vrep.simx_opmode_oneshot)
    if err_right != vrep.simx_error_noerror and err_right == vrep.simx_error_novalue_flag:
        print "Fehler beim Bewegen des rechten Gelenks des Roboters dr20"
    
def moveSonicJoint(velocity):
    err_sonic = vrep.simxSetJointTargetVelocity(Variables.clientID, Variables.sonicJoint, velocity, vrep.simx_opmode_oneshot)
    if err_sonic != vrep.simx_error_noerror and err_sonic == vrep.simx_error_novalue_flag:
        print "Fehler beim Bewegen des sonic Gelenks des Roboters dr20"
   
def odometryData():
    err_pos_o, pos_o = vrep.simxGetObjectPosition(Variables.clientID, 
                                              Variables.bodyHandle,
                                              -1, vrep.simx_opmode_streaming)
    
    err_pos_n, pos = vrep.simxGetObjectPosition(Variables.clientID, 
                                              Variables.bodyHandle,
                                              -1, vrep.simx_opmode_buffer)
    if Variables.robot_pos_new != pos:
        Variables.robot_pos_old = Variables.robot_pos_new
        Variables.robot_pos_new = pos 
           