@ start = 0

while ( $start < 140 )

    set zlo = `echo $start | awk '{print $1*0.005}'`
    set zhi = `echo $start | awk '{print ($1+2)*0.005}'`
    set tag = `printf "%04d" $start`
    set inputname = `printf "~/process_MICE_dataset/data_files/data_zlo%4.3f_zhi%4.3f_arcseconds.dat" $zlo $zhi`
    echo python plot_sliced_data_heatmap.py $inputname $tag
         python plot_sliced_data_heatmap.py $inputname $tag

    @ start += 1

end
