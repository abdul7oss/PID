import PID as p

def correct_error(cx, cy, image):
    h, w, d = image.shape
    # NOTE: If it doesn't seems to work, try changing to cy to cx
    #err = cx - w/2
    # NOTE: If the motion is too erratic, then consider a median range
    #      where there shall be no lateral movement

    # TODO: Propel linearly
    linear_thrust = 1600
    #slope = 5/16
    #rot_thrust = err*slope
    #gains 
    P = 5/16
    I = 1
    D = 0
    pi = p.PID(P,I,D)

    pi.setpoint = w/2

    feedback = cx

    #limits for integral error 
    # can set by using func pi.setWindup(windup) by default it is -20 and 20.

    #set sample time by using func pi.setSampleTime(Sample time)

    
    
    pi.update(feedback)
    rot_thrust = pi.output

    rot_thrust = max(-100, min(rot_thrust, 100))
    if rot_thrust >= 0:
        print('Left')
    else:
        print('Right')

    print('rot_thrust = ', rot_thrust)

    err_y = cy - h/2
    constant = 90
    y_slope = 1/30.
    m.hp_control(err_y*y_slope + constant)

    thrusts = {
        m.pin_l: linear_thrust + rot_thrust,
        m.pin_r: linear_thrust - rot_thrust,
    }
    m.custom_thrusts(thrusts)