program problem9;

var
    a,b,c:integer;

begin
    for a := 1 to 1000 do
        for b := a to 1000 do
            for c := b to 1000 do
                if (a+b+c = 1000) and (a*a+b*b=c*c) then
                    writeln(a:4,b:4,c:4);
end.
