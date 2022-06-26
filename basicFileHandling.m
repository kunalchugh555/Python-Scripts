function [c s l] = e4_text_stats(fname)
    c = -1;
    s = -1;
    l = -1;
    fid = fopen(fname, 'r');
    if fid>=0
        c = 0;
        s = 0;
        l = 0;
        one_line = fgetl(fid);
        while ischar(one_line)
            c = c+length(one_line);
            l = l+1;
            s = s + length(strfind(one_line,'.')) + length(strfind(one_line,'?')) + length(strfind(one_line,'!'));
            one_line = fgetl(fid); 
        end
    end
    fclose(fid);
end