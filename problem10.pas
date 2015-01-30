program problem10;


function isPrime(n:longint):boolean;
var
    i : longint;
begin
    for i:=2 to round(sqrt(n)) do
        begin
            if (n mod i = 0) then
            begin
                isPrime := false;
                break;
            end 
            else if i = round(sqrt(n)) then
                isPrime := true
        end;
end;


{=================main======================}

const
    max = 2000000;

var
   n,sum : longword;
BEGIN
    sum := 0;
    for n := 1 to max do
    begin
        if isPrime(n) then
        begin
            sum :=  sum + n;
            writeln(sum, ' ', n);
        end;
    end;
     writeln(sum);
END .
