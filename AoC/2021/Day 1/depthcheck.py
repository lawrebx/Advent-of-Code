def depthCheck(depth_prev,depth_current,output_type=0):
    
    if depth_prev > depth_current:
        string_depth_compare = 'Decreased'
        int_depth_compare = -1

    elif depth_prev < depth_current:
        string_depth_compare = 'Increased'
        int_depth_compare = 1

    elif depth_prev == depth_current:
        string_depth_compare = 'No Change'
        int_depth_compare = 0

    else:
        string_depth_compare = "Something went wrong."
        int_depth_compare = 400
    
    if output_type == 1:
        return(string_depth_compare)
    else:
        return(int_depth_compare)
