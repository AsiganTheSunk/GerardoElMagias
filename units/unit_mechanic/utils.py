# Pre Save State for Enemy List: target_list


def get_alive_targets(target_list):
    pre_target_list = []
    for enemy_unit in target_list:
        if enemy_unit.alive:
            pre_target_list.append(True)
        else:
            pre_target_list.append(False)

    return pre_target_list
