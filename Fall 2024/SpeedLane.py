def reward_function(params):
    # Calculate center variance
    center_variance = params["distance_from_center"] / params["track_width"]

    # Define the racing lines (waypoints)
    left_lane = [23,24,50,51,52,53,61,62,63,64,65,66,67,68]
    center_lane = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,26,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,54,55,56,57,58,59,60,69,70]
    right_lane = [29,30,31,32,33,34]

    # Define speed zones
    fast = [0,1,2,3,4,5,6,7,8,9,25,26,27,28,29,30,31,32,51,52,53,54,61,62,63,64,65,66,67,68,69,70]
    moderate = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,55,56,57,58,59,60]
    slow = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    # Initialize reward
    reward = 30

    # Check if all wheels are on track
    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    # Reward for staying on the correct lane
    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    # Reward for maintaining proper speed in different zones
    if params["closest_waypoints"][1] in fast:
        if params["speed"] > 1.5:
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in moderate:
        if 1 <= params["speed"] <= 1.5:
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] <= 1:
            reward += 10
        else:
            reward -= 10

    # Return the final reward
    return float(reward)
