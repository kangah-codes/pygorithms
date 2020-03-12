# void hanoi(int tiles, int start=1, int end=3){
# 	if (tiles){
# 		hanoi(tiles-1, start, 6-start-end);
# 		cout << "Move disk " << tiles << " from " << start << " to " << end << endl;
# 		hanoi(tiles-1, 6-start-end, end);
# 	}
# }

# int main(){
# 	hanoi(10000);
# 	return 0;
# }

steps = 0

def hanoi(tiles, start=1, end=3):
	if tiles:
		hanoi(tiles-1, start, 6-start-end)
		print(f"Move disk {tiles} from {start} to {end}")
		hanoi(tiles-1, 6-start-end, end)
		global steps
		steps += 1

hanoi(20)
print(f"Completed in {steps} moves")