@ start = 0

while ( $start < 40 )

    set inputname = `printf "galaxy_slices/output_wechsler_%04d_arcseconds.dat" $start`
    python plot_sliced_data_heatmap.py $inputname $start

    @ start += 1

end
