program problem5_2;
uses math;

var
    i, num: integer;

begin
    num := lcm(1,2);
    for i := 2 to 20 do
        num := lcm(num, i);
    writeln(num);
end.
