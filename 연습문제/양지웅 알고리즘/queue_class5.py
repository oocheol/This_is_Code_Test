def run_cmd_with_stack(cmd, queue):
    cmd_type = cmd[0]
    # cmd_type, num = cmd

    if cmd_type == "push":
        _, num = cmd
        queue.append(num)
    elif cmd_type == "pop":
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif cmd_type == "size":
        print(len(queue))
    elif cmd_type == "empty":
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif cmd_type == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif cmd_type == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
     
    # return queue

n = int(input())
queue = []

for _ in range(n):
    command = input().split()
    run_cmd_with_stack(command, queue)

    # queue = run_cmd_with_stack(command, queue)