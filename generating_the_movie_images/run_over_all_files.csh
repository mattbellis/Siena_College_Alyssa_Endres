#python sort_the_data.py /data/Astronomy/catalogs/Wechsler/wechsler_gals.cat

@ i = 0

while ( $i < 10 )

    python plot_data_heatmap.py galaxy_slices/output_wechsleroutput_$i.dat $i

    @ i += 1

end
