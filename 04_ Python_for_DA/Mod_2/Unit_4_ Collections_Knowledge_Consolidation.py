from collections import defaultdict, deque

def task_manager(tasks):
    # prior_deque = deque()
    task_dict = defaultdict(deque)
    for i_num_t, i_srv, i_prior in tasks:
        if i_prior == False:
            task_dict[i_srv].append(i_num_t)
        else:
            task_dict[i_srv].appendleft(i_num_t)
        
    return task_dict
    

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))