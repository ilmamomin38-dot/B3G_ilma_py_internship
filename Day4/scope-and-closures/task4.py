def update_status():
    status = "pending"

    def complete_task():
        nonlocal status
        status = "completed"

    complete_task()
    print("Final status:", status)


update_status()