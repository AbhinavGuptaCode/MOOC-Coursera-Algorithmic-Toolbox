# python3
import sys

def compute_min_refills(distance, tank, stops):
    ''' checking how the input is getting stored
    print(distance)
    print(tank)
    stops.sort(reverse=True)
    print(stops)
    '''
    # write your code here
    
    #sorting list of stops in desceding as per the logic used in code
    stops.sort(reverse=True)
    #min_stopsis nothing but number of refills
    min_stops=0
    #current position is 0 and then the stops of refill
    current_position=0
    
            
    while distance>tank:
        # checking if last stop and destination distance is greater than tank capacity
        if distance-stops[0]>tank:
            return (-1)
        
        for stop in stops:
            if tank>=(stop-current_position):
                distance=distance-(stop-current_position)
                current_position=stop
                min_stops=min_stops+1
                #now break the for loop
                break
        #making list of next stops and checking if trip is impossible        
        next_stops=[]
        for stop in stops:
            if stop>current_position:
                next_stops.append(stop)
        
        #for case when last stop is req for refill, then next_stops[] will be empty
        #therefore next_stops[-1] will throw error
        #we include (if distance-stops[0]>tank:) in beginnning of this loop because below code-
        #- will not handle cases when last stop is required for refill as per greedy algorithm
        try:
            if (next_stops[-1]-current_position)>tank:
                return(-1)
        except:
            pass        
           
    return min_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
