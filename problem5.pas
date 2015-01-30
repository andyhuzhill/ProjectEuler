program projeular5;

var
    flag : boolean = False;
    n    : longint = 0;
    i    : integer ;

Begin
    n := 2520;
    while not flag do
    begin
        for i := 1 to 20 do
            begin
                if (n mod i <> 0) then
                begin
                    inc(n);
                    break;
                end
                else
                if ((i = 20) and(n mod i =0)) then
                    flag := True;
            end;
    end;
    writeln(n);
end.


