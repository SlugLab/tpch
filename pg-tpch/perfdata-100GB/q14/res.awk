{
	if ($1 == "Front-End" && $2 == "Bound:"){
		print $3; }
	if ($1 == "Bad" && $2 == "Speculation:"){ 
		print $3; } 
	if ($1 == "Back-End" && $2 == "Bound:"){
		print $3; } 
	if ($1 == "Core" && $2 == "Bound:"){
		print $3; }
	if ($1 == "Memory" && $2 == "Bound:"){
		print $3; } 
	if ($1 == "DRAM" && $2 == "Bound:"){
		print $3; } 
	if ($1 == "Memory" && $2 == "Bandwidth:"){
		print $3; }
	if ($1 == "Memory" && $2 == "Latency:"){
		print $3; }
}
