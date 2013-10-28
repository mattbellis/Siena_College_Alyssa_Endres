@ start = 0

while ( $start < 10000000 )

    @ stop = $start + 1000000

    echo $start $stop

    python plot_data_heatmap.py /home/bellis/Work/Astronomy/catalogs/Wechsler/wechsler_gals.cat $start $stop

    @ start += 500000

end
