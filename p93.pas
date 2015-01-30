program p93;
var 
a,b :longint;
begin
    read(a);
    write(a,'=');
    b := 2;
    while a <> 1 do
        begin
            while a mod b =0 do
                begin
                    a := a div b;
                    if a = 1 then
                        write(b)
                    else    
                        write(b,'*')
                end;
            inc(b);
        end;
     writeln()
end.

