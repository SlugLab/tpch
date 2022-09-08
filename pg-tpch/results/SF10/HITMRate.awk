{
if($1=="Load" && $2=="LLC" && $3=="hit")
	{p1=$5;}
if($1=="Load" && $2=="Local" && $3=="HITM")
	{p2=$5;}
if($1=="Load" && $2=="Remote" && $3=="HITM")
	{p3=$5;}
}
END{
print (p2+p3)/p1;
}
