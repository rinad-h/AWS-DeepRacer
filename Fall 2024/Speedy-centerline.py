def reward_function(params):
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Reward parameters
    center_distance_threshold = 0.1 * track_width
    speed_threshold = 3.0  # Encourage speed > 3 m/s

    reward = 1.0  # Base reward

    # Reward for staying close to the center line
    if distance_from_center <= center_distance_threshold:
        reward += 1.0
    
    # Reward for speed above threshold
    if speed > speed_threshold:
        reward += 1.5
    
    return float(reward)
