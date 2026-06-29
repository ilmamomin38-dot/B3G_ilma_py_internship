count=0

def track_calls():
    global count
    count+=1

track_calls()
track_calls()
track_calls()
track_calls()

print("Final count:",count)
